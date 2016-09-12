'''
Write a function called validParentheses that takes a string of parentheses,
and determines if the order of the parentheses is valid.
validParentheses should return true if the string is valid, and false if it's invalid.

Examples:
validParentheses( "()" ) => returns true
validParentheses( ")(()))" ) => returns false
validParentheses( "(" ) => returns false
validParentheses( "(())((()())())" ) => returns true

All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'
'''

def valid_parentheses(string):
    cnt = 0
    for c in string:
        if c == ')': cnt -= 1
        elif c == '(': cnt += 1
        if cnt < 0: return False

    return cnt == 0

    # NOTE general praenthesis checker
    # iparens = iter('(){}[]<>')
    # parens = dict(zip(iparens, iparens))
    # closing = parens.values()
    # stack = []
    # for c in string:
    #     paren = parens.get(c, None)
    #     if paren:
    #         stack.append(paren)
    #     elif c in closing:
    #         if not stack or c != stack.pop():
    #             return False
    # return not stack


assert valid_parentheses("  (") == False
assert valid_parentheses(")test") == False
assert valid_parentheses("") == True
assert valid_parentheses("hi())(") == False
assert valid_parentheses("hi(hi)()") == True
