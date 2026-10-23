# P18 · property-driven-proof-generator

> 机制簇：模糊测试→形式证明

## 费曼三层

- **L0（12 岁能懂）**：你只写了'这个属性应该永远成立'，这个工具自动生成证明功夫的架子。
- **L1（机制本质）**：属性(forall x, P(x))→生成量词+占位证明骨架。
- **L2（怎么用上）**：gen(prop) → 骨架字符串。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P18 © 2026 chenhz01`。
