import DP
import intree
import unittest

class TestDP(unittest.TestCase):
    def setUp(self):
        # Two Nodes
        self.tree0 = intree.InTree()
        self.tree0.add_node(0)
        self.tree0.add_node(1,0)
        self.rev0 = [1, 2]
        self.f0 = [0, 0.5]
        self.cost0 = [0, 0.25]
        self.cust0 = [[0,0,0.5],[0,1,0.5]]
        
        # Path with 4 nodes
        self.tree1 = intree.InTree()
        self.tree1.add_node(0)
        self.tree1.add_node(1,0)
        self.tree1.add_node(2,1)
        self.tree1.add_node(3,2)
        self.rev1 = [1, 1, 3, 4]
        self.f1 = [0, 1, 2, 3]
        self.cost1 = [0.5, 0.5, 0.5, 0.5]
        self.cust1 = [[0,3,0.25],[1,3,0.25],[2,3,0.25],[0,2,0.25]]

        # Binary tree with 3 nodes
        self.tree2 = intree.InTree()
        self.tree2.add_node(0)
        self.tree2.add_node(1)
        self.tree2.add_node(2,0,1)
        self.rev2 = [1, 1, 1]
        self.f2 = [0, 0.7]
        self.cost2 = [0,0,0]
        self.cust2 = [[0,2,0.5], [1,2,0.5]]

        # Binary tree with 7 nodes
        self.tree3 = intree.InTree()
        self.tree3.add_node(0)
        self.tree3.add_node(1)
        self.tree3.add_node(2)
        self.tree3.add_node(3)
        self.tree3.add_node(4, 0, 1)
        self.tree3.add_node(5, 2, 3)
        self.tree3.add_node(6, 4, 5)
        self.rev3 = [1,1,2,1,3,2,4]
        self.f3 = [0, 0.25, 0.5]
        self.cost3 = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
        self.cust3 = [[0,6,0.25],[1,6,0.25],[2,6,0.25],[3,6,0.25]]
        
    # Test revenue calculations along a path of length 2
    def test_preprocess_rev_path1(self):
        Rev,Rev_Sub,_,_ = DP.preprocess(self.tree0,self.rev0,self.f0,self.cust0)
        self.assertEqual(Rev[0],1)
        self.assertEqual(Rev[1],1)
        self.assertEqual(Rev_Sub[0,1],1)

    # Test revenue calculations along a path of length 4
    def test_preprocess_rev_path2(self):
        Rev,Rev_Sub,_,_ = DP.preprocess(self.tree1,self.rev1,self.f1,self.cust1)
        self.assertEqual(Rev[0],0.5)
        self.assertEqual(Rev[1],0.75)
        self.assertEqual(Rev[2],3)
        self.assertEqual(Rev[3],3)
        self.assertEqual(Rev_Sub[0,3],1)
        self.assertEqual(Rev_Sub[1,2],2.25)

    # Test revenue calculations in a binary tree of size 3
    def test_preprocess_rev_tree1(self):
        Rev,Rev_Sub,_,_ = DP.preprocess(self.tree2,self.rev2,self.f2,self.cust2)
        self.assertEqual(Rev[0],0.5)
        self.assertEqual(Rev[1],0.5)
        self.assertEqual(Rev[2],1)
        self.assertEqual(Rev_Sub[0,2],0.5)
        self.assertEqual(Rev_Sub[1,2],0.5)

    # Test revenue calculations in a binary tree of size 7
    def test_preprocess_rev_tree2(self):
        Rev,Rev_Sub,_,_ = DP.preprocess(self.tree3,self.rev3,self.f3,self.cust3)
        self.assertEqual(Rev[2],0.5)
        self.assertEqual(Rev[4],1.5)
        self.assertEqual(Rev[6],4)
        self.assertEqual(Rev_Sub[1,4],0.75)
        self.assertEqual(Rev_Sub[1,6],1)
        self.assertEqual(Rev_Sub[5,6],2)

    # Test penalty calculations along a path of length 2
    def test_preprocess_pen_path1(self):
        _,_,Pen,Pen_Sub = DP.preprocess(self.tree0,self.rev0,self.f0,self.cust0)
        self.assertEqual(Pen[0],0)
        self.assertEqual(Pen[1],0.25)
        self.assertEqual(Pen_Sub[0,1],0.25)

    # Test penalty calculations along a path of length 4
    def test_preprocess_pen_path2(self):
        _,_,Pen,Pen_Sub = DP.preprocess(self.tree1,self.rev1,self.f1,self.cust1)
        self.assertEqual(Pen[0],0)
        self.assertEqual(Pen[1],0.5)
        self.assertEqual(Pen[2],1.25)
        self.assertEqual(Pen[3],1.5)
        self.assertEqual(Pen_Sub[0,3],0.75)
        self.assertEqual(Pen_Sub[1,2],1.25)

    # Test penalty calculations in a binary tree of size 3
    def test_preprocess_pen_tree1(self):
        _,_,Pen,Pen_Sub = DP.preprocess(self.tree2,self.rev2,self.f2,self.cust2)
        self.assertEqual(Pen[0],0)
        self.assertEqual(Pen[1],0)
        self.assertEqual(Pen[2],0.7)
        self.assertEqual(Pen_Sub[0,2],0.35)
        self.assertEqual(Pen_Sub[1,2],0.35)

    # Test penalty calculations in a binary tree of size 7
    def test_preprocess_pen_tree2(self):
        _,_,Pen,Pen_Sub = DP.preprocess(self.tree3,self.rev3,self.f3,self.cust3)
        self.assertEqual(Pen[2],0)
        self.assertEqual(Pen[4],0.125)
        self.assertEqual(Pen[6],0.5)
        self.assertEqual(Pen_Sub[1,4],0.0625)
        self.assertEqual(Pen_Sub[1,6],0.125)
        self.assertEqual(Pen_Sub[5,6],0.25)

    # Test overall DP in a path of size 2
    def test_DP_path1(self):
        subset, rev = DP.DP(self.tree0,self.rev0,self.cost0,self.f0,self.cust0)
        self.assertEqual([0],subset)
        self.assertEqual(1, rev)

    # Test overall DP in a path of size 4
    def test_DP_path2(self):
        subset, rev = DP.DP(self.tree1,self.rev1,self.cost1,self.f1,self.cust1)
        self.assertEqual([2],subset)
        self.assertEqual(1.25, rev)

    # Test overall DP in a binary tree of size 3
    def test_DP_tree1(self):
        subset, rev = DP.DP(self.tree2,self.rev2,self.cost2,self.f2,self.cust2)
        self.assertEqual(set([0,1]),set(subset))
        self.assertEqual(1, rev)

    # Test overall DP in a binary tree of size 7   
    def test_DP_tree2(self):
        subset, rev = DP.DP(self.tree3,self.rev3,self.cost3,self.f3,self.cust3)
        self.assertEqual([6],subset)
        self.assertEqual(3.25, rev)
        
