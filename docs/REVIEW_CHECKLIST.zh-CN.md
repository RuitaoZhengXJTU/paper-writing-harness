# 论文修改 Review Checklist

## 范围

- [ ] Agent 只修改了授权文件和段落。
- [ ] 未指定内容没有被“顺便优化”。
- [ ] 没有未经授权的整节重写。
- [ ] 没有意外删除公式、引用、标签、图表说明或过渡段。

## Preview Review

- [ ] 当前 preview 有明确的 preview ID 和 revision。
- [ ] `preview.md` 是唯一权威可编辑源。
- [ ] PDF/TeX 只是从 Markdown 生成的 review view，没有独立维护措辞。
- [ ] PDF paragraph anchor 能映射回 Markdown paragraph ID。
- [ ] PDF annotation 已记录到 `review/decisions.md`。
- [ ] 所有已接受 annotation 都先修改 Markdown，再重新生成 TeX/PDF。
- [ ] `PARTIAL / REJECTED / BLOCKED` annotation 有明确原因。
- [ ] PDF 中的 review-only 标记不会进入正式论文。
- [ ] `APPLY_PREVIEW` 使用的是明确批准的 preview ID + revision。

## 科学与证据

- [ ] 新增或增强的 claim 能映射到 `CLAIM_LEDGER.yaml`。
- [ ] 数字来自 `results/manifest.yaml` 中的 verified 证据。
- [ ] provisional 结果没有写成确定事实。
- [ ] “may / suggests / designed to”等限定没有被增强。
- [ ] 没有虚构 citation、baseline、显著性或复杂度结论。

## 语言表达

- [ ] 同一技术对象在全文使用一致的 canonical term。
- [ ] `predict / identify / determine / estimate` 等动词没有造成无意的语义强度漂移。
- [ ] 表述符合 `TERMINOLOGY.yaml` 和 `PROSE_STYLE.yaml`。
- [ ] 能用具体 subject + action + object 表述的地方，没有保留空泛的 “improves / enhances / provides superior ...” 评价。
- [ ] observation、mechanism 和 interpretation 被清楚区分。
- [ ] 没有不必要的 `It should be noted that`、`This clearly demonstrates` 等 meta/formulaic framing。
- [ ] 没有连续短句或 micro-paragraph 把完整论证拆成说明书式结构。
- [ ] hedging 与真实证据强度匹配，既没有过强 claim，也没有空洞的自我保护式 hedging。
- [ ] Language Change Ledger 中获批准的条目才被 `EXACT_EDIT` 实施。
- [ ] 语言修改没有改变段落顺序、rhetorical role、claim、因果方向、证据解释、数字、公式、引用、scope 或 limitation。

## 防御性写作

- [ ] 没有为了说明当前方法“不包含 X”而重新详细介绍已弃用的 X。
- [ ] 没有无必要地讨论历史版本、失败方案或内部迭代。
- [ ] 没有反复强调 method does not / is not / should not be confused with。
- [ ] 没有为普通设计选择加入过长的预防性辩护。
- [ ] 没有为了假想 reviewer objection 添加不改变科学解释的 disclaimer。
- [ ] 真正影响 validity / interpretation / reproducibility 的 limitation、assumption 和 caveat 被保留。

## 跨章节重复与信息职责

- [ ] 每个重要机制、方法细节、结果和 limitation 有明确 canonical owner section。
- [ ] Introduction 只保留 contribution-level summary，没有提前完整复述 Method。
- [ ] Discussion 没有变成第二个 Method 或第二个 Results。
- [ ] Conclusion 是压缩 synthesis，而不是重新复制 Introduction。
- [ ] 不同章节用不同措辞重复同一语义的情况已被检查。
- [ ] 必要重复确实承担不同 rhetorical role，并且相对 owner section 有明显压缩。

## 全局一致性

- [ ] Abstract、Introduction、Method、Experiments、Discussion、Conclusion 仍一致。
- [ ] 公式、图、表、章节和引用交叉引用有效。
- [ ] 改动影响到的章节已更新或标记 stale。
- [ ] 不同章节中的结果数字和方法名称一致。

## Audit

- [ ] AUDIT 默认为只读，没有未经批准直接重写。
- [ ] 选择了适合的 `FULL / LANGUAGE / CONSISTENCY / EVIDENCE` profile。
- [ ] 对冗余优先考虑 `DELETE / MERGE / COMPRESS`，而不是添加更多说明。
- [ ] duplication finding 指明了 canonical owner section。
- [ ] defensive-writing finding 与真正必要的 limitation/caveat 被区分开。
- [ ] LANGUAGE profile 返回的是 Language Change Ledger，而不是整节重写稿。
- [ ] HIGH/MEDIUM finding 已处理或明确接受风险。

## 技术验收

- [ ] Preview PDF 和/或正式论文构建通过，或失败原因被准确记录。
- [ ] `git diff` 中没有非预期大范围变化。
- [ ] 最终提交只包含本轮确认过的文件。
