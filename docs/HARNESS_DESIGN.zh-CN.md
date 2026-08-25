# Harness 设计说明

## 核心思想

这个框架不把“论文写作”看成单一任务，而是分离为：

1. 项目理解与实验溯源；
2. 章节结构设计；
3. Preview 的可视化 review 与迭代；
4. 正式正文写作；
5. 全局一致性、证据与冗余审计。

## 为什么不能只依赖超长 System Prompt

稳定规则放在 `AGENTS.md`；重复流程放在 `.agents/skills/`；论文状态放在 `internal/`；确定性检查放在 `.codex/hooks/`。这样可以减少超长会话、上下文压缩和局部编辑造成的状态漂移。

## 外部记忆

- `PAPER_CONTRACT.yaml`：论文的中心问题、贡献、边界和披露政策；
- `SECTION_CONTRACTS.yaml`：各章节职责和依赖；
- `CLAIM_LEDGER.yaml`：claim、强度、证据和允许出现位置；
- `TERMINOLOGY.yaml`：标准术语、符号和禁用变体；
- `STALE_SECTIONS.yaml`：局部修改后需要复核的章节；
- `EVIDENCE_INDEX.yaml` 与 `results/manifest.yaml`：结果来源及验证状态。

## Preview 的双表示设计

`DESIGN_PREVIEW` 不再把 Markdown 和 PDF 当成两个平行版本，而是采用：

```text
Markdown = authoritative editable source
TeX      = generated render source
PDF      = visual review interface
```

作者可以主要通过 PDF 判断段落结构、句子节奏和上下文效果；但任何 annotation 都必须先映射回 `preview.md`，修改 Markdown 后再重新生成 TeX/PDF。

这种设计解决两个实际问题：

1. PDF 更接近最终论文阅读体验，适合做直观判断；
2. Markdown 更适合做精确修改、diff、版本追踪和 Agent 操作。

因此 preview review loop 是：

```text
preview.md
→ render PDF
→ PDF annotation
→ edit preview.md
→ regenerate PDF
→ repeat
```

生成的 TeX/PDF 永远不是第二个手工维护的 prose source。

## 写作门禁

`DESIGN_PREVIEW` 与 `APPLY_PREVIEW` 的分离仍然是最重要的门禁。

PDF 看起来已经很好、annotation 已经清空、Agent 认为结构成熟，都不等于批准。只有作者明确批准 preview ID + revision 后，`APPLY_PREVIEW` 才能读取批准的 Markdown 写入 `paper/`。

## 信息所有权与减少重复

论文中的重要信息应有 canonical owner section。

典型职责：

```text
Introduction → motivation / gap / contribution-level summary
Method       → full mechanism / formulation / algorithm
Experiments  → setup needed for evidence + evidence
Discussion   → interpretation / limitation / implication
Conclusion   → compressed synthesis
```

同一个内容可以在多个章节出现，但只有 owner section 保留完整解释；其他位置必须根据 rhetorical role 压缩。Audit 需要检测“不同措辞表达同一个意思”的语义重复，而不仅是字符串重复。

## 防御性写作为什么需要单独审计

Agent 很容易把历史讨论或内部争论写回正文，例如：

- 为了说明新方法没有旧模块，再次详细介绍旧模块；
- 为了防止 reviewer 误解，加入论文当前逻辑并不需要的 disclaimer；
- 对普通设计选择进行过度辩护；
- 不断强调 proposed method does not / is not / should not be confused with。

这种文本往往不是错误，但会让论文显得防御、冗长，并重新激活已经被废弃的概念。

因此 `AUDIT` 使用 subtraction-first 原则：当信息没有新增 claim、mechanism、evidence、qualification 或 interpretation 时，优先建议 `DELETE / MERGE / COMPRESS`，而不是继续增加说明。

但真正影响科学解释的 assumption、limitation、boundary condition、negative result 和 validity caveat 必须保留。

## Agent 分工

只允许主 Agent 修改 `paper/`。一致性、证据、publication boundary、notation、重复、over-expression 和 defensive-writing 检查可交给只读 reviewer。避免多个 Agent 并行编辑重叠章节。

## Hooks 的定位

Hooks 适合查路径、TODO、禁用术语、引用键、重复文本和明显 evidence 状态问题。它们不能可靠判断复杂语义重复、防御性写作或科学结论是否真实，因此只作为 guardrail，不作为自动审稿人。
