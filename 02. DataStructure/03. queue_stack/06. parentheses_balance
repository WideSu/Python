#goal: given a list of '(' and ')', check whether the list valid (number match and order of () is right).

#code:
def parentheses_check(input):
  s = []
  for c in input:
    if c == '(':
      s.append(c)
    else:
      if len(s) > 0 and s[-1] == '(':
        s.pop()
      else:
        return False
  return not s

#more general case including (){}[]:
def balance_check(input):
  s = []
  for c in input:
    if c == '(' or c == '{' or c == '[':
      s.append(c)
    elif c == ')':
      if len(s) > 0 and '(' in s:
        s.remove('(')
      else:
        return False
    elif c == ']':
      if len(s) > 0 and '[' in s:
        s.remove('[')
      else:
        return False
    elif c == '}':
      if len(s) > 0 and '{' in s:
        s.remove('{')
      else:
        return False
  return not s
