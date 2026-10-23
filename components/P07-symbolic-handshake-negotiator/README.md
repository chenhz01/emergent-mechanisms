# P07 · symbolic-handshake-negotiator

> 机制簇：智能体间涌现语言

## 费曼三层

- **L0（12 岁能懂）**：两个 AI 第一次合作，先对一下彼此都懂的词，避免鸡同鸭讲。
- **L1（机制本质）**：取双方词表交集作为共享符号表；交集为空则回退到最小公共协议。
- **L2（怎么用上）**：handshake(a_vocab, b_vocab) 返回共享符号表。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P07 © 2026 chenhz01`。
