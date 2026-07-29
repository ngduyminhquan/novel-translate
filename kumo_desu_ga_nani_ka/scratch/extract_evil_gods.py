import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("Page 8 text:")
print(reader.pages[8].extract_text()[:500])
print("="*40)
print("Page 9 text:")
print(reader.pages[9].extract_text()[:1000])
print("="*40)
print("Page 10 text:")
print(reader.pages[10].extract_text()[:1000])
print("="*40)
print("Page 11 text:")
print(reader.pages[11].extract_text()[:1000])
