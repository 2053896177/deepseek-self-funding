"""主入口：扫描 issue → 生成修复方案 → 输出报告"""
import os
import sys
from datetime import datetime
from pathlib import Path

from scanner import search_bounty_issues, load_config
from fixer import get_client, generate_fix


def generate_report(issues: list, fixes: list, output_dir: str):
    """生成 markdown 报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    report_path = Path(output_dir)
    report_path.mkdir(parents=True, exist_ok=True)

    filename = f"bounty-report-{today}.md"
    filepath = report_path / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# 每日 Bounty 报告 - {today}\n\n")
        f.write(f"今日扫描到 {len(issues)} 个候选 issue\n\n")

        for i, (issue, fix) in enumerate(zip(issues, fixes), 1):
            f.write(f"---\n\n")
            f.write(f"## {i}. {issue['title']}\n\n")
            f.write(f"- **Issue 链接**: {issue['html_url']}\n")
            f.write(f"- **Labels**: {', '.join(issue['labels'])}\n")
            f.write(f"- **更新时间**: {issue['updated_at'][:10]}\n\n")
            f.write(f"### 修复方案\n\n")
            f.write(fix + "\n\n")

    print(f"报告已生成: {filepath}")
    return str(filepath)


def main():
    config_path = os.environ.get("CONFIG_PATH", "config.yaml")
    config = load_config(config_path)

    print("🔍 正在扫描带赏金的 issue...")
    issues = search_bounty_issues(config)
    print(f"找到 {len(issues)} 个候选 issue")

    if not issues:
        print("没有找到合适的 issue，退出。")
        return

    print("\n🤖 正在调用 DeepSeek 生成修复方案...")
    client = get_client(config)

    fixes = []
    for i, issue in enumerate(issues, 1):
        print(f"  处理第 {i}/{len(issues)} 个: {issue['title'][:50]}...")
        try:
            fix = generate_fix(client, issue, config)
            fixes.append(fix)
        except Exception as e:
            print(f"  ❌ 失败: {e}")
            fixes.append("（生成失败）")

    output_dir = config["output"]["dir"]
    report_path = generate_report(issues, fixes, output_dir)

    print(f"\n✅ 全部完成！报告在: {report_path}")


if __name__ == "__main__":
    main()
