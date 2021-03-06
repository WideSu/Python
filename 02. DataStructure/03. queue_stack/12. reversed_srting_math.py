#goal:Evaluate the value of an arithmetic expression in Reverse Polish Notation.

#example:["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9

#code:
def reversed_string_math(str):
  import operator
  ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
  operands = []
  for elem in str:
    if elem in '+-*/':
      right, left = operands.pop(), operands.pop()
      operands.append(int(ops[elem](left,right)))
    else:
      operands.append(int(elem))
  return operands[0]

#complexity:
#time: O(n)
#space: O(n)
