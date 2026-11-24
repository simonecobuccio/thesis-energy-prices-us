"""Shared paths and small helpers used by every notebook."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
CLEAN = ROOT / "data" / "clean"
FIG = ROOT / "outputs" / "figures"
DASH = ROOT / "outputs" / "dashboard"

plt.rcParams.update({"figure.figsize": (9, 4.5), "figure.dpi": 120, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.3,
                     "text.parse_math": False, "legend.title_fontsize": 0})


def distance_km(lat, lon, lats, lons):
    """Distance in km between one point and arrays of points."""
    lat, lon, lats, lons = map(np.radians, [lat, lon, lats, lons])
    a = np.sin((lats - lat) / 2) ** 2 + np.cos(lat) * np.cos(lats) * np.sin((lons - lon) / 2) ** 2
    return 6371 * 2 * np.arcsin(np.sqrt(a))


def save_fig(name):
    """Save the current matplotlib figure into outputs/figures.
    Every y-axis starts at 0, unless the data go below 0 (then 0 stays inside the axis)."""
    for ax in plt.gcf().axes:
        if ax.get_ylim()[0] > 0:
            ax.set_ylim(bottom=0)
    FIG.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIG / f"{name}.png", bbox_inches="tight")


# ---------- Market geography (used from notebook 03 on) ----------
# One "home" state per PJM zone: used for gas price, weather, renewable share and RGGI membership.
ZONE_STATE = {"AECO": "NJ", "AEP": "OH", "APS": "PA", "ATSI": "OH", "BGE": "MD", "COMED": "IL", "DAY": "OH",
              "DEOK": "OH", "DOM": "VA", "DPL": "MD", "DUQ": "PA", "EKPC": "KY", "JCPL": "NJ", "METED": "PA",
              "PECO": "PA", "PENELEC": "PA", "PEPCO": "MD", "PPL": "PA", "PSEG": "NJ", "RECO": "NJ"}
ZONES = list(ZONE_STATE)

# Capacity market: a zone pays its own LDA price if it cleared separately, else its parent area, else RTO.
EMAAC = ["AECO", "DPL", "JCPL", "PECO", "PSEG", "RECO"]
MAAC = EMAAC + ["BGE", "METED", "PENELEC", "PEPCO", "PPL"]

# Track 2: hub -> (states for gas / weather, states whose generation mix represents the hub's market)
HUBS = {"PJM West":  {"ice": "PJM WH Real Time Peak",   "state": "PA", "region": list(set(ZONE_STATE.values()) | {"WV", "DE", "DC"})},
        "Mass Hub":  {"ice": "Nepool MH DA LMP Peak",   "state": "MA", "region": ["CT", "MA", "ME", "NH", "RI", "VT"]},
        "Mid-C":     {"ice": "Mid C Peak",              "state": "OR", "region": ["OR", "WA", "ID"]},
        "Palo Verde": {"ice": "Palo Verde Peak",        "state": "AZ", "region": ["AZ", "NM", "NV"]},
        "SP15":      {"ice": "SP15 EZ Gen DA LMP Peak", "state": "CA", "region": ["CA"]}}

RGGI_STATES = ["CT", "DE", "ME", "MD", "MA", "NH", "NJ", "NY", "RI", "VT"]   # VA only 2021-01 to 2023-12

STATE_NAME = {"AL": "Alabama", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
              "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia", "ID": "Idaho",
              "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
              "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
              "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
              "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
              "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
              "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
              "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia",
              "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}
# NOAA nClimDiv numbers the 48 contiguous states alphabetically by full name: 001 = Alabama ... 048 = Wyoming
NOAA_CODE = {abbr: f"{i:03d}" for i, abbr in enumerate(sorted(STATE_NAME, key=STATE_NAME.get), start=1)}
