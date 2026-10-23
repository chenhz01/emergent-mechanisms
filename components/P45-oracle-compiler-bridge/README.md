# P45 · oracle-compiler-bridge

> 机制簇：多智能体验证 oracle

## 费曼三层

- **L0（12 岁能懂）**：把 AI 的答案丢给编译器/检查器去判对错，不靠 AI 自评。
- **L1（机制本质）**：调用外部 oracle_fn 校验，返回 pass/fail + 原因。
- **L2（怎么用上）**：check(output, oracle_fn) → (bool, info)。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P45 © 2026 chenhz01`。
