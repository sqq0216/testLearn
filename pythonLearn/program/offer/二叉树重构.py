# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回构造的TreeNode根节点
#     def reConstructBinaryTree(self, pre, tin):
#         # write code here
#         if len(pre) == 0:
#             return None
#         if len(pre) == 1:
#             return TreeNode(pre[0])
#         else:
#             flag = TreeNode(pre[0])
#             flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
#             flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
#         return flag
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 返回构造的TreeNode根节点
def reConstructBinaryTree(pre, tin):
    # write code here
    if not pre:
        return None
    root_val = pre[0]
    root = TreeNode(root_val)
    for i in range(len(tin)):
        if tin[i] == root_val:
            break
    root.left = reConstructBinaryTree(pre[1:1+i], tin[:i])
    root.right = reConstructBinaryTree(pre[1+i:], tin[i+1:])
    print(root.val)
    return root

def preorder(root):
    if root:
        preorder(root.left)
        print(root.val)
        preorder(root.right)
preorder(reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7]))