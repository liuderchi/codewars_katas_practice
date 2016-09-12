'''
You're fed up about changing the version of your software manually.
Instead, you will create a little script that will make it for you.

Exercice

Create a function nextVersion, that will take a string in parameter, and will return a string containing the next version number.

For example:

nextVersion("1.2.3") === "1.2.4";
nextVersion("0.9.9") === "1.0.0.";
nextVersion("1") === "2";
nextVersion("1.2.3.4.5.6.7.8") === "1.2.3.4.5.6.7.9";
nextVersion("9.9") === "10.0";

Rules

All numbers, except the first one, must not be greater than 10:
    if there are, you have to set them to 0 and increment the next number in sequence.

You can assume all tests inputs to be valid.
'''

def nextVersion(version):

    digits = map(lambda c: int(c), version.split('.'))
    carry, index = 1, len(digits) - 1   # start from rightest element

    while carry == 1:

        digits[index] += 1

        # determine carry vlaue
        if digits[index] >= 10 and index > 0:
            carry = 1
            digits[index] -= 10
        else:
            carry = 0

        index -= 1  # move left

    return '.'.join(map(lambda i: str(i), digits))


assert nextVersion("1.2.3") == "1.2.4"
assert nextVersion("0.9.9") == "1.0.0"
assert nextVersion("1") == "2"
assert nextVersion("1.2.3.4.5.6.7.8") == "1.2.3.4.5.6.7.9"
assert nextVersion("9.9") == "10.0"
