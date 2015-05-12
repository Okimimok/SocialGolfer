from intree import InTree
from DP import DP
from HonhonDP import DeltaMinus, DeltaPlus, Alg3, NPrev, prodPurchases
import unittest
import numpy as np

#################################### TEST CASE 1 #########
# Example 3 from Honhon et al. A five-product intree. 
##########################################################

class TestDPHonhon(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1)
		self.tree.add_node(2, lparent_index=0, rparent_index=1)
		self.tree.add_node(3)
		self.tree.add_node(4, lparent_index=2, rparent_index=3)
	
		self.rev  = [8.0, 21.0, 11.5, 20.0, 2.0]
		self.K    = [2.0, 2.0, 2.0, 2.0, 2.0]
		self.f	  = [0.0, 0.2, 0.4, 0.6]
		self.cust = [[i, 4, 0.2] for i in xrange(5)]

	def test_FirstStep(self):	
		# First step of Honhon's alg is to find the optimal assortment when there
		#	are no fixed costs (K = 0 for all products). For the above example
		#	{1, 2, 3, 4} (assuming products 0-indexed).  Jake's DP used here.

		SOpt = DP(self.tree, self.rev, np.zeros(5), self.f, self.cust)[0]
		self.assertEqual(sorted(SOpt), [1, 2, 3, 4])

	def test_LowerBd(self):
		# From there, Honhon's alg, attempts to add product 4 (the root), and computes
		# 	a lower bd. on the marginal revenue added by including it in the 
		#	assortment (when all products upstream offered)
		
		tmp = DeltaMinus(self.tree, self.rev, [], 4, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, -1.6)

	def test_UpperBd(self):
		# Because lower bound is negative, Honhon's alg then computes an upper bound
		#	on the marginal revenue asssociated with adding product 4 (when no 
		#	upstream products offered) 
		tmp = DeltaPlus(self.tree, self.rev, [], 4, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, -0.24)

	def test_solve(self):
		# Honhon's algorithm, from start to finish. Optimal assortment is {2, 3}.
		#	Revenue of 6.82. (Actually, 6.72, but we tweak Honhon's model slightly.)
		opt, optObj = Alg3(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertAlmostEqual(optObj, 6.82)
		self.assertEqual(sorted(opt), [2, 3])

	def test_optRev(self):
		# Checking if optimal assortment yields the desired revenue
		tmp = NPrev(self.tree, self.cust, self.rev, self.K, self.f, [2, 3])
		self.assertAlmostEqual(tmp, 6.82)

	def test_purchase(self):
		# Checks, given the optimal assortment, whether customers buy the 
		#	appropriate products: [2, 2, 2, 3, -1], respectively
		#   (-1 the null purchase)
		buy  = [0, 0, 0, 0, 0]		
		for i in xrange(5):
			path = self.tree.get_path(self.cust[i][0], self.custs[i][1])
			buy[i], _ = prodPurchases(path, [2, 3])
		self.assertEqual(buy, [2, 2, 2, 3, -1])
		

#################################### TEST CASE 2 #########
# One-node intree with one customer class. Optimal asst.
#	 empty, as fixed cost > revenue for that product. 
##########################################################

class TestDPSingleton(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.rev  = [2.0]
		self.K	  = [3.0]
		self.f    = [0.0]
		self.cust = [[0, 0, 1]]

	def test_FirstStep(self):	
		# Optimal assortment when K = 0 should be to include the product
		SOpt1 = DP(self.tree, self.rev, [0], self.f, self.cust)[0]
		self.assertEqual(SOpt1, [0])

	def test_LowerBd(self):
		# Lower bound and upper bound should both be -1.
		tmp = DeltaMinus(self.tree, self.rev, [], 0, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, -1)

	def test_UpperBd(self):
		tmp = DeltaPlus(self.tree, self.rev, [], 0, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, -1)

	def test_solve(self):
		# Optimal assortment generates revenue of 0
		opt, optObj = Alg3(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertAlmostEqual(optObj, 0)
		self.assertEqual(opt, [])

	def test_optRev(self):
		tmp = NPrev(self.tree, self.cust, self.rev, self.K, self.f, [])
		self.assertAlmostEqual(tmp, 0)

	def test_purchase(self):
		path   = self.tree.get_path(self.cust[0][0], self.custs[0][1])
		buy, _ = prodPurchases(path, [])
		self.assertEqual(buy, -1)

#################################### TEST CASE 3 #########
# One-node intree with one customer class. Optimal asst.
#	 contains that product. 
##########################################################

class TestDPSingleton2(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.rev  = [2.0]
		self.K	  = [1.0]
		self.f    = [0.0]
		self.cust = [[0, 0, 1]]

	def test_FirstStep(self):	
		# Optimal assortment when K = 0 should be to include the product
		SOpt1 = DP(self.tree, self.rev, [0], self.f, self.cust)[0]
		self.assertEqual(SOpt1, [0])

	def test_LowerBd(self):
		# Lower bound and upper bound should both be 1
		tmp = DeltaMinus(self.tree, self.rev, [], 0, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, 1)

	def test_UpperBd(self):
		tmp = DeltaPlus(self.tree, self.rev, [], 0, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, 1)

	def test_solve(self):
		# Optimal assortment generates revenue of 1
		opt, optObj = Alg3(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertAlmostEqual(optObj, 1)
		self.assertEqual(opt, [0])

	def test_optRev(self):
		tmp = NPrev(self.tree, self.cust, self.rev, self.K, self.f, [0])
		self.assertAlmostEqual(tmp, 1)

	def test_purchase(self):
		path   = self.tree.get_path(self.cust[0][0], self.custs[0][1])
		buy, _ = prodPurchases(path, [0])
		self.assertEqual(buy, 0)

#################################### TEST CASE 4 #########
# Three-node intree, arranged in a line. Optimal asst. 
#	 contains first and third product.  
##########################################################

class TestDPChain(unittest.TestCase):
	def setUp(self):
		self.tree  = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1, lparent_index = 0)
		self.tree.add_node(2, lparent_index = 1)
		self.rev  = [6, 2.9, 3.2]
		self.K	  = [1.0, 1.0, 1.0]
		self.f    = [0.0, 0.4, 0.8]
		self.cust = [[0, 2, 1.0/3], [1, 2, 1.0/3], [2, 2, 1.0/3]]

	def test_FirstStep(self):	
		# Optimal assortment when K = 0: add all three products 
		# 	Product 1 added because substitution cost > Rev(2) - Rev(1)
		SOpt1 = DP(self.tree, self.rev, np.zeros(3), self.f, self.cust)[0]
		self.assertEqual(sorted(SOpt1), [0, 1, 2])

	def test_LowerBd(self):
		# Lower bound when adding product 2
		tmp = DeltaMinus(self.tree, self.rev, [], 2, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, 0.2/3)

	def test_UpperBd(self):
		# Upper bound when adding product 2
		tmp = DeltaPlus(self.tree, self.rev, [], 2, self.f, self.K, self.cust)
		self.assertAlmostEqual(tmp, 1.80)
	
	def test_solve(self):
		# Optimal assortment generates revenue of 2
		opt, optObj = Alg3(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertAlmostEqual(optObj, 2)
		self.assertEqual(sorted(opt), [0, 2])

	def test_optRev(self):
		tmp = NPrev(self.tree, self.cust, self.rev, self.K, self.f, [0, 2])
		self.assertAlmostEqual(tmp, 2)

	def test_purchase(self):
		buy = [0, 0, 0]
		for i in xrange(3):
			path      = self.tree.get_path(self.cust[i][0], self.custs[i][1])
			buy[i], _ = prodPurchases(path, [0, 2])

		self.assertEqual(buy, [0, 2, 2])

if __name__ == '__main__':
	unittest.main() 
