import csv
import json

INPUT = "data/hygdata_v3.csv"
OUTPUT = "data/stars_min.json"

def main():
    stars = []

    with open(INPUT, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            mag = row.get("mag")
            ra = row.get("ra")
            dec = row.get("dec")

            if not mag or not ra or not dec:
                continue

            try:
                mag = float(mag)
                ra = float(ra)
                dec = float(dec)
            except:
                continue

            if mag <= 5.0:
                stars.append({
                    "h": row.get("hip", ""),
                    "r": ra,
                    "d": dec,
                    "m": mag
                })

    print("Stars count:", len(stars))

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(stars, f, separators=(",", ":"))

if __name__ == "__main__":
    main()
