a,b,d = map(int,input().split())

import math

a_dash = math.cos(math.radians(d)) * a - math.sin(math.radians(d)) * b
b_dash = math.sin(math.radians(d)) * a + math.cos(math.radians(d)) * b


print(a_dash,b_dash)
