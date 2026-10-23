# P04 · cot-compression-router

> 机制簇：自适应思考路由

## 费曼三层

- **L0（12 岁能懂）**：AI 思考过程很长，传给下一步时又长又费钱。这个工具把中间思考压短，只留关键的。
- **L1（机制本质）**：保留首步、末步与信息密度最高的 k 步，其余丢弃，按比例压缩 CoT。
- **L2（怎么用上）**：compress(steps, keep_ratio) 返回压缩后的步骤列表。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P04 © 2026 chenhz01`。
