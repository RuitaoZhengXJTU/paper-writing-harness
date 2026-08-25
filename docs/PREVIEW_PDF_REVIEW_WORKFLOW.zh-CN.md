# DESIGN_PREVIEW PDF Review 速查

这是一页式操作说明。目标是让作者主要通过 PDF 判断写作效果，但让 Agent 始终在 Markdown 中实施修改。

## 核心规则

```text
Markdown = source of truth
TeX      = generated render source
PDF      = visual review interface
Annotation = revision request
```

**永远不要直接把 PDF/TeX 修改成另一份独立版本。**

## 第 1 轮：生成 Preview

向 Agent 使用：

```text
MODE: DESIGN_PREVIEW
```

Agent 应生成：

```text
scratch/previews/<preview-id>/
├── preview.md
├── render/preview.tex
├── render/preview.pdf
└── review/decisions.md
```

作者主要打开 `render/preview.pdf` 阅读。

## PDF 上怎么批注

直接在 PDF 对具体内容 annotation，例如：

- “这句话删掉”；
- “这里重复上一段”；
- “这一段应该合并”；
- “这里不要再解释历史方法”；
- “这个 claim 太强”；
- “这句话换成更正式的表述”；
- “把这个解释提前到上一段”；
- “这里缺少一个已经存在的结果支撑”。

不需要为了方便 Agent 而先手动去找 Markdown 行号。

## Agent 收到 PDF annotation 后

必须按以下顺序：

```text
PDF annotation
→ 找到 paragraph anchor / marked sentence
→ 映射到 preview.md
→ decisions.md 记录解释
→ 修改 preview.md
→ revision +1
→ 重新生成 TeX
→ 重新编译 PDF
```

禁止：

```text
PDF annotation → 直接改 preview.tex → 完成
```

因为这会造成 Markdown 与 PDF 两个版本逐渐分叉。

## Annotation 状态

每条批注标记：

```text
ACCEPTED
PARTIAL
REJECTED
BLOCKED
```

如果批注会加入无证据 claim、违反 locked decision 或破坏全局一致性，Agent 应说明问题，而不是机械执行。

## 多轮 Review

```text
preview.md R1
→ PDF R1
→ annotation
→ preview.md R2
→ PDF R2
→ annotation
→ preview.md R3
→ PDF R3
```

作者可以只重点阅读每轮的新 PDF；Markdown 保留可精确编辑、可 diff、可追踪的底层版本。

## 如何正式批准

只有明确发送：

```text
APPROVED PREVIEW:
- Preview ID: <id>
- Revision: R3
```

才允许进入：

```text
MODE: APPLY_PREVIEW
```

以下表达默认不算批准：

- “这版好多了”；
- “没什么问题”；
- “PDF 看起来可以”；
- 本轮没有新 annotation。

## APPLY_PREVIEW 时

Agent 必须从批准的 `preview.md` 写入正式论文，不能从 PDF/TeX 反向复制。

写入后运行 `AUDIT`。

## AUDIT 最值得优先看的三件事

### 1. 是否说太多

问：删掉这句话后，是否损失新的 claim、mechanism、evidence、qualification 或 interpretation？

如果没有，优先删或压缩。

### 2. 是否在防御历史版本

问：一个第一次读这篇论文的 reviewer 是否真的需要知道这个被弃用的方法、内部迭代或“不包含 X”的解释？

如果不需要，就不应通过“当前方法没有 X”让 X 继续留在正文里。

### 3. 是否在多个章节重复同一件事

为每个信息指定一个 canonical owner：

```text
Introduction → why / gap / contribution summary
Method       → how / full mechanism
Experiments  → evidence
Discussion   → interpretation / limitation
Conclusion   → compressed synthesis
```

其他地方只保留当前 rhetorical role 真正需要的压缩版本。
