from collections import Counter

def wordle_feedback(answer: str, guess: str) -> str:
    answer = answer.upper()
    guess = guess.upper()

    result = ["B"] * 5
    remaining = Counter(answer)

    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = "G"
            remaining[guess[i]] -= 1

    for i in range(5):
        if result[i] == "G":
            continue
        if remaining[guess[i]] > 0:
            result[i] = "Y"
            remaining[guess[i]] -= 1

    return "".join(result)
