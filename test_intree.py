import intree
import unittest

class TestInTree(unittest.TestCase):
    def setUp(self):
        self.tree1 = intree.InTree()
        self.tree1.add_node(1)

        self.tree2 = intree.InTree()
        self.tree2.add_node(1)
        self.tree2.add_node(2)
        self.tree2.add_node(3,1,2)

        self.tree3 = intree.InTree()
        self.tree3.add_node(1)
        self.tree3.add_node(2)
        self.tree3.add_node(3, 1, 2)
        self.tree3.add_node(4)
        self.tree3.add_node(5)
        self.tree3.add_node(6, 3, 4)
        self.tree3.add_node(7, 5)
        self.tree3.add_node(8, 6, 7)
        self.tree3.add_node(9, 8)

    # Test that the correct size is returned
    def test_size(self):
        self.assertEqual(self.tree1.size(),1)
        self.assertEqual(self.tree2.size(),3)
        self.assertEqual(self.tree3.size(),9)

    # Test that get_node returns the correct node
    def test_get_node(self):
        self.assertEqual(self.tree2.get_node(1).index(), 1)
        self.assertEqual(self.tree2.get_node(2).index(), 2)
        self.assertEqual(self.tree2.get_node(3).index(), 3)

    # Test that parents and children are set correctly
    def test_add_node(self):
        self.assertEqual(self.tree2.get_node(1).child(), 3)
        self.assertEqual(self.tree2.get_node(1).rparent(), None)
        self.assertEqual(self.tree2.get_node(1).lparent(), None)
        self.assertEqual(self.tree2.get_node(3).rparent(), 1)
        self.assertEqual(self.tree2.get_node(3).lparent(), 2)
        self.assertEqual(self.tree2.get_node(3).child(), None)

    # Test that get_path returns [] if no path
    def test_get_path_empty(self):
        self.assertEqual(self.tree2.get_path(1,2), [])
        self.assertEqual(self.tree2.get_path(3,1), [])

    # Test that get_path(i,i) returns [i]
    def test_get_path_single(self):
        self.assertEqual(self.tree1.get_path(1,1),[1])    

    # Test that get_path returns the correct path
    def test_get_path(self):
        self.assertEqual(self.tree2.get_path(1,3), [1,3])
        self.assertEqual(self.tree3.get_path(4,8), [4, 6, 8])
        self.assertEqual(self.tree3.get_path(2,9), [2, 3, 6, 8, 9])

    # Test simple cases of get_ordered_pairs
    def test_get_ordered_pairs_simple(self):
        self.assertEqual(self.tree1.get_ordered_pairs(), [[1, 'empty']])
        self.assertEqual(self.tree2.get_ordered_pairs(), \
                         [[1,3], [1, 'empty'], [2,3], [2,'empty'],[3, 'empty']])        

    # Test get_ordered_pairs returns pairs such that all parent
    # pairs are calculated before child pairs
    def test_get_ordered_pairs(self):
        pair_list = self.tree3.get_ordered_pairs()

        i = 1
        j = 3
        for k in [6, 8, 9]:
            indexi = pair_list.index([i,k])
            indexj = pair_list.index([j,k])
            self.assertTrue(indexi < indexj )
        
