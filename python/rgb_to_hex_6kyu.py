'''
The rgb() method is incomplete.

Complete the method so that passing in RGB decimal values will
result in a hexadecimal representation being returned.

The valid decimal values for RGB are 0 - 255.
Any (r,g,b) argument values that fall out of that range should
be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

def rgb(r, g, b):
    round256 = lambda x: max(0, min(x, 255))
    return ('{:02X}'*3).format(round256(r), round256(g), round256(b))


assert rgb(0,0,0) == "000000"
assert rgb(1,2,3) == "010203"
assert rgb(255,255,255) == "FFFFFF"
assert rgb(254,253,252) == "FEFDFC"
assert rgb(-20,275,125) == "00FF7D"
