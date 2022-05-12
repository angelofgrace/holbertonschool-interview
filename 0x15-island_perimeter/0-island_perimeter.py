#!/usr/bin/python3
"""
Island Perimeter Algorithm Problem
Recursive Solution
"""

def count_sides(grid, i, j, perimeter):
  """ Defining count_sides, it counts sides"""
  grid[i][j] = 2
  if (i == 0 or grid[i-1][j] == 0):
    perimeter+=1
  if (i == len(grid)-1 or grid[i+1][j] == 0):
    perimeter+=1
  if (j == 0 or grid[i][j-1] == 0):
    perimeter+=1
  if (j == len(grid[0])-1 or grid[i][j+1] == 0):
    perimeter+=1

  if (i > 0 and grid[i-1][j] == 1):
    count_sides(grid, i-1, j, perimeter)
  if (i < len(grid)-1 and grid[i+1][j] == 1):
    count_sides(grid, i+1, j, perimeter)
  if (j > 0 and grid[i][j-1] == 1):
    count_sides(grid, i, j-1, perimeter)
  if (j < len(grid[0])-1 and grid[i][j+1] == 1):
    count_sides(grid, i, j+1, perimeter)
    
def island_perimeter(grid):
  """ Defining island_perimeter, it finds the perimeter of the island """
  perimeter = 0
  height = len(grid)
  width = len(grid[0])
  
  for (i = 0; i < height; i+=1):
    for (j = 0; j < width; j+=1):
      if (grid[i][j] == 1):
        count_sides(grid, i, j, perimeter)
  return perimeter
