import data_4
from collections import Counter

lines = data_4.text.splitlines()

parts = [line.split("-") for line in lines]

tuples = [("".join(part[0:-1]), int(part[-1].split("[")[0]), part[-1].split("[")[1][0:-1])
          for part in parts]

sorted_words = [
    (
        "".join(
            [l[1] for l in sorted([(-v, k) for k, v in Counter(word).items()])]
        )[:5],
        id_,
        checksum
    )
    for word, id_, checksum in tuples]

valid_ids = [id_ for word, id_, checksum in sorted_words if word == checksum]

print sum(valid_ids)



tuples = [("-".join(part[0:-1]), int(part[-1].split("[")[0]), part[-1].split("[")[1][0:-1])
          for part in parts]

char_map = {i:char for i,char in enumerate("abcdefghijklmnopqrstuvwxyz")}
index_map = {v:k for k, v in char_map.items()}


for t in tuples:
  new_str = "".join(
    char_map[(index_map[char]+t[1]) % 26] if char in index_map else " "
    for char in t[0]
  )
  if "north" in new_str:
    print new_str, t


