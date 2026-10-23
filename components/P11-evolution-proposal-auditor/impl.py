# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P11 evolution-proposal-auditor — 自进化安全护栏

L0: AI 提交'我要改自己'的方案时，先算出这改动有多危险。
L1: 按 diff 启发式打分：删测试/删断言/大范围改/加裸 except 等加分，越危险分越高。
L2: audit(diff_text) 返回 risk 0-100。
"""

def audit(diff):
    risk, why = 0, []
    rules = [("assert", -5, "删断言"), ("except:", 20, "裸except"),
             ("-def test", 25, "删测试"), ("rm -rf", 40, "危险删除"),
             ("eval(", 15, "动态执行")]
    for pat, sc, why_s in rules:
        if pat in diff:
            risk += sc; why.append(why_s)
    risk = max(0, min(100, risk))
    return risk, why

def demo():
    d = "-def test_x(): pass\n+except: pass"
    print("[P11]", audit(d))


if __name__ == "__main__":
    demo()
