import pypdf
import os

reader = pypdf.PdfReader("source/vol_15/So I’m a Spider, So What_, Vol. 15.pdf")
output_dir = "source/images/vol_15"
os.makedirs(output_dir, exist_ok=True)

image_count = 0
for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    for image_file_object in page.images:
        image_count += 1
        name = image_file_object.name
        ext = os.path.splitext(name)[1]
        if not ext:
            ext = ".png" # default to png if not specified
        out_name = f"page_{page_num}_img_{image_count}{ext}"
        out_path = os.path.join(output_dir, out_name)
        with open(out_path, "wb") as fp:
            fp.write(image_file_object.data)
        print(f"Extracted image to {out_path}")

print(f"Total images extracted: {image_count}")
