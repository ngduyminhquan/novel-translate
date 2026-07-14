import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("Page 60 snippet:")
print(reader.pages[60].extract_text()[:400])
print("\n" + "="*40 + "\nPage 67 snippet:")
print(reader.pages[67].extract_text()[:400])

# Let's extract pages 60 to 67 inclusive (meaning up to page 67, since page 68 starts chapter 3)
interlude_text = []
for i in range(60, 68):
    text = reader.pages[i].extract_text()
    interlude_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)

output_path = "source/vol_9/interlude_the_old_butlers_frightful_experience.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(interlude_text))
print(f"Extraction complete. Written to {output_path}")
