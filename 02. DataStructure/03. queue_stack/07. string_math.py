#goal: given a simple string type math function (like '((1+2)/(3+4))'), calculate it.

#code:
import operator 
def string_math(str):
  operands = []
  operators = []
  ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
  for term in str:
    if term == '(': #it means start a calculation
      continue
    elif term == ')':
      right, left = operands.pop(), operands.pop()
      operands.append(ops[operators.pop()](left,right))
    elif term in ops:
      operators.append(term)
    else:
      operands.append(int(term))
  return operands[0]
      
