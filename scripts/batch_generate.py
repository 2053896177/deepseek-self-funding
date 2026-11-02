"""批量生成多套产品
用法: python scripts/batch_generate.py --count 5 --category shenlun
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.utils import load_config, get_client, call_deepseek, save_output
from scripts.generate_product import build_prompt


def main():
    parser = argparse.ArgumentParser(description="批量生成产品内容")
    parser.add_argument("--count", type=int, default=3, help="生成数量")
    parser.add_argument("--category", required=True, help="产品品类")
    parser.add_argument("--output", default="products", help="输出目录")
    parser.add_argument("--config", default="config.yaml", help="配置文件路径")
    args = parser.parse_args()

    config = load_config(args.config)
    client = get_client(config)
    prompt = build_prompt(args.category)

    print(f"🚀 批量生成: {args.category} × {args.count} 套")

    for i in range(1, args.count + 1):
        print(f"\n--- 第 {i}/{args.count} 套 ---")
        try:
            content = call_deepseek(
                client,
                prompt,
                model=config["deepseek"]["model"],
                temperature=config["generation"]["temperature"] + 0.1,  # 每次稍微加点随机性
                max_tokens=config["generation"]["max_tokens"],
            )
            filename = f"{args.category}_v{i}"
            save_output(content, args.output, filename, config["output"]["format"])
        except Exception as e:
            print(f"❌ 第 {i} 套生成失败: {e}")
            continue

    print(f"\n✅ 批量生成完成！输出目录: {args.output}")


if __name__ == "__main__":
    main()
