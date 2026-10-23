# P31 · tool-use-intent-classifier

> 机制簇：工具可供性学习

## 费曼三层

- **L0（12 岁能懂）**：听用户说什么，猜他要用哪个工具。
- **L1（机制本质）**：关键词重叠度打分，取最高分工具。
- **L2（怎么用上）**：classify(text, tools) → (tool, score)。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P31 © 2026 chenhz01`。
