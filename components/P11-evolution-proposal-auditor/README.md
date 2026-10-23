# P11 · evolution-proposal-auditor

> 机制簇：自进化安全护栏

## 费曼三层

- **L0（12 岁能懂）**：AI 提交'我要改自己'的方案时，先算出这改动有多危险。
- **L1（机制本质）**：按 diff 启发式打分：删测试/删断言/大范围改/加裸 except 等加分，越危险分越高。
- **L2（怎么用上）**：audit(diff_text) 返回 risk 0-100。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P11 © 2026 chenhz01`。
