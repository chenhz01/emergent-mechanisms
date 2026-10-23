# P25 · drift-aware-consolidator

> 机制簇：记忆巩固/溯源

## 费曼三层

- **L0（12 岁能懂）**：记忆会过时、重复。这个工具合并重复的、丢掉过时的。
- **L1（机制本质）**：按 token Jaccard 相似度合并近重复，保留置信度高者。
- **L2（怎么用上）**：consolidate(items, thr) → 合并后列表。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P25 © 2026 chenhz01`。
