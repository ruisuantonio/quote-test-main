import os

footer = """
<watermark-footer>
<p align="center">
  <a href="https://github.com/ruisuan/ruisuan/blob/stable/contribute.md">Contribute ☕</a> •
</p>
</watermark-footer>
"""

base_path = '.'

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r+', encoding='utf-8') as f:
                content = f.read()
                if footer.strip() not in content:
                    f.write(f'\n\n{footer.strip()}')