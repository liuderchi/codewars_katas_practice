'''
function that takes an integer number (index of the Excel column) and returns the string represents the title of this column.

## Intro

In the MS Excel lines are numbered by decimals, columns - by sets of letters.
For example, the first column has the title "A", second column - "B", 26th - "Z", 27th - "AA".
"BA"(53) comes after "AZ"(52), "AAA" comes after "ZZ".

## Input
It takes only one argument - column decimal index number. Argument num is a natural number.

## Output
Output is the upper-case string represents the title of column. It contains the English letters: A..Z

## Errors
For cases num < 1 your function should throw/raise IndexError. In case of non-integer argument you should throw/raise TypeError.
In Java, you should throw Exceptions.
Nothing should be returned in Haskell.

# Examples

>>> get_column_title(52)
"AZ"
>>> get_column_title(1337)
"AYK"
>>> get_column_title(432778)
"XPEH"
>>> get_column_title()
TypeError:
>>> get_column_title("123")
TypeError:
>>> get_column_title(0)
IndexError:
'''

def get_column_title(num):
    if not isinstance(num, (int, long)):  TypeError('column number must be an integer')
    if num < 1 : raise ValueError('column number must be >= 1')
    title = ''
    while num:
        num, charIndex = divmod(num-1, 26)   # num - 1 since A is zero
        # charIndex = (num-1)%26    # NOTE lowest char correspond to mod
        # num = (num-charIndex)/26  # NOTE e.g. 52->AZ toggle 25 times leads A to Z
        title += chr(ord('A') + charIndex)  # get char from small to large
    return title[::-1]

assert get_column_title(1) == "A"
assert get_column_title(27) == "AA"
assert get_column_title(53) == "BA"

assert get_column_title(26) == "Z"
assert get_column_title(52) == "AZ"
assert get_column_title(702) == "ZZ"


def get_column_title_slow(num):
    if num < 1 :
        raise IndexError
    if not isinstance(num, int):
        raise TypeError

    res = [0]
    count = 0
    while count < num:        # NOTE Time complexity is n
        res[0] += 1
        carry, i = 0, 0

        while i < len(res):
            res[i] += carry
            carry = 0
            if res[i] > 26:
                carry = 1
                res[i] = 1
                if i == len(res) -1:
                    res.append(1)
                    break
            i += 1

        count += 1
    return ''.join(chr(64 + x) for x in res[::-1])

assert get_column_title_slow(26) == "Z"
assert get_column_title_slow(27) == "AA"
assert get_column_title_slow(52) == "AZ"
assert get_column_title_slow(53) == "BA"
assert get_column_title_slow(702) == "ZZ"


def get_column_title_complex(num):
    res = []

    if num < 1 :
        raise IndexError
    if not isinstance(num, int):
        raise TypeError

    _, mod = divmod(num, 26)

    if mod == 0:
        num, mod = divmod(num, 26)
        res.append(mod)
        while num >= 27:
            num, mod = divmod(num, 27)
            res.append(mod)
        res.append(num)

        # NOTE nagative carry back
        carry = -1
        for i, _ in enumerate(res):
            res[i] += carry
            if res[i] < 0:
                res[i] = 26
            else:
                carry = 0

        # NOTE remove leading zeros
        while True:
            if res[-1] == 0:
                res.pop()
            else:
                break

    else:
        num, mod = divmod(num, 26)
        res.append(mod)
        while num >= 26:
            num, mod = divmod(num, 26)
            res.append(mod)
        if num > 0:
            res.append(num)

    return ''.join(chr(64 + x) for x in res[::-1])

#
assert get_column_title_complex(1) == "A"
assert get_column_title_complex(27) == "AA"
assert get_column_title_complex(53) == "BA"

# has factor 26
assert get_column_title_complex(26) == "Z"
assert get_column_title_complex(52) == "AZ"
assert get_column_title_complex(702) == "ZZ"
