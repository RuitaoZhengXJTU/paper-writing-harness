# 单次论文修改流程

## 1. 判断模式

### 已经知道具体怎么改：`EXACT_EDIT`

适用于已经批准的论文正文中明确的句子、公式、术语、顺序或局部段落修改。目标是最小 diff，未指定内容全部锁定。

### 只知道章节应表达什么，或仍在修改 preview：`DESIGN_PREVIEW`

用于结构设计、完整 preview prose 生成，以及所有尚未批准 preview 的 PDF annotation 迭代。这个阶段不触碰正式论文。

### 已明确批准某个 preview：`APPLY_PREVIEW`

只有当作者明确批准 preview ID + revision 后才进入。正式实现必须读取批准的 `preview.md`，而不是从 PDF 或生成的 TeX 反向抄写。

### 只做检查：`AUDIT`

默认只读。除科学一致性外，重点检查语义重复、过度表达、防御性写作、段落碎片化和信息职责漂移。

---

## 2. 编写 Prompt

每次至少写清楚：

- `MODE`：本轮模式；
- `TARGET`：文件、章节或行范围；
- `REQUIRED CHANGES` / `SECTION MUST EXPLAIN`；
- `LOCKED CONTENT`：不能改变的内容；
- `AVAILABLE VERIFIED MATERIAL`：允许使用的依据；
- `ACCEPTANCE CRITERIA`：怎样算完成；
- `GLOBAL CONSISTENCY`：关联章节只报告还是允许同步修改。

模板位于 `prompts/`。

---

## 3. Review `EXACT_EDIT`

先看 diff，而不是只读修改后的全文：

1. 是否只改了授权范围；
2. 是否误删了句子、公式、引用或段落；
3. 是否增强了结论；
4. 是否改变数字、公式编号、符号或 citation key；
5. 是否加入路径、脚本、命令或 agent 叙述；
6. 是否新增防御性解释或“为了说明没有 X 而再次讨论 X”；
7. 哪些相关章节因此 stale。

可追加指令：

```text
Show the manuscript diff only. Do not apply further edits.
Explain each nontrivial change in one sentence.
```

---

## 4. `DESIGN_PREVIEW`：一个 Preview 一个文件夹 + Markdown 设计源 + PDF 视觉 Review

### 4.1 新建 Preview 时先创建独立目录

每一个**新的** preview 都必须先生成唯一 preview ID，再创建独立目录。推荐命名：

```text
YYYYMMDD-HHMM-<section-slug>-<short-id>
```

例如：

```text
20260825-1154-method-screening-a7f3
```

然后创建：

