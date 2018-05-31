# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    node_stack = []
    cur_node = None
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.build(root)

    def build(self, root):
        temp = root
        while temp and temp.left:
            self.node_stack.append(temp)
            temp = temp.left
        self.cur_node = temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_node


    def next(self):
        """
        :rtype: int
        """
        return_object = self.cur_node
        if self.cur_node.right:
            self.build(self.cur_node.right)
        elif len(self.node_stack)>0:
            self.cur_node = self.node_stack.pop()
        else:
            self.cur_node = None
        return return_object

        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())