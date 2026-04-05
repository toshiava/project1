"""西暦を和暦に変換するスクリプト。

使い方:
    python wareki.py <西暦年>

例:
    python wareki.py 2024  -> 2024年 → 令和6年
    python wareki.py 1989  -> 1989年 → 平成元年
"""

import sys

# Windows環境でも日本語を正しく出力できるようにUTF-8を強制
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# 元号テーブル: (開始西暦, 元号名) を新しい順に定義
GENGO_TABLE = [
    (2019, "令和"),
    (1989, "平成"),
    (1926, "昭和"),
    (1912, "大正"),
    (1868, "明治"),
]

EARLIEST_YEAR = GENGO_TABLE[-1][0]  # 1868


def to_wareki(year: int) -> str:
    """西暦年を和暦文字列に変換する。"""
    if year < EARLIEST_YEAR:
        raise ValueError(f"{year}年は対応範囲外です（{EARLIEST_YEAR}年以降を指定してください）。")

    for start, name in GENGO_TABLE:
        if year >= start:
            nen = year - start + 1
            nen_str = "元" if nen == 1 else str(nen)
            return f"{name}{nen_str}年"

    # ここには到達しないが念のため
    raise ValueError(f"{year}年は対応する元号が見つかりません。")


def main() -> None:
    if len(sys.argv) != 2:
        print("使い方: python wareki.py <西暦年>", file=sys.stderr)
        sys.exit(1)

    raw = sys.argv[1]
    try:
        year = int(raw)
    except ValueError:
        print(f"エラー: '{raw}' は整数ではありません。", file=sys.stderr)
        sys.exit(1)

    try:
        result = to_wareki(year)
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"{year}年 → {result}")


if __name__ == "__main__":
    main()
