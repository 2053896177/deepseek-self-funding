# DeepSeek Self-Funding

用 DeepSeek API 批量生成数字产品 → 被动售卖 → 收入回流充值，让 API 自己养活自己的自循环系统。

## 核心理念

DeepSeek API 定价极低（flash 模型闲时输入约 0.02 元/百万 token），**6 块钱免费额度足够生成几十万到上百万字的内容**。

这套项目就是把这 6 块钱当种子，用它批量生成可售卖的数字产品，卖出去的钱再充回 API，形成正循环。

## 项目结构

```
deepeek-self-funding/
├── scripts/                # 核心脚本
│   ├── generate_product.py    # 单次生成产品内容
│   ├── batch_generate.py      # 批量生成多套产品
│   └── utils.py               # 工具函数（API 调用、文件输出）
├── templates/              # 各品类的 Prompt 模板
│   └── shenlun/              # 公考申论模板
├── products/               # 生成的成品存放目录（自动输出到这里）
├── docs/                   # 文档
│   └── business-model.md      # 商业模式与变现路径
├── config.example.yaml     # 配置示例（复制为 config.yaml 填入你的 API Key）
└── requirements.txt        # Python 依赖
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

```bash
cp config.example.yaml config.yaml
# 编辑 config.yaml，填入你的 DeepSeek API Key
```

### 3. 生成第一套产品

```bash
python scripts/generate_product.py --category shenlun --output products/
```

### 4. 批量生成

```bash
python scripts/batch_generate.py --count 5 --category shenlun
```

## 变现路径

| 平台 | 适合卖什么 | 门槛 |
|---|---|---|
| 爱发电 | 模板、电子书、Prompt 库 | 极低 |
| 闲鱼 | 虚拟资料、题库 | 极低 |
| 小红书 | 发笔记引流，私域成交 | 需养号 |
| GitHub Sponsors | 开源工具赞助 | 需攒 star |

详见 [docs/business-model.md](docs/business-model.md)。

## 成本估算

以 deepseek-flash 模型为例：
- 生成一套 1 万字的申论模板，约消耗 2 万 input + 1.5 万 output tokens
- 闲时成本约 **0.05 元**
- 定价 9.9 元卖出 1 份，回本 200 倍

## License

MIT