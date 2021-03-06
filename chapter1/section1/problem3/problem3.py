'''
Probelem:
  Find the first n Ulam numbers

Constraints:
  n - must be a positive integer
'''

Ulam_List = [1, 2, 3, 4, 6, 8, 11, 13, 16]

def solve(n):
  global Ulam_List

  if (n <= 0):
    raise ValueError("n must be a positive integer")
  elif (n == 1):
    return [1]
  elif (n == 2):
    return [1, 2]
  else:
    if (len(Ulam_List) >= n):
      return Ulam_List[0:n]
    else:
      ulam_candidate = Ulam_List[-1] + 1

      while (len(Ulam_List) < n):

        if (isUlamNum(ulam_candidate)):
          Ulam_List.append(ulam_candidate)
          ulam_candidate += 1
        else:
          ulam_candidate += 1

      return Ulam_List

def isUlamNum(num):
  low = 0
  high = len(Ulam_List) - 1
  matches = 0

  while (low < high):
    if (Ulam_List[low] + Ulam_List[high] < num):
      low += 1
    elif (Ulam_List[low] + Ulam_List[high] > num):
      high -= 1
    else:
      low += 1
      high -= 1

      if (matches >= 1):
        return False
      else:
        matches += 1

  if (matches == 1):
    return True


  return False
