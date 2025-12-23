import requests

WORD_LIST_URL = "https://gist.github.com/cfreshman/dec102adb5e60a8299857cbf78f6cf57/raw"

def load_words_from_web(url: str = WORD_LIST_URL) -> list[str]:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    words = [
        w.strip().upper()
        for w in resp.text.splitlines()
        if len(w.strip()) == 5 and w.strip().isalpha()
    ]
    return sorted(set(words))
