# Keepway — UNHack 2026 submission

**Tagline:** Keep the road open when the flood comes.

**One-line summary:** Keepway is route, cost and schedule software for road builders that designs roads to stay open in floods, built from an engineering study of four First Nations whose only road keeps washing out.

## Problem
Many First Nations depend on a single road. In 2025–2026, floods cut off Potlotek (NS), English River / Patuanak (SK, about 500 people, about 6 days), Minegoziibe (MB) and Kashechewan (ON). Roads rarely fail everywhere: they fail at a few creek crossings and low sections. Communities know where the road goes under, but the engineering answer funders and builders need (which route, what fix, what cost, when) takes months of consultant work, so roads get patched every spring instead of fixed.

## What we found
We priced three approaches for all four communities (2026 CAD, AACE Class 5):
- Fixing the failing crossings: $1.8M–$9.9M per community
- Building new roads: $7.5M–$2.2B, and they still cross the same water
- Diversion channels and storage: $5.6M–$1.4B, and useless against river ice jams

## The product: Keepway (working prototype)
- **Keepway Planner:** load terrain, place a start and end, and get the best route plus alternatives (upgrade the existing road, lowest lifecycle cost, highest ground, shortest drive) on a map with the 1-in-100-year flood. Each option comes with a cost range, 30-year lifecycle cost, crossings sized by catchment, and a construction-season schedule with earliest, likely and delayed completion.
- **Crossing screener:** enter a community's failing crossings and get the cheapest standard fix, priced and ranked into a capital plan.
- **Business model (proposed):** contractors and engineering firms pay per seat; owners and ministries pay for a portfolio licence; First Nations use it free.

## Links
- Pitch deck: https://claude.ai/artifact/Dt48EUY96WL48FaSxxrsUL
- Keepway Planner (route + map demo): https://claude.ai/artifact/WgRWvcN6kQ8YPZVCv3uMF2
- Crossing screener: https://claude.ai/artifact/5T8fXEyM4LrDy1HimZbxLz
- Flood simulator: https://claude.ai/artifact/X3MipoMaJMY6A5BosiD7ZN

## Honest limits
- The Planner demo runs on generated terrain; it accepts real elevation data (ESRI ASCII grid) but live satellite and street maps need the product hosted outside the prototype.
- Costs are screening estimates (−50% / +100%), not quotes or stamped designs. Flood depths use a terrain-based screening method; ice jams are not modelled in the Planner.
- Pricing is proposed, not a live offer.

## Included files
Pitch summary, engineering README with decision tables, construction cost workbook, implementation timeline workbook, two graphs, a 217-entry source register, and the three prototype HTML files.
