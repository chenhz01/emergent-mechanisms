# P02 · token-budget-thought-allocator

> 机制簇：自适应思考路由

## 费曼三层

- **L0（12 岁能懂）**：一道题里，有的步骤很难、有的很简单。这个工具把'想多久'的额度按难度分给每一步，难的多想、简单的少想。
- **L1（机制本质）**：按每步不确定性归一化后分配思考预算：uncertainty 越大分配越多 token，总量守恒。
- **L2（怎么用上）**：allocate(uncertainties, total_budget) 返回每步预算列表；配合你的生成器逐段限额。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P02 © 2026 chenhz01`。
