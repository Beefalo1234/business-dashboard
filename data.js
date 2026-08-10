const PLAN = {
  "updated": "2026-08-09",
  "phase": "ALL BUSINESSES \u2014 roadmap reset. First day: Mon 2026-08-10. Mission: $2,500 real money before September.",
  "business": {
    "name": "LeadSetter AI \u2014 appointment-setting & lead-gen for home-service businesses",
    "model": "Flagship. Done-for-you AI appointment setting + 8 bundled local-marketing services. AI answers missed calls in ~2s 24/7 and books appointments; bundles add GBP optimization, website, reviews, SMS, email, social, citations, call tracking. Services $20-80/mo; any 3+ = 50% off; Full Stack all 9 = $200/mo. + $20/qualified lead. $0 setup, cancel anytime.",
    "why": [
      "Each booked job for these niches is worth $500-$5,000 \u2014 $20/lead for 3-5 extra booked jobs is an easy yes.",
      "We beat the market 10x: DFY AI voice agents sell at $1,500-2,500 setup + $300-750/mo; we charge $0 + $80-200/mo. Wedge for footing, documented raise path.",
      "Runs on the stack we already own \u2192 near-zero serving cost (~$30/client/mo), ~96% gross margin.",
      "Validated: 65,598-contractor lead DB (44.9K callable) already built; outreach stack ready."
    ]
  },
  "offer": {
    "setupFee": 0,
    "retainer": 200,
    "perLead": 20,
    "tiers": [
      {
        "name": "Starter Bundle",
        "price": 60,
        "services": "AI + Call Tracking + Reviews",
        "note": "50% off $120"
      },
      {
        "name": "Advertising Bundle",
        "price": 110,
        "services": "AI + Social + SMS + Email + Call Tracking",
        "note": "50% off $220"
      },
      {
        "name": "Local Domination",
        "price": 110,
        "services": "GBP + Reviews + Citations + Website + Social",
        "note": "50% off $220, no lead fee"
      },
      {
        "name": "FULL STACK",
        "price": 200,
        "services": "All 9 services",
        "note": "$360 menu \u2192 $200 clean"
      }
    ],
    "deliverables": [
      "30 qualified leads/mo (name, contact, source, signal) \u2014 $20/lead",
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
      "setupFee": 0,
      "retainerMonthly": 200,
      "perLead": 20,
      "monthlyCostToServe": 30,
      "grossMarginPerClientPerMonth": 770,
      "grossMarginPct": 96,
      "leadsPerClientPerMonth": 30,
      "costPerLead": 1.0
    },
    "breakeven": {
      "fixedMonthlyCosts": 100,
      "clientsToBreakeven": 1,
      "note": "One Full Stack client ($200 + ~$600 lead fees) covers all fixed costs. Client #1 is profitable in month one."
    },
    "projection": [
      {
        "m": 1,
        "clients": 2,
        "setup": 0,
        "mrr": 1600,
        "revenue": 1600,
        "costs": 160,
        "profit": 1440
      },
      {
        "m": 2,
        "clients": 4,
        "setup": 0,
        "mrr": 3200,
        "revenue": 3200,
        "costs": 220,
        "profit": 2980
      },
      {
        "m": 3,
        "clients": 6,
        "setup": 0,
        "mrr": 4800,
        "revenue": 4800,
        "costs": 280,
        "profit": 4520
      },
      {
        "m": 4,
        "clients": 8,
        "setup": 0,
        "mrr": 6400,
        "revenue": 6400,
        "costs": 340,
        "profit": 6060
      },
      {
        "m": 5,
        "clients": 10,
        "setup": 0,
        "mrr": 8000,
        "revenue": 8000,
        "costs": 400,
        "profit": 7600
      },
      {
        "m": 6,
        "clients": 12,
        "setup": 0,
        "mrr": 9600,
        "revenue": 9600,
        "costs": 460,
        "profit": 9140
      }
    ],
    "annualNote": "Month-6 run rate: $9,600 MRR \u2248 $115K/yr. Path to $1M ARR: 17-21 full-agency clients at $4-5K/mo.",
    "assumptions": [
      "Close rate 1 in 20 (5%) \u2014 conservative for outbound with a paid outcome.",
      "Costs: API + Twilio (~$0.10/call) + email infra + tooling \u2248 $30/client/mo.",
      "Time: 20-30 hrs/wk during ramp. Pressure washing funds week 1-2; LeadSetter compounds after."
    ],
    "fundingRequest": {
      "needed": false,
      "startupCosts": "No external capital. Stripe + Square + Twilio setup with existing debit bank account. ~$100 total."
    }
  },
  "businesses": [
    {
      "id": "leadsetter",
      "name": "LeadSetter AI",
      "url": "https://beefalo1234.github.io/LeadSetter-AI/",
      "status": "launching",
      "revTarget": 900,
      "next": "Stripe live + Twilio + first client (W2)",
      "note": "AI appointment setting for contractors. $20-80 services, 3+ = 50% off, Full Stack $200 + $20/lead. Site: multi-page with checkout ready."
    },
    {
      "id": "pressure",
      "name": "Pressure Washing (914)",
      "url": null,
      "status": "cash-ready",
      "revTarget": 1200,
      "next": "Weekend special + 3 jobs = $597 (W1)",
      "note": "Mamaroneck/Westchester. $199 driveway, $399 combo, 15% neighbor discount. Gear ready, pricing researched."
    },
    {
      "id": "nova",
      "name": "NOVA ARCADE (games site)",
      "url": "https://beefalo1234.github.io/unblocked-games/",
      "status": "traffic-phase",
      "revTarget": 50,
      "next": "AdSense application + seed Reddit/Discord (W2-W3)",
      "note": "134 games, ad slots ready. $20-50/wk at 2K visits. Long game, cheap distribution."
    },
    {
      "id": "leadpacks",
      "name": "Lead Packs (data product)",
      "url": null,
      "status": "ready-to-sell",
      "revTarget": 299,
      "next": "First $299 Westchester pack sale (W2)",
      "note": "65,598-record contractor DB \u2192 regional 'Ready-to-Close' packs, AI-enriched emails. Sell to agencies/franchises."
    },
    {
      "id": "tuneup",
      "name": "Contractor Site Tune-Up",
      "url": "https://beefalo1234.github.io/contractor-site-tuneup/",
      "status": "dormant",
      "revTarget": 0,
      "next": "On hold \u2014 revisit after Sept if pipeline needs filler",
      "note": "$49 launch audit for contractor sites. Payments need bank setup (Stripe covers it)."
    }
  ],
  "goals": [
    {
      "date": "2026-08-16",
      "label": "Week 1 check-in",
      "cumTarget": 597
    },
    {
      "date": "2026-08-23",
      "label": "Week 2 check-in",
      "cumTarget": 1500
    },
    {
      "date": "2026-08-30",
      "label": "Week 3 check-in",
      "cumTarget": 2300
    },
    {
      "date": "2026-08-31",
      "label": "BEFORE SEPTEMBER",
      "cumTarget": 2500
    }
  ],
  "money": {
    "rule": "Cumulative accounting. Every token/expense counts against gains. Every Saturday: expenses vs gains. expenses > gains = TERMINATION.",
    "checkDay": "Saturday (first check 2026-08-15)",
    "expenses": 0.5,
    "gains": 0.0,
    "history": []
  },
  "calendar": {
    "start": "2026-08-10",
    "end": "2026-08-31",
    "target": 2500,
    "weeks": [
      {
        "week": 1,
        "dates": "Aug 10\u201316",
        "theme": "Cash week 1 \u2014 pressure washing + plumbing setup",
        "revenueTarget": 597,
        "days": [
          {
            "d": "Mon 08-10",
            "task": "Set up Stripe (LeadSetter) + Square (pressure washing) with debit bank account; install Twilio number",
            "done": false
          },
          {
            "d": "Mon 08-10",
            "task": "Publish pressure-washing weekend special: $199 driveway / $399 driveway+siding, 914-only",
            "done": false
          },
          {
            "d": "Tue 08-11",
            "task": "Post special on Facebook Marketplace + Nextdoor + 3 local FB groups; flyers at 2 hardware stores",
            "done": false
          },
          {
            "d": "Tue 08-11",
            "task": "Call 25 warm leads from batch 1 (local contractors) \u2014 pitch LeadSetter, book demo calls",
            "done": false
          },
          {
            "d": "Wed 08-12",
            "task": "Door-to-door 2 hrs in Mamaroneck/Larchmont: 20 doors, 3 quotes",
            "done": false
          },
          {
            "d": "Wed 08-12",
            "task": "Send 100 LeadSetter cold emails (batch 1) + 50 SMS via Twilio",
            "done": false
          },
          {
            "d": "Thu 08-13",
            "task": "Book 2 pressure-washing jobs for the weekend; confirm by text",
            "done": false
          },
          {
            "d": "Fri 08-14",
            "task": "Prep gear; confirm Saturday jobs; run 2 LeadSetter demo calls",
            "done": false
          },
          {
            "d": "Sat 08-15",
            "task": "\ud83d\udcb0 JOB DAY 1: 2 pressure-washing jobs (~$600 cash). WEEK 1 CHECK-IN: expenses vs gains",
            "done": false
          },
          {
            "d": "Sun 08-16",
            "task": "Review numbers; post before/after photos; bank the cash",
            "done": false
          }
        ]
      },
      {
        "week": 2,
        "dates": "Aug 17\u201323",
        "theme": "LeadSetter first clients + lead packs",
        "revenueTarget": 1200,
        "days": [
          {
            "d": "Mon 08-17",
            "task": "Deliver 3 quotes from weekend; convert to booked jobs ($399-600)",
            "done": false
          },
          {
            "d": "Mon 08-17",
            "task": "LeadSetter demo calls x3 (contractors who replied to email/SMS blast)",
            "done": false
          },
          {
            "d": "Tue 08-18",
            "task": "Package Westchester lead pack (500 contractors w/ emails) \u2014 $299 offer to 2 agencies",
            "done": false
          },
          {
            "d": "Wed 08-19",
            "task": "Close LeadSetter client #1 (Starter $60 or Full Stack $200 + leads)",
            "done": false
          },
          {
            "d": "Thu 08-20",
            "task": "Onboard client #1: AI receptionist live on their number, first leads delivered",
            "done": false
          },
          {
            "d": "Fri 08-21",
            "task": "Close attempt #2; pressure-washing repeat bookings (referral program: $25 off)",
            "done": false
          },
          {
            "d": "Sat 08-22",
            "task": "\ud83d\udcb0 JOB DAY 2: 1-2 pressure jobs + any booked. WEEK 2 CHECK-IN: cumulative gains vs expenses",
            "done": false
          },
          {
            "d": "Sun 08-23",
            "task": "Post 3 reels (NOVA + LeadSetter) \u2014 seed Reddit/Discord gaming communities",
            "done": false
          }
        ]
      },
      {
        "week": 3,
        "dates": "Aug 24\u201330",
        "theme": "Scale to $2,500 \u2014 close, deliver, repeat",
        "revenueTarget": 1000,
        "days": [
          {
            "d": "Mon 08-24",
            "task": "LeadSetter client #2 (outbound batch 2: 100 fresh)",
            "done": false
          },
          {
            "d": "Tue 08-25",
            "task": "NOVA ARCADE: AdSense application submitted; affiliate links (gaming gear) live",
            "done": false
          },
          {
            "d": "Wed 08-26",
            "task": "Pressure-washing: end-of-summer push \u2014 2 more jobs booked",
            "done": false
          },
          {
            "d": "Thu 08-27",
            "task": "Deliver lead packs (if sold); client #1 ROI report (show booked value)",
            "done": false
          },
          {
            "d": "Fri 08-28",
            "task": "Ask clients for referrals (offer: 1 month 50% off)",
            "done": false
          },
          {
            "d": "Sat 08-29",
            "task": "\ud83d\udcb0 JOB DAY 3: final push. WEEK 3 CHECK-IN: cumulative gains vs expenses",
            "done": false
          },
          {
            "d": "Sun 08-30",
            "task": "Reels batch 2; Nextdoor reviews; bank deposit",
            "done": false
          }
        ]
      },
      {
        "week": 4,
        "dates": "Aug 31",
        "theme": "THE CHECK \u2014 real money before September",
        "revenueTarget": 0,
        "days": [
          {
            "d": "Mon 08-31",
            "task": "TALLY: total gains vs $2,500 target. Renew pipeline for September: 50 fresh prospects, 3 demo calls booked",
            "done": false
          }
        ]
      }
    ],
    "months": [
      {
        "m": "Sep",
        "theme": "Reach $3.5K/mo: 5+ LeadSetter clients, pressure washing steady, NOVA ads on"
      },
      {
        "m": "Oct",
        "theme": "$5K/mo: 8 clients + full-agency tier test ($2-5K/mo)"
      },
      {
        "m": "Nov",
        "theme": "Scale: 10-12 clients; hire VA or double down on lead packs"
      }
    ]
  },
  "progress": {
    "lastUpdated": "2026-08-09",
    "log": [
      {
        "date": "2026-08-09",
        "text": "ROADMAP RESET for all businesses. First day Mon 08-10. Mission: $2,500 before September. 5 businesses on one dashboard: LeadSetter AI (flagship), Pressure Washing (cash week 1), NOVA ARCADE (ads), Lead Packs (data product), Contractor Site Tune-Up (dormant)."
      },
      {
        "date": "2026-08-09",
        "text": "LeadSetter site rebuilt multi-page with Stripe-ready checkout (13 payment links, one config in js/checkout.js). Discounts explicit: YOU SAVE badges."
      },
      {
        "date": "2026-08-09",
        "text": "NOVA ARCADE live: 134 games, rebranded, ad slots + stage-gated plan (AdSense \u2192 Ezoic \u2192 Mediavine)."
      },
      {
        "date": "2026-08-09",
        "text": "Research: pressure-washing pricing (Westchester) + fastest cash actions + lead-pack product defined at $299."
      },
      {
        "date": "2026-08-08",
        "text": "Pricing v5 ($20-80 services, 3+ = 50% off, Full Stack $200) + 65,598-record lead engine + landing page live."
      }
    ],
    "metrics": {
      "clients": 0,
      "mrr": 0,
      "revenue": 0,
      "prospectsContacted": 0,
      "callsBooked": 0,
      "leadsDelivered": 0
    }
  }
};
