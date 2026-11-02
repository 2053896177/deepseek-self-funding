"""单次生成产品内容
用法: python scripts/generate_product.py --category shenlun --output products/
"""
import argparse
import sys
from pathlib import Path

# 把项目根目录加入 path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.utils import load_config, get_client, call_deepseek, save_output


def build_prompt(category: str) -> str:
    """根据品类构建生成 Prompt"""
    prompts = {
        "shenlun": """请生成一套【公考申论大作文万能模板】，包含以下内容：

1. 开头万能公式（3套，适用于不同主题）
2. 中间分论点结构（2套，含论点展开方式）
3. 结尾升华模板（3套）
4. 完整范文（2篇，分别围绕"青年担当"和"基层治理"主题）
5. 金句素材库（20条，可直接套用）

要求：
- 语言正式、规范，符合公考申论风格
- 模板要能直接套用，不要太抽象
- 每部分标注使用场景和注意事项
""",
        "zhuanshengben": """请生成一套【专升本英语作文万能模板】，包含：

1. 议论文模板（开头+中间+结尾，3套不同难度）
2. 书信模板（道歉信、邀请信、感谢信各1套）
3. 必背句型 30 条
4. 常用连接词分类整理
5. 完整范文 2 篇

要求：
- 词汇难度适配专升本水平
- 模板结构清晰，学生可以直接填空使用
""",
        "mianshi": """请生成一套【事业单位/网格员面试 100 问】，包含：

1. 自我认知类 15 题（含逐字稿答案）
2. 综合分析类 20 题
3. 应急应变类 20 题
4. 人际关系类 20 题
5. 组织计划类 25 题

要求：
- 每题都要有完整的参考答案
- 答案结构：表态 + 分析 + 对策
- 语言自然，像真人在说话，不要太书面化
""",
    }
    
    if category not in prompts:
        raise ValueError(f"未知品类: {category}，可选: {list(prompts.keys())}")
    
    return prompts[category]


def main():
    parser = argparse.ArgumentParser(description="生成一套数字产品内容")
    parser.add_argument("--category", required=True, help="产品品类: shenlun / zhuanshengben / mianshi")
    parser.add_argument("--output", default="products", help="输出目录")
    parser.add_argument("--config", default="config.yaml", help="配置文件路径")
    args = parser.parse_args()

    print(f"🚀 开始生成: {args.category}")
    
    config = load_config(args.config)
    client = get_client(config)
    
    prompt = build_prompt(args.category)
    print(f"📝 Prompt 已构建，调用 DeepSeek API...")
    
    content = call_deepseek(
        client,
        prompt,
        model=config["deepseek"]["model"],
        temperature=config["generation"]["temperature"],
        max_tokens=config["generation"]["max_tokens"],
    )
    
    filename = f"{args.category}_template_v1"
    save_output(content, args.output, filename, config["output"]["format"])
    
    print(f"🎉 生成完成！")


if __name__ == "__main__":
    main()
