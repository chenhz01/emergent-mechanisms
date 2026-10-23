# P03 · confidence-gated-reasoning-switcher

> 机制簇：自适应思考路由

## 费曼三层

- **L0（12 岁能懂）**：信心高就用快模型，信心低才换慢而准的模型。省钱又不掉质量。
- **L1（机制本质）**：置信度门控：confidence>=hi 用 fast；<=lo 用 slow；中间用 medium。
- **L2（怎么用上）**：pick(confidence) 返回模型档位，接在你的模型路由处。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P03 © 2026 chenhz01`。
