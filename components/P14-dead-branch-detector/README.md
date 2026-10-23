# P14 · dead-branch-detector

> 机制簇：静默失败猎手

## 费曼三层

- **L0（12 岁能懂）**：有些代码永远跑不到，还占地方骗人。这个工具找出来。
- **L1（机制本质）**：检测 if False/if 0 常量分支与 return 之后的不可达语句。
- **L2（怎么用上）**：find(code) 返回可疑行号。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P14 © 2026 chenhz01`。
