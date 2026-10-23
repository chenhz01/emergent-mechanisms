# P10 · capability-regression-sentinel

> 机制簇：自进化安全护栏

## 费曼三层

- **L0（12 岁能懂）**：AI 升级后要复测，哪项能力退步了就报警、回滚。
- **L1（机制本质）**：比较升级前后各指标，跌幅超容差即标记 regression。
- **L2（怎么用上）**：check(before, after, tol) 返回退化项列表。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P10 © 2026 chenhz01`。
