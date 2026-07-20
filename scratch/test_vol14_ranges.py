import pypdf

reader = pypdf.PdfReader("source/vol_14/So I’m a Spider, So What_, Vol. 14.pdf")

chapters = [
    ("00_insert_copyright", 0, 6),
    ("01_l1_the_lord_who_had_no_name", 7, 7),
    ("02_ch1_before_the_battle", 8, 16),
    ("03_b1_reminisce_first_meeting", 17, 23),
    ("04_interlude_potimass_beginning", 24, 24),
    ("05_ch2_the_starting_bell_of_the_final_battle", 25, 37),
    ("06_l2_the_lord_who_was_once_a_lab_rat", 38, 42),
    ("07_interlude_potimass_experiments", 43, 43),
    ("08_b2_ruminate_the_lost_angel_and_the_dragon", 44, 51),
    ("09_ch3_showdown_annihilation", 52, 60),
    ("10_l3_the_lord_who_had_friends", 61, 64),
    ("11_b3_ruminate_blocked_by_the_demon_lord_of_the_business_world", 65, 73),
    ("12_interlude_potimas_and_conjuring", 74, 74),
    ("13_ch4_showdown_spider_vs_robot", 75, 80),
    ("14_l4_the_lord_learns_a_lesson", 81, 88),
    ("15_b4_ruminate_vampires", 89, 100),
    ("16_interlude_potimas_and_vampires", 101, 101),
    ("17_ch5_showdown_spider_vs_mega_robot", 102, 120),
    ("18_l5_the_lord_looks_on", 121, 127),
    ("19_b5_ruminate_ma_energy", 128, 136),
    ("20_interlude_potimas_and_the_popularization_of_ma_energy", 137, 138),
    ("21_ch6_showdown_chance_meeting", 139, 153),
    ("22_interlude_the_old_man_and_the_witchy_little_ladies", 154, 161),
    ("23_l6_the_lord_alone", 162, 181),
    ("24_b6_ruminate_ragnarok", 182, 191),
    ("25_interlude_the_presidents_decision", 192, 196),
    ("26_interlude_potimas_and_the_gods_sacrifice", 197, 198),
    ("27_ch7_showdown_countless_spider_eyes", 199, 206),
    ("28_l7_the_lord_avenged", 207, 222),
    ("29_b7_ruminate_thus_history_moves_again", 223, 226),
    ("30_ch8_end_of_battle_she_who_walks_with_the_lord", 227, 231),
    ("31_afterword", 232, 233),
    ("32_copyright", 234, 236),
    ("33_yen_newsletter", 237, 237),
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
