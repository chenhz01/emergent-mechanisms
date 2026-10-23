# P08 · cross-llm-message-translator

> 机制簇：智能体间涌现语言

## 费曼三层

- **L0（12 岁能懂）**：A 模型爱说一种格式，B 模型看不懂。这个工具把 A 的说法翻译成 B 能用的紧凑格式。
- **L1（机制本质）**：按显式映射表翻译内部表示字段，未知字段保守透传。
- **L2（怎么用上）**：translate(msg, mapping) 返回 B 侧可读 dict。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P08 © 2026 chenhz01`。
