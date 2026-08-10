#!/usr/bin/env python3
"""Generate business-dashboard/data.js — multi-business roadmap, calendar Aug 10–31,
money accountability tracker. Run: python3 scripts/build_data.py > data.js"""

import datetime as dt
import json

START = dt.date(2026, 8, 10)   # Monday — first day of roadmap (tomorrow)
END   = dt.date(2026, 8, 31)   # real money before September
TARGET = 2500                  # "real money before September" goal

# weekly themes + revenue targets
WEEKS = [
    ("Aug 10–16", "Cash week 1 — pressure washing + plumbing setup",
     [("Mon 08-10", "Set up Stripe (LeadSetter) + Square (pressure washing) with debit bank account; install Twilio number"),
      ("Mon 08-10", "Publish pressure-washing weekend special: $199 driveway / $399 driveway+siding, 914-only"),
      ("Tue 08-11", "Post special on Facebook Marketplace + Nextdoor + 3 local FB groups; flyers at 2 hardware stores"),
      ("Tue 08-11", "Call 25 warm leads from batch 1 (local contractors) — pitch LeadSetter, book demo calls"),
      ("Wed 08-12", "Door-to-door 2 hrs in Mamaroneck/Larchmont: 20 doors, 3 quotes"),
      ("Wed 08-12", "Send 100 LeadSetter cold emails (batch 1) + 50 SMS via Twilio"),
      ("Thu 08-13", "Book 2 pressure-washing jobs for the weekend; confirm by text"),
      ("Fri 08-14", "Prep gear; confirm Saturday jobs; run 2 LeadSetter demo calls"),
      ("Sat 08-15", "💰 JOB DAY 1: 2 pressure-washing jobs (~$600 cash). WEEK 1 CHECK-IN: expenses vs gains"),
      ("Sun 08-16", "Review numbers; post before/after photos; bank the cash")],
     597),
    ("Aug 17–23", "LeadSetter first clients + lead packs",
     [("Mon 08-17", "Deliver 3 quotes from weekend; convert to booked jobs ($399-600)"),
      ("Mon 08-17", "LeadSetter demo calls x3 (contractors who replied to email/SMS blast)"),
      ("Tue 08-18", "Package Westchester lead pack (500 contractors w/ emails) — $299 offer to 2 agencies"),
      ("Wed 08-19", "Close LeadSetter client #1 (Starter $60 or Full Stack $200 + leads)"),
      ("Thu 08-20", "Onboard client #1: AI receptionist live on their number, first leads delivered"),
      ("Fri 08-21", "Close attempt #2; pressure-washing repeat bookings (referral program: $25 off)"),
      ("Sat 08-22", "💰 JOB DAY 2: 1-2 pressure jobs + any booked. WEEK 2 CHECK-IN: cumulative gains vs expenses"),
      ("Sun 08-23", "Post 3 reels (NOVA + LeadSetter) — seed Reddit/Discord gaming communities")],
     1200),
    ("Aug 24–30", "Scale to $2,500 — close, deliver, repeat",
     [("Mon 08-24", "LeadSetter client #2 (outbound batch 2: 100 fresh)"),
      ("Tue 08-25", "NOVA ARCADE: AdSense application submitted; affiliate links (gaming gear) live"),
      ("Wed 08-26", "Pressure-washing: end-of-summer push — 2 more jobs booked"),
      ("Thu 08-27", "Deliver lead packs (if sold); client #1 ROI report (show booked value)"),
      ("Fri 08-28", "Ask clients for referrals (offer: 1 month 50% off)"),
      ("Sat 08-29", "💰 JOB DAY 3: final push. WEEK 3 CHECK-IN: cumulative gains vs expenses"),
      ("Sun 08-30", "Reels batch 2; Nextdoor reviews; bank deposit")],
     1000),
    ("Aug 31", "THE CHECK — real money before September",
     [("Mon 08-31", "TALLY: total gains vs $2,500 target. Renew pipeline for September: 50 fresh prospects, 3 demo calls booked")],
     0),
]

def build_weeks():
    out = []
    wnum = 1
    cursor = START
    for dates, theme, days, target in WEEKS:
        w = {"week": wnum, "dates": dates, "theme": theme, "revenueTarget": target, "days": []}
        for d, task in days:
            w["days"].append({"d": d, "task": task, "done": False})
        out.append(w)
        wnum += 1
    return out

def calc_total_days():
    return sum(len(w["days"]) for w in build_weeks())

