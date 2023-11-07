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
Your used a different decrease pattern, so the angle between C and b is not 45°.
Start the script with the argument -a and give it the angle.
(example: python3 knittomat.py -a 23)

Case 3:
You just want to know how to increase evenly from stitchcount A to stitchcount B.
In that case you don't care about any angle or sinus.
Start the script with argument -n for "no sinus"
(example: python3 knittomat.py -n)
"""

import sys
import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--angle", type=float, help="Which angle does the edge you are knitting into have?")
parser.add_argument("-n",
                    "--no_sinus",
                    action="store_true",
                    help="Flag: Do you not want to enter the target stitchcount yourself? Default: %(default)s")

args = parser.parse_args()

# args
no_sinus = args.no_sinus
angle = args.angle

# let's assume you knit a typical triangular shape,
# where you decrease every second row.
# this will result in a 45° angle of the decrease edge.
if not angle:
    edgeangle = 45
# if you have a different decrease pattern you'll have a different angle, which you can pass as argument
else:
    edgeangle = angle

# now, if you pick up stitches along this diagonal edge and continue knitting parallel to that edge,
# you must increase the stitches in order to maintain the overall height.
# to do that, you have to divide the edge stitches by the sinus of that angle.
sinus = math.sin(math.radians(edgeangle))

# so first we should know how many edge stitches there are
# (with a triangle shape and 45 degree angle it would be half the stitches of the triangle bottom row)
current_stitches = int(input(" Amount of bound off edge stitches: "))

# now we can calculate the target amount of stitches
target_stitches = round(current_stitches / sinus)
# give it a custom phrase for the string output
target_stitches_phrase = " to maintain the same overall height."

# in case you don't use the triangle angle at all
if no_sinus:
    target_stitches = int(input(" Amount of new stitches: "))
    target_stitches_phrase = "."

# now we can calculate the amount of increases
increases = target_stitches - current_stitches

# the gaps are the available gaps between existing stitches (--> minus the last stitch)
# in these gaps you can work the increases
gaps = current_stitches - 1

# the somewhat tricky thing is to find out how to distribute the increase stitches evenly
distribution = int(gaps / increases)

# if you can distribute them in such a way that there is no rest it's easy
# otherwise you need to distribute the "uneven" rest of stitches across the increases
rest = gaps % increases

# and now we can print all that shit!

print("\n")
print(f' c = {current_stitches}: Current amount of stitches.')
print(f' t = {target_stitches}: Target amount of stitches.')
print(f' i = {increases}: Amount of increase stitches.')
print(f' g = {gaps}: Available gaps between your existing stitches where you can work your increases.\n')

if increases >= gaps:
    print(
        "you have more increases than available gaps. this is what the script doesn't handle yet. figure it out yourself!:)\n"
    )
    sys.exit()
if distribution == 1:
    phrase = ""
else:
    phrase = f'{distribution}. '

print(" -->\n")

if rest <= 1:
    # phrase it differently if distribution is 1
    print(f' d = {distribution}: Make a new stitch after each {phrase}existing stitch.\n')
else:
    # this is a more complicated case
    print(f' In theory you could make an increase after every {phrase}stitch.')
    print(f' However, you would end up with {rest} stitches too much.')
    # we need to also distribute the rest evenly
    rest_distribution = round(increases / rest) + 1
    print(f' So, follow the pattern of an increase after each {phrase}stitch,')
    print(f' but work one regular stitch more after each {rest_distribution}. increase.\n')
