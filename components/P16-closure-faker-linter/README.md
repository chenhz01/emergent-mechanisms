# P16 · closure-faker-linter

> 机制簇：静默失败猎手

## 费曼三层

- **L0（12 岁能懂）**：有的函数嘴上说'做完了'，其实返回个占位符。这个工具识破它。
- **L1（机制本质）**：检测函数体只有 return 'TODO'/pass/NotImplementedError 的伪完成。
- **L2（怎么用上）**：lint(code) 返回伪完成函数名。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P16 © 2026 chenhz01`。
