import os
import csv
import json

INPUT_CSV = "data/hygdata_v3.csv"
OUTPUT_JSON = "data/stars_min.json"

def main():
    os.makedirs("data", exist_ok=True)

    stars = []

    with open(INPUT_CSV, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                mag = float(row["mag"])
            except:
                continue

            # 5等級まで
            if mag <= 5.0:
                try:
                    ra = float(row["ra"])
                    dec = float(row["dec"])
                except:
                    continue

                stars.append({
                    "h": row.get("hip", ""),  # HIP番号（空でもOK）
                    "r": ra,
                    "d": dec,
                    "m": mag
                })

    # 等級（m）が小さい順にソート
    stars.sort(key=lambda x: x["m"])

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(stars, f, separators=(",", ":"), ensure_ascii=False)

    print(f"Saved {OUTPUT_JSON} with {len(stars)} stars")

if __name__ == "__main__":
    main()
