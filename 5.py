import hashlib
import sys

string = "ojvtpuvg"

hashes = []
result = list("________")
for i in xrange(1000000000):
  h = hashlib.md5(string+str(i)).hexdigest()
  if h.startswith("00000"):
    if h[5] in "01234567" and result[int(h[5])] == "_":
      result[int(h[5])] = h[6]
    hashes.append(h)



  if i % 1000 == 0:
    sys.stdout.write("{:>10} - {:>2} | {}\r".format(i, len(hashes),"".join(result)))
    sys.stdout.flush()
    if "_" not in result:
      break

print""
print "".join(i[5] for i in hashes[:8])


