# Paper Writing Harness

一个面向 Codex/代码型写作 Agent 的学术论文写作模板，用于把论文正文、项目分析、写作预览、实验依据和长期状态分离管理。

它主要解决五类问题：

1. Agent 把本地脚本、运行流程和项目分析写进论文；
2. 局部修改造成前后矛盾、重复叙述和术语漂移；
3. 精确改写与开放式结构设计被混为一谈；
4. 流畅的 AI 预览被误认为已批准、已验证的正式论文内容；
5. Agent 通过过度表达、防御性写作和跨章节重复，把论文写成说明书或报告而不是连续学术论证。

## 两种使用方式

### 已有论文仓库

1. 用 Codex 打开已有论文仓库根目录。
2. 打开 [`prompts/INITIALIZE_EXISTING_REPOSITORY.md`](prompts/INITIALIZE_EXISTING_REPOSITORY.md)。
3. 复制全文到新的 Agent 会话。
4. 让 Agent 执行迁移、初始化外部记忆、创建 skills/hooks 并运行验证。
5. 人工检查 `git diff`，确认后再提交。

这份初始化 Prompt 默认禁止 Agent commit、push、删除未确认文件或静默改写论文科学内容。

### 新论文项目

复制或使用此仓库作为模板，然后：

1. 把论文源文件放入 `paper/`；
2. 补充 `internal/PAPER_CONTRACT.yaml`；
3. 让 Agent 根据论文草稿初始化其余外部记忆；
4. 按四种修改模式推进写作。

## 四种修改模式

| 模式 | 什么时候使用 | 是否直接改正文 |
|---|---|---|
| `EXACT_EDIT` | 已明确具体措辞、公式、顺序或局部变化 | 是，最小 diff |
| `DESIGN_PREVIEW` | 结构仍在设计，或正在对 preview PDF 做 annotation 迭代 | 否，只改 `scratch/previews/` |
| `APPLY_PREVIEW` | 已明确批准某个 preview ID + revision | 是，仅实施批准范围 |
| `AUDIT` | 检查科学一致性、重复、防御性写作、过度表达、证据、术语和泄漏 | 默认只读 |

完整操作说明见 [`docs/SINGLE_EDIT_WORKFLOW.zh-CN.md`](docs/SINGLE_EDIT_WORKFLOW.zh-CN.md)。

## DESIGN_PREVIEW：PDF 看，Markdown 改

Preview 采用双表示流程：

```text
Markdown = authoritative editable source
TeX      = generated render source
PDF      = visual review interface
```

标准循环：

```text
preview.md
→ compile preview.pdf
→ PDF annotation
→ map annotation back to Markdown
→ edit preview.md
→ regenerate TeX/PDF
→ repeat until explicit approval
```

即使 PDF annotation 精确到了一个词或一句话，只要内容仍属于未批准 preview，就继续使用 `DESIGN_PREVIEW`，不要误切换到 `EXACT_EDIT`。

快速说明见 [`docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md`](docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md)。

## AUDIT：subtraction-first

Audit 不只检查“有没有错误”，还检查论文是否说得太多。

重点寻找：

- 相邻句子或段落重复同一语义；
- 不同章节用不同措辞反复解释同一机制、贡献或 limitation；
- 已弃用历史方法通过“当前方法没有 X”的形式重新进入正文；
- 为假想 reviewer objection 写出的 disclaimer 或预防性解释；
- 一个完整论证被拆成多个短小说明书式段落。

默认修复优先级：

```text
DELETE / MERGE / COMPRESS
before
adding more explanation
```

真正影响 validity、interpretation、reproducibility 的 assumptions、limitations、boundary conditions 和 caveats 不应被误删。

## 常用入口

- 初始化已有仓库：[`prompts/INITIALIZE_EXISTING_REPOSITORY.md`](prompts/INITIALIZE_EXISTING_REPOSITORY.md)
- 精确修改模板：[`prompts/EXACT_EDIT.md`](prompts/EXACT_EDIT.md)
- 结构预览模板：[`prompts/DESIGN_PREVIEW.md`](prompts/DESIGN_PREVIEW.md)
- 应用预览模板：[`prompts/APPLY_PREVIEW.md`](prompts/APPLY_PREVIEW.md)
- 只读审计模板：[`prompts/AUDIT.md`](prompts/AUDIT.md)
- PDF Preview Review 速查：[`docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md`](docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md)
- 单次修改流程：[`docs/SINGLE_EDIT_WORKFLOW.zh-CN.md`](docs/SINGLE_EDIT_WORKFLOW.zh-CN.md)
- Review 清单：[`docs/REVIEW_CHECKLIST.zh-CN.md`](docs/REVIEW_CHECKLIST.zh-CN.md)
- Harness 原理：[`docs/HARNESS_DESIGN.zh-CN.md`](docs/HARNESS_DESIGN.zh-CN.md)

## 目录职责

```text
paper/       reviewer-facing manuscript
internal/    项目外部记忆、claim/evidence、决策和审计状态
scratch/     未批准的 preview Markdown、review PDF、annotation 决策和探索稿
results/     verified / provisional 结果与来源清单
.agents/     Codex repository-scoped skills
.codex/      可选 hooks 和静态检查脚本
```

## 最小日常流程

### 精确修改

```text
EXACT_EDIT → diff review → AUDIT → compile → commit
```

### 结构性修改

```text
DESIGN_PREVIEW Markdown
→ render PDF
→ PDF annotation
→ edit Markdown
→ regenerate PDF
→ explicit approval
→ APPLY_PREVIEW
→ AUDIT
→ compile + git diff
→ commit
```

最重要的默认规则：

- 不确定时只生成 preview，不改论文；
- Preview PDF 用来直观看，Markdown 才是修改源；
- 精确修改时锁定未指定内容，只接受最小 diff；
- 正式更新后做只读 audit；
- Audit 优先删除、合并和压缩冗余，而不是写更多防御性解释；
- 聊天记忆不是论文状态数据库，`internal/` 才是。

## 安全说明

`.codex/hooks.json` 和 `.codex/hooks/` 是参考实现。项目首次打开时，先阅读脚本再信任或启用 hooks。静态检查是启发式 guardrail，不能替代作者对科学正确性、语义重复和防御性写作的判断。
