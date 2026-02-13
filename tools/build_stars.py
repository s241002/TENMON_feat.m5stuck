import os
import json
from astroquery.vizier import Vizier

def main():
    os.makedirs("data", exist_ok=True)

    print("Downloading Hipparcos catalog...")

    Vizier.ROW_LIMIT = -1
    catalog = Vizier(columns=["HIP", "RA_ICRS", "DE_ICRS", "Vmag"])
    result = catalog.query_constraints(catalog="I/239/hip_main", Vmag="<5")

    stars = result[0]

    out = []

    for row in stars:
        if row["Vmag"] is not None:
            out.append({
                "h": int(row["HIP"]),
                "r": float(row["RA_ICRS"]),
                "d": float(row["DE_ICRS"]),
                "m": float(row["Vmag"]),
            })

    out.sort(key=lambda x: x["m"])

    with open("data/stars_min.json", "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))

    print(f"Saved stars_min.json ({len(out)} stars)")

if __name__ == "__main__":
    main()
