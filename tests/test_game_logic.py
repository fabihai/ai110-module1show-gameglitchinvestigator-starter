from logic_utils import (
    check_guess,
    parse_guess,
    get_range_for_difficulty,
)


def test_check_guess_messages_and_outcome():
    # Numeric comparisons should return the correct outcome and human message
    outcome, message = check_guess(99, 68)
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = check_guess(1, 68)
    assert outcome == "Too Low"
    assert "HIGHER" in message

    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_parse_guess_bounds_and_float_parsing():
    low, high = get_range_for_difficulty("Normal")

    ok, val, err = parse_guess("50.0", low, high)
    assert ok is True and val == 50 and err is None

    ok, val, err = parse_guess("0", low, high)
    assert ok is False
    assert val is None
    assert "out of bounds" in err.lower()


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
