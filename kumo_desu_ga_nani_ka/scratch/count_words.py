import os

source_dir = "source/vol_10"
files = sorted([f for f in os.listdir(source_dir) if f.endswith(".txt")])

print(f"{'Filename':<60} | {'Lines':<6} | {'Words':<8} | {'Chars':<8}")
print("-" * 90)
for file in files:
    path = os.path.join(source_dir, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        lines = len(content.splitlines())
        words = len(content.split())
        chars = len(content)
        print(f"{file:<60} | {lines:<6} | {words:<8} | {chars:<8}")
