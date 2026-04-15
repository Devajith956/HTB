import random

# =========================
# TEST CONFIGURATION
# =========================

INPUT_SIZES = [
    5,
    10,
    20,
    50,
    100,
    500,
    1000,
    2000,
    5000,
    10000,
]

QUESTION_COUNT = len(INPUT_SIZES)

# last visible (public) test
LAST_VISIBLE_TEST_IDX = 4

TIME_LIMIT_SEC = 5
TIME_LIMIT_COMPILED_SEC = 3


# =========================
# CORE GENERATOR FUNCTION
# =========================

def gen_question(test_idx: int):
    """
    Returns:
        question (str): input format for solver
        answer (str): correct output
    """

    n = INPUT_SIZES[test_idx]

    # optional: make results reproducible per test
    random.seed(1000 + test_idx)

    # =========================
    # EXAMPLE PROBLEM TEMPLATE
    # (you replace THIS section)
    # =========================

    MIN_VAL, MAX_VAL = -10_000, 10_000

    # example logic (you replace this with your problem logic)
    a = random.randint(MIN_VAL, MAX_VAL)
    b = random.randint(MIN_VAL, MAX_VAL)
    target = a + b

    arr = [a, b]

    # fill remaining values
    while len(arr) < n:
        x = random.randint(MIN_VAL, MAX_VAL)

        # avoid trivial duplicates that break uniqueness
        if target - x not in arr:
            arr.append(x)

    random.shuffle(arr)

    # =========================
    # BUILD INPUT STRING
    # =========================

    question = f"{target} {n}\n"
    question += " ".join(map(str, arr))

    # =========================
    # BUILD ANSWER STRING
    # =========================

    answer = f"{min(a, b)} {max(a, b)}"

    return question, answer
