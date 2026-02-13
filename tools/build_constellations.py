import os
import json

# ★ここは任意でライブラリ化できます
# 例: constellation_lines_raw は HIP番号ペアの一覧
constellation_lines_raw = {
    "Ori": [
        [24436, 25336],
        [25336, 27913],
        [27913, 26207]
    ],
    "CMa": [
        [32349, 30438],
        [30438, 27913]
    ]
    # ... 88星座分を網羅
}

def main():
    os.makedirs("data", exist_ok=True)

    # 軽量化（必要であれば）
    data_out = {}
    for cname, lines in constellation_lines_raw.items():
        data_out[cname] = [{"from": p[0], "to": p[1]} for p in lines]

    with open("data/constellation_lines.json", "w", encoding="utf-8") as f:
        json.dump(data_out, f, separators=(",", ":"), ensure_ascii=False)

    print("Saved constellation_lines.json")

if __name__ == "__main__":
    main()
