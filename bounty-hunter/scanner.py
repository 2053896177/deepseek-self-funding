"""扫描 GitHub 上带赏金的 issue"""
import requests
import yaml
from datetime import datetime


def load_config(config_path: str = "config.yaml") -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def search_bounty_issues(config: dict) -> list:
    """搜索 GitHub 上带赏金的 issue"""
    token = config["github"]["token"]
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    keywords = config["scanner"]["keywords"]
    languages = config["scanner"]["languages"]
    max_results = config["scanner"]["max_results"]

    all_issues = []

    for keyword in keywords:
        for lang in languages:
            query = f"{keyword} language:{lang} state:open"
            url = "https://api.github.com/search/issues"
            params = {
                "q": query,
                "sort": config["scanner"].get("sort", "updated"),
                "per_page": min(max_results, 10),
            }

            try:
                resp = requests.get(url, headers=headers, params=params, timeout=30)
                resp.raise_for_status()
                data = resp.json()

                for item in data.get("items", []):
                    # 过滤掉 PR（只保留 issue）
                    if "pull_request" in item:
                        continue
                    all_issues.append({
                        "title": item["title"],
                        "html_url": item["html_url"],
                        "repo_url": item["repository_url"],
                        "number": item["number"],
                        "state": item["state"],
                        "labels": [l["name"] for l in item.get("labels", [])],
                        "created_at": item["created_at"],
                        "updated_at": item["updated_at"],
                        "body": item.get("body", "")[:2000],  # 截断，避免太长
                    })
            except Exception as e:
                print(f"搜索失败 [{keyword}/{lang}]: {e}")
                continue

    # 去重（按 URL）
    seen = set()
    unique = []
    for issue in all_issues:
        if issue["html_url"] not in seen:
            seen.add(issue["html_url"])
            unique.append(issue)

    return unique[:max_results]


if __name__ == "__main__":
    config = load_config()
    issues = search_bounty_issues(config)
    print(f"找到 {len(issues)} 个 issue")
    for i, iss in enumerate(issues[:5], 1):
        print(f"{i}. {iss['title']}")
        print(f"   {iss['html_url']}")