```text
scratch/previews/20260825-1154-method-screening-a7f3/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

并同步登记：

```text
scratch/previews/INDEX.md
```

`INDEX.md` 至少记录：preview ID、目标章节、创建时间、最新 revision、状态和路径。

**禁止**把多个 preview 的 `.md`、`.tex`、`.pdf` 直接堆在 `scratch/previews/` 根目录。根目录只保留索引/说明文件和各个 preview 子目录。

同一章节出现一个 materially different 的新结构方案，也要创建新的 preview 文件夹，不能覆盖旧 preview。只有 PDF annotation 驱动的 `R1 → R2 → R3` 才继续留在同一个 preview 文件夹。

旧 preview 不删除，而在 `INDEX.md` 中标记：

```text
ACTIVE
APPROVED
REJECTED
SUPERSEDED
```

### 4.2 Preview 文件职责

- `preview.md` 是唯一权威、可编辑的 preview source；
- `render/preview.tex` 是从 Markdown 生成的中间渲染文件；
- `render/preview.pdf` 是作者主要用于视觉 review 的界面；
- `review/decisions.md` 保存每轮 annotation 的解释和处理状态。

`preview.md` 至少包括：

- preview ID + creation timestamp + revision；
- section thesis；
- paragraph cards；
- stable paragraph ID（例如 `P01`、`P02`）；
- claim–evidence 关系；
- assumptions / exclusions / missing evidence；
- complete unapproved preview prose；
- acceptance checklist。

### 4.3 生成 Review PDF

Agent 只把当前 preview 文件夹中 `preview.md` 的 preview prose 转换成独立 TeX，并编译到同一个 preview 文件夹的 `render/` 中。

Review PDF 应尽可能呈现真实论文阅读体验，同时加入轻量、仅用于 review 的 paragraph anchor，使 PDF annotation 可以稳定映射回 Markdown。

TeX 编译的 working/output directory 也必须限定在该 preview 的 `render/` 中。`.aux`、`.log`、`.out`、`.fls`、`.fdb_latexmk`、`.synctex.gz` 等辅助文件不能落到 `scratch/previews/` 根目录，也不能混入其他 preview 文件夹。

**禁止把 TeX 变成第二份人工维护的源文件。** 如果 PDF 中发现一句话需要改，不能直接只改 `.tex`；必须回到该 preview 的 `preview.md` 修改。

### 4.4 作者在 PDF 上 annotation

作者优先在 PDF 上直接圈出或批注：

- 某句太长；
- 某段逻辑不顺；
- 某个词需要替换；
- 两句话应该合并；
- 这一段不应该出现某个内容；
- 某处需要补充已有证据；
- 某段应该移动到其他位置。

这些 annotation 属于 `DESIGN_PREVIEW`，即使批注精确到了一个词或一句话，也**不要切换到 `EXACT_EDIT`**。

### 4.5 Agent 处理 annotation

第一步先确认被 annotation 的 PDF 属于哪个 preview ID，然后固定执行：

```text
读取 PDF annotation
→ 确认 preview-id
→ 映射到该 preview 的 paragraph ID / Markdown span
→ 记录该 preview 的 decisions.md
→ 修改该 preview 的 preview.md
→ 更新 revision
→ 重新生成该 preview 的 render/preview.tex
→ 重新编译该 preview 的 render/preview.pdf
→ 更新 INDEX.md
```

Agent 对每条 annotation 标记：

- `ACCEPTED`
- `PARTIAL`
- `REJECTED`
- `BLOCKED`

如果 annotation 会加入没有证据的 claim、违反 locked decision、改变证据强度或与其他章节产生已知冲突，则不能为了“服从批注”直接改写，应标记为 `PARTIAL` 或 `BLOCKED` 并说明原因。

禁止在 `scratch/previews/` 根目录创建 `preview-R2.tex`、`method-preview-2.pdf` 等松散 revision 文件。

### 4.6 多轮循环

同一个 preview 的连续 annotation 使用同一个目录：

```text
<preview-id>/preview.md R1
→ <preview-id>/render/preview.pdf R1
→ annotation
→ <preview-id>/preview.md R2
→ <preview-id>/render/preview.pdf R2
→ annotation
→ <preview-id>/preview.md R3
→ ...
```

不同设计 preview 则一定是不同目录。作者可以通过 `scratch/previews/INDEX.md` 先定位历史 preview，再打开对应 PDF。

### 4.7 批准

以下情况**都不等于批准**：

- PDF 看起来不错；
- 本轮没有 annotation；
- 作者说“这版好多了”；
- Agent 认为已经完成。

必须明确批准：

```text
APPROVED PREVIEW:
- Preview ID: <id>
- Revision: <R#>
```

只有之后才能进入 `APPLY_PREVIEW`。同时将该 preview 在 `INDEX.md` 中标记为 `APPROVED`。

---

## 5. 执行正式更新：`APPLY_PREVIEW`

预览批准后，要求 Agent：

- 从批准 preview 文件夹中的 `preview.md` 读取内容；
- 不从 PDF 或 render TeX 重新推断措辞；
- 不带入 paragraph anchors、annotation 或 review metadata；
- 只实现批准范围；
- 不添加未批准的新论点；
- 不编造证据；
- 更新 claim、section、terminology 和 stale 状态；
- 运行 publication、evidence、notation、redundancy、defensive-writing 和 consistency checks。

应用后比较：

```text
approved preview.md
vs.
implemented paper section
```

任何因为 LaTeX integration、citation、label 或上下文一致性而产生的偏差都必须明确报告。

---

## 6. 最终审计：`AUDIT`

正式更新后单独运行一次只读审计。

### 6.1 科学一致性

检查：

- unintended deletion；
- claim-strength drift；
- evidence / number consistency；
- terminology / notation；
- citation / figure / table / equation reference；
- stale dependent sections。

### 6.2 过度表达

重点找：

- 两句话实际上在表达同一个意思；
- 下一段再次总结上一段；
- contribution / motivation 被重复说多次；
- 已经显然的 implication 又被解释一遍；
- 过多 roadmap、过渡语、总结语；
- 一个完整论证被拆成多个很短的说明书式段落。

处理原则：**优先删、合并、压缩，而不是增加更多解释。**

### 6.3 防御性写作

重点找：

- 已弃用历史方法重新出现在正文；
- 为了说明“当前方法没有 X”而详细讨论 X；
- “unlike our previous version”“this should not be confused with...” 等不必要的内部版本防御；
- 反复解释 scope exclusion；
- 对普通设计选择进行过长辩护；
- 为假想 reviewer objection 写出的段落；
- 没有对应真实不确定性的过度 hedging。

但不要误删真正影响科学解释的 assumptions、limitations、boundary conditions、negative results 和 validity caveats。

### 6.4 跨章节语义重复

不能只搜索相同句子。Agent 需要判断不同措辞是否实际上在重复同一个 motivation、mechanism、contribution、result、limitation 或 implication。

为每个重复信息确定一个 canonical owner：

```text
Introduction → gap / motivation / contribution-level summary
Method       → full mechanism and formulation
Experiments  → setup required for evidence + evidence
Discussion   → interpretation / limitation / implication
Conclusion   → compressed synthesis
```

其他章节只保留与自身 rhetorical role 相匹配的压缩引用。

### 6.5 Audit 输出动作

每个 finding 指定一个主动作：

```text
KEEP
DELETE
MERGE
COMPRESS
RELOCATE
REWRITE
```

默认 `AUTOFIX: NO`。

---

## 7. 人工验收与提交

```bash
git status
git diff
# 运行项目现有论文构建命令
git add <reviewed-files>
git commit -m "Revise <section>"
```

不要默认让 Agent 自动 commit。先检查 diff、编译 PDF、audit finding、stale section，以及是否有任何未批准 preview 内容进入正式论文。

---

## 一行流程

### 精确修改

```text
EXACT_EDIT → diff review → AUDIT → compile → commit
```

### 结构性修改

```text
NEW DESIGN_PREVIEW
→ create unique preview folder + INDEX entry
→ preview.md
→ render/preview.pdf
→ PDF annotation
→ edit same preview.md
→ regenerate same preview PDF
→ repeat until explicit approval
→ APPLY_PREVIEW
→ AUDIT
→ compile + git diff
→ commit
```
