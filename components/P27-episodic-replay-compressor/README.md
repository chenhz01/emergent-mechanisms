# P27 · episodic-replay-compressor

> 机制簇：记忆巩固/溯源

## 费曼三层

- **L0（12 岁能懂）**：把一长串经历压成几句能回放的摘要，省地方还能重演。
- **L1（机制本质）**：按事件类型去重后按时间拼接，截断到 max_len。
- **L2（怎么用上）**：compress(events, max_len) → 摘要字符串。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P27 © 2026 chenhz01`。
