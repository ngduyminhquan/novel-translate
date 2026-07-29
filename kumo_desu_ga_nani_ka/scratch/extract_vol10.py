import pypdf
import os

reader = pypdf.PdfReader("source/vol_10/So I’m a Spider, So What_, Vol. 10.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 9),
    ("prologue_thus_a_goddess_was_born.txt", 10, 10),
    ("01_lets_set_a_goal.txt", 11, 28),
    ("02_lets_make_preparations.txt", 29, 43),
    ("interlude_the_slacker_demon_lord.txt", 44, 49),
    ("03_lets_take_action.txt", 50, 77),
    ("o_ill_do_what_i_can.txt", 78, 95),
    ("04_lets_bring_the_pain.txt", 96, 100),
    ("special_chapter_the_elf_cackles.txt", 101, 104),
    ("05_lets_observe_a_meeting.txt", 105, 124),
    ("interlude_brothers.txt", 125, 132),
    ("interlude_the_elder_demon_admits_defeat.txt", 133, 143),
    ("06_lets_file_a_complaint.txt", 144, 165),
    ("interlude_the_vampire_servants_annihilation.txt", 166, 182),
    ("interlude_asaka_and_kunihiko.txt", 183, 188),
    ("07_lets_make_a_threat.txt", 189, 201),
    ("interlude_a_teacher_wants_only_what_is_best_for_her_students.txt", 202, 209),
    ("08_lets_wrap_things_up.txt", 210, 225),
    ("epilogue_thus_an_evil_god_is_born.txt", 226, 235),
    ("afterword.txt", 236, 237),
    ("yen_newsletter.txt", 238, 238),
]

output_dir = "source/vol_10"
os.makedirs(output_dir, exist_ok=True)

for filename, start, end in chapters:
    print(f"Extracting {filename} (Pages {start} to {end})...")
    ch_text = []
    for i in range(start, end + 1):
        text = reader.pages[i].extract_text()
        ch_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)
    
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(ch_text))
    print(f"  Saved to {output_path}")

print("All extractions completed successfully!")
