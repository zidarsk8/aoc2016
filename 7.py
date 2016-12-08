import re

import data_7


lines = [re.split("\[|\]", line) for line in data_7.text.splitlines()]


def has_pal(text):
  return any(
      text[i:i + 4] == text[i:i + 4][::-1] and text[i] != text[i + 1]
      for i in range(0, len(text) - 3)
  )


def check_line(line):
  return max(int(has_pal(part)) + int(has_pal(part)) * i%2
          for i, part in enumerate(line)) == 1

print sum(check_line(line) for line in lines)
