# P39 · reflection-loop-breaker

> 机制簇：反思触发

## 费曼三层

- **L0（12 岁能懂）**：如果反思本身绕成一个圈，这个工具负责一脚踹出去。
- **L1（机制本质）**：检测状态序列中的循环 (a->b->a)，返回跳出建议。
- **L2（怎么用上）**：break_loop(seq) → bool。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P39 © 2026 chenhz01`。
