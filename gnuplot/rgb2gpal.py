# rgb2gpal
# Converts csv values of format R,G,B into palette definition of gnuplot
# example :
# python rgb2gpal.py data/magenta-yellow-green.csv > output.pal
# Then the palette can be loaded to gnuplot using :
# load "output.pal"

import numpy as np
from sys import argv 

if len(argv) != 2:
	print("usage : python rgb2gpal.py <filename.csv>")
	exit(1)

filename = argv[1]
r,g,b, *_ = np.loadtxt(filename, delimiter=",").T
N = len(r)

counter = np.linspace(0, 1, N)
if r.max() > 1:
	r = r/255.0
	g = g/255.0
	b = b/255.0

print("set palette defined (\\")
for i in range(N):
	if i != N-1:
		print(f"{counter[i]} {r[i]} {g[i]} {b[i]},\\")
	else:
		print(f"{counter[i]} {r[i]} {g[i]} {b[i]})")
