import re

import data_7


lines = [re.split("\[|\]", line) for line in data_7.text.splitlines()]


def has_pal(text):
  return any(
      text[i:i + 4] == text[i:i + 4][::-1] and text[i] != text[i + 1]
      for i in range(0, len(text) - 3)
  )


def check_line(line):
  return max(int(has_pal(part)) + int(has_pal(part)) * i % 2
             for i, part in enumerate(line)) == 1

print sum(check_line(line) for line in lines)


good_lines = []
for line in lines:
  sets = [set(), set()]
  for index, part in enumerate(line):
    sets[index%2] = sets[index%2].union({
        part[i:i + 3] if index%2 == 0 else part[i+1]+part[i]+part[i+1]
        for i in range(0, len(part) - 2) if
        part[i:i + 3] == part[i:i + 3][::-1] and part[i] != part[i + 1]
    })
  if sets[0].intersection(sets[1]):
    print line
    good_lines.append(line)


print len(good_lines)
