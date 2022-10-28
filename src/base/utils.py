def get_swear_words() -> set:
    SWEAR_WORDS = set()
    with open('swear_words.txt', 'r') as f:
        for row in f:
            SWEAR_WORDS.add(row[:-1])
    return SWEAR_WORDS