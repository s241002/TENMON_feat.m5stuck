import json
import urllib.request

API = "https://www.astropical.space/api.php?table=stars&magmax=5&limit=5000&format=json"

def fetch(magmax=5, limit=5000):
    url = API.format(magmax=magmax, limit=limit)

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (GitHub Actions)"
        }
    )

    with urllib.request.urlopen(req) as r:
        raw = r.read().decode("utf-8")

    return json.loads(raw)


def main():
    magmax = 5
    limit = 6000

    data = fetch(magmax=magmax, limit=limit)

    stars = data.get("hipstars", [])
    out = []

    for s in stars:
        # 必要なキーが揃ってるものだけ
        if "hip" not in s or "ra" not in s or "de" not in s or "mag" not in s:
            continue
        out.append({
            "h": int(s["hip"]),
            "r": float(s["ra"]),
            "d": float(s["de"]),
            "m": float(s["mag"]),
        })

    # 明るい順に並べる（magnitudeが小さいほど明るい）
    out.sort(key=lambda x: x["m"])

    # 保存
    with open("data/stars_min.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

    print(f"saved: data/stars_min.json  count={len(out)}  magmax={magmax}")

if __name__ == "__main__":

    main()

