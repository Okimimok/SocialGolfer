from intree import InTree
from DP import DP as JakeDP
from HonhonDP import Alg3 as HonhonDP
import unittest
import numpy as np

# A series of unit tests to determine whether the two DPs are equivalent: e.g., whether
#	they output the same optimal assortments and expected revenues

#################################### TEST CASE 1 #########
# Example 3 from Honhon et al.	
##########################################################

class HonhonUnitTest1(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1)
		self.tree.add_node(2, lparent_index=0, rparent_index=1)
		self.tree.add_node(3)
		self.tree.add_node(4, lparent_index=2, rparent_index=3)
	
		self.rev   = [8.0, 21.0, 11.5, 20.0, 2.0]
		self.K	   = [2.0, 2.0, 2.0, 2.0, 2.0]
		self.f	   = [0.0, 0.2, 0.4, 0.6]
		self.cust  = [[i, 4, 0.2] for i in xrange(5)]


	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)

#################################### TEST CASE 2 #########
# One-node intree. Test case 2 from test_HonHonDP.py
##########################################################

class HonhonUnitTest2(unittest.TestCase):
	def setUp(self):
		self.tree  = InTree()
		self.tree.add_node(0)
		self.rev   = [2.0]
		self.K	   = [3.0]
		self.f	   = [0.0]
		self.cust  = [[0, 0, 1]]

	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)

#################################### TEST CASE 3 #########
# One-node intree. Test case 3 from test_HonhonDP.py
##########################################################

class HonhonUnitTest3(unittest.TestCase):
	def setUp(self):
		self.tree  = InTree()
		self.tree.add_node(0)
		self.rev   = [2.0]
		self.K	   = [1.0]
		self.f	   = [0.0]
		self.cust  = [[0, 0, 1]]

	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)

#################################### TEST CASE 4 #########
# Three-node intree. Test case 4 from test_HonhonDP.py
##########################################################

class HonhonUnitTest4(unittest.TestCase):
	def setUp(self):
		self.tree  = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1, lparent_index = 0)
		self.tree.add_node(2, lparent_index = 1)
		self.rev   = [6, 2.9, 3.2]
		self.K	   = [1.0, 1.0, 1.0]
		self.f	   = [0.0, 0.4, 0.8]
		self.cust  = [[0, 2, 1.0/3], [1, 2, 1.0/3], [2, 2, 1.0/3]]

	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)


#################################### TEST CASE 5 #########
# Two-node intree. Test case 1 from test_DP.py
##########################################################

class DPUnitTest1(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1,0)
		self.rev  = [1, 2]
		self.f	  = [0, 0.5]
		self.K	  = [0, 0.25]
		self.cust = [[0,0,0.5],[0,1,0.5]]

	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)

#################################### TEST CASE 6 #########
# Four-node intree. Test case 2 from test_DP.py
##########################################################

class DPUnitTest2(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1,0)
		self.tree.add_node(2,1)
		self.tree.add_node(3,2)
		self.rev  = [1, 1, 3, 4]
		self.f	  = [0, 1, 2, 3]
		self.K	  = [0.5, 0.5, 0.5, 0.5]
		self.cust = [[0,3,0.25],[1,3,0.25],[2,3,0.25],[0,2,0.25]]

	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)

#################################### TEST CASE 7 #########
# Three-node intree. Test case 3 from test_DP.py
##########################################################

class DPUnitTest3(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1)
		self.tree.add_node(2,0,1)
		self.rev  = [1, 1, 1]
		self.f	  = [0, 0.7]
		self.K	  = [0,0,0]
		self.cust = [[0,2,0.5], [1,2,0.5]]

	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)

#################################### TEST CASE 8 #########
# Seven-node intree. Test case 4 from test_DP.py
##########################################################

class DPUnitTest4(unittest.TestCase):
	def setUp(self):
		self.tree = InTree()
		self.tree.add_node(0)
		self.tree.add_node(1)
		self.tree.add_node(2)
		self.tree.add_node(3)
		self.tree.add_node(4, 0, 1)
		self.tree.add_node(5, 2, 3)
		self.tree.add_node(6, 4, 5)
		self.rev  = [1,1,2,1,3,2,4]
		self.f	  = [0, 0.25, 0.5]
		self.K	  = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
		self.cust = [[0,6,0.25],[1,6,0.25],[2,6,0.25],[3,6,0.25]]

	def test_solutions(self):
		optH, optObjH = HonhonDP(self.tree, self.rev, self.K, self.f, self.cust)
		optJ, optObjJ = JakeDP(self.tree, self.rev, self.K, self.f, self.cust)
		self.assertEqual(sorted(optH), sorted(optJ))
		self.assertAlmostEqual(optObjH, optObjJ)
if __name__ == '__main__':
	unittest.main() 
