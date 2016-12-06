from collections import Counter
import data_6

chars = [list(line) for line in data_6.text.splitlines()]

chars = zip(*chars)

counts = [sorted([(v,k) for k,v in Counter(line).items()]) for line in chars]
print "".join(line[0][1] for line in counts)
