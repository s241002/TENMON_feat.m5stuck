import os
import ssl
import json
import urllib.request

# Hip Stars API (astropical.space)
API = "https://www.astropical.space/api.php?table=stars&magmax={magmax}&limit={limit}&offset={offset}&format=json"

def fetch_chunk(magmax, limit, offset):
    url = API.format(magmax=magmax, limit=limit, offset=offset)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }
    )

    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    os.makedirs("data", exist_ok=True)

    magmax = 5
    chunk = 200
    offset = 0
    all_stars = []

    print("Fetching stars ...")
    while True:
        data = fetch_chunk(magmax, chunk, offset)
        stars = data.get("hipstars", [])
        if not stars:
            break
        all_stars.extend(stars)
        offset += chunk

    # reduce to needed keys
    out = []
    for s in all_stars:
        if "hip" in s and "ra" in s and "de" in s and "mag" in s:
            out.append({
                "h": int(s["hip"]),      # HIP番号
                "r": float(s["ra"]),     # 赤経
                "d": float(s["de"]),     # 赤緯
                "m": float(s["mag"]),    # 等級
            })

    out.sort(key=lambda x: x["m"])

    with open("data/stars_min.json", "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"), ensure_ascii=False)

    print(f"Saved stars_min.json ({len(out)} stars)")

if __name__ == "__main__":
    main()
