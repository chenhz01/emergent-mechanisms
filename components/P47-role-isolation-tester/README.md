# P47 · role-isolation-tester

> 机制簇：多智能体验证 oracle

## 费曼三层

- **L0（12 岁能懂）**：检查两个 AI 的'私密记忆'有没有互相串味。
- **L1（机制本质）**：比对两 agent 状态键交集，非空即泄漏。
- **L2（怎么用上）**：leaks(state_a, state_b) → 泄漏键。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P47 © 2026 chenhz01`。
