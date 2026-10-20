"""Unicode-aware text helpers: display width and line splitting."""

import unicodedata

__all__ = ["display_width", "split_lines", "is_zero_width"]

_COMBINING_CATEGORIES = {"Mn", "Me", "Cf"}


def is_zero_width(ch: str) -> bool:
    """True for combining marks and format characters."""
    return unicodedata.category(ch) in _COMBINING_CATEGORIES


def display_width(text: str) -> int:
    """Return the number of display columns `text` occupies.

    Combining marks and format characters count as zero; everything
    else counts as one column (East Asian wide characters are treated
    as one column for simplicity).
    """
    return sum(0 if is_zero_width(ch) else 1 for ch in text)


def split_lines(text: str, width: int) -> list:
    """Split `text` into chunks of at most `width` display columns.

    Splits on the last space inside the window when possible,
    otherwise breaks at exactly `width` columns.
    """
    if width <= 0:
        raise ValueError("width must be positive")
    out = []
    line = []
    used = 0
    for ch in text:
        w = 0 if is_zero_width(ch) else 1
        if used + w > width:
            joined = "".join(line)
            cut = joined.rfind(" ")
            if 0 < cut:
                out.append(joined[:cut])
                rest = joined[cut + 1:]
                if rest:
                    line = [c for c in rest]
                    used = display_width(rest)
                else:
                    line = []
                    used = 0
            else:
                out.append(joined)
                line = []
                used = 0
            if ch == " ":
                continue
        line.append(ch)
        used += w
    if line:
        out.append("".join(line))
    return out
