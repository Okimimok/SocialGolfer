from intree import InTree
from HonhonDP import Alg3 as HonhonDP
from DP import DP as JakeDP
from os.path import dirname, realpath, join
from math import ceil, log
import numpy as np
import time

# Randomly-generated instances in which revenue and fixed cost are normal random
# 	variables. We test "full" intrees containing 1, 3, 7, 15, and 31 nodes, e.g:
#
# 				0     4     2      6      1     5      3      7  
#				   8	       10            9            11
#					    12                         13
#									  14
#
# Nodes are labeled this way so that parents of a given node are easier to
#	compute: e.g., for a node on level > 1, where the root is at level 1: 
#			LeftParent(i)  = i - 2^(level(i)) 
#			RightParent(i) = i - 2^(level(i)-1)
#
# Runtime estimated by taking the average over iid sample paths.

if __name__ == "__main__":
	basePath   = dirname(realpath(__file__))
	outputFile = "randomOutput.txt"
	outputPath = join(basePath, outputFile)

	# Assortment sizes to be tested
	Nvals = np.array([1, 3, 7, 15, 31, 63, 127])

	# Number of iterations to determine avg. runtime
	iters = 250
	
	# Vector of runtimes
	rtJake   = np.zeros(len(Nvals))
	rtHonhon = np.zeros(len(Nvals))

	for i in xrange(len(Nvals)):
		# Build tree
		N    = Nvals[i]
		lvls = int(log(N+1, 2))
		tree = InTree()
	
		cnt = 0
		for l in xrange(lvls, 0, -1):
			# Number of nodes in level l = 2^(l-1)
			num = 2**(l-1)
			if l == lvls:
				# Topmost level
				for m in xrange(num):
					tree.add_node(cnt)
					cnt += 1
			else: 
				for m in xrange(num):
					idxL = cnt - 2**l
					idxR = cnt - 2**(l-1)
					tree.add_node(cnt, lparent_index=idxL, rparent_index=idxR)
					cnt += 1
				
		for j in xrange(iters):			
			# Randomly-generated problem parameters
			rev   = abs(np.random.normal(3, 1, N))
			b     = 0.25
			f     = np.arange(0, lvls*b, b)
			K     = abs(np.random.normal(1, 1, N)) 
			custs = [[k, N-1, 1.0/N] for k in range(N)]

			# Solving the appropriate DP
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
			f.write('%i %.6f %.6f\n' % (Nvals[i], rtJake[i], rtHonhon[i]))
