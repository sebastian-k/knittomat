"""
This is meant as a simple tool to calculate the needed amount of increases.

Case 1:
You have knitted a triangle shape with 45° angles and want to attach to one of the 45° angle sides.
        /\
       /||\
    a /||||\ b
     /|||h||\
 45 ---------- 45
         C

    |\
    ||\
  h |||\ b
    ||||\
90  ------ 45
    C

If you remember trigonometry, the long side is C, the other 2 sides are a and b.
Or you have half a triangle with one 90° angle and one 45° angle. 
So let's say you want to knit into b.
To maintain the same height of the triangle (h) you need to increase the stitch count along b.

    |\/ / / /           |
    ||\/ / /            |
  h |||\b / /   --> ... h
    ||||\/ /            |
    ------
    C

In a triangle with a 45° angle you have to increase by dividing the edge stitches of b by the sinus of 45°, which is about 0.707.
That will give you the amount of needed stitches.
The script with also try to calculate the pattern for how to increase.


Case 2:
Your used a different decrease pattern, so the angle between C and b is different.
Start the script with the argument -a and give it the angle.
(example: python3 knittomat.py -a 23)

Case 3:
You just want to know how to increase evenly from stitchcount A to stitchcount B.
In that case you don't care about any angle or sinus.
Start the script with argument -n for "no sinus"
(example: python3 knittomat.py -n)
"""

import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--angle", type=int, help="Which angle does the edge you are knitting into have?")
parser.add_argument("-n",
                    "--no_sinus",
                    action="store_true",
                    help="Flag: Do you not want to enter the target stitchcount yourself? Default: %(default)s")

args = parser.parse_args()
no_sinus = args.no_sinus
angle = args.angle

# let's assume you knit a typical triangular shape,
# where you decrease every second row.
# this will result in a 45° angle of the decrease edge.
if angle:
    edgeangle = angle
else:
    edgeangle = 45

# now, if you want to knit into this 45° edge by following it
# perpendicular, you must increase the stitches in order to maintain the overall height.
# to do that, you have to divide the edge stitches by the sinus of 45°.
sinus = math.sin(math.radians(edgeangle))

# so first we should know how many edge stitches there are
# (with a triangle shape it will be half the stitches of the triangle bottom row)
old_stitches = int(input("amount of bound off edge stitches: "))

# now we can calculate the target amount of stitches
new_stitches = round(old_stitches / sinus)
new_stitches_phrase = " to maintain the same overall height."
if no_sinus:
    new_stitches = int(input("amount of new stitches: "))
    new_stitches_phrase = "."
increases = new_stitches - old_stitches
print("\n")
print(f'{old_stitches} is the current amount of stitches')
print(
    f'{new_stitches} is the target amount of stitches you need to increase{new_stitches_phrase}')
print(f'{increases} is the amount of increase stitches')

# the gaps are the available gaps between existing stitches (--> minus the last stitch)
# in these gaps you can work the increases
gaps = old_stitches - 1
print(f'there are {gaps} available gaps between your existing stitches.\n')

# the tricky thing is to find out how to distribute them evenly
distribution = int(gaps / increases)

# if you can distribute them in such a way that there is no rest it's easy
# otherwise you need to distribute the "uneven" rest of stitches across the increases
rest = gaps % increases

if distribution == 1:
    phrase = ""
else:
    phrase = f'{distribution}.'
if rest <= 1:
    # phrase it differently if distribution is 1
    print(f'so, make a new stitch after each {phrase} exisiting stitch.\n')
    # quick summary
    print(f'C = {old_stitches}\ng = {gaps}\na = {new_stitches}\ni = {increases}\nd = {distribution}')
else:
    # this is a more complicated case
    print(f'in theory you could make an increase after every {phrase}stitch.')
    print(f'however, that would be {rest} stitches too much.')
    # we need to also distribute the rest evenly
    rest_distribution = round(increases / rest) + 1
    print(f'so, follow the pattern of an increase after each {phrase}stitch,')
    print(f'but skip one extra stitch after each {rest_distribution}. increase\n')
    # quick summary
    print(
        f'C = {old_stitches}\ng = {gaps}\na = {new_stitches}\ni = {increases}\n\nd = {distribution}\ns = {rest_distribution}'
    )
