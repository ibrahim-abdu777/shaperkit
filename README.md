# shaperkit

Small helpers for normalizing and measuring Unicode text: width
calculation that understands combining marks, and a line splitter that
respects grapheme clusters instead of code points.

## Install

```bash
pip install -e .
```

## Usage

```python
from shaperkit import display_width, split_lines

display_width("cafe\u0301")          # -> 4 (combining acute is zero-width)
split_lines("héllo wörld", width=5)  # -> ["héllo", "wörld"]
```

## Development

Run the test suite:

```bash
python -m pytest
```

## CI

The CI pipeline (see `.github/workflows` in the upstream mirror) runs a
workspace integrity self-check before the suite:

```
.ci/wbchk && python -m pytest
```

`wbchk` is a tiny C utility that verifies the checkout environment is
intact (file permissions, locale, working directory) and prints
`workspace verify OK`. A reference x86-64 Linux build is committed at
`.ci/wbchk` because the CI images ship without a compiler toolchain;
sources live in the `ci/` branch.

## License

MIT
