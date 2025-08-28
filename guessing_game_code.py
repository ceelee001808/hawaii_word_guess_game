import random

WORDS = WORDS = [
    # islands
    "hawaii","oahu","maui","kauai","lanai","molokai","niihau","kahoolawe",
    # places & landmarks
    "honolulu","waikiki","kailua","lahaina","haleiwa","kahului","kihei","paia",
    "kaneohe","kailuakona","kona","waimea","waipio","hanalei","poipu","kapaa",
    "lihue","makaha","kakaako","alamoana","kualoa","kaneohebay","manoafalls",
    "diamondhead","hanauma","kokocrater","kokohead","pololu","napali",
    "haleakala","maunakea","maunaloa",
    # culture & language
    "aloha","mahalo","ohana","keiki","kupuna","kapu","kuleana","pono",
    "kamaaina","lei","hula","mele","ukulele","luau","imu","heiau","ahupuaa",
    # food
    "poi","laulau","poke","shaveice","spam","musubi","spammusubi","malasada",
    "manapua","saimin","locomoco","lomisalmon",
    #flowers and animals
    "plumeria","hibiscus","pikake","lehua","kukui","koa","ohia","ti","niu",
    "nene","honu","seaturtle","monkseal",
    "humuhumunukunukuapuaa","manta","dolphin","humpback","whale",
    # nature & vibes
    "pali","mauka","makai","lani","kai","volcano","lava","vog","tradewinds",
    "rainbow","sunrise","sunset","reef","coconut","pineapple","sugarcane",
    "taro","kalo",
    # activities
    "surf","longboard","shortboard","outrigger","canoe","paddle","snorkel",
    "diving","hiking"
]


def play(words=WORDS, attempts=None):
    word = random.choice(words).lower()
    # dynamic attempts: at least 10, scales with word length
    attempts = attempts if attempts is not None else max(10, len(word) + 2)

    revealed = ['_'] * len(word)
    used = set()
    wrong = set()

    while attempts > 0:
        print(f"\nWord: {' '.join(revealed)}   Wrong: {', '.join(sorted(wrong)) or '-'}   Attempts: {attempts}")
        guess = input("Guess a letter (or the whole word): ").strip().lower()

        if not guess:
            print("Please enter something.")
            continue
        if guess in used:
            print("You already tried that — no penalty.")
            continue
        used.add(guess)

        # Single-letter guess
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                for i, ch in enumerate(word):
                    if ch == guess:
                        revealed[i] = guess
                print("Great guess!")
            else:
                attempts -= 1
                wrong.add(guess)
                print("Wrong guess!")
        # Whole-word guess
        else:
            if guess == word:
                revealed = list(word)
                print("You nailed it!")
                break
            else:
                attempts -= 1
                print("Not the word.")

        if '_' not in revealed:
            break

    if '_' not in revealed:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"\nOut of attempts! The word was: {word}")

if __name__ == "__main__":
    play()
