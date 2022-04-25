def levelOrder(self,root ):
        bfs = []
        current_level = []
        if root is None:
            return bfs
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            level_size = len(queue)
           # current_level = []
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current.data)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            bfs.append(current_level)
        return current_level
