# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # 1. dfs to visit all root-to-leaf nodes
        # 2. hash table(freq) stores frequency of all digits
        # 3. an int var(odds) that stores number of digits having odd frequency for a given root-to-leaf path
        # 4. a path is palindromic if at most one digit in the path has odd frequency

        if root is None:
            return 0

        def dfs (node, odds):
            if node is None:
                return 0
            freq[node.val] += 1
            # increment odds if freq. of digit is odd
            # else decrement odds
            odds = (odds - 1) if freq[node.val] % 2 == 0 else (odds + 1) 
            if node.left is None and node.right is None:
                # remove node as it has no children
                freq[node.val] -= 1
                return 0 if odds > 1 else 1
            # res is sum of no. of psuedo-palindromic paths
            # in left and right sub tree
            res = dfs(node.left, odds) + dfs(node.right, odds)
            # remove node as we've visited both of it's children
            freq[node.val] -= 1
            return res
        
        freq = defaultdict(int)
        return dfs(root, 0)
