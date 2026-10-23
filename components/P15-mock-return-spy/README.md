# P15 · mock-return-spy

> 机制簇：静默失败猎手

## 费曼三层

- **L0（12 岁能懂）**：测试用的假数据偷偷跑到正式运行里，结果全是假的。这个工具抓它。
- **L1（机制本质）**：检测 except 分支里 return None/常量 的'假成功'模式。
- **L2（怎么用上）**：spy(code) 返回可疑行号。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P15 © 2026 chenhz01`。
