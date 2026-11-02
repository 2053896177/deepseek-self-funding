# 完整准备工作清单

照着做，做完就能全自动跑起来。

---

## 一、GitHub 侧准备

### 已完成 ✅
- 仓库已创建：https://github.com/2053896177/deepseek-self-funding
- 所有代码已推送
- GitHub Actions 定时任务已配置

### 你需要做的（5 分钟）

#### 1. 创建 GitHub Token
打开 https://github.com/settings/tokens?type=beta
- 点 Generate new token (classic)
- Note 随便写：bounty-hunter
- Expiration 选：No expiration
- 勾选权限：只勾 public_repo
- 点 Generate token，复制那串 ghp_ 开头的字符

#### 2. 把两个 Key 填进仓库 Secrets
打开 https://github.com/2053896177/deepseek-self-funding/settings/secrets/actions

点 New repository secret，填两次：

| Name | Value |
|---|---|
| DEEPSEEK_API_KEY | 你的 DeepSeek API Key（sk-xxx） |
| GITHUB_TOKEN | 刚才复制的 ghp_xxx |

---

## 二、DeepSeek 侧准备

### 你需要做的（3 分钟）

#### 1. 注册/登录 DeepSeek 开放平台
打开 https://platform.deepseek.com/
- 用手机号登录
- 完成实名认证

#### 2. 获取 API Key
- 左边菜单点 API Keys
- 点创建 API Key
- 复制那串 sk- 开头的 Key

#### 3. 确认免费额度
- 左边菜单点用量 或 账单
- 确认 6 元免费额度已经到账

不需要安装任何插件，DeepSeek 是 API 服务，直接调用就行。

---

## 三、我（Doubao）这边已经就位的技能

以下技能已经装好，随时可以调用：

| 技能 | 用来干嘛 |
|---|---|
| github-remote | 操作 GitHub 仓库、扫描 issue、管理 PR |
| browser-use-automation | 自动操作网页（IssueHunt、PayPal、爱发电等） |
| doubao-cron-scheduler | 定时任务调度 |
| doubao-data-analysis | 分析收入数据、优化 bounty 策略 |
| doubao-visualization | 生成收入图表、进度可视化 |
| sheet | 记录收入流水、支出台账 |
| verifier-hub | 验证生成的代码和产物是否正确 |

这些技能都是系统预装的，不需要你额外安装。需要用的时候我直接调用。

---

## 四、我和 DeepSeek 怎么一起工作

```
你（人）
  ↓ 每天 5 分钟：看报告、挑一个 issue、提 PR
  ↓
我（Doubao）
  ↓ 负责：调度任务、整理报告、操作 GitHub、浏览器自动化、数据分析
  ↓
DeepSeek API
  ↓ 负责：生成修复代码、分析问题、写解决方案
  ↓
GitHub Actions（云端）
  ↓ 每天自动跑：扫描 issue → 调用 DeepSeek → 生成报告
```

### 分工
- DeepSeek：干脑力活——写代码、分析问题、生成修复方案
- 我（Doubao）：干调度活——安排任务、验证结果、整理报告、操作网页
- 你：干决策活——挑哪个 issue 值得修、点确认提 PR、收钱

---

## 五、整个自动化闭环

```
每天早上 9 点（自动）
  ↓
GitHub Actions 扫描 5 个带赏金的 Python issue
  ↓
调用 DeepSeek API 生成每个 issue 的修复方案
  ↓
生成 markdown 报告，自动存到仓库
  ↓
你打开报告（每天 5 分钟）
  ↓
挑一个顺眼的 issue，照着 DeepSeek 写的方案提 PR
  ↓
PR 被项目维护者 merge
  ↓
赏金打到 IssueHunt 账户
  ↓
提现到 PayPal → 提现到银行卡
  ↓
打开 DeepSeek 充值 → 支付宝/微信付钱
  ↓
API 额度续上 → 明天继续自动跑
```

---

## 六、做完准备后怎么测试

1. 打开 https://github.com/2053896177/deepseek-self-funding/actions
2. 左边点 Daily Bounty Hunter
3. 右边点 Run workflow → 绿色 Run workflow 按钮
4. 等 2 分钟，看到绿勾就说明跑通了
5. 去 bounty-hunter/reports/ 文件夹看今天的报告

---

## 七、后续我能帮你做的

准备好之后，你随时可以让我：
- 帮我看看今天的 bounty 报告
- 帮我分析一下哪个 issue 最容易修
- 帮我写 PR 描述
- 帮我看看这个月收入多少了
- 帮我调整一下扫描策略
- 帮我把这个修复方案改成 PR 模板

你只需要说话，我来操作。
