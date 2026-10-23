# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P12 rollback-safe-skill-mutator — 自进化安全护栏

L0: 改技能前先拍快照，改坏了能一键退回。
L1: 先 deepcopy 快照；提供 rollback 闭包；返回(mutated, rollback)。
L2: mutate(skill_dict, updater) → (new, rollback_fn)。
"""

import copy
def mutate(skill, updater):
    snap = copy.deepcopy(skill)
    new = copy.deepcopy(skill)
    updater(new)
    def rollback(): return copy.deepcopy(snap)
    return new, rollback

def demo():
    s = {"name":"t","v":1}
    new, rb = mutate(s, lambda d: d.update(v=2))
    print("[P12]", new, "->rollback", rb())


if __name__ == "__main__":
    demo()
