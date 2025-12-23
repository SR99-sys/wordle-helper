from collections import Counter

def expected_greens_score(guess: str, pos_counts: list[Counter], total: int) -> float:
    return sum(pos_counts[i][guess[i]] / total for i in range(5))

def suggest_best_guess(remaining: list[str], allowed: list[str]) -> tuple[str, float]:
    total = len(remaining)
    pos_counts = [Counter() for _ in range(5)]

    for w in remaining:
        for i, ch in enumerate(w):
            pos_counts[i][ch] += 1

    best_word, best_score = None, -1.0
    for g in allowed:
        score = expected_greens_score(g, pos_counts, total)
        if score > best_score:
            best_word, best_score = g, score

    return best_word, best_score  # type: ignore
