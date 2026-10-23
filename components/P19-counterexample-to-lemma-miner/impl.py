# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P19 counterexample-to-lemma-miner — 模糊测试→形式证明

L0: 一堆反例里藏着规律，这个工具把它们归纳成可复用的'小定理'。
L1: 按谓词名聚合反例，生成 lemma 列表。
L2: mine(cases) 返回 lemma 文本列表。
"""

def mine(cases):
    from collections import defaultdict
    g = defaultdict(list)
    for c in cases:
        g[c.split(":")[0]].append(c)
    return [f"lemma {p}_cases : \u2200 x \u2208 {{{', '.join(v)}}}, P x := by sorry"
            for p, v in g.items()]

def demo():
    print("[P19]", mine(["add:0","add:1","mul:0"]))


if __name__ == "__main__":
    demo()
