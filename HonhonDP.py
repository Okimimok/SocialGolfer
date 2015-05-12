import intree
from DP import *

#Function that computes \Delta^- from Honhon supplemental section
#S:Assortment
#j:prod you are considering adding
#All of the other variables are the same as the descriptions in DP.py
def DeltaMinus(tree, rev, S, j, f, costs, cust_classes):


    Delta=-costs[j]
    for g in cust_classes:

        #Since all predecessors are offered only cusotmers who start with j buy j
        if g[0]==j:
            
            path = tree.get_path(g[0],g[1])
            pathLength=len(path)
            
            #Find closest successor
            foundSuc=0
            for i in path[1:]:
                if i in S and foundSuc==0:
                    foundSuc=1
                    closestSuc=i
                    countLevel=path.index(closestSuc)

            #Two cases given in supplement of Honhon
            if foundSuc==0:
                Delta+=g[2]*(rev[j]-f[0])
            else:
                Delta+=g[2]*(rev[j]-rev[closestSuc] + (f[countLevel]-f[0])) 

    return Delta

#Function that computes \Delta^+ from Honhon supplemental section
def DeltaPlus(tree, rev, S, j, f, costs, cust_classes):

    Delta=-costs[j]
    for g in cust_classes:

        
        path = tree.get_path(g[0],g[1])
        
        #Check to see if j will be purchased
        if j in path:
            levelJ=path.index(j)
            purchaseFlag=0
            for i in path[:levelJ]:
                if i in S:
                    purchaseFlag=1

            #If j is purchased find closest successor
            if purchaseFlag==0:
                
                pathLength=len(path)
        
                foundSuc=0
                for i in path[1:]:
                    if i in S and foundSuc==0:
                        foundSuc=1
                        closestSuc=i
                        countLevel=path.index(closestSuc)


                #Two cases in Honhon supplement
                if foundSuc==0:
                    Delta+=g[2]*(rev[j]-f[levelJ])
                else:
                    Delta+=g[2]*(rev[j]-rev[closestSuc] + (f[countLevel]-f[levelJ])) 

    return Delta

#Finds the product that customer will buy given assortment S
#customer: nonparamtric customer class
#S: Assortment
def prodPurchases(customer, S):

    sub=0

    for prod in customer:

        if prod in S:

            return prod,sub

        sub+=1

    

    return -1,sub

#Calculates the revenue from assortment S
def NPrev(tree, cust_classes,rev,costs, f,S):
    
    revTotal=0
    for j in S:
        revTotal-=costs[j]
    
    for g in cust_classes:
        path = tree.get_path(g[0],g[1])
        
        purchase,sub=prodPurchases(path,S)

        if purchase!=-1:
            revTotal+=g[2]*(rev[purchase]-f[sub])


        
    return revTotal



#Run Honhon Algorithm 3
def Alg3(tree, rev, costs, f, cust_classes):

    n = tree.size()

    
    #Initialization of algorithm  
    NDict={n:0}
    SDict={0:[]}

    #Get optimal assortment with no fixed costs
    SOpt= DP(tree, rev, [0]*n, f, cust_classes)[0]

    
    

    for j in range(n-1,-1,-1):
      
        NDict[j]=NDict[j+1]

        if j in SOpt:
           
            #Calculate Delta+ and Delta-
            for i in range(0,NDict[j+1]+1):

                if DeltaMinus(tree, rev, SDict[i], j, f, costs, cust_classes)>0:
                    SDict[i]+=[j]
                elif DeltaPlus(tree, rev, SDict[i], j, f, costs, cust_classes)>0:
                    NDict[j]+=1
                    SDict[NDict[j]]=[j]+SDict[i]


    #Find the best assortment from the candidate assortments
    bestRev=-1000000
    for j in SDict.keys():
        S=SDict[j]
        currentRev=NPrev(tree, cust_classes,rev,costs, f,S)
        if currentRev>bestRev:
            bestRev=currentRev
            bestAssort=S



    return bestAssort,bestRev




# An example problem
if __name__ == "__main__":
    tree = intree.InTree()
    tree.add_node(0)
    tree.add_node(1,0)
    tree.add_node(2)
    tree.add_node(3,2,1)
    tree.add_node(4,3)

    rev = [1, 0.5, 3, 2, 1]
    costs = [0, 0, 0, 0, 0]
    f = [0, 0, 0, 0,0]
    cust_classes = [[0,4,0.5],[2,4,0.5]]


    print Alg3(tree, rev, costs, f, cust_classes)
    
