import os
import json

# IAU constellation line data（簡略例）
constellation_lines = {
    "Ori": [[24436,25336],[25336,27913],[27913,26207]],
    "UMa": [[67301,65378],[65378,62956],[62956,59774]],
}

def main():
    os.makedirs("data", exist_ok=True)

    out = {}
    for k,v in constellation_lines.items():
        out[k] = [{"from":a,"to":b} for a,b in v]

    with open("data/constellation_lines.json","w") as f:
        json.dump(out,f,separators=(",",":"))

    print("Saved constellation_lines.json")

if __name__ == "__main__":
    main()
