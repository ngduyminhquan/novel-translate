import pypdf

reader = pypdf.PdfReader("source/vol_11/So I’m a Spider, So What_, Vol. 11.pdf")
print("Total pages:", len(reader.pages))

try:
    outline = reader.outline
    def print_outline(outline, depth=0):
        for item in outline:
            if isinstance(item, list):
                print_outline(item, depth + 1)
            else:
                try:
                    page_num = reader.get_destination_page_number(item)
                    print("  " * depth + f"{item.title} -> Page {page_num}")
                except Exception as ex:
                    print("  " * depth + f"{item.title} -> Page unknown ({ex})")
    print("Outline:")
    print_outline(outline)
except Exception as e:
    print("No outline or error:", e)
