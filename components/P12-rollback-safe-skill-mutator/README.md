# P12 · rollback-safe-skill-mutator

> 机制簇：自进化安全护栏

## 费曼三层

- **L0（12 岁能懂）**：改技能前先拍快照，改坏了能一键退回。
- **L1（机制本质）**：先 deepcopy 快照；提供 rollback 闭包；返回(mutated, rollback)。
- **L2（怎么用上）**：mutate(skill_dict, updater) → (new, rollback_fn)。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P12 © 2026 chenhz01`。
