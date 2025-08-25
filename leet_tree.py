from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        # If we're at a leaf node, check if the path sum equals targetSum
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursively check left and right subtrees with updated targetSum
        remaining_sum = targetSum - root.val
        return (
            self.hasPathSum(root.left, remaining_sum) or
            self.hasPathSum(root.right, remaining_sum)
        )

    def dfs_listPath(self, root):
        
        def backtrack(current, path_sofar, result):

            #print("current:", current)
            #print("path_sofar:", path_sofar)
            #print("result:", result)
    
            new_path = path_sofar + [current.val]

            if current.left is None and current.right is None:
                result.append(new_path)
                return
            if current.left is not None:
                backtrack(current.left, new_path, result)
            if current.right is not None:
                backtrack(current.right, new_path, result)

        result = []
        backtrack(root, [], result)
        return result            

    

    def bfs_listPath(self, root):
        result = []
        queue = deque()
        queue.append((root, []))         

        while queue:
            current, path_sofar = queue.popleft()
            new_path = path_sofar + [current.val]

            if current.left is None and current.right is None:
                result.append(new_path)
                continue
            if current.left is not None:
                queue.append((current.left, new_path))
            if current.right is not None:
                queue.append((current.right, new_path))

        
        return result




    def dfs_inorderTraversal(self, root):
        if not root:
            return []
        return self.dfs_inorderTraversal(root.left) + [root.val] + self.dfs_inorderTraversal(root.right)


    def dfsiter_inorderTraversal(self, root):

        result = []
        stack = []
        current = root

        while current or stack:

            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result






def build_tree(level_order):
    if not level_order or level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        node = queue.popleft()

        # Left child
        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root





# Example test
if __name__ == "__main__":
    # Create the following tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \
    # 7    2

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    target = 22

    sol = Solution()
    result = sol.hasPathSum(root, target)
    print("Has path sum:", result)  # Should print: Has path sum: True



    tree_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    target = 21

    root = build_tree(tree_list)
    sol = Solution()
    print("Has path sum:", sol.hasPathSum(root, target))


    output_list = sol.bfs_listPath(root)
    print("bfs:", output_list)


    output_list = sol.dfs_listPath(root)
    print("dfs:", output_list)


    output_list = sol.dfs_inorderTraversal(root)
    print("dfs_inorderTraversal:", output_list)

    output_list = sol.dfsiter_inorderTraversal(root)
    print("dfsinter_inorderTraversal:", output_list)


