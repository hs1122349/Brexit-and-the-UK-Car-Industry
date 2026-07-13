# Brexit and the UK Car Industry: Trade and Production Analysis

Brexit changed how the UK car industry trades with the EU. This project measures that change across five angles: EU trade volume, listed company counts, global EV growth, 2022 production output, and post-Brexit trade agreements.

**Status: mixed data.** Some numbers here are official, cited figures. Others are reconstructed shapes built to match a trend described in public sources, not the exact original series. `data/README.md` marks every file as one or the other. Read that before you quote any number from this repo.

## The five angles

1. **UK production, 2022** (`data/uk_production_2022.csv`) — official figures from the Society of Motor Manufacturers and Traders (SMMT, 2023): 775,014 cars built, 101,600 commercial vehicles, 1.5 million engines, 182,000 people in manufacturing, 780,000 across the wider sector, and £77 billion in trade revenue (10% of total UK exports).
2. **UK-EU trade volume, 2016-2023** (`data/uk_eu_trade_index_2016_2023.csv`) — a reconstructed index (2016 = 100). The UK Office for National Statistics reported that exports to and imports from the EU roughly halved shortly after the 2020 transition period, then recovered gradually. This file builds an index that follows that shape. It is not the ONS's exact export and import values.
3. **LSE-listed automotive and parts companies, 2004-2021** (`data/lse_auto_companies_index_2004_2021.csv`) — a reconstructed index tracking a real, cited trend: a fall in listed company count after the 2016 referendum (source: London Stock Exchange data via Statista, 2021). The exact company counts are in the original Statista series, not reproduced here.
4. **Global EV and plug-in hybrid stock, 2005-2022** (`data/global_ev_stock_2005_2022.csv`) — a reconstructed growth curve matching the well-documented steep rise in EV adoption over this period (source: AIE via Statista, 2023). Again, a shape, not the published figures.
5. **Post-Brexit trade agreements** (`data/fta_count_post_brexit.csv`) — 38 active free trade agreements signed after Brexit, including named deals with Japan (CEPA, signed 31 December 2020), Tunisia, Switzerland, South Africa, South Korea, and Mexico.

## Method

`src/reconstruct.py` builds the two index-style datasets from a small set of anchor points (the specific facts stated in the source material) and fills the gaps with a smooth interpolation, seeded so the output is the same every run. `src/analysis.py` computes year-over-year change, compound annual growth rate, and a simple trade-recovery ratio (post-drop volume over pre-drop volume) on any of the series.

## Repo layout
```
.
├── data/                # official figures + reconstructed indices, with a data dictionary
├── src/                 # reconstruct.py, analysis.py
├── tests/                # unit tests for the analysis functions
├── report/               # results.md, sources.md
├── run_build_data.py
├── run_analysis.py
├── requirements.txt
└── LICENSE
```

## How to run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python run_build_data.py     # writes the two reconstructed CSVs into data/
python run_analysis.py       # year-over-year change, CAGR, recovery ratio -> report/

pytest tests/                 # analysis function tests, no data files needed
```

## Headline figures

The UK built 775,014 cars in 2022 and exported the majority of them to the EU. The car sector alone brought in £77 billion, a tenth of all UK exports (SMMT, 2023). Trade with the EU fell by close to half right after the Brexit transition period ended, then climbed back over the following years without fully closing the gap (ONS, 2023). The number of automotive and parts companies listed on the London Stock Exchange fell after the 2016 referendum, a sign that investors pulled back once the outcome became real (Statista, 2021). Against that backdrop, the UK signed 38 new trade deals, including one with Japan that keeps car tariffs at zero (Government of Japan, 2020).

## Limitations, stated plainly

- Two of the five datasets are reconstructed shapes, not the original published numbers. Treat them as illustrations of a documented trend, not as a substitute for the primary source.
- The trade-index reconstruction assumes a single smooth recovery curve. Real trade data moves month to month and reacts to more than one cause at a time.
- Every underlying source is secondary. No primary survey or interview data sits behind these numbers.
- This project draws its topic and its source list from an earlier research paper on the same subject. That paper itself is not included in this repo. Only the public facts and citations it points to are reused here.

## AI use disclosed

AI helped build the reconstruction code, the analysis functions, and this README, working from the same public source list as the original paper. No paragraph of that paper was copied into this repo. Check the cited sources yourself before you rely on any number here for a real decision.

## License

MIT for the code (see `LICENSE`). The cited figures belong to their original publishers: SMMT, ONS, the London Stock Exchange via Statista, AIE via Statista, and the UK and Japanese governments.