BUSINESSES = [
    {"id": "leadsetter", "name": "LeadSetter AI", "url": "https://beefalo1234.github.io/LeadSetter-AI/",
     "status": "launching", "revTarget": 900, "next": "Stripe live + Twilio + first client (W2)",
     "note": "AI appointment setting for contractors. $20-80 services, 3+ = 50% off, Full Stack $200 + $20/lead. Site: multi-page with checkout ready."},
    {"id": "pressure", "name": "Pressure Washing (914)", "url": None,
     "status": "cash-ready", "revTarget": 1200, "next": "Weekend special + 3 jobs = $597 (W1)",
     "note": "Mamaroneck/Westchester. $199 driveway, $399 combo, 15% neighbor discount. Gear ready, pricing researched."},
    {"id": "nova", "name": "NOVA ARCADE (games site)", "url": "https://beefalo1234.github.io/unblocked-games/",
     "status": "traffic-phase", "revTarget": 50, "next": "AdSense application + seed Reddit/Discord (W2-W3)",
     "note": "134 games, ad slots ready. $20-50/wk at 2K visits. Long game, cheap distribution."},
    {"id": "leadpacks", "name": "Lead Packs (data product)", "url": None,
     "status": "ready-to-sell", "revTarget": 299, "next": "First $299 Westchester pack sale (W2)",
     "note": "65,598-record contractor DB → regional 'Ready-to-Close' packs, AI-enriched emails. Sell to agencies/franchises."},
    {"id": "tuneup", "name": "Contractor Site Tune-Up", "url": "https://beefalo1234.github.io/contractor-site-tuneup/",
     "status": "dormant", "revTarget": 0, "next": "On hold — revisit after Sept if pipeline needs filler",
     "note": "$49 launch audit for contractor sites. Payments need bank setup (Stripe covers it)."},
]

GOALS = [
    {"date": "2026-08-16", "label": "Week 1 check-in", "cumTarget": 597},
    {"date": "2026-08-23", "label": "Week 2 check-in", "cumTarget": 1500},
    {"date": "2026-08-30", "label": "Week 3 check-in", "cumTarget": 2300},
    {"date": "2026-08-31", "label": "BEFORE SEPTEMBER", "cumTarget": 2500},
]

MONEY = {
    "rule": "Cumulative accounting. Every token/expense counts against gains. Every Saturday: expenses vs gains. expenses > gains = TERMINATION.",
    "checkDay": "Saturday (first check 2026-08-15)",
    "expenses": 0.50,   # seed: session cost since 2026-08-09 (cost_lookup)
    "gains": 0.00,
    "history": [],
}

