# P09 · pac-gated-self-modifier

> 机制簇：自进化安全护栏

## 费曼三层

- **L0（12 岁能懂）**：AI 想改自己时，先考试，考不过就不许改。防止越改越傻。
- **L1（机制本质）**：PAC 式门控：候选评分须不低于基线减 margin 才放行，margin 随样本量收缩。
- **L2（怎么用上）**：gate(cand, base, n) 返回 (allow, margin)。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P09 © 2026 chenhz01`。
