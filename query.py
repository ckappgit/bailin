#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
查询 fcitx5 词库中指定词的词频。

用法：
    python query.py <词库文件> <要查询的词>
"""

import sys


def query(dict_path, word):
    found = []
    try:
        with open(dict_path, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                parts = s.split()
                if len(parts) >= 3 and parts[0] == word:
                    found.append((parts[1], parts[2]))
    except FileNotFoundError:
        print(f"文件不存在：{dict_path}")
        sys.exit(1)

    if not found:
        print(f"未找到：{word}")
    else:
        print(f"{word} 的词频：")
        for pinyin, freq in found:
            print(f"  {pinyin}\t{freq}")


def main():
    if len(sys.argv) < 3:
        print("用法: python query.py <词库文件> <要查询的词>")
        print("示例: python query.py frost_dict_for_fcitx5.txt 的")
        sys.exit(1)

    dict_path = sys.argv[1]
    word = sys.argv[2]
    query(dict_path, word)


if __name__ == "__main__":
    main()
