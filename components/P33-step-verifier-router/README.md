# P33 · step-verifier-router

> 机制簇：PRM验证器引导计算

## 费曼三层

- **L0（12 岁能懂）**：某步分数低就多展开想想，分数高就直接过。
- **L1（机制本质）**：score>=thr → prune(过)，否则 expand(展开)。
- **L2（怎么用上）**：route(score, thr) → 'prune'/'expand'。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P33 © 2026 chenhz01`。
