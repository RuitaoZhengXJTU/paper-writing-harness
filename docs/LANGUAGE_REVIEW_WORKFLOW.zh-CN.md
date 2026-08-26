# 论文语言审校流程

这套流程用于在不改变论文叙述逻辑的前提下，统一术语、提高表达精度、减少防御性写作，并让语言更接近事实与证据。

## 1. 先 AUDIT，不直接润色

使用：

```text
MODE: AUDIT
AUDIT PROFILE: LANGUAGE
AUTOFIX: NO
```

语言审校只提出建议，不直接修改 `paper/`。

## 2. Logic Lock

审校过程中锁定：

- 章节和段落顺序；
- 每段的 rhetorical role；
- claim 及其强度；
- 因果方向；
- evidence interpretation；
- 数字、公式、引用；
- assumptions、limitations、scope；
- 方法学含义和论证依赖。

如果某个建议需要改变这些内容，应标记 `LOGIC_REVIEW_REQUIRED`，不要把它当作语言修改。

## 3. 重点检查

### 术语

- 同一对象是否被多个名称指代；
- 不同对象是否被同一个模糊词混用；
- `predict / identify / determine` 等动词是否造成语义强度漂移；
- canonical term 是否符合 `TERMINOLOGY.yaml`。

### 写实表达

优先把抽象评价改成具体、可核对的描述。

例如：

```text
improves computational flexibility
```

如果真实机制是跨数据中心迁移 workload，更具体的表达是：

```text
allows the optimizer to reallocate deferrable workloads across data centers
```

不要从机制描述自动推导出没有证据支持的性能提升。

### 防御性写作

删除或压缩：

- 已弃用内部版本；
- “当前方法不包含 X”式负面定义；
- 假想 reviewer objection；
- 不改变科学解释的重复 disclaimer；
- meta-writing。

保留真正影响 validity、interpretation 或 reproducibility 的 limitation、assumption 和 boundary condition。

### 专业语言

检查：

- technical collocation；
- 过度 nominalization；
- 连续短句和 micro-paragraph；
- 公式化 AI 强调句；
- 不必要或不足的 hedging；
- 过量 transition/signaling。

## 4. 输出 Language Change Ledger

不要生成整节重写版。输出：

```text
L001
Location:
Category:
Current:
Suggested:
Reason:
Canonical term/style rule:
Logic impact: NONE
Confidence: HIGH
```

只保留有明确收益的建议，避免提供大量可互换的“风格选项”。

## 5. 人工批准

例如：

```text
APPROVE: L001, L003, L006
REJECT: L002
HOLD: L004
```

## 6. 用 EXACT_EDIT 执行

```text
MODE: EXACT_EDIT

SOURCE:
- Approved language findings: L001, L003, L006

RULES:
- Apply only these approved language changes.
- Preserve logic, claim strength, evidence, paragraph order, equations, citations, and all unspecified wording.
- Use the minimum sufficient diff.
```

## 一行流程

```text
AUDIT: LANGUAGE → Language Change Ledger → 人工批准 → EXACT_EDIT → diff review
```
