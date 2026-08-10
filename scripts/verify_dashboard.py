#!/usr/bin/env python3
"""Ad-hoc verification for business-dashboard (data.js + index.html).
Checks: (1) data.js evaluates in Node (JS-valid keys), (2) every PLAN.* path
used in index.html resolves against the evaluated data, (3) headless Edge
render produces expected DOM nodes. Chromium-internal stderr noise filtered.
Run: python3 scripts/verify_dashboard.py [--keep-temp]
"""
import json, os, re, subprocess, sys, tempfile

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE, "data.js")
html_path = os.path.join(BASE, "index.html")
node = r"C:\Program Files\nodejs\node.exe"
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
failures = []
tmp = tempfile.gettempdir()

# ── 1. evaluate data.js in Node (JS object literal → JSON) ─────
probe = os.path.join(tmp, "hermes-verify-plan.cjs")
with open(probe, "w", encoding="utf-8") as f:
    f.write("const fs=require('fs');const vm=require('vm');"
            "const src=fs.readFileSync(process.argv[2],'utf8');"
            "const ctx={};vm.createContext(ctx);"
            "let out;"
            "try{out=vm.runInContext(src+';PLAN',ctx);}catch(e){console.error('EVAL_ERR:'+e.message);process.exit(3);}"
            "if(!out){console.error('NO_PLAN');process.exit(4);}"
            "console.log(JSON.stringify(out))")
try:
    r = subprocess.run([node, probe, data_path], capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        failures.append(f"data.js eval FAILED (rc={r.returncode}): {r.stderr[:300]}")
    else:
        plan = json.loads(r.stdout)
        weeks = plan["calendar"]["weeks"]
        days = sum(len(w["days"]) for w in weeks)
        print(f"data.js evaluates OK: weeks={len(weeks)}, days={days}, biz={len(plan['businesses'])}, proj_rows={len(plan['math']['projection'])}, log={len(plan['progress']['log'])}")
        if len(weeks) != 4 or days != 26:
            failures.append(f"calendar shape wrong: weeks={len(weeks)} days={days} (expect 4/28)")
        if len(plan["math"]["projection"]) != 6:
            failures.append(f"projection rows={len(plan['math']['projection'])} (expect 6)")
        if plan["offer"]["retainer"] != 200 or plan["offer"]["setupFee"] != 0:
            failures.append("offer pricing mismatch (expect $0 setup / $200 retainer)")
except Exception as e:
    failures.append(f"node probe crashed: {e}")

# ── 2. every PLAN.* reference in index.html resolves ───────────
if "plan" in dir() and plan:
    html = open(html_path, encoding="utf-8").read()
    refs = sorted(set(re.findall(r"PLAN\.[A-Za-z0-9_.]+", html)))

    def path_ok(ref):
        parts = ref.split(".")[1:]
        cur = plan
        for p in parts:
            if p in ("map", "length", "reverse", "join"):
                break
            if not isinstance(cur, dict) or p not in cur:
                return False
            cur = cur[p]
        return True

    missing = [r for r in refs if not path_ok(r)]
    if missing:
        failures.append(f"unresolved PLAN refs: {missing}")
    else:
        print(f"all {len(refs)} PLAN.* references resolve OK")

# ── 3. headless render + content assertions ────────────────────
if os.path.exists(edge):
    url = "file:///" + html_path.replace("\\", "/")
    r1 = subprocess.run([edge, "--headless", "--disable-gpu", "--dump-dom", url],
                        capture_output=True, text=True, timeout=45)
    dom = r1.stdout
    checks = {
        "title rendered": "LeadSetter AI" in dom,
        "30-lead deliverable": "30 qualified leads/mo" in dom,
        "gross margin 96%": "96%" in dom,
        "funding not required": "Not required." in dom,
        "mission marker": "before September" in dom,
        "break-even text": "covers all fixed costs" in dom,
        "4 week blocks": dom.count('class="week"') + dom.count('class="weekhead"') >= 4,
        "6 stat boxes": dom.count('class="stat"') >= 6,
        "6 projection rows": dom.count("<tr>") >= 6,
    }
    for name, ok in checks.items():
        print(f"  render [{name}]: {'PASS' if ok else 'FAIL'}")
        if not ok:
            failures.append(f"render check failed: {name}")
    real_errs = [l for l in (r1.stderr or "").splitlines()
                 if ("uncaught" in l.lower() or "failed to load" in l.lower()
                     or "syntaxerror" in l.lower() or "referenceerror" in l.lower()
                     or "typeerror" in l.lower())]
    if real_errs:
        failures.append(f"browser page errors: {real_errs[:3]}")
else:
    failures.append("Edge not found — render check skipped")

# ── cleanup + report ───────────────────────────────────────────
if "--keep-temp" not in sys.argv:
    try: os.remove(probe)
    except OSError: pass

if failures:
    print("\nVERIFICATION FAILED:")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("\nALL CHECKS PASSED (ad-hoc verification, not a suite)")
