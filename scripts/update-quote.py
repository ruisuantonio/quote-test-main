import sys
sys.path.insert(0, './libs')

import requests
from deep_translator import GoogleTranslator
import chardet

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        quote_data = response.json()[0]
        return f"{quote_data['q']} — {quote_data['a']}"
    return "No quote available"

def translate_quote(quote, dest_language='pt'):
    return GoogleTranslator(source='auto', target=dest_language).translate(quote)

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

def update_readme(file_path, new_quote):
    encoding = detect_encoding(file_path)
    with open(file_path, "r", encoding=encoding) as file:
        lines = file.readlines()
    
    with open(file_path, "w", encoding='utf-8') as file:
        for line in lines:
            if line.startswith("> **Citacao:**") or line.startswith("> **Quote:**"):
                file.write(f"> **Citacao:** {new_quote}\n")
            else:
                file.write(line)

if __name__ == "__main__":
    quote_en = get_quote()
    if quote_en:
        if os.getenv('GITHUB_ACTIONS') == 'true':
            update_readme("README.md", quote_en)
    
            quote_pt = translate_quote(quote_en, dest_language='pt')
            update_readme("README-br.md", quote_pt)
        else:
        print("This script is not running on GitHub Actions.")
