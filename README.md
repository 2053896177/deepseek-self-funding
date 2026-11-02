# DeepSeek Self-Funding

用 DeepSeek API 批量生成内容 → 被动变现 → 收入回流充值，让 API 自己养活自己的自循环系统。

## 两个子项目

### 1. 数字产品工厂

批量生成数字产品（申论模板、英语模板、面试题库等），挂爱发电/闲鱼售卖。

```
scripts/          # 生成脚本
templates/        # 各品类 Prompt 模板
products/         # 生成的成品输出
```

### 2. Bounty Hunter

自动扫描 GitHub 上带赏金的开源 issue，用 DeepSeek 生成修复方案，你照着提 PR 拿 bounty。

```
bounty-hunter/
├── scanner.py      # 扫描带赏金的 issue
├── fixer.py        # 调用 DeepSeek 生成修复方案
├── run.py          # 主入口，生成每日报告
├── reports/        # 每日报告自动输出到这里
└── .github/workflows/  # 每天自动跑一次
```

## 快速开始

### 数字产品工厂
```bash
pip install -r requirements.txt
cp config.example.yaml config.yaml
# 编辑 config.yaml 填入 API Key
python scripts/generate_product.py --category shenlun
```

### Bounty Hunter
```bash
cd bounty-hunter
pip install -r requirements.txt
cp config.example.yaml config.yaml
# 编辑 config.yaml 填入 API Key 和 GitHub Token
python run.py
```

## 成本估算

- DeepSeek flash 模型闲时输入约 0.02 元/百万 token
- 6 元免费额度足够生成几十万字内容
- 或足够跑 100+ 个 issue 的修复方案生成

## License

MIT
