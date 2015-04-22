# SocialGolfer

For this project we will code up two algorithms to a solve a costed assortment optimization problems under a ranking based choice model.  In this choice model, a customer type is characterized by a ranking of the products and an arrival probability. Customers purchase the first offered product in their rankings.  The general assortment problem is NP Hard and as hard to approximate as independent set.  To make the problem tractable, we restrict the set of possible customer types.  

Take a binary intree and assume the nodes are products. A customer type now can be any path on this tree.  We have a DP approach to solve the problem optimally in O(n^2logn), where n is the number of products in the tree.  Honhon et al considered the problem before us and gave an O(2^n) algorithm which seems to perform well in practice. The goal is to test our DP approach versus the Honhon algorithm and find instances where we beat her algorithm substantially.  
