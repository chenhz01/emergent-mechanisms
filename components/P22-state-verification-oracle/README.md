# P22 · state-verification-oracle

> 机制簇：事件级世界模型

## 费曼三层

- **L0（12 岁能懂）**：运行中随时问'现在世界该是什么样'，答不上就是有 bug。
- **L1（机制本质）**：对当前状态批量校验断言集合，返回失败项。
- **L2（怎么用上）**：verify(model, assertions) → 失败列表。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P22 © 2026 chenhz01`。
