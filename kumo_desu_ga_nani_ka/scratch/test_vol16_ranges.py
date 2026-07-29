import pypdf

reader = pypdf.PdfReader("source/vol_16/So I’m a Spider, So What_, Vol. 16.pdf")
outline = reader.outline

def print_page_previews(outline):
    for item in outline:
        if isinstance(item, list):
            print_page_previews(item)
        else:
            try:
                page_idx = reader.get_destination_page_number(item)
                text = reader.pages[page_idx].extract_text()
                # Get first 150 chars of the page to inspect
                preview = " ".join(text.split()[:25])
                print(f"[{item.title}] (Page index {page_idx}): {preview}...")
            except Exception as ex:
                print(f"[{item.title}]: Error ({ex})")

print_page_previews(outline)
