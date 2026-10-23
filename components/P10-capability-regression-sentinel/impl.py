# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P10 capability-regression-sentinel — 自进化安全护栏

L0: AI 升级后要复测，哪项能力退步了就报警、回滚。
L1: 比较升级前后各指标，跌幅超容差即标记 regression。
L2: check(before, after, tol) 返回退化项列表。
"""

def check(before, after, tol=0.02):
    return {k: (before[k], after[k]) for k in before
            if k in after and after[k] < before[k] - tol}

def demo():
    print("[P10]", check({"math":0.9,"code":0.8}, {"math":0.92,"code":0.75}))


if __name__ == "__main__":
    demo()
