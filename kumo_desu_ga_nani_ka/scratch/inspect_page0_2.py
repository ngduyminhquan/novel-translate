import pypdf

reader = pypdf.PdfReader("source/vol_16/So I’m a Spider, So What_, Vol. 16.pdf")
for idx in [0, 1, 2]:
    print(f"--- Page {idx} ---")
    page = reader.pages[idx]
    print("Images:", len(page.images))
    print("Text preview:", repr(page.extract_text()[:300]))
