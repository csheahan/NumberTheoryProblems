'''
Problem:
  List the moves in the tower of Hanoi puzzle
'''

def problem():
  answer = []

  for i in xrange(1, 4):
    for j in xrange(1, 4):
      if (i != j):
        answer.append(str(i) + " -> " + str(j))

  return answer
