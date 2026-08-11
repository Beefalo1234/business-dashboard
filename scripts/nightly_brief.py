#!/usr/bin/env python3
"""Morning brief generator — reads business-dashboard/data.js, prints today's
brief. Zero LLM cost; runs as a no_agent cron every morning at 08:00."""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data.js")

def load():
    s = open(DATA, encoding="utf-8").read()
    return json.loads(s[s.index("=") + 1:].strip().rstrip(";"))

def main():
    d = load()
    today = datetime.date.today()
    today_s = today.isoformat()

    out = []
    out.append("☀️ MORNING BRIEF — " + today.strftime("%A %b %d"))
    out.append("")

    # mission tracker
    m = d.get("money", {})
    exp, gains = m.get("expenses", 0), m.get("gains", 0)
    net = round(gains - exp, 2)
    verdict = "✅ PROFITABLE" if net > 0 else ("🟡 BREAK-EVEN" if net == 0 else "🔴 RED")
    out.append(f"💸 Accountability: gains ${gains:.2f} - expenses ${exp:.2f} = {verdict} (${net:.2f})")
    out.append(f"   Check-in: {m.get('checkDay','Saturday')}")
    out.append("")

    # today's task from the calendar
    task = None
    for w in d.get("calendar", {}).get("weeks", []):
        for day in w.get("days", []):
            if day.get("date") == today_s:
                task = (w.get("title"), day)
                break
        if task: break
    if task:
        wtitle, day = task
        out.append(f"📌 TODAY ({wtitle}):")
        for line in day.get("tasks", []):
            out.append("   • " + line)
        if day.get("revenueTarget"):
            out.append(f"   🎯 week revenue target: {day['revenueTarget']}")
    else:
        out.append("📌 TODAY: no task scheduled — see https://beefalo1234.github.io/business-dashboard/")
    out.append("")

    # businesses snapshot
    out.append("🏢 BUSINESSES:")
    for b in d.get("businesses", []):
        out.append(f"   • {b.get('name','?')} [{b.get('status','?')}] — {b.get('nextAction','')}")
    out.append("")

    # countdown to Sept 1
    sept = datetime.date(2026, 9, 1)
    days = (sept - today).days
    goals = d.get("goals", [])
    target = ""
    if goals:
        g = goals[-1]
        target = f"${g.get('cumTarget','?')}"
    if days >= 0:
        out.append(f"⏳ {days} days until September — target {target} by Aug 31.")
    out.append("")
    out.append("Full dashboard: https://beefalo1234.github.io/business-dashboard/")

    print("\n".join(out))

if __name__ == "__main__":
    main()
