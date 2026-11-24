"""Office joke entry for "Make the AI Judge Laugh: the Office Joke Open".

Writes one line of office comedy to /output/entry.txt (1-200 chars, UTF-8).
"""

import os

# The joke: 125 characters, inside the gate's 1-200 range. The payoff lands
# in the last few words ("It ran 40 minutes over"), which is what the
# judge's brief rewards.
LINE = "The meeting that could have been an email became a meeting about why it could not have been an email. It ran 40 minutes over."

MAX_LEN = 200

assert 1 <= len(LINE) <= MAX_LEN

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Read-back verification: the file must contain exactly the line, nothing more.
with open("/output/entry.txt", encoding="utf-8", newline="") as f:
    assert f.read() == LINE
