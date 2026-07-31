# Harness 设计说明

## 核心思想

这个框架不把“论文写作”看成单一任务，而是分离为：

1. 项目理解与实验溯源；
2. 章节结构设计；
3. 正式正文写作；
4. 全局一致性与证据审计。

## 为什么不能只依赖超长 System Prompt

稳定规则放在 `AGENTS.md`；重复流程放在 `.agents/skills/`；论文状态放在 `internal/`；确定性检查放在 `.codex/hooks/`。这样可以减少超长会话、上下文压缩和局部编辑造成的状态漂移。

## 外部记忆

- `PAPER_CONTRACT.yaml`：论文的中心问题、贡献、边界和披露政策；
- `SECTION_CONTRACTS.yaml`：各章节职责和依赖；
- `CLAIM_LEDGER.yaml`：claim、强度、证据和允许出现位置；
- `TERMINOLOGY.yaml`：标准术语、符号和禁用变体；
- `STALE_SECTIONS.yaml`：局部修改后需要复核的章节；
- `EVIDENCE_INDEX.yaml` 与 `results/manifest.yaml`：结果来源及验证状态。

## 写作门禁

`DESIGN_PREVIEW` 与 `APPLY_PREVIEW` 的分离是最重要的门禁。预览再流畅，也不自动成为正式正文。正式写入必须有明确批准的 preview ID 或精确修改指令。

## Agent 分工

只允许主 Agent 修改 `paper/`。一致性、证据、publication boundary、notation 和重复检查可交给只读 reviewer。避免多个 Agent 并行编辑重叠章节。

## Hooks 的定位

Hooks 适合查路径、TODO、禁用术语、引用键、重复文本和明显 evidence 状态问题。它们不能判断复杂科学结论是否真实，因此只作为 guardrail，不作为自动审稿人。
