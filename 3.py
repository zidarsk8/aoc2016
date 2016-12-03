import data_3

lines = [sorted(map(int, line.split())) for line in data_3.text.splitlines()]

proper_triangles = [line for line in lines if line[0]+line[1] > line[2]]
print len(proper_triangles)


lines = [map(int, line.split()) for line in data_3.text.splitlines()]
n = 3
row = sum(map(list, zip(*lines)), [])
rows = [sorted(row[i:i + n]) for i in xrange(0, len(row), n)]

proper_triangles = [line for line in rows if line[0]+line[1] > line[2]]
print len(proper_triangles)
