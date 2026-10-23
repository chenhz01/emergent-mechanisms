# P20 · predicate-world-model-runtime

> 机制簇：事件级世界模型

## 费曼三层

- **L0（12 岁能懂）**：把世界当成一串'发生了什么事'，每条事都能被检查对不对，而不是一张画。
- **L1（机制本质）**：事件驱动状态机：apply(event) 更新谓词集合，check(invariant) 验证不变式。
- **L2（怎么用上）**：w=PredicateWorldModel(); w.apply('door_open'); w.check('door_open')。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P20 © 2026 chenhz01`。
