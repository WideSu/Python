#goal:Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

#example: pushed = [1,2,3,4,5], popped =[4,5,3,2,1] -> true (push 1,2,3,4 then pop 4, then push 5, and pop all)

#code:
def stack_sequence_check(pushed,popped):
  s, next_consumed = [], 0
  for item in popped:
    while (not s or s[-1] != item) and next_consumed < len(pushed):
      s.append(pushed[next_consumed])
      next_consumed += 1
    if s[-1] != item:
      break
    s.pop()
return not s
