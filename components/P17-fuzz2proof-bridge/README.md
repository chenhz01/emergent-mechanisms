# P17 · fuzz2proof-bridge

> 机制簇：模糊测试→形式证明

## 费曼三层

- **L0（12 岁能懂）**：模糊测试找到一个让程序出错的输入，这个工具把它变成一道'数学题'，让机器去严格证明。
- **L1（机制本质）**：把反例(输入+期望+实际)转成证明器定理骨架（Lean/Rocq 风格字符串）。
- **L2（怎么用上）**：to_skeleton(name, inp, exp, act, lang) 返回证明骨架文本。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P17 © 2026 chenhz01`。
