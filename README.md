This is meant as a simple tool to calculate the needed amount of increases.
It seems to work so far, but in some cases it might not behave quite correct.

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
