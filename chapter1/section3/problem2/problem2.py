'''
Problem:
  Cover a 2^n x 2^n chessboard that is missing one square using L-shaped
  pieces.

Constraints:
  n - must be a positive integer
'''

Curr_Num = 1

def solve(n):
  if (n <= 0):
    raise ValueError("n must be a positive integer")

  global Curr_Num
  Curr_Num = 1

  bound = 2**n

  # Initialize List
  answer = [[' ' for x in xrange(bound)] for x in xrange(bound)]

  return _solve(answer, 0, bound, 0, bound)

def _solve(grid, lowx, highx, lowy, highy):
  global Curr_Num

  # Base Case: 2x2 square
  if (highx - lowx == 2 and highy - lowy == 2):
    # Determine if we are in a case where we are filling out a 2x2 square or
    # have a 2x2 square that has the missing spot via a 2 pass approach
    count = 0
    for x in xrange(lowx, highx):
      for y in xrange(lowy, highy):
        if (grid[x][y] != ' '):
          count += 1

    # If count is 0, then we are in the 2x2 with the missing spot
    # Else we fill each spot with curr num
    if (count == 0):
      grid[lowx][lowy] = str(Curr_Num)
      grid[lowx + 1][lowy] = str(Curr_Num)
      grid[lowx][lowy + 1] = str(Curr_Num)
      grid[lowx + 1][lowy + 1] = 'x'
    else:
      for x in xrange(lowx, highx):
        for y in xrange(lowy, highy):
          if (grid[x][y] == ' '):
            grid[x][y] = str(Curr_Num)

    Curr_Num += 1
  else:
    # Use a divide and conquor approach: mark the middle, split into 4 2^n-1
    # squares recursively

    # First, mark the center
    centerX = ((lowx + highx) / 2) - 1
    centerY = ((lowy + highy) / 2) - 1

    # To determine the pattern to use, check the 4 corners and act
    # appropriately
    if (grid[lowx][lowy] != ' '):
      # Mark away from top left
      grid[centerX][centerY + 1] = str(Curr_Num)
      grid[centerX + 1][centerY] = str(Curr_Num)
      grid[centerX + 1][centerY + 1] = str(Curr_Num)
    elif (grid[highx - 1][lowy] != ' '):
      # Mark away from top right
      grid[centerX][centerY] = str(Curr_Num)
      grid[centerX][centerY + 1] = str(Curr_Num)
      grid[centerX + 1][centerY + 1] = str(Curr_Num)
    elif (grid[lowx][highy - 1] != ' '):
      # Mark away from bottom left
      grid[centerX][centerY] = str(Curr_Num)
      grid[centerX + 1][centerY] = str(Curr_Num)
      grid[centerX + 1][centerY + 1] = str(Curr_Num)
    else:
      # Mark away from bottom right
      # Or the default if none are marked
      grid[centerX][centerY] = str(Curr_Num)
      grid[centerX + 1][centerY] = str(Curr_Num)
      grid[centerX][centerY + 1] = str(Curr_Num)

    Curr_Num += 1

    # Divide
    _solve(grid, lowx, centerX + 1, lowy, centerY + 1)
    _solve(grid, centerX + 1, highx, lowy, centerY + 1)
    _solve(grid, lowx, centerX + 1, centerY + 1, highy)
    _solve(grid, centerX + 1, highx, centerY + 1, highy)

  return grid
