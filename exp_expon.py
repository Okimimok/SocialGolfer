from intree import InTree
from HonhonDP import Alg3 as HonhonDP
from DP import DP as JakeDP
from os.path import dirname, realpath, join
import numpy as np
import time

# An example in which the algorithm by Honhon et al. seems to run (empirically)
# 	in exponential time (in the # of products). Tree a chain (no branching
#	Products are identical in the sense that they generate the same revenue,
#	and have the same (relatively high) fixed cost. Substitution cost is high. 
if __name__ == "__main__":
	basePath   = dirname(realpath(__file__))
	outputFile = "exponOutput.txt"
	outputPath = join(basePath, outputFile)

	# Assortment sizes to be tested
	Nvals = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

	# Number of iterations to determine avg. runtime
	iters = 30
	
	# Vector of runtimes
	rtJake   = np.zeros(len(Nvals))
	rtHonhon = np.zeros(len(Nvals))

	for i in xrange(len(Nvals)):
		# Build tree
		N    = Nvals[i]
		tree = InTree()
		tree.add_node(0)
		for k in range(1, N):
			tree.add_node(k, lparent_index = k-1)

		# Problem parameters
		rev   = 3.0*np.ones(N)
		b     = (rev[0]-0.001)/(N-1)
		f     = np.arange(0, N*b, b)
		K     = (4.5/N)*np.ones(N)
		custs = [[k, N-1, 1.0/N] for k in range(N)]

		for j in xrange(iters):
			startJ     = time.clock()
			JakeDP(tree, rev, K, f, custs)
			endJ       = time.clock()
			rtJake[i] += (endJ - startJ)/iters

			startH       = time.clock()
			HonhonDP(tree, rev, K, f, custs)
			endH         = time.clock()
			rtHonhon[i] += (endH - startH)/iters
		
	
	with open(outputPath, 'w') as f:
		f.write("#N JakeDPRuntime HonhonDPRuntime\n")
		for i in xrange(len(Nvals)):
			f.write('%i %.3f %.3f\n' % (Nvals[i], rtJake[i], rtHonhon[i]))
