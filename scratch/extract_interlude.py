import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("Page 24 snippet:")
print(reader.pages[24].extract_text()[:400])
print("\n" + "="*40 + "\nPage 33 snippet:")
print(reader.pages[33].extract_text()[:400])

# Let's extract pages 24 to 32 inclusive (meaning up to page 32, since page 33 starts X1)
interlude_text = []
for i in range(24, 33):
    text = reader.pages[i].extract_text()
    interlude_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)

output_path = "source/vol_9/interlude_the_veteran_demons_secret_feud.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(interlude_text))
print(f"Extraction complete. Written to {output_path}")
