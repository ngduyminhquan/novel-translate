import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")

chapters = [
    ("00_insert_copyright", 0, 8),
    ("evil_gods_dont_smile", 9, 10),
    ("01_arrival_in_the_demon_realm", 11, 23),
    ("interlude_the_veteran_demons_secret_feud", 24, 32),
    ("x1_the_former_sword_king_reigar", 33, 47),
    ("02_arrival_at_the_demon_lords_castle", 48, 59),
    ("interlude_the_old_butlers_frightful_experience", 60, 67),
    ("03_arrival_of_the_hooligan", 68, 78),
    ("interlude_the_demon_dukes_distress", 79, 85),
    ("x2_administrator_gyuriedistodiez", 86, 97),
    ("04_arrival_in_heaven", 98, 111),
    ("interlude_the_vampire_princesss_midnight_lesson", 112, 122),
    ("05_arrival_at_the_great_elroe_labyrinth", 123, 133),
    ("x3_ice_dragon_nia", 134, 140),
    ("06_arrival_at_mr_onis_place", 141, 170),
    ("o_wrath", 171, 199),
    ("07_arrival_in_japan", 200, 206),
    ("evil_gods_dont_laugh", 207, 224),
    ("evil_elves_do_sneer", 225, 227),
    ("afterword", 228, 230),
    ("yen_newsletter", 231, 231),
]

for name, start, end in chapters:
    print(f"=== {name} ({start} -> {end}) ===")
    # Print the first line of the start page
    start_text = reader.pages[start].extract_text().strip()
    first_lines = [line.strip() for line in start_text.split("\n") if line.strip()]
    if first_lines:
        print("  Start:", first_lines[0])
        if len(first_lines) > 1:
            print("        ", first_lines[1])
    else:
        print("  Start: [Empty Page or Image]")
        
    # Print the last line of the end page
    end_text = reader.pages[end].extract_text().strip()
    last_lines = [line.strip() for line in end_text.split("\n") if line.strip()]
    if last_lines:
        print("  End:  ", last_lines[-1])
    else:
        print("  End:   [Empty Page or Image]")
    print()
