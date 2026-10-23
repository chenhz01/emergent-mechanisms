# P13 · silent-except-scanner

> 机制簇：静默失败猎手

## 费曼三层

- **L0（12 岁能懂）**：代码里最坑的 bug 是'出错了却装作没事'。这个工具把它们揪出来。
- **L1（机制本质）**：AST 扫描裸 except / except: pass / 空 handler。
- **L2（怎么用上）**：scan(code) 返回问题列表 (行号, 类型)。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P13 © 2026 chenhz01`。
