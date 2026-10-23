# P34 · verifier-guided-beam

> 机制簇：PRM验证器引导计算

## 费曼三层

- **L0（12 岁能懂）**：生成很多候选，用打分员挑最好的几个留下。
- **L1（机制本质）**：按 scorer 分数排 top-k。
- **L2（怎么用上）**：beam(cands, scorer, k) → top-k。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P34 © 2026 chenhz01`。
