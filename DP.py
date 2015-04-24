import intree
import numpy as np

# Assume nodes indexed 0,..,n-1


def preprocess(tree, rev, f, cust_classes):
    n = tree.size()
    Rev = np.zeros(shape=(n))
    Rev_Sub = np.zeros(shape=(n,n))
    Pen = np.zeros(shape=(n))
    Pen_Sub = np.zeros(shape=(n,n))
    
    
    for g in cust_classes:
        path = tree.get_path(g[0],g[1])
        prob = g[2]
        
        m = len(path)
        for x in range(m):
            i = path[x]
            Rev[i] += prob*rev[i]
            Pen[i] += prob*f[x]
            
            for y in range(x,m):
                j = path[y]
                Rev_Sub[i][j] += prob*rev[j]
                Pen_Sub[i][j] += prob*f[y]

    return Rev, Rev_Sub, Pen, Pen_Sub

def generate_subset(i, j, Picked):
    node = tree.get_node(i)
    rparent, lparent = node.rparent(), node.lparent()

    subset = []
    picked = Picked[i,j]
    if picked:
        subset.append(i)
    if (rparent is not None):
        if picked:
            subset.extend(generate_subset(rparent, i, Picked))
        else:
            subset.extend(generate_subset(rparent, j, Picked))
    if (lparent is not None):
        if picked:
            subset.extend(generate_subset(lparent, i, Picked))
        else:
            subset.extend(generate_subset(lparent, j, Picked))
            
    return subset


def DP(tree, rev, cost, f, cust_classes):
    n = tree.size()
    Values = np.zeros(shape = (n,n))
    Picked = np.zeros(shape = (n,n))

    Rev, Rev_Sub, Pen, Pen_Sub = preprocess(tree, rev, f, cust_classes)
    ordered_pairs = tree.get_ordered_pairs()

    for [i,j] in ordered_pairs:
        node = tree.get_node(i)
        rparent, lparent = node.rparent(), node.lparent()

        not_choose = 0
        choose = Rev[i]-Rev_Sub[i][j]-cost[i]-Pen[i]+Pen_Sub[i][j]
        if rparent is not None:
            not_choose += Values[rparent][j] 
            choose += Values[rparent][i] 
        if lparent is not None:
            not_choose += Values[lparent][j]
            choose += Values[lparent][i]

        Values[i][j] = max(not_choose, choose)
        Picked[i][j] = (choose > not_choose)
    Picked[n-1][n-1] = 1

    return generate_subset(n-1,n-1,Picked)


if __name__ == "__main__":
    tree = intree.InTree()
    tree.add_node(0)
    tree.add_node(1,0)
    tree.add_node(2)
    tree.add_node(3,2,1)
    tree.add_node(4,3)

    rev = [1, 0.5, 3, 2, 1]
    costs = [0, 0, 0, 0, 0]
    f = [0, 0, 0, 0]
    cust_classes = [[0,4,0.5],[2,4,0.5]]

    print DP(tree, rev, costs, f, cust_classes)
        
    
                
        
    
