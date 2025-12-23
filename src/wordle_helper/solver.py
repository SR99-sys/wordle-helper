from .feedback import wordle_feedback
from .scoring import suggest_best_guess

def filter_candidates(candidates: list[str], guess: str, feedback: str) -> list[str]:
    return [w for w in candidates if wordle_feedback(w, guess) == feedback]

def play_wordle_hybrid(all_words: list[str], max_turns: int = 6):
    remaining = all_words[:]

    print("\n=== WORDLE HELPER (Manual Turn 1, Auto Turn 2..6) ===")

    first_guess = input("Enter your FIRST guess: ").strip().upper()
    first_fb = input(f"Enter feedback for {first_guess}: ").strip().upper()

    if first_fb == "GGGGG":
        print("Solved on Turn 1 🎉")
        return

    remaining = filter_candidates(remaining, first_guess, first_fb)

    for turn in range(2, max_turns + 1):
        best, score = suggest_best_guess(remaining, all_words)
        print(f"\nTurn {turn}: Auto-picked {best} (score={score:.4f})")

        fb = input(f"Enter feedback for {best}: ").strip().upper()
        if fb == "GGGGG":
            print("Solved! 🎉")
            return

        remaining = filter_candidates(remaining, best, fb)
