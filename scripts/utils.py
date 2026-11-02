"""工具函数：DeepSeek API 调用、文件输出等"""
import os
import yaml
from pathlib import Path
from openai import OpenAI


def load_config(config_path: str = "config.yaml") -> dict:
    """加载配置文件"""
    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"配置文件 {config_path} 不存在，请复制 config.example.yaml 为 config.yaml 并填入 API Key"
        )
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_client(config: dict) -> OpenAI:
    """创建 DeepSeek API 客户端"""
    return OpenAI(
        api_key=config["deepseek"]["api_key"],
        base_url=config["deepseek"]["base_url"],
    )


def call_deepseek(
    client: OpenAI,
    prompt: str,
    model: str = "deepseek-chat",
    temperature: float = 0.7,
    max_tokens: int = 4096,
) -> str:
    """调用 DeepSeek API 生成内容"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个专业的内容创作者，擅长撰写高质量的备考资料和模板。"},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def save_output(content: str, output_dir: str, filename: str, format: str = "markdown"):
    """保存生成的内容到文件"""
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    ext = "md" if format == "markdown" else "txt"
    file_path = out_path / f"{filename}.{ext}"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ 已保存: {file_path}")
    return str(file_path)
