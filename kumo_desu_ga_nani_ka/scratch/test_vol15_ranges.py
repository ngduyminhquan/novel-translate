import pypdf

reader = pypdf.PdfReader("source/vol_15/So I’m a Spider, So What_, Vol. 15.pdf")

chapters = [
    ("00_insert_copyright", 0, 15),
    ("01_ch1_a_new_dawn", 16, 41),
    ("02_s1_waking_to_a_new_world", 42, 47),
    ("03_ch2_the_world_is_terribly_cruel", 48, 70),
    ("04_s2_the_value_of_a_life", 71, 77),
    ("05_ch3_if_you_re_not_strong_enough_you_d_better_get_groveling", 78, 100),
    ("06_s3_there_s_no_point_dwelling_on_past_misfortunes", 101, 118),
    ("07_ch4_friends", 119, 140),
    ("08_interlude_kunihiko_tagawa", 141, 149),
    ("09_interlude_kengo_natsume", 150, 153),
    ("10_interlude_yuri", 154, 156),
    ("11_ch5_world_quest", 157, 173),
    ("12_s4_change_of_scenery", 174, 178),
    ("13_interlude_katia", 179, 189),
    ("14_special_chapter_the_demon_lord_left_behind", 190, 200),
    ("15_s5_an_ever_changing_world", 201, 211),
    ("16_interlude_dustin", 212, 216),
    ("17_special_chapter_the_demon_lord_makes_her_move", 217, 220),
    ("18_interlude_speeches_from_each_side", 221, 225),
    ("19_epilogue_and_prologue", 226, 228),
    ("20_afterword", 229, 234),
    ("21_yen_newsletter", 235, 235),
]

for name, start, end in chapters:
    print(f"=== {name} ({start} -> {end}) ===")
    
    # Start page
    start_text = reader.pages[start].extract_text()
    if start_text:
        start_text = start_text.strip()
        first_lines = [line.strip() for line in start_text.split("\n") if line.strip()]
        if first_lines:
            print("  Start:", first_lines[:3])
        else:
            print("  Start: [Empty or Whitespace Only]")
    else:
        print("  Start: [No Text / Image]")
        
    # End page
    end_text = reader.pages[end].extract_text()
    if end_text:
        end_text = end_text.strip()
        last_lines = [line.strip() for line in end_text.split("\n") if line.strip()]
        if last_lines:
            print("  End:  ", last_lines[-3:])
        else:
            print("  End:   [Empty or Whitespace Only]")
    else:
        print("  End:   [No Text / Image]")
    print()
