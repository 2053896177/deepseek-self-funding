"""调用 DeepSeek API 生成 issue 修复方案"""
from openai import OpenAI
import yaml


def load_config(config_path: str = "config.yaml") -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_client(config: dict) -> OpenAI:
    return OpenAI(
        api_key=config["deepseek"]["api_key"],
        base_url=config["deepseek"]["base_url"],
    )


def generate_fix(client: OpenAI, issue: dict, config: dict) -> str:
    """根据 issue 内容生成修复方案"""
    prompt = f"""你是一个资深软件工程师。请分析下面这个 GitHub issue，并给出完整的修复方案。

## Issue 信息
标题：{issue['title']}
仓库：{issue['repo_url']}
Labels：{', '.join(issue['labels'])}

## Issue 描述
{issue['body']}

## 请输出以下内容：

### 1. 问题分析
简要说明这个 issue 到底要解决什么问题。

### 2. 修复方案
具体的修复思路和步骤。

### 3. 代码示例
给出关键代码片段的修改前后对比（如果涉及代码）。

### 4. 测试建议
怎么验证修复是对的。

请用简洁、专业的语言输出，像一个工程师在写 PR 描述。
"""

    response = client.chat.completions.create(
        model=config["deepseek"]["model"],
        messages=[
            {"role": "system", "content": "你是一个资深全栈工程师，擅长快速分析和修复开源项目的 bug。"},
            {"role": "user", "content": prompt},
        ],
        temperature=config["fixer"]["temperature"],
        max_tokens=config["fixer"]["max_tokens"],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    config = load_config()
    client = get_client(config)
    # 测试用
    test_issue = {
        "title": "Test issue",
        "repo_url": "https://github.com/example/repo",
        "labels": ["bug"],
        "body": "This is a test issue body.",
    }
    result = generate_fix(client, test_issue, config)
    print(result)
