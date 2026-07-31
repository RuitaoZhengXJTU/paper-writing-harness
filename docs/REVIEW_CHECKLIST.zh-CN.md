# 论文修改 Review Checklist

## 范围

- [ ] Agent 只修改了授权文件和段落。
- [ ] 未指定内容没有被“顺便优化”。
- [ ] 没有未经授权的整节重写。
- [ ] 没有意外删除公式、引用、标签、图表说明或过渡段。

## 科学与证据

- [ ] 新增或增强的 claim 能映射到 `CLAIM_LEDGER.yaml`。
- [ ] 数字来自 `results/manifest.yaml` 中的 verified 证据。
- [ ] provisional 结果没有写成确定事实。
- [ ] “may / suggests / designed to”等限定没有被增强。
- [ ] 没有虚构 citation、baseline、显著性或复杂度结论。

## 论文表达

- [ ] 没有本地路径、脚本名、命令、调试过程或 agent 叙述。
- [ ] 实现细节位于正确层级：正文、附录、仓库文档或 internal。
- [ ] 术语、缩写、符号和大小写符合 `TERMINOLOGY.yaml`。
- [ ] 没有与相邻章节重复解释同一内容。

## 全局一致性

- [ ] Abstract、Introduction、Method、Experiments、Discussion、Conclusion 仍一致。
- [ ] 公式、图、表、章节和引用交叉引用有效。
- [ ] 改动影响到的章节已更新或标记 stale。
- [ ] 不同章节中的结果数字和方法名称一致。

## 技术验收

- [ ] 论文构建通过，或失败原因被准确记录。
- [ ] `git diff` 中没有非预期大范围变化。
- [ ] 审计报告的 HIGH/MEDIUM 问题已处理或记录。
- [ ] 最终提交只包含本轮确认过的文件。
