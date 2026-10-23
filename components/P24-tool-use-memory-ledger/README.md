# P24 · tool-use-memory-ledger

> 机制簇：记忆巩固/溯源

## 费曼三层

- **L0（12 岁能懂）**：记住'哪个工具怎么用过'，并且记得它是从哪儿知道的，防止瞎编。
- **L1（机制本质）**：每条记忆带(source, confidence, ts)；cite(query) 返回带溯源的命中。
- **L2（怎么用上）**：L=MemoryLedger(); L.add(...); L.cite('deploy')。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P24 © 2026 chenhz01`。
