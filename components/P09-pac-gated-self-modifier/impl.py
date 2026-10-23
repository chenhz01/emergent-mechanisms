# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P09 pac-gated-self-modifier — 自进化安全护栏

L0: AI 想改自己时，先考试，考不过就不许改。防止越改越傻。
L1: PAC 式门控：候选评分须不低于基线减 margin 才放行，margin 随样本量收缩。
L2: gate(cand, base, n) 返回 (allow, margin)。
"""

def gate(cand, base, n, c=0.5):
    margin = c / (n ** 0.5) if n > 0 else 1.0
    return (cand >= base - margin), round(margin, 3)

def demo():
    print("[P09] small-n:", gate(0.70, 0.80, 10))
    print("[P09] large-n:", gate(0.79, 0.80, 10000))


if __name__ == "__main__":
    demo()
