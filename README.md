# 白磷词库

白磷词库是从[白霜拼音](https://github.com/gaboolic/rime-frost) 1.0.3 分叉出来的 fcitx5 词库维护分支。

## 分叉原因

白霜拼音 1.0.4 版本的 fcitx5 词库基本上没法用，因此从 1.0.3 拉出独立分支进行维护。

## 维护目标

- 以 1.0.3 词库为基础长期维护
- 上游词频更新会尽可能移植
- 自行维护词频，根据实际输入体验持续调优

## 文件说明

| 文件 | 说明 |
|------|------|
| `gen.py` | fcitx5 词频调整脚本 |
| `down.txt` | 需要降频的词条配置 |
| `up.txt` | 需要升频的词条配置 |

## 使用方法

```bash
python gen.py frost_dict_for_fcitx5.txt output.txt down.txt up.txt
```

- `frost_dict_for_fcitx5.txt`：原始 fcitx5 词库文件
- `output.txt`：调整后的输出词库
- `down.txt` / `up.txt`：可选，分别指定降频、升频系数

配置格式（每行一条）：

```
词语 系数
```

例如：

```
的 10
```

在 `down.txt` 中表示该词词频除以 10；在 `up.txt` 中则表示乘以 10。