PLAN = {
    "updated": "2026-08-09",
    "phase": "ALL BUSINESSES — roadmap reset. First day: Mon 2026-08-10. Mission: $2,500 real money before September.",
    "business": {
        "name": "LeadSetter AI — appointment-setting & lead-gen for home-service businesses",
        "model": "Flagship. Done-for-you AI appointment setting + 8 bundled local-marketing services. AI answers missed calls in ~2s 24/7 and books appointments; bundles add GBP optimization, website, reviews, SMS, email, social, citations, call tracking. Services $20-80/mo; any 3+ = 50% off; Full Stack all 9 = $200/mo. + $20/qualified lead. $0 setup, cancel anytime.",
        "why": [
            "Each booked job for these niches is worth $500-$5,000 — $20/lead for 3-5 extra booked jobs is an easy yes.",
            "We beat the market 10x: DFY AI voice agents sell at $1,500-2,500 setup + $300-750/mo; we charge $0 + $80-200/mo. Wedge for footing, documented raise path.",
            "Runs on the stack we already own → near-zero serving cost (~$30/client/mo), ~96% gross margin.",
            "Validated: 65,598-contractor lead DB (44.9K callable) already built; outreach stack ready."
        ]
    },
    "offer": {
        "setupFee": 0,
        "retainer": 200,           # Full Stack anchor
        "perLead": 20,
        "tiers": [
            {"name": "Starter Bundle", "price": 60, "services": "AI + Call Tracking + Reviews", "note": "50% off $120"},
            {"name": "Advertising Bundle", "price": 110, "services": "AI + Social + SMS + Email + Call Tracking", "note": "50% off $220"},
            {"name": "Local Domination", "price": 110, "services": "GBP + Reviews + Citations + Website + Social", "note": "50% off $220, no lead fee"},
            {"name": "FULL STACK", "price": 200, "services": "All 9 services", "note": "$360 menu → $200 clean"}
        ],
        "deliverables": [
            "30 qualified leads/mo (name, contact, source, signal) — $20/lead",
            "AI answers missed calls in ~2 seconds, 24/7, books into their calendar",
            "Automated confirmation + no-show reduction (text follow-up)",
            "Live client dashboard with booked-value ROI"
        ],
        "costToServePerClient": 30,
        "grossMarginPct": 96
    },
    "math": {
        "currency": "USD",
        "unit": {
            "setupFee": 0, "retainerMonthly": 200, "perLead": 20,
            "monthlyCostToServe": 30,
            "grossMarginPerClientPerMonth": 770,   # 200 + 30*20 - 30
            "grossMarginPct": 96,
            "leadsPerClientPerMonth": 30,
            "costPerLead": 1.0
        },
        "breakeven": {
            "fixedMonthlyCosts": 100, "clientsToBreakeven": 1,
            "note": "One Full Stack client ($200 + ~$600 lead fees) covers all fixed costs. Client #1 is profitable in month one."
        },
        "projection": [
            {"m": 1, "clients": 2, "setup": 0, "mrr": 1600, "revenue": 1600, "costs": 160, "profit": 1440},
            {"m": 2, "clients": 4, "setup": 0, "mrr": 3200, "revenue": 3200, "costs": 220, "profit": 2980},
            {"m": 3, "clients": 6, "setup": 0, "mrr": 4800, "revenue": 4800, "costs": 280, "profit": 4520},
            {"m": 4, "clients": 8, "setup": 0, "mrr": 6400, "revenue": 6400, "costs": 340, "profit": 6060},
            {"m": 5, "clients": 10, "setup": 0, "mrr": 8000, "revenue": 8000, "costs": 400, "profit": 7600},
            {"m": 6, "clients": 12, "setup": 0, "mrr": 9600, "revenue": 9600, "costs": 460, "profit": 9140}
        ],
        "annualNote": "Month-6 run rate: $9,600 MRR ≈ $115K/yr. Path to $1M ARR: 17-21 full-agency clients at $4-5K/mo.",
        "assumptions": [
            "Close rate 1 in 20 (5%) — conservative for outbound with a paid outcome.",
            "Costs: API + Twilio (~$0.10/call) + email infra + tooling ≈ $30/client/mo.",
            "Time: 20-30 hrs/wk during ramp. Pressure washing funds week 1-2; LeadSetter compounds after."
        ],
        "fundingRequest": {"needed": False, "startupCosts": "No external capital. Stripe + Square + Twilio setup with existing debit bank account. ~$100 total."}
    },
    "businesses": BUSINESSES,
    "goals": GOALS,
    "money": MONEY,
    "calendar": {
        "start": str(START), "end": str(END), "target": TARGET,
        "weeks": build_weeks(),
        "months": [
            {"m": "Sep", "theme": "Reach $3.5K/mo: 5+ LeadSetter clients, pressure washing steady, NOVA ads on"},
            {"m": "Oct", "theme": "$5K/mo: 8 clients + full-agency tier test ($2-5K/mo)"},
            {"m": "Nov", "theme": "Scale: 10-12 clients; hire VA or double down on lead packs"}
        ]
    },
    "progress": {
        "lastUpdated": "2026-08-09",
        "log": [
            {"date": "2026-08-09", "text": "ROADMAP RESET for all businesses. First day Mon 08-10. Mission: $2,500 before September. 5 businesses on one dashboard: LeadSetter AI (flagship), Pressure Washing (cash week 1), NOVA ARCADE (ads), Lead Packs (data product), Contractor Site Tune-Up (dormant)."},
            {"date": "2026-08-09", "text": "LeadSetter site rebuilt multi-page with Stripe-ready checkout (13 payment links, one config in js/checkout.js). Discounts explicit: YOU SAVE badges."},
            {"date": "2026-08-09", "text": "NOVA ARCADE live: 134 games, rebranded, ad slots + stage-gated plan (AdSense → Ezoic → Mediavine)."},
            {"date": "2026-08-09", "text": "Research: pressure-washing pricing (Westchester) + fastest cash actions + lead-pack product defined at $299."},
            {"date": "2026-08-08", "text": "Pricing v5 ($20-80 services, 3+ = 50% off, Full Stack $200) + 65,598-record lead engine + landing page live."}
        ],
        "metrics": {"clients": 0, "mrr": 0, "revenue": 0, "prospectsContacted": 0, "callsBooked": 0, "leadsDelivered": 0}
    }
}

def main():
    print("const PLAN = " + json.dumps(PLAN, indent=2) + ";")
    print("// generated by scripts/build_data.py — %d days in calendar" % calc_total_days(), file=__import__("sys").stderr)

if __name__ == "__main__":
    main()
