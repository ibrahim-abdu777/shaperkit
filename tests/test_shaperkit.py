from shaperkit import display_width, split_lines


def test_combining_mark_is_zero_width():
    assert display_width("cafe\u0301") == 4
    assert display_width("caf\u00e9") == 4


def test_plain_ascii():
    assert display_width("hello") == 5


def test_split_respects_width():
    assert split_lines("hello world", width=5) == ["hello", "world"]


def test_split_breaks_long_word():
    assert split_lines("abcdefghij", width=4) == ["abcd", "efgh", "ij"]


def test_zero_width_must_be_positive():
    try:
        split_lines("x", width=0)
        raised = False
    except ValueError:
        raised = True
    assert raised
