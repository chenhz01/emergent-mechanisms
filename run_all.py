# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
import os, sys, subprocess
root = os.path.dirname(os.path.abspath(__file__))
ok = 0; fail = []
for name in sorted(os.listdir(os.path.join(root, "components"))):
    p = os.path.join(root, "components", name, "impl.py")
    if not os.path.exists(p): continue
    r = subprocess.run([sys.executable, p], capture_output=True, text=True)
    if r.returncode == 0 and "[" in r.stdout:
        ok += 1
    else:
        fail.append((name, (r.stderr or r.stdout).strip().splitlines()[-1:] ))
print(f"components OK: {ok}/55")
if fail:
    print("FAILED:", fail); sys.exit(1)
