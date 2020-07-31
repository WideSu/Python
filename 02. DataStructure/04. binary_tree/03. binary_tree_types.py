'''
there are few binary tree types we care about:
  1. balanced binary tree: 
    the difference between depth of every left and right node is 1 or less.
  ok:      10                    not ok:        10
          /  \                                 /  \
         5    15                              5   15
        / \   /                              / \  /
       2  7  12                             2  7  12
                                                 /
                                                13
  
  2.complete binary tree:
    every level except the last is completely filledand all nodes are as far left as possible.
  ok:      10                    not ok:        10
          /  \                                 /  \
         5    15                              5   15
        / \   /                              / \    \
       2  7  20                             2  7    20

  3.binary search tree:
    for each node, its left node must be smaller than it, while the right node must be larger than it.
  ok:      10                    not ok:        10
          /  \                                 /  \
         5    15                              5   15
        / \   / \                            / \  / \
       2  7  12  20                         2  7 12  13
'''
