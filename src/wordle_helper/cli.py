from .wordlist import load_words_from_web
from .solver import play_wordle_hybrid

def main():
    words = load_words_from_web()
    print(f"Loaded {len(words)} words.")
    play_wordle_hybrid(words, max_turns=6)

if __name__ == "__main__":
    main()
