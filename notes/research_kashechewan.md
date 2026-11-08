# Kashechewan First Nation: research notes (compiled 2026-11-07)

Evidence classes: **Verified primary** (government / agency / official dataset), **Reported** (news, consultant marketing pages, secondary), **Estimated** (derived by us from coordinates/data), **Unknown** (not found).
Note: CBC, APTN and Open Canada (search.open.canada.ca QP notes) pages returned HTTP 403 / connection refused to the fetch tool. Their content below comes from search-result snippets or republications (Turtle Island News / TimminsToday, CP24), and is marked Reported.

---

## 1. Hydrometric gauges (Water Survey of Canada, via ECCC GeoMet API)

**No WSC gauge is at Kashechewan.** The nearest Albany River gauges are about 100 km and 180 km upstream. Both use an **ASSUMED vertical datum**, so their stages can't be converted to m ASL or to levels at the community. At Kashechewan, flood levels are controlled by ice jams near the river mouth, so upstream open-water discharge is only a partial indicator. Hatch (2013) built its ice-jam forecasting tool on "flow records collected 200 km upstream of the community".

Kashechewan community reference point: approx. 52.29 N, 81.62 W (approximate, from the Wikipedia/airport coordinates; Estimated).

### 04HA001 Albany River near Hat Island
- Source: https://api.weather.gc.ca/collections/hydrometric-stations/items/04HA001?f=json (Verified primary, accessed 2026-11-07)
- Location: 51.3306 N, 83.8333 W. Status Active, real-time = yes, vertical datum ASSUMED.
- Drainage area (gross): **89,310 km²** per current WSC metadata. This **conflicts** with the 118,000 km² carried by R-ArcticNet/HYDAT-derived listings (https://www.r-arcticnet.sr.unh.edu/v4.0/Points/Des4347.txt, Reported). The full Albany basin is about 135,200 km² (Wikipedia / Canadian Encyclopedia, Reported). Use the WSC value of 89,310 km² and flag the discrepancy.
- Straight-line distance to Kashechewan: **about 180 km** WSW / upstream (Estimated from coordinates).
- Annual maximum discharge (instantaneous peak, m³/s): https://api.weather.gc.ca/collections/hydrometric-annual-peaks/items?STATION_NUMBER=04HA001&DATA_TYPE_EN=Discharge&PEAK_CODE_EN=Maximum (Verified primary)
  - 1965 4190; 1968 3790; 1969 6230; 1970 4730; 1971 5320; 1972 3600; 1973 3620; 1977 5040; 1978 4250; 1979 3590; 1980 5290; 1981 3050; 1982 6040; 1984 4290; 1988 4060; 1989 4620; 1990 4710; 1991 2740; **1992 8070**; 1993 3750; 1994 3370; 1999 3510; 2000 3990; 2002 4670 (partial day); 2003 4150; 2004 6000; **2006 8060 (24 Apr)**; 2007 5240; 2008 5040 (26 Apr); 2009 4770; 2013 5940; 2014 5960; 2015 4420; 2016 3460; 2017 3970; 2018 6580; 2019 5710; 2020 4040; 2022 7200; **2023 10,400 (14 May, record)**; 2024 2810.
  - 41 years of record. Maximum is 10,400 m³/s (2023-05-14). Median is about 4,420 m³/s (Estimated).
  - 2025 peak: not available in the API. The daily-mean query for Apr–May 2025 returned 0 records, presumably because the 2025 data is still provisional. Not found.
- Annual maximum water level (m, assumed datum): 1995 5.147; 1997 8.590; 1998 4.078; 1999 5.747; 2001 7.139; 2002 6.146; 2003 5.577; 2004 5.900; 2005 7.658; **2006 7.874 (19 Apr)**; 2007 5.913; 2008 6.886; 2009 6.342; 2010 3.884; 2012 7.262; 2013 5.855; 2014 7.391; 2015 8.404; 2016 5.846; 2017 5.336; 2018 6.759; 2019 7.407; 2020 6.632; **2021 8.643 (max)**; 2022 7.477; 2023 7.470; 2024 4.231. (Verified primary, same API, DATA_TYPE_EN=Water Level)

### 04HA002 Albany River above Fishing Creek Island (closest Albany main-stem gauge)
- 51.8538 N, 82.9754 W. Active, ASSUMED datum, gross drainage area **98,050 km²**. https://api.weather.gc.ca/collections/hydrometric-stations/items?bbox=-83.5,51.8,-80.5,52.8 (Verified primary)
- About **100 km** upstream of Kashechewan in straight line (Estimated).
- Annual peaks (https://api.weather.gc.ca/collections/hydrometric-annual-peaks/items?STATION_NUMBER=04HA002&PEAK_CODE_EN=Maximum, Verified primary):
  - Discharge (m³/s): 2011 6600; 2015 4890; 2016 3670; 2017 4330; 2020 4350; **2022 7410**; 2024 3010.
  - Water level (m, assumed datum): 2011 5.054; **2014 12.671 (max, 7 May)**; 2015 11.765; 2016 8.416; 2017 12.567; 2018 11.356; 2020 8.702; 2022 11.188; 2024 8.464. Water levels this high at relatively modest flows suggest ice effects (interpretation).
  - Short, gappy record (2011–2024).

### 04HA003 Stooping River above the Mouth
- 51.9306 N, 82.0155 W, 4,325 km² gross drainage area, assumed datum. This is a tributary, not the Albany main stem (Verified primary, same bbox query).

---

## 2. Flood levels and dike
- Ring dike length: **~5 km** around the community (Hatch project page https://www.hatch.com/Projects/Energy/Kashechewan-First-Nation-flood-risk-forecasting-and-mitigation; Hatch 2018 news release). Reported (engineering consultant).
- Built: **1995** (Hatch 2018 paper; CBC). Anishinabek News says completed 1997. Reported, with conflicting dates.
- Dike height / crest elevation: **Not found** in any accessible source.
- 2006: the dike was "almost overtopped" (Hatch, CBC quoting the Hatch 2015 report). The Weather Network says water came "within 0.6 m from the top of the dikes", but it is ambiguous whether this refers to Kashechewan, Fort Albany or both (https://www.theweathernetwork.com/en/news/weather/severe/this-day-in-weather-history-april-27-2008-fort-albany-flooding-and-evacuations). Reported.
- Flood stage elevations at Kashechewan for 2006/2008/2012/2014/2017/2024/2025 in m ASL: **Not found**. Only upstream assumed-datum stages exist (section 1).
- Hatch 2015 dam-safety assessment, commissioned January 2015: the ring dike was classed "very high hazard" under Ontario dam safety rules, with "intolerable risk" from its deteriorated condition (CBC 1.3016291; NDP release 31 Mar 2015). Reported.
- 2015 repair cost dispute: Canada offered **$1.14 million**. The band estimated **$4–12 million** was needed and refused the offer (CBC 2015 via search snippets). Reported.
- Hatch stabilizing berm / flood-forecasting work ran 2008–2018 and won a 2018 CCE Award of Excellence. Forecast lead time is **10 days** (Hatch). Reported.
- ISC dike repair spending 2006–2020: **Not found** (the Open Canada QP notes were unreachable).
- Long-term mitigation study: Knack et al. 2024, *Can. J. Civ. Eng.* 51(8):898–907, doi:10.1139/cjce-2023-0061. Compared dams, dykes, pier/weir ice-control structures and conveyance channels using DynaRICE. Numbers are behind the paywall. Reported (peer-reviewed abstract).

## 3. Airport (CZKE / IATA ZKE)
- ICAO identifier: **CZKE**. "CYKX" is wrong (Wikipedia citing Canada Flight Supplement 27 Nov 2025–22 Jan 2026; airport directories). Reported, citing CFS. Not checked directly against NAV CANADA.
- Elevation **35 ft (11 m) AMSL**. Reported (CFS-derived).
- Runway 06/24, gravel, **3,903 ft × 100 ft (1,190 m)** per CFS-derived infobox. Wikipedia body text and FSHub give 3,500 ft (1,067 m), so the sources conflict. Reported.
- Coordinates 52.2825 N, 81.6778 W. Operator: Government of Ontario.
- Distance to the community: Wikipedia gives "0.7 NM W" and also "approx. 4 km south", which conflict. From coordinates, the airport is about **3–4 km W/SW** of the townsite centre (Estimated).
- Airport access road length: **Not found** in any source. The coordinate estimate is about 3–4 km (Estimated).

## 4. Elevations / terrain
- Community: **"generally situated between el. 7 m and 9 m" within a flood-prone delta**. The region ranges from sea level to about el. 20 m (Hatch 2018 technical paper abstract https://www.hatch.com/About-Us/Publications/Technical-Papers/2018/06/Reducing-life-safety-risks-at-a-remote-nothern-Canadian-First-Nations-community). Reported (engineering). The datum is presumably geodetic, but the abstract doesn't say.
- Airport is 11 m AMSL (section 3).
- Terrain: Hudson Bay Lowlands. Very flat (average slope about 0.5 m/km), with more than 90% peatland/wetland (NJG review https://njgjournal.nl/index.php/njg/article/view/12883). Permafrost is discontinuous in the SE of the lowland. Kashechewan-specific geotechnical data (marine clays, permafrost presence): **Not found**.

## 5. Relocation
- Framework agreement ("Together We Work for Hope") signed by Canada, Ontario and Kashechewan FN on **9 May 2019**. A federal note gives 5 May 2019. It is not legally binding (CBC). Reported, citing QP notes.
- The 2019 timeline was 8–10 years, with a target of **2029**. A CBC article of 16 Sep 2024 quotes the federal government as saying the 2029 target "would be a challenge… but still stands". Reported.
- Site 5: north shore of the Albany River, **34 km upstream** (Colliers Project Leaders https://www.colliersprojectleaders.com/projects/kashechewan-first-nation-road-to-site-five/). CBC 2024 says "about 30 km". It is Ontario Crown land, and adding it to the reserve needs Fort Albany's agreement because the two First Nations share the Fort Albany 67 reserve. Reported.
- Road to Site 5: IAAC registry lists a **32.645 km** winter road. Phase 1 is clearing and grubbing, and phase 2 is upgrading to an all-season access road. Start date 2020-10-01, status "in progress" (https://iaac-aeic.gc.ca/050/evaluations/proj/81040). Verified primary.
- Road cost about **$3 million/km, ~$90 million** (CBC Dec 2019). Reported.
- Relocation cost: the early federal estimate was "over **$800 million**" (QP note 2019, via snippet). Media ranges are $500 million–$1 billion, the chief has cited about $750 million, and the community estimates about $1 billion. By 2024, the federal government said there was "no estimate yet". Reported.
- Status: conceptual design, moving to a construction-management delivery model (Colliers). 2025–2026 updates: **Not found**.

## 6. Costs
- Annual precautionary flood evacuations cost **$18–22 million** each (CBC/APTN, about 2019). Reported.
- The ISC QP note (Dec 2019) gives about **$9 million/yr**. Reported (snippet of a primary note that could not be fetched). The two figures conflict.
- The 2014 evacuation cost **$21 million**, reported in 2015 (CBC 1.2678622). Reported.
- 2026 water-crisis evacuation (not a flood): **$100–150 million** estimated by the community's economic development director. ISC said final costs are not known. Water system repairs cost **>$9 million** (CP24, 29 Jul 2026 https://www.cp24.com/news/canada/2026/07/29/after-7-months-kashechewan-first-nation-evacuees-finally-heading-home/). Reported.
- A TrueNorth headline (Jan 2026) claims "$242M taxpayer dollars later" for the water crisis. This is an advocacy outlet and the breakdown was not seen. Reported, low confidence.

## 7. 2025 and 2026 events
- **2025**: state of emergency and annual precautionary evacuation from mid-April (CBC 1.7509725; APTN 15 Apr 2025). On **1 May 2025**, the KFN Youth Advisory post said "at **7:13 a.m.**, our airport road was compromised and has begun to flood". Leaders said this had not been seen since 2006. Helicopters ferried people across the river to Fort Albany, which sits on slightly higher ground. Fort Albany paused its own evacuation flights to help (TimminsToday via Turtle Island News 1 May 2025 https://theturtleislandnews.com/index.php/2025/05/01/kashechewan-calls-for-helicopters-after-airport-access-cut-off-by-flooding/; APTN/CP 1 May 2025). Returns began the week of **12 May 2025** (CBC via NationTalk). Total 2025 evacuee count: not found. Reported.
- Separately, in **Feb 2025** about 200 people were sent to Thunder Bay during water treatment plant repairs (TBNewswatch). Reported.
- **2026**: water-system failure. Sewage backed up into the drinking water, and 60–90 people were sickened by cryptosporidium. A state of emergency was declared on **7 Jan 2026**, and from mid-January about **1,700** members were evacuated (Turtle Island News 14 Jan 2026; CP24 29 Jul 2026). During the spring flood season, on **20 Apr 2026**, more than 100 vulnerable residents were flown out, with only about 300 people in the community. Ice was thicker than usual after a snowy winter (TimminsToday via Turtle Island News 22 Apr 2026 https://theturtleislandnews.com/index.php/2026/04/22/were-trying-not-to-take-any-chances-potential-flooding-forces-another-evacuation/). A **full-scale mandatory flood evacuation** was declared about **29 Apr 2026**, with about 240 people remaining (CBC https://www.cbc.ca/news/canada/sudbury/kashechewan-full-scale-evacuation-9.7181654, via ILRToday snippet). Returns started around 31 Jul 2026 and from 4 Aug 2026 (CP24). So **yes, 2026 had a flood evacuation**, on top of the water-crisis evacuation. Reported.

## 8. Winter road / access
- James Bay Winter Road (Moosonee–Fort Albany–Kashechewan–Attawapiskat): **~301–312 km**, depending on source. It has about 58 water crossings, 5 of them major tidal rivers, and is run by Kimesskanemenow LP (Northern Ontario Business; TimminsToday). Reported.
- Season: construction starts in December. Colliers gives an operating window of about **February to April**, with heavy traffic usually only from early February (Reported). Barge access runs July–October, and air access is year-round (Colliers). There is **no all-season road**. A 2021 feasibility study recommended a **333 km** coastal all-season route from Moosonee (Reported). The Wetum Road is a 170 km winter route from Moosonee to Otter Rapids (Reported).

## Population
- About 2,000 residents (Hatch 2016/2018). About 2,200 (Turtle Island News Jan & Apr 2026). About 2,300 (CBC, earlier). The 2026 water evacuation moved about 1,700 people. CIRNAC Oct 2024 figures (via Wikipedia): 3,309 on reserve, 2,187 off reserve, 5,597 total. These figures appear to be for registered members, and may be mixed with Fort Albany on the shared reserve. Use with caution. Band number 243. The FNP page could not be checked.

## Database claim checks
| Claim | Verdict | Basis |
|---|---|---|
| ~2,000 on-reserve residents (2025) | **Agree (approx.)**. Reported figures are 2,000–2,200; 2,200 in 2026 news is better | Hatch; Turtle Island News 2026 |
| Annual spring breakup flood evacuations >10 years | **Agree, with caveats**. CBC calls it the "annual precautionary evacuation", with evacuations reported 2012–2019 and 2022–2026. Before about 2012 it was episodic (8 since 1976 per Hatch). 2020–2021 used COVID "on the land" alternatives, which are not confirmed | CBC 1.7509725; Hatch; CBC 1.6431209 |
| Airport road flooding ~7:13 a.m. 1 May 2025; helicopters via Fort Albany | **Agree** | TimminsToday/Turtle Island News 1 May 2025; APTN/CP 1 May 2025 |
| No year-round road; winter road only | **Agree**. Also barge Jul–Oct and air year-round | Colliers; IAAC |
| No confirmed permanent protection of airport road | **Agree (no evidence found)**. No source describes raising or protecting it | absence of evidence |
