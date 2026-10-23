# P23 · sim-world-differential-tester

> 机制簇：事件级世界模型

## 费曼三层

- **L0（12 岁能懂）**：让两个模拟器跑同一串操作，第一个不同的地方就是 bug 所在。
- **L1（机制本质）**：逐步执行两个 sim，返回首次分歧步与两侧状态。
- **L2（怎么用上）**：diff(simA, simB, actions) → (step, a, b) 或 None。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P23 © 2026 chenhz01`。
