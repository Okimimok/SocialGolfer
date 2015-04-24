
# A node has an index and the indices of it's child, right parent, and
# left parent

class Node:
    def __init__(self, index):
        self._index = index
        self._rparent = None
        self._lparent = None
        self._child = None

    def index(self):
        return self._index

    def child(self):
        return self._child

    def rparent(self):
        return self._rparent

    def lparent(self):
        return self._lparent

    def add_child(self, child_index):
        self._child = child_index

    def add_rparent(self, rparent_index):
        self._rparent = rparent_index

    def add_lparent(self, lparent_index):
        self._lparent = lparent_index
        

# InTree Class.
# Construction is done from the top level to the root node
# which must be set. There is no method for deleting nodes
class InTree:

    def __init__(self):
        self._nodes = {}
        self._root = None
        self._leaves = []

    def size(self):
        return len(self._nodes.keys())

    def get_node(self, index):
        return self._nodes[index]

    # add_node adds a child node to rparent and lparent
    # must be used top-down in the tree
    def add_node(self, index, rparent_index=None, lparent_index = None):
        node = Node(index)
        self._nodes[index] = node

        if rparent_index is not None:
            node.add_rparent(rparent_index)
            self._nodes[rparent_index].add_child(index)
            
        if lparent_index is not None:
            node.add_lparent(lparent_index)
            self._nodes[lparent_index].add_child(index)

        if rparent_index is None and lparent_index is None:
            self._leaves.append(index)

        self._root = index
        return node

    # get_path returns the list of indices in the path from index_i to index_j
    def get_path(self, index_i, index_j):
        node = self._nodes[index_i]
        path_nodes = [index_i]

        while path_nodes[-1] != index_j:
            child = node.child()
            if child is None:
                return []
            node = self._nodes[child]
            path_nodes.append(node.index())
        return path_nodes
                

    # get_ordered_pairs returns a list of node ancestor pairs such that for a 
    # parent i and child j all pairs of the form [i, k] are listed before
    # pairs of the form [j, k] for all k
    def get_ordered_pairs(self):
        pairs = []
        curr_level = self._leaves

        while len(curr_level)>0:
            next_level = set()
            for i in curr_level:
                for j in self.get_path(i, self._root)[1:]:
                    pairs.append([i,j])
                    
                child = self._nodes[i].child()
                if child != self._root and child != None:
                    next_level.add(child)     
            curr_level = next_level

        return pairs
            
        

# Example for initialzing an InTree
#    tree = InTree()
#    tree.add_node(1)
#    tree.add_node(2)
#    tree.add_node(3,1,2)
#    tree.add_node(4, 3)
#    Pairs = tree.get_ordered_pairs()

    
