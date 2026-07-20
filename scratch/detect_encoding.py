encodings = ["utf-8", "utf-8-sig", "utf-16", "utf-16le", "utf-16be", "cp1258", "cp1252", "latin1"]
file_path = r"d:\workspace\translate\context\relationships.md"

for enc in encodings:
    try:
        with open(file_path, "r", encoding=enc) as f:
            content = f.read()
        print(f"SUCCESS: {enc} works!")
    except Exception as e:
        print(f"FAILED: {enc} - {e}")
