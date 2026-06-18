#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
极简 fcitx5 词频调整工具（保留原始数值格式）

用法：
    python adjust.py input.txt output.txt down.txt up.txt
"""

import sys


def load(path):
    cfg = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        cfg[parts[0]] = float(parts[1])
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass
    return cfg


def main():
    if len(sys.argv) < 3:
        print("用法: python adjust.py input.txt output.txt [down.txt] [up.txt]")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]
    down = load(sys.argv[3]) if len(sys.argv) > 3 else {}
    up = load(sys.argv[4]) if len(sys.argv) > 4 else {}

    with open(infile, "r", encoding="utf-8") as fin, open(
        outfile, "w", encoding="utf-8"
    ) as fout:
        for line in fin:
            s = line.strip()
            if not s or s.startswith("#"):
                fout.write(s + "\n")
                continue

            parts = s.split()
            if len(parts) < 3:
                fout.write(s + "\n")
                continue

            word, pinyin, raw_freq = parts[0], parts[1], parts[2]

            # 判断原始格式：不含 . 和 e 视为整数
            is_int = "." not in raw_freq and "e" not in raw_freq and "E" not in raw_freq

            try:
                if is_int:
                    freq = int(raw_freq)
                else:
                    freq = float(raw_freq)
            except ValueError:
                fout.write(s + "\n")
                continue

            # 应用升降频
            if word in down:
                freq = freq / down[word]
            if word in up:
                freq = freq * up[word]

            # 限制范围
            freq = max(0.0, min(1.0, freq)) if not is_int else max(0, int(freq))

            # 输出：整数输出整数，浮点用 str 保留精度
            if is_int:
                out_freq = int(freq)
            else:
                out_freq = freq

            fout.write(f"{word} {pinyin} {out_freq}\n")

    print("处理完成")


if __name__ == "__main__":
    main()
