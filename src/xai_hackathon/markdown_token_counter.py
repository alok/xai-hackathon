from pathlib import Path
import tiktoken

def count_tokens(text: str) -> int:
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(encoding.encode(text))

def count_tokens_in_markdown_files(directory: str) -> dict:
    """
    Count tokens in all Markdown files in the given directory.
    
    Args:
    directory (str): Path to the directory containing Markdown files.
    
    Returns:
    dict: A dictionary with filenames as keys and token counts as values.
    """
    token_counts = {}
    dir_path = Path(directory)
    for file_path in dir_path.glob("*.md"):
        content = file_path.read_text(encoding='utf-8')
        token_counts[file_path.name] = count_tokens(content)
    return token_counts

# Example usage
if __name__ == "__main__":
    info_dir = Path("info/ebook.md")
    results = count_tokens_in_markdown_files(info_dir)
    for filename, count in results.items():
        print(f"{filename}: {count} tokens")

