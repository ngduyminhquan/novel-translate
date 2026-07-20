import os
import re
import sys

# Reconfigure stdout to use utf-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

translated_dir = r"d:\workspace\translate\translated"

def search_ariel_speech():
    pattern = re.compile(r'“[^”]*”')
    for root, dirs, files in os.walk(translated_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Find occurrences of Ariel's dialogue if possible
                # Let's search for "Ariel" near speech quotes, or search for files with "ariel" in the name
                if 'ariel' in file.lower() or 'special' in file.lower() or 'interlude' in file.lower():
                    matches = pattern.findall(content)
                    print(f"File: {file}")
                    count = 0
                    for m in matches:
                        if any(x in m for x in ["ta", "tôi", "chúng ta", "các ngươi", "các bạn"]):
                            print(f"  {m}")
                            count += 1
                            if count > 20:
                                break

if __name__ == "__main__":
    search_ariel_speech()
