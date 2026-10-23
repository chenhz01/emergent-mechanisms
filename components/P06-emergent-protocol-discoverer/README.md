# P06 · emergent-protocol-discoverer

> 机制簇：智能体间涌现语言

## 费曼三层

- **L0（12 岁能懂）**：AI 们反复说同样的话，其实可以提炼出'暗号'。这个工具从聊天记录里自动找出这些暗号。
- **L1（机制本质）**：从日志抽取高频 n-gram 作为候选协议 token，按频次与长度打分。
- **L2（怎么用上）**：discover(logs, k) 返回候选协议 token 列表。

## 运行

```bash
python impl.py
```

## License

代码 Apache-2.0（见仓库根 LICENSE）；本说明文档 CC BY 4.0（见 LICENSE-SPEC）。
署名：`EIM-1.0 · P06 © 2026 chenhz01`。
