import random

VALID_KEYWORDS = ["+", "-", "/", "*", "(", ")", " "]

DIFFICULTIES = {
    'easy': 1,
    'medium': 2,
    'hard': 3
}


def calculate(user_input: str):
    user_input = list(user_input)
    
    for phrase in user_input:
        if (not (phrase.isdecimal() or phrase.isdigit())) and phrase not in VALID_KEYWORDS:
            raise SyntaxError('Word found in equation. (use * for multiply)')

    return eval(' '.join(user_input))


def create_question(difficulty: str):
    difficulty = DIFFICULTIES[difficulty]
    _sum = ""

    for i in range(difficulty):
        if _sum != "" and _sum[-1] not in VALID_KEYWORDS:
            _sum += " " + random.choice(VALID_KEYWORDS[:4]) + " "
        _sum += str(round(random.choice([(random.randint(3, 27) * random.randint(9, 36) - 7),
                                         (random.randint(2, 7) / random.randint(21, 45) - 5)]))) + " "
        _sum += random.choice(VALID_KEYWORDS[:4]) + " "
        _sum += str(round(random.choice([((random.randint(3, 27) * random.randint(9, 36)) - 7),
                                         ((random.randint(2, 7) / random.randint(21, 45)) - 5)])))

    return _sum
