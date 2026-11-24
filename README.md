# Data centers and wholesale electricity prices in the US

Code, data and outputs of the MSc thesis "Data Centers and Wholesale Electricity Prices in the US: How Much of the 2019-2026 Increase Can Be Attributed to Data Center Load Growth?" (Simone Cobuccio, Davide Tissino, MSc in Business Analytics and Data Science, POLIMI Graduate School of Management, 2025/2026).

The thesis estimates which share of the increase in the all-in wholesale price (energy + capacity) between 2019-21 and the latest twelve months (August 2025 - July 2026) can be attributed to data centers in PJM. The answer is a range: 43% / 63% / 85% in Dominion (Virginia) and 12% / 41% / 64% in the rest of PJM.

## Folders

| Folder               | Content                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data/raw/`          | Original inputs: data center lists (Cleanview, Brockovich, IM3), hub prices, load, gas, weather, generation, CPI and a few small hand-made tables in `manual/` (capacity prices, large-load adjustments, county-to-zone map, RGGI auctions, events). Sources are listed in `data/raw/README.md`. The PJM day-ahead prices (`pjm_lmp/`) and the source reports (`reports/`) are not included in this repository: see *How to run*. |
| `data/clean/`        | The unified data center list (`dc_unified.csv`), the zone and hub panels (`.parquet`), the model results and the final answer (`final_answer.csv`).                                                                                                                                                                                                                                                                               |
| `notebooks/`         | The eight notebooks of the analysis, plus `utils.py` with the shared paths, zone and hub lists and plot style.                                                                                                                                                                                                                                                                                                                    |
| `outputs/figures/`   | The figures used in the thesis.                                                                                                                                                                                                                                                                                                                                                                                                   |
| `outputs/dashboard/` | `dc_dashboard.html`, the interactive map of US data centers                                                                                                                                                                                                                                                                                                                                                                       |
| `report/`            | The thesis (`Thesis_Cobuccio_Tissino.pdf`) and the slides of the defense (`Slideshow_Cobuccio_Tissino.pdf`).                                                                                                                                                                                                                                                                                                                      |

## Notebooks

| Notebook               | What it does                                                                     | Main output                                                 |
| ---------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `01_DC_List`           | Merges the data center sources, removes duplicates, keeps sites of 10 MW or more | `dc_unified.csv`                                            |
| `02_Dashboard`         | Updates the dashboard with the latest list                                       | `dc_dashboard.html`                                         |
| `03_Zone_Panel`        | Builds the zone-month and hub-month panels                                       | `panel_zone_month.parquet`, `panel_hub_month.parquet`       |
| `04_EDA`               | Descriptive figures                                                              | Figures of Chapters 1 and 2                                 |
| `05_DiD`               | Difference-in-differences, event studies and regression tables                   | `did_track1.csv`, `did_track2.csv`, `regression_tables.csv` |
| `06_synthetic_control` | Synthetic Dominion and placebo test                                              | `synthetic_dom.csv`, `synthetic_summary.csv`                |
| `07_dml`               | Double Machine Learning                                                          | `dml_results.csv`                                           |
| `08_decomposition`     | Decomposition and final range                                                    | `final_answer.csv`                                          |

## How to run

1. Download the PJM day-ahead prices (see *Notes*). From [PJM Data Miner 2](https://dataminer2.pjm.com), feed *Day-Ahead Hourly LMPs* (`da_hrl_lmps`), filter on type `ZONE` and export 2019-01-01 to 2026-10-02 as CSV. Save the files, gzipped, in `data/raw/pjm_lmp/` with names starting with `pjm_da_hrl_lmps_zone_` (e.g. `pjm_da_hrl_lmps_zone_2019-01-01_2019-12-31.csv.gz`). Splitting the period into several files is fine: notebook 03 reads all of them, drops duplicates and keeps the rows with `row_is_current = True`.
2. Install the packages (tested with Python 3.10): `pip install -r requirements.txt`
3. Run the notebooks in order, from `01` to `08`. Each one reads from `data/raw` or `data/clean` and writes to `data/clean` or `outputs`; no notebook downloads data. The whole pipeline takes less than a minute.

Notebooks 04 to 08 only need `data/clean`, so they can be run without step 1. With the versions in `requirements.txt` the notebooks reproduce the files in `data/clean` and `outputs` (up to floating-point differences in the last decimals across machines, and the build date printed in the dashboard).

## Notes

- PJM price data come from PJM Data Miner and are for internal use only: they are not redistributed here and must be downloaded as described above. The reports in `data/raw/reports/` (PJM auction and load reports, Market Monitor analyses, JLARC, LBNL) are public and are listed in the bibliography of the thesis.
- The data center list is incomplete outside Virginia, and start years are available mainly for Virginian sites (see Section 2.4 of the thesis).

## License

The code (notebooks and `utils.py`) is released under the MIT License (see `LICENSE`). The thesis and the slides in `report/` are © 2026 Simone Cobuccio and Davide Tissino, all rights reserved. Third-party data in `data/raw/` remain subject to the terms of their original sources.
