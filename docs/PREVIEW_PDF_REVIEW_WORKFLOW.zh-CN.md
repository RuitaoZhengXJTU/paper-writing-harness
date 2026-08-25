# DESIGN_PREVIEW PDF Review 速查

这是一页式操作说明。目标是让作者主要通过 PDF 判断写作效果，但让 Agent 始终在 Markdown 中实施修改，并让每个历史 preview 都能独立定位。

## 核心规则

```text
一个新 Preview = 一个新文件夹
Markdown = source of truth
TeX      = generated render source
PDF      = visual review interface
Annotation = revision request
```

**永远不要把多个 preview 的 Markdown/TeX/PDF 堆在 `scratch/previews/` 根目录，也不要直接把 PDF/TeX 修改成另一份独立版本。**

## 第 1 轮：生成一个新的 Preview

向 Agent 使用：

```text
MODE: DESIGN_PREVIEW
```

Agent 必须先生成唯一 preview ID，推荐格式：

```text
YYYYMMDD-HHMM-<section-slug>-<short-id>
```

例如：

```text
20260825-1154-method-screening-a7f3
```

然后创建独立目录：

```text
scratch/previews/20260825-1154-method-screening-a7f3/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

同时在：

```text
scratch/previews/INDEX.md
```

登记 preview ID、目标章节、创建时间、最新 revision、状态和路径。

作者主要打开该目录里的 `render/preview.pdf` 阅读。

### 禁止的结构

```text
scratch/previews/
├── method_preview.md
├── method_preview.tex
├── method_preview.pdf
├── intro_preview.tex
├── results_preview.tex
└── ...
```

也禁止把不同 preview 放在同一个 TeX 编译工作目录里，因为 `.aux`、`.log`、`.out` 等文件会混在一起。

## 什么情况下创建新文件夹

创建新的 preview 文件夹：

- 第一次为某个目标生成 preview；
- 同一章节提出一个 materially different 的结构方案；
- 放弃旧设计、重新开始另一套设计。

继续使用同一个 preview 文件夹：

- 只是在 PDF 上 annotation；
- 调整同一设计中的句子、段落、顺序或表达；
- `R1 → R2 → R3` 的连续 review。

旧 preview 不要删除。在 `INDEX.md` 中将状态改成：

```text
APPROVED
REJECTED
SUPERSEDED
```

这样历史版本仍然可以直接定位。

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

必须先确认 PDF 属于哪个 `<preview-id>`，然后按以下顺序：

```text
PDF annotation
→ 确认 preview-id
→ 找到 paragraph anchor / marked sentence
→ 映射到该文件夹中的 preview.md
→ 该文件夹中的 decisions.md 记录解释
→ 修改该 preview.md
→ revision +1
→ 重新生成同目录 render/preview.tex
→ 重新编译同目录 render/preview.pdf
→ 更新 INDEX.md
```

禁止：

```text
PDF annotation → 直接改 preview.tex → 完成
```

也禁止：

```text
R2 → 在 scratch/previews/ 根目录创建 preview-R2.tex
```

因为这两种做法都会破坏 preview 的历史隔离。

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
<same preview folder>/preview.md R1
→ <same preview folder>/render/preview.pdf R1
→ annotation
→ preview.md R2
→ render/preview.pdf R2
→ annotation
→ preview.md R3
→ render/preview.pdf R3
```

作者可以只重点阅读每轮的新 PDF；Markdown 保留可精确编辑、可 diff、可追踪的底层版本。不同 preview 之间则由不同文件夹隔离。

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

批准后，把 `INDEX.md` 对应行状态改为 `APPROVED`。

## APPLY_PREVIEW 时

Agent 必须从批准目录中的 `preview.md` 写入正式论文，不能从 PDF/TeX 反向复制。

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
