import os

footer = """
<watermark-footer>
<p align="center">
  <a href="https://github.com/ruisuan/ruisuan/blob/stable/contribute.md">Contribute ☕</a>
</p>
</watermark-footer>
"""

base_path = '.'

def update_footer(file_path):
    with open(file_path, 'r+', encoding='utf-8') as f:
        content = f.read()
        
        if '<watermark-footer>' in content:
            start_index = content.find('<watermark-footer>')
            end_index = content.find('</watermark-footer>') + len('</watermark-footer>')
            current_footer = content[start_index:end_index]
            
            if current_footer.strip() != footer.strip():
                print(f'Updating footer in {file_path}')
                content = content[:start_index] + footer.strip() + content[end_index:]
                f.seek(0)
                f.write(content)
                f.truncate()
            else:
                print(f'Footer is already up to date in {file_path}')
        else:
            print(f'Adding footer to {file_path}')
            f.write(f'\n\n{footer.strip()}')

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            update_footer(file_path)