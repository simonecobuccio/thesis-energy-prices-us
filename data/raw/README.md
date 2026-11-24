# Raw data (never edit these files)

| Folder | What | Source | Used in |
|---|---|---|---|
| dc/ | Data center lists: brockovich.csv (474), cleanview_national.csv (first 100 rows), cleanview_virginia.csv (748, VA sample), im3_atlas.csv (1,479, no MW) | brockovichdatacenter.com; cleanview.co/data-centers; IM3 Atlas v2026.02.09 (PNNL, DOI 10.57931/3017294) | 01, 02 |
| pjm_lmp/ | PJM day-ahead hourly LMP by zone, 2019-01 to 2026-10-02 (short 1-day files fill gaps; drop duplicates, keep row_is_current). **Not in the repository**: download it as explained in the main README | PJM Data Miner 2, feed da_hrl_lmps. Licence: internal use only, do not redistribute | 03 |
| hub_prices/ | Daily wholesale prices at 8 US hubs, 2019-2026 | EIA Wholesale Electricity Market Data (ICE) | 03 |
| load/ | Hourly load by PJM sub-region (EIA-930) | EIA API v2, region-sub-ba-data | 03 |
| gas/ | gas_price_power_plants_by_state.xls: gas price paid by power plants by state (NG_PRI_SUM...xls) | EIA | 03 |
| weather/ | Monthly heating/cooling degree days by state | NOAA nClimDiv | 03 |
| generation/ | generation_monthly.xlsx: generation by state and fuel | EIA state data | 03, 04 |
| macro/ | CPI-U, to convert prices to 2025 dollars | FRED CPIAUCSL | 03 |
| manual/ | Small hand-made tables: capacity prices by area (from BRA reports), large-load adjustments (from PJM load reports), county to PJM zone, RGGI auction prices (rggi.org), event calendar | see reports/ and the sites named | 03, 05, 08 |
| reports/ | PDFs behind the manual tables + IMM, LBNL, JLARC reports for the context and the capacity slice. **Not in the repository** (public documents, see the bibliography of the thesis); not needed to run the notebooks | PJM, Monitoring Analytics, LBNL, JLARC | report, 08 |
