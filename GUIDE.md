# 小白操作指南

照着做就行，总共只需要点 3 步，之后全自动跑。

---

## 第一步：创建 GitHub Token（2 分钟）

1. 打开这个链接：https://github.com/settings/tokens?type=beta
2. 点右上角 **Generate new token (classic)**
3. 填写：
   - Note：随便写，比如 `bounty-hunter`
   - Expiration：选 `No expiration`（永不过期）
   - 勾选权限：只勾 **`public_repo`**（其他都不勾）
4. 点最下面绿色按钮 **Generate token**
5. 复制生成的那串字符（`ghp_` 开头），**先存到记事本里**，等下要用

---

## 第二步：把两个 Key 填到仓库里（2 分钟）

1. 打开这个链接：https://github.com/2053896177/deepseek-self-funding/settings/secrets/actions
2. 点绿色按钮 **New repository secret**

### 填第一个：DeepSeek API Key
- Name 填：`DEEPSEEK_API_KEY`
- Secret 填：你的 DeepSeek API Key（就是你那 6 块钱额度对应的 sk-xxx 那串）
- 点 Add secret

### 填第二个：GitHub Token
- 再点一次 New repository secret
- Name 填：`GITHUB_TOKEN`
- Secret 填：刚才第一步复制的 `ghp_xxx` 那串
- 点 Add secret

---

## 第三步：手动跑一次测试（1 分钟）

1. 打开这个链接：https://github.com/2053896177/deepseek-self-funding/actions
2. 左边点 **Daily Bounty Hunter**
3. 右边点 **Run workflow** 按钮 → 再点绿色的 Run workflow
4. 等 1-2 分钟，刷新页面，看到绿勾就说明跑成功了

---

## 之后每天自动跑什么？

每天早上 9 点，系统自动：
1. 扫描 GitHub 上 5 个带赏金的 Python issue
2. 调用 DeepSeek 给每个 issue 生成修复方案
3. 生成一份报告，自动存到 `bounty-hunter/reports/` 文件夹

你每天只需要打开仓库的 `bounty-hunter/reports/` 文件夹，看当天的报告就行。

---

## 怎么看到账了多少钱？

### Bounty 收入在哪里看？

主要来自两个地方：

1. **IssueHunt**（最主要）
   - 打开 https://issuehunt.io/
   - 用你的 GitHub 账号登录
   - 点右上角头像 → Dashboard
   - 就能看到你有多少 bounty 待领取

2. **GitHub Sponsors**（以后慢慢会有）
   - 打开 https://github.com/sponsors
   - 能看到谁赞助了你

---

## 怎么提现到银行卡？

### 从 IssueHunt 提现：
1. 登录 IssueHunt → Dashboard
2. 点 **Withdraw** 按钮
3. 绑定你的 PayPal 账号
4. 钱打到 PayPal 之后，从 PayPal 提现到银行卡

### 从 PayPal 提现到国内银行卡：
1. 打开 PayPal 官网（paypal.com）
2. 绑定你的国内储蓄卡（任意银行都行）
3. 点 **钱包 → 提现 → 提现到银行账户**
4. 1-3 个工作日到账

---

## 怎么把钱充回 DeepSeek？

1. 打开 DeepSeek 开放平台：https://platform.deepseek.com/
2. 登录你的账号
3. 左边菜单点 **充值**
4. 选金额（最低充 10 元）
5. 用支付宝或微信支付
6. 到账后自动就能用了，不用改任何配置

---

## 整个循环就是：

```
每天自动扫 issue → 自动生成修复方案 → 你照着提 PR
→ PR 被 merge → 赏金到账 IssueHunt
→ 提现到 PayPal → 提现到银行卡
→ 打开 DeepSeek 充值 → 支付宝微信付钱
→ API 额度续上 → 继续自动跑
```

---

## 常见问题

**Q：每天会花多少钱？**
A：扫 5 个 issue，调用 DeepSeek 生成修复方案，一天大约 0.5 元。6 块钱额度够跑 12 天左右。

**Q：多久能赚到第一笔钱？**
A：看你提的 PR 被不被 merge。一般来说，提 5-10 个 PR，能有 1-2 个被 merge，每个赏金 $5-$50 不等。

**Q：我不会写代码怎么办？**
A：报告里 DeepSeek 已经把修复方案和代码都写好了，你只需要照着复制粘贴，提 PR 就行。不需要你自己懂代码。

**Q：每天要花我多少时间？**
A：5 分钟。打开报告，挑一个顺眼的 issue，照着 DeepSeek 写的修复方案，点几下鼠标提 PR。
