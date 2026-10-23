# P05 · agent-lingua-compressor

> 机制簇：智能体间涌现语言

## 费曼三层

- **L0（12 岁能懂）**：两个 AI 聊天时用一长串话，很费钱。这个工具让它们用缩写符号说话，省好几倍。
- **L1（机制本质）**：统计高频短语→映射为符号 token，压缩后测压缩率。
- **L2（怎么用上）**：compress(text, symbols) 返回(压缩文本, 压缩率)；symbols 由 build_symbols 生成。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P05 © 2026 chenhz01`。
