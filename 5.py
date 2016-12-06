import hashlib
import sys

string = "ojvtpuvg"

hashes = []
for i in xrange(100000000):
  h = hashlib.md5(string+str(i)).hexdigest()
  if h.startswith("00000"):
    hashes.append(h)
  if i % 100 == 0:
    sys.stdout.write("{:>10} - {}\r".format(i, len(hashes)))
    sys.stdout.flush()
    if len(hashes) > 7:
      break

print""
print "".join(i[5] for i in hashes[:8])


