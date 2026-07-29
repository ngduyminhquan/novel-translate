import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("Page 67 snippet:")
print(reader.pages[67].extract_text()[:400])
print("\n" + "="*40 + "\nPage 68 snippet:")
print(reader.pages[68].extract_text()[:400])
print("\n" + "="*40 + "\nPage 78 snippet:")
print(reader.pages[78].extract_text()[:400])
print("\n" + "="*40 + "\nPage 79 snippet:")
print(reader.pages[79].extract_text()[:400])
