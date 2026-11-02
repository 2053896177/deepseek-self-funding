# Bounty Hunter

自动扫描 GitHub 上带赏金的开源 issue，用 DeepSeek 生成修复方案。

## 工作原理

定时扫描 GitHub 上带 bounty/funded 标签的 issue → 筛选适合修复的 → 调用 DeepSeek 生成修复代码 → 输出每日报告 → 你照着报告提 PR → PR 被 merge → 赏金到账 → 充值回 DeepSeek。

## 为什么是半自动

全自动提 PR 到别人的仓库容易被当成 spam。MVP 先做到自动扫描 + 自动生成修复方案，你只需要复制粘贴就能提 PR。跑通几个赚到钱之后再加全自动。

## 成本估算

- 扫描 issue：免费
- 生成修复：每个 issue 约 0.05–0.1 元
- 每天扫 10 个 ≈ 0.5–1 元/天
- 6 元额度够跑 6–12 天

每天一个 PR 被 merge，按平均 $10 赏金算，回本几十倍。
