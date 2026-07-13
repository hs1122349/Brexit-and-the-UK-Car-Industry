# Data

Two kinds of files live here. Read the label before you use a number.

## Official (exact figures from the cited source)

- `uk_production_2022.csv` — UK car, commercial vehicle, and engine output for 2022, plus employment and export revenue. Source: Society of Motor Manufacturers and Traders (SMMT), 2023.
- `fta_count_post_brexit.csv` — count of free trade agreements signed after Brexit, with six named examples. Source: as compiled in the underlying research report, referencing UK government FTA records.

## Reconstructed (shape only, not the exact published series)

- `uk_eu_trade_index_2016_2023.csv` — annual index (2016 = 100) built from a small set of anchor points and a smooth interpolation. It follows the trend the UK Office for National Statistics described: a drop of roughly half in UK-EU trade shortly after the 2020 transition period, then a gradual climb back. The exact £ figures live in the ONS release, not here.
- `lse_auto_companies_index_2004_2021.csv` — annual index (2004 = 100) following the direction reported by the London Stock Exchange via Statista: a fall in listed automotive and parts companies after the 2016 referendum. The exact company counts live in the original Statista chart, not here.
- `global_ev_stock_2005_2022.csv` — annual index tracking the steep, well-documented rise in global EV and plug-in hybrid ownership over this period, per AIE data via Statista. The exact vehicle counts live in the original chart, not here.

## Why reconstruct instead of scrape

Statista and the ONS release detailed series behind paywalls or in formats this project does not have direct access to. Rebuilding the documented shape, with the method spelled out in `src/reconstruct.py`, lets the analysis run end to end and stay honest about which numbers are real and which are illustrations.
