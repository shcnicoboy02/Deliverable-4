# GenAI log – Deliverable 4, Task 1

**Tool:** Claude Code (model: Claude Opus 5.5), used as an extension in VS Code
**Date:** 25 November 2026
**Scope:** Task 1 (`temperature.py` and `test_temperature.py`)

## How we used the AI

We set the AI up as a reviewer, not as a code generator. Project instructions told it
not to write solution code. It was to point out problems, explain why they matter and
ask guiding questions, and leave the fixes to us. We wrote all of the code in
`temperature.py` and `test_temperature.py` ourselves.

## Summary of the conversation

### 1. First review of `temperature.py`
We asked the AI to review our first version of the `Temperature` class. It read the task
description in the notebook, ran the module with two Python versions and tried a few
edge cases. Its feedback:

- **Strengths it pointed out:** read-only attributes made with `@property`, unit
  validation kept in one shared helper, all comparisons done in Kelvin with the same
  tolerance, and `NotImplemented` returned for non-`Temperature` operands.
- **Python version issue:** `-> Temperature` inside the class crashed with `NameError`
  on Python 3.9, but worked on Python 3.14 (our virtual environment). Instead of giving
  us the fix, the AI asked *when* Python evaluates type hints.
- **NaN passes validation:** `Temperature(float("nan"))` is accepted, because every
  comparison with NaN is `False`. The AI said this is not required by the task.
- **Unhashable instances:** defining `__eq__` sets `__hash__` to `None`. Not required by
  the task, but a useful concept to understand.
- **`__ne__` is redundant:** in Python 3, `!=` is derived from `__eq__` automatically.
  We kept it because the task asks for all six comparisons.
- **Style:** the conversion methods had no docstrings.

### 2. Our fixes
We fixed the Python version issue by adding `from __future__ import annotations`, and we
added docstrings. The AI checked that the module now imports on both Python 3.9 and
3.14. It also noted that one docstring line is longer than PEP 8 recommends. We chose not
to deal with NaN or hashing, because neither is part of the task.

### 3. Review of `test_temperature.py`
At first the AI said Task 1 was not finished because the test file was missing. That was
wrong: it had listed the folder before we created the file. When we pointed this out, it
read the file and ran pytest (59 passed). It confirmed that all six required test areas
are covered, and noted that the `NotImplemented` test only checks `__eq__` and `__lt__`
directly, not all six comparison methods.

## Reflection

- **Useful:** the AI ran the code with a different Python version than ours and found a
  bug we would not have caught ourselves. It also explained concepts we had not thought
  about (when annotations are evaluated, NaN comparisons, `__hash__`).
- **Learning:** because the AI asked questions instead of handing over fixes, we had to
  understand each problem before fixing it.
- **Limitations:** the AI made a factual mistake (it said the test file was missing).
  Its answers have to be checked, not just accepted.
