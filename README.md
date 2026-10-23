# emergent-mechanisms · EIM-1.0

**Emergent Intelligence Mechanisms** — 55 个零依赖参考实现，把 AI 系统里"自己冒出来"的能力工程化：
自适应思考路由、智能体间涌现语言、自进化安全护栏、静默失败猎手、模糊测试→形式证明、
事件级世界模型、记忆溯源、工具可供性、PRM 引导计算、反思触发、技能涌现检测、
多智能体验证、涌现能力探针、涌现拓扑规划。

## 费曼层：这是什么 / 为什么有用 / 怎么用

- **这是什么**：AI 会自发长出一些本事（自己决定想多久、彼此发展暗号、偷偷失败不吭声……）。这里把 14 类本事做成 55 个能直接跑的小工具。
- **为什么有用**：每个都是零依赖纯 Python，可嵌进自己的 agent 循环，省 token、少踩坑、能自检。
- **怎么用**：`python components/<组件>/impl.py` 直接看 demo 输出；或 `python run_all.py` 一次跑完 55 个。

## 组件索引

| ID | 组件 | 机制簇 | 一句话 |
|---|---|---|---|
| P01 | [no-think-draft-agreement-router](components/P01-no-think-draft-agreement-router/) | 自适应思考路由 | AI 有时不用细想也能答对。这个工具帮它先给个快速草稿，草稿够确定就… |
| P02 | [token-budget-thought-allocator](components/P02-token-budget-thought-allocator/) | 自适应思考路由 | 一道题里，有的步骤很难、有的很简单。这个工具把'想多久'的额度按难度… |
| P03 | [confidence-gated-reasoning-switcher](components/P03-confidence-gated-reasoning-switcher/) | 自适应思考路由 | 信心高就用快模型，信心低才换慢而准的模型。省钱又不掉质量。… |
| P04 | [cot-compression-router](components/P04-cot-compression-router/) | 自适应思考路由 | AI 思考过程很长，传给下一步时又长又费钱。这个工具把中间思考压短，… |
| P05 | [agent-lingua-compressor](components/P05-agent-lingua-compressor/) | 智能体间涌现语言 | 两个 AI 聊天时用一长串话，很费钱。这个工具让它们用缩写符号说话，… |
| P06 | [emergent-protocol-discoverer](components/P06-emergent-protocol-discoverer/) | 智能体间涌现语言 | AI 们反复说同样的话，其实可以提炼出'暗号'。这个工具从聊天记录里… |
| P07 | [symbolic-handshake-negotiator](components/P07-symbolic-handshake-negotiator/) | 智能体间涌现语言 | 两个 AI 第一次合作，先对一下彼此都懂的词，避免鸡同鸭讲。… |
| P08 | [cross-llm-message-translator](components/P08-cross-llm-message-translator/) | 智能体间涌现语言 | A 模型爱说一种格式，B 模型看不懂。这个工具把 A 的说法翻译成 … |
| P09 | [pac-gated-self-modifier](components/P09-pac-gated-self-modifier/) | 自进化安全护栏 | AI 想改自己时，先考试，考不过就不许改。防止越改越傻。… |
| P10 | [capability-regression-sentinel](components/P10-capability-regression-sentinel/) | 自进化安全护栏 | AI 升级后要复测，哪项能力退步了就报警、回滚。… |
| P11 | [evolution-proposal-auditor](components/P11-evolution-proposal-auditor/) | 自进化安全护栏 | AI 提交'我要改自己'的方案时，先算出这改动有多危险。… |
| P12 | [rollback-safe-skill-mutator](components/P12-rollback-safe-skill-mutator/) | 自进化安全护栏 | 改技能前先拍快照，改坏了能一键退回。… |
| P13 | [silent-except-scanner](components/P13-silent-except-scanner/) | 静默失败猎手 | 代码里最坑的 bug 是'出错了却装作没事'。这个工具把它们揪出来。… |
| P14 | [dead-branch-detector](components/P14-dead-branch-detector/) | 静默失败猎手 | 有些代码永远跑不到，还占地方骗人。这个工具找出来。… |
| P15 | [mock-return-spy](components/P15-mock-return-spy/) | 静默失败猎手 | 测试用的假数据偷偷跑到正式运行里，结果全是假的。这个工具抓它。… |
| P16 | [closure-faker-linter](components/P16-closure-faker-linter/) | 静默失败猎手 | 有的函数嘴上说'做完了'，其实返回个占位符。这个工具识破它。… |
| P17 | [fuzz2proof-bridge](components/P17-fuzz2proof-bridge/) | 模糊测试→形式证明 | 模糊测试找到一个让程序出错的输入，这个工具把它变成一道'数学题'，让… |
| P18 | [property-driven-proof-generator](components/P18-property-driven-proof-generator/) | 模糊测试→形式证明 | 你只写了'这个属性应该永远成立'，这个工具自动生成证明功夫的架子。… |
| P19 | [counterexample-to-lemma-miner](components/P19-counterexample-to-lemma-miner/) | 模糊测试→形式证明 | 一堆反例里藏着规律，这个工具把它们归纳成可复用的'小定理'。… |
| P20 | [predicate-world-model-runtime](components/P20-predicate-world-model-runtime/) | 事件级世界模型 | 把世界当成一串'发生了什么事'，每条事都能被检查对不对，而不是一张画… |
| P21 | [event-causality-tracker](components/P21-event-causality-tracker/) | 事件级世界模型 | 看日志里谁总在谁之前发生，猜出'因为所以'。… |
| P22 | [state-verification-oracle](components/P22-state-verification-oracle/) | 事件级世界模型 | 运行中随时问'现在世界该是什么样'，答不上就是有 bug。… |
| P23 | [sim-world-differential-tester](components/P23-sim-world-differential-tester/) | 事件级世界模型 | 让两个模拟器跑同一串操作，第一个不同的地方就是 bug 所在。… |
| P24 | [tool-use-memory-ledger](components/P24-tool-use-memory-ledger/) | 记忆巩固/溯源 | 记住'哪个工具怎么用过'，并且记得它是从哪儿知道的，防止瞎编。… |
| P25 | [drift-aware-consolidator](components/P25-drift-aware-consolidator/) | 记忆巩固/溯源 | 记忆会过时、重复。这个工具合并重复的、丢掉过时的。… |
| P26 | [cite-or-abstain-memory](components/P26-cite-or-abstain-memory/) | 记忆巩固/溯源 | 没有出处就别硬答，直接说'不知道'，比为编一个更可信。… |
| P27 | [episodic-replay-compressor](components/P27-episodic-replay-compressor/) | 记忆巩固/溯源 | 把一长串经历压成几句能回放的摘要，省地方还能重演。… |
| P28 | [tool-affordance-miner](components/P28-tool-affordance-miner/) | 工具可供性学习 | 看代码就能知道这个工具'能干什么、什么时候该用'。… |
| P29 | [api-capability-extractor](components/P29-api-capability-extractor/) | 工具可供性学习 | 从接口文档里自动读出'这个接口要什么参数'。… |
| P30 | [self-tool-forge](components/P30-self-tool-forge/) | 工具可供性学习 | 缺什么工具就现场造一个能跑的小函数。… |
| P31 | [tool-use-intent-classifier](components/P31-tool-use-intent-classifier/) | 工具可供性学习 | 听用户说什么，猜他要用哪个工具。… |
| P32 | [prm-compute-allocator](components/P32-prm-compute-allocator/) | PRM验证器引导计算 | 每步值不值得多想，用'打分员'给分来决定。… |
| P33 | [step-verifier-router](components/P33-step-verifier-router/) | PRM验证器引导计算 | 某步分数低就多展开想想，分数高就直接过。… |
| P34 | [verifier-guided-beam](components/P34-verifier-guided-beam/) | PRM验证器引导计算 | 生成很多候选，用打分员挑最好的几个留下。… |
| P35 | [self-consistency-scorer](components/P35-self-consistency-scorer/) | PRM验证器引导计算 | 同一个问题问好几遍，答案多数一致才可信。… |
| P36 | [probing-reflection-trigger](components/P36-probing-reflection-trigger/) | 反思触发 | 不是每次都反思，而是先探一探'是不是该反思了'。… |
| P37 | [stuck-detector](components/P37-stuck-detector/) | 反思触发 | AI 原地打转就提醒它换个思路。… |
| P38 | [reflection-budget-governor](components/P38-reflection-budget-governor/) | 反思触发 | 反思很贵，次数要封顶，防止无限反省。… |
| P39 | [reflection-loop-breaker](components/P39-reflection-loop-breaker/) | 反思触发 | 如果反思本身绕成一个圈，这个工具负责一脚踹出去。… |
| P40 | [skill-emergence-scanner](components/P40-skill-emergence-scanner/) | 技能涌现检测 | 代码里反复出现的套路，其实可以打包成一个'技能'。… |
| P41 | [duplicate-skill-detector](components/P41-duplicate-skill-detector/) | 技能涌现检测 | 两个技能其实干的是同一件事，留着浪费。这个工具找重复。… |
| P42 | [skill-maturity-grader](components/P42-skill-maturity-grader/) | 技能涌现检测 | 给技能打个成熟度分，知道哪个能放心用。… |
| P43 | [cross-repo-skill-harvester](components/P43-cross-repo-skill-harvester/) | 技能涌现检测 | 横扫很多仓库，把能复用的能力捞出来。… |
| P44 | [agent-output-verifier](components/P44-agent-output-verifier/) | 多智能体验证 oracle | 几个 AI 各给一个答案，交叉比对，找出那个不对劲的。… |
| P45 | [oracle-compiler-bridge](components/P45-oracle-compiler-bridge/) | 多智能体验证 oracle | 把 AI 的答案丢给编译器/检查器去判对错，不靠 AI 自评。… |
| P46 | [consensus-fork-detector](components/P46-consensus-fork-detector/) | 多智能体验证 oracle | 大家意见分裂成几派时，这个工具把派别分出来。… |
| P47 | [role-isolation-tester](components/P47-role-isolation-tester/) | 多智能体验证 oracle | 检查两个 AI 的'私密记忆'有没有互相串味。… |
| P48 | [emergence-probe-suite](components/P48-emergence-probe-suite/) | 涌现能力度量/探针 | 用几个小测试探一探：这个系统到底'长出'了什么本事。… |
| P49 | [capability-drift-meter](components/P49-capability-drift-meter/) | 涌现能力度量/探针 | 能力会不会悄悄退化？画条线看趋势。… |
| P50 | [surprise-bench](components/P50-surprise-bench/) | 涌现能力度量/探针 | 系统遇到意外的程度，也是一种'聪明'的指标。… |
| P51 | [emergent-topology-mapper](components/P51-emergent-topology-mapper/) | 涌现拓扑/规划/抽象 | 看谁跟谁常联系，画出'谁最能牵线'的关系网。… |
| P52 | [subgoal-decomposer](components/P52-subgoal-decomposer/) | 涌现拓扑/规划/抽象 | 大目标拆成小步骤，先干什么后干什么。… |
| P53 | [concept-distiller](components/P53-concept-distiller/) | 涌现拓扑/规划/抽象 | 一堆零碎概念，归出一个大类小类的树。… |
| P54 | [uncertainty-calibrator](components/P54-uncertainty-calibrator/) | 涌现拓扑/规划/抽象 | AI 说'我八成确定'时，它真的八成对吗？这个工具算差值。… |
| P55 | [causal-discoverer](components/P55-causal-discoverer/) | 涌现拓扑/规划/抽象 | 看两个事件是不是总一起出现，猜它们有没有关系。… |

## 运行

```bash
python run_all.py          # 冒烟：逐个跑 demo
python components/P13-silent-except-scanner/impl.py   # 单独跑
```

## 定位

每个 `impl.py` 是**参考实现（minimal reference implementation）**：真实可跑、逻辑真实、无外部依赖，
但刻意做小以展示机制本质。生产使用请按 README 扩展到你的场景。

## License

本项目**双许可**：

- **代码**：Apache-2.0（Apache License 2.0） — 见 [LICENSE](LICENSE)
- **规范/文档**：CC BY 4.0（Creative Commons Attribution 4.0 International） — 见 [LICENSE-SPEC](LICENSE-SPEC)

引用规范时请署名：`EIM-1.0 (emergent-mechanisms) © 2026 chenhz01, CC BY 4.0`。
详见 [NOTICE](NOTICE)。
