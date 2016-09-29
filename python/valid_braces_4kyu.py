'''
Write a function called validBraces that takes a string of braces,
and determines if the order of the braces is valid. validBraces should
return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces
four new characters. Open and closed brackets, and open and closed curly braces.
Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of
open parentheses '(' , closed parentheses ')',
open brackets '[', closed brackets ']',
open curly braces '{' and closed curly braces '}'.

What is considered Valid? A string of braces is considered valid if all braces
are matched with the correct brace.

For example:
'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.
'''

def validBraces(string):
    iparens = iter('(){}[]<>')
    parens = dict(zip(iparens, iparens))   # NOTE a k-v pair with braces
    closing = parens.values()
    stack = []
    for c in string:
        paren = parens.get(c, None)
        if paren:
            stack.append(paren)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack


# NOTE alternative, replace until result is not changed
# def validBraces(s, previous = ''):
    # while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
    # return not s


assert validBraces( "()" ) is True
assert validBraces( "(){}[]" ) is True
assert validBraces( "(}" ) is False
assert validBraces( "[(])" ) is False
assert validBraces( "([{}])" ) is True
