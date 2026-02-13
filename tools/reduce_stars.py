import json
import os

def main():
    os.makedirs("data", exist_ok=True)

    # 読み込み
    with open("data/stars_raw.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    stars = raw.get("hipstars", [])

    reduced = []

    for s in stars:
        # 必要なキーだけ抽出
        if all(k in s for k in ["hip", "ra", "de", "mag"]):
            reduced.append({
                "h": int(s["hip"]),     # HIP番号
                "r": float(s["ra"]),    # 赤経
                "d": float(s["de"]),    # 赤緯
                "m": float(s["mag"]),   # 等級
            })

    # 等級順にソート（明るい順）
    reduced.sort(key=lambda x: x["m"])

    # 保存（超軽量フォーマット）
    with open("data/stars_min.json", "w", encoding="utf-8") as f:
        json.dump(reduced, f, separators=(",", ":"), ensure_ascii=False)

    print(f"Reduced: {len(reduced)} stars saved.")

if __name__ == "__main__":
    main()
