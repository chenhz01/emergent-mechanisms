# P21 · event-causality-tracker

> 机制簇：事件级世界模型

## 费曼三层

- **L0（12 岁能懂）**：看日志里谁总在谁之前发生，猜出'因为所以'。
- **L1（机制本质）**：按时间序统计 A→B 共现，生成有向因果候选边。
- **L2（怎么用上）**：track(logs) 返回边列表 (a,b,score)。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P21 © 2026 chenhz01`。
