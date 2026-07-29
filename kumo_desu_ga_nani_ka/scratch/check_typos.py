import re
import sys

# Ensure UTF-8 output for Windows console
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

files_to_check = [
    "context/glossary.md",
    "context/characters.md",
    "context/relationships.md"
]

# Patterns for typical Telex typing failures, like "dd", "aa", "ee", "oo", "ow", "uw", "w" (uncombined)
# and common typos in Vietnamese.
telex_fail_pattern = re.compile(r'\b\w*(?:aa|ee|oo|dd|uw|ow)\w*\b', re.IGNORECASE)

print("--- Running typo checks ---")
for file_path in files_to_check:
    print(f"Scanning {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            # Check Telex failure
            fails = telex_fail_pattern.findall(line)
            # Filter out valid English/non-Vietnamese words like 'been', 'free', 'need', 'good', 'book', 'wood', 'feel', 'foot', 'look', 'seed', 'deep', 'keep', 'meet', 'green', 'seem', 'week', 'peer', 'steel', 'speed', 'career', 'queen'
            filtered_fails = []
            for word in fails:
                w_lower = word.lower()
                # Skip common English words
                if w_lower in [
                    'been', 'free', 'need', 'good', 'book', 'wood', 'feel', 'foot', 'look', 'seed', 'deep', 'keep', 
                    'meet', 'green', 'seem', 'week', 'peer', 'steel', 'speed', 'career', 'queen', 'between', 'sleep', 
                    'tree', 'sweet', 'indeed', 'teeth', 'cheese', 'creature', 'cooperate', 'blood', 'flood', 'door', 
                    'floor', 'poor', 'cool', 'tool', 'pool', 'root', 'shoot', 'smooth', 'choose', 'loose', 'doom', 
                    'gloom', 'room', 'spoon', 'fool', 'wool', 'boot', 'loop', 'soon', 'seen', 'screen', 'sheet', 
                    'heel', 'wheel', 'fever', 'jeep', 'beep', 'creep', 'steep', 'sweep', 'weep', 'fleet', 'greet', 
                    'sheet', 'sleeve', 'breeze', 'freeze', 'squeeze', 'steel', 'peer', 'steer', 'cheer', 'queer', 
                    'pioneer', 'volunteer', 'engineer', 'career', 'guarantee', 'refugee', 'employee', 'committee', 
                    'decree', 'agree', 'disagree', 'flee', 'degree', 'three', 'coffee', 'too', 'zoo', 'shampoo', 
                    'kangaroo', 'bamboo', 'tattoo', 'igloo', 'cuckoo', 'lagoon', 'monsoon', 'typhoon', 'cocoon', 
                    'balloon', 'cartoon', 'saloon', 'harpoon', 'buffoon', 'baboon', 'maroon', 'noon', 'afternoon', 
                    'afterword', 'password', 'keyword', 'forward', 'reward', 'ward', 'cow', 'how', 'now', 'row', 
                    'show', 'slow', 'snow', 'blow', 'flow', 'glow', 'grow', 'throw', 'crow', 'know', 'brown', 'crown', 
                    'clown', 'down', 'town', 'gown', 'drown', 'frown', 'power', 'tower', 'flower', 'shower', 'bowl', 
                    'fowl', 'howl', 'owl', 'growl', 'prowl', 'allow', 'bow', 'low', 'mow', 'sow', 'tow', 'below', 
                    'arrow', 'narrow', 'barrow', 'sorrow', 'borrow', 'tomorrow', 'shadow', 'widow', 'window', 'elbow', 
                    'yellow', 'bellow', 'fellow', 'hollow', 'follow', 'swallow', 'willow', 'billow', 'pillow', 'shallow', 
                    'rowing', 'showing', 'blowing', 'flowing', 'growing', 'knowing', 'throwing', 'allowing', 'following', 
                    'owned', 'owner', 'ownership', 'lower', 'lowest', 'slowly', 'slowdown', 'download', 'upload', 
                    'township', 'downward', 'downwind', 'downstairs', 'downtown', 'needless', 'needy', 'feeling', 
                    'speedy', 'weekly', 'seeming', 'seemingly', 'creepy', 'greedy', 'greed', 'sleepy', 'sleepless', 
                    'sleeping', 'sweepstake', 'fleetness', 'refugees', 'guarantees', 'agreements', 'degrees', 'coffeehouse', 
                    'bloody', 'flooding', 'doors', 'floors', 'roommate', 'spoons', 'boots', 'loops', 'moisture', 
                    'cooperation', 'cooperative', 'coordinate', 'coordination', 'woodland', 'woodpecker', 'wooden', 
                    'woods', 'goodness', 'goodbye', 'goods', 'bookstore', 'books', 'booklet', 'booking', 'lookout', 
                    'looking', 'looks', 'smoothly', 'smoothness', 'choosing', 'rooms', 'spoonful', 'fools', 'boots', 
                    'igloos', 'bamboos', 'balloons', 'cartoons', 'cocoons', 'noontime', 'spooky', 'drizzle', 'grizzly', 
                    'web', 'app', 'dev', 'git', 'npm', 'npx', 'vite', 'next', 'tailwind', 'css', 'html', 'js', 
                    'epub', 'docx', 'pdf', 'txt', 'md', 'readme', 'unreal', 'ruler', 'gma', 'shiraori', 'meido', 
                    'byaku', 'reise', 'hyuvan', 'nia', 'gohka', 'bloe', 'kugo', 'kogou', 'sanatoria', 'basgath', 
                    'goyef', 'potimas', 'hyrince', 'julius', 'leston', 'schlain', 'analeit', 'anabald', 'karnatia', 
                    'filimes', 'filimõs', 'harrifenas', 'suriya', 'feirune', 'shinohara', 'mirei', 'kengo', 'natsume', 
                    'renxandt', 'vandwald', 'yurin', 'ullen', 'yaana', 'jeskan', 'hawkin', 'cylis', 'ronandt', 
                    'aurel', 'sophia', 'keren', 'klevea', 'shiraori', 'basgath', 'agner', 'huey', 'sakurazaki', 
                    'temarikawa', 'furuta', 'kyouya', 'sasajima', 'rihoko', 'kouta', 'naofumi', 'issei', 'ogiwara', 
                    'tagawa', 'kunihiko', 'asaka', 'kushitani', 'seras', 'john', 'dustin', 'kusama', 'shinobu', 
                    'tiva', 'agrissa', 'furyu', 'kakashi', 'asahi', 'asahiro', 'editor', 'erguner', 'ricep', 
                    'reigar', 'phthalo', 'wald', 'phelmina', 'foduey', 'daztrudia', 'alleius', 'kasanagara', 
                    'kusorion', 'garam', 'uine', 'taratect', 'zatona', 'sariella', 'ohts', 'convenience', 
                    'uppenbebetenia', 'nguyen', 'iena', 'darad', 'elroe', 'labyrinths', 'labyrinth', 'g-meteo', 
                    'gluttonous', 'gloria', 'omega', 'gregor', 'gregore', 'byakuya', 'byakko', 'byaku', 'reise', 
                    'kuro', 'shiro', 'kumoko', 'zagan', 'watashi', 'nameless', 'dragon', 'dragons', 'wyrm', 'wyrms', 
                    'system', 'status', 'level', 'skill', 'skills', 'magic', 'resist', 'resistance', 'nullification', 
                    'mitigation', 'recovery', 'speed', 'perception', 'operation', 'telepathy', 'concentration', 
                    'stealth', 'appraisal', 'skanda', 'fortitude', 'stronghold', 'solidity', 'strength', 'durability', 
                    'acceleration', 'skanda', 'taboo', 'pride', 'overeating', 'gorge', 'satiation', 'sloth', 'greed', 
                    'lust', 'charity', 'mercy', 'patience', 'humility', 'temperance', 'chastity', 'diligence', 
                    'wisdom', 'hades', 'abyss', 'heresy', 'spatial', 'dimensional', 'cutting', 'piercing', 'impact', 
                    'shock', 'rot', 'acid', 'poison', 'paralysis', 'petrification', 'faint', 'fear', 'evil', 'eye', 
                    'annihilating', 'jinx', 'inert', 'warped', 'antimagic', 'sealing', 'cursed', 'telescopic', 
                    'clairvoyance', 'panoptic', 'vision', 'thread', 'creation', 'control', 'utility', 'divine', 
                    'weaving', 'swordsmanship', 'sword', 'mastery', 'warfare', 'mental', 'battle', 'divinity', 
                    'summoning', 'breath', 'scales', 'barrier', 'refere', 'referee', 'referees', 'reference', 
                    'references', 'ferry', 'ferryman', 'cherry', 'merry', 'berry', 'sherry', 'terry', 'perry', 
                    'carrier', 'barrier', 'barriers', 'harry', 'potter', 'tumblr', 'instagram', 'twitter', 
                    'facebook', 'yenpress', 'booklink', 'press', 'newsletter', 'mp4directs', 'goldenagato', 
                    'mp4directs.com', 'http', 'https', 'www', 'url', 'uri', 'pdf', 'epub', 'docx', 'txt', 'md'
                ]:
                    continue
                filtered_fails.append(word)
            
            if filtered_fails:
                print(f"  [Telex Fail] Line {idx+1}: {filtered_fails} in line: {line.strip()}")
