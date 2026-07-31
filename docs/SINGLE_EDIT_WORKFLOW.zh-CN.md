# 单次论文修改流程

## 1. 判断模式

### 已经知道具体怎么改：`EXACT_EDIT`

适用于明确的句子、公式、术语、顺序或局部段落修改。目标是最小 diff，未指定内容全部锁定。

### 只知道章节应表达什么：`DESIGN_PREVIEW`

先生成段落卡片和 claim–evidence 设计，不触碰正式论文。确认后再用 `APPLY_PREVIEW`。

### 已批准结构预览：`APPLY_PREVIEW`

只实现批准的 preview，不重新设计，不自行补充不受支持的论点。

### 只做检查：`AUDIT`

默认只读，检查矛盾、重复、术语、证据、数字、引用和内部信息泄漏。

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

## 3. Review 修改

### Review `EXACT_EDIT`

先看 diff，而不是只读修改后的全文：

1. 是否只改了授权范围；
2. 是否误删了句子、公式、引用或段落；
3. 是否增强了结论；
4. 是否改变数字、公式编号、符号或 citation key；
5. 是否加入路径、脚本、命令或 agent 叙述；
6. 哪些相关章节因此 stale。

可追加指令：

```text
Show the manuscript diff only. Do not apply further edits.
Explain each nontrivial change in one sentence.
```

### Review `DESIGN_PREVIEW`

不要因为示例正文流畅就直接批准。逐个检查 paragraph card：

- 这段为什么存在；
- main claim 是否准确；
- 有何证据；
- 与其他段落是否重复；
- 明确排除了什么；
- 哪些内容仍不确定；
- 是否遗漏核心贡献。

将反馈分为：

```text
APPROVED:
REVISE:
REMOVE:
LOCKED:
```

只要求修改 preview，不修改 `paper/`。

## 4. 执行正式更新

预览批准后使用 `APPLY_PREVIEW`，明确 preview ID、目标文件和锁定决策。要求 Agent：

- 只实现批准范围；
- 不添加未批准的新论点；
- 不编造证据；
- 缺少支持时保留为可追踪 placeholder 或停止该 claim；
- 更新 claim、section、terminology 和 stale 状态；
- 运行 publication、evidence、notation 和 consistency checks。

## 5. 最终审计

正式更新后单独运行一次 `AUDIT`：

```text
MODE: AUDIT
SCOPE:
- Files changed in the previous task
- Their declared dependent sections
AUTOFIX: NO
CHECKS:
- unintended deletions
- claim-strength changes
- terminology and notation
- numerical consistency
- duplicated explanations
- publication-boundary leakage
- stale abstract/introduction/conclusion statements
Report only HIGH and MEDIUM findings.
```

## 6. 人工验收与提交

```bash
git status
git diff
# 运行项目现有论文构建命令
git add <reviewed-files>
git commit -m "Revise <section>"
```

不要默认让 Agent 自动 commit。先检查 diff、编译结果和审计报告。

## 一行流程

```text
判断模式 → 写 Prompt → Review preview/diff → 正式应用 → 只读审计 → 编译与 git diff → 人工提交
```
