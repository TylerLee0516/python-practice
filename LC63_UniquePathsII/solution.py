class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if self.isOnlyOneDirection(obstacleGrid):
            if self.isObstacle(obstacleGrid):
                return 0
            else:
                return 1
        else:
            result = 0
            rightGrid = self.getInnerGrid(obstacleGrid, 'right')
            downGrid = self.getInnerGrid(obstacleGrid, 'down')
            result += self.uniquePathsWithObstacles(rightGrid)
            result += self.uniquePathsWithObstacles(downGrid)
            return result

    def isOnlyOneDirection(self, grid):
        if len(grid) == 1:
            return True
        if len(grid[0]) == 1:
            return True
        return False

    def isObstacle(self, grid):
        for l in grid:
            for num in l:
                if num == 1:
                    return True
        return False

    def getInnerGrid(self, grid, direction):
        if direction == 'right':
            if grid[0][1] == 1:
                return []
            else:
                innerGrid = []
                for l in grid:
                    del l[0]
                    innerGrid.append(l)
                return innerGrid
        else:
            if grid[1][0] == 1:
                return []
            else:
                innerGrid = grid
                del innerGrid[0]
                return innerGrid
