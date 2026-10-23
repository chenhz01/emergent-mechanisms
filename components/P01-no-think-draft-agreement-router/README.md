# P01 · no-think-draft-agreement-router

> 机制簇：自适应思考路由

## 费曼三层

- **L0（12 岁能懂）**：AI 有时不用细想也能答对。这个工具帮它先给个快速草稿，草稿够确定就跳过深度思考，省电省钱。
- **L1（机制本质）**：用草稿一致性分数做路由：先取若干快速草稿，若多数草稿相互一致(agreement>=阈值)则 skip_think，否则 think。
- **L2（怎么用上）**：route(drafts) 返回 'skip_think'/'think'，把它接在推理循环最前面即可。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P01 © 2026 chenhz01`。
