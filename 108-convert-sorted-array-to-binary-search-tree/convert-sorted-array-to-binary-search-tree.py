# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root = None
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        def insert(root,val):
            if not root:
                new = TreeNode(val)
                return new
            
            if root.val > val:
                root.left = insert(root.left,val)
            if root.val <val:
                root.right = insert(root.right,val)
            

            return root
        
        def solve(arr,start,end):
            if start >= end:
                return 
            
            mid = (start + end )//2
            self.root = insert(self.root,arr[mid])
            solve(arr,start, mid)
            solve(arr,mid + 1 , end)
        solve(nums,0,len(nums))
        
        return self.root
        