This is meant as a simple tool to calculate the needed amount of increases.
It seems to work so far, but in some cases it might not behave quite correct.

### Case 1:
You have knitted a triangle shape with 45° angles and want to attach to one of the 45° angle sides.
```
        /\
       /||\
    a /||||\ b
     /|||h||\
 45 ---------- 45
         C
```
```

    |\
    ||\
  h |||\ b
    ||||\
90  ------ 45
    C
```

If you remember trigonometry, the long side is _C_, the other 2 sides are _a_ and _b_.
Or you have half a triangle with one 90° angle and one 45° angle. 

So let's say you want to knit into _b_ by picking up stitches, resulting in rows that are parallel to _b_.
To maintain the same height of the triangle (_h_) you need to increase the stitch count along _b_.

```
    |\/ / / /           |
    ||\/ / /            |
  h |||\b / /   --> ... h
    ||||\/ /            |
    ------
    C
```
In a triangle with a 45° angle you have to increase by dividing the edge stitches of _b_ by the sinus of 45°, which is about 0.707.
That will give you the amount of needed stitches.
The script will also try to calculate the pattern for how to increase.


### Case 2:
You used a different decrease pattern, so the angle between _C_ and _b_ is not 45°.
Start the script with the argument `-a` and give it the angle:
 
`python3 knittomat.py -a 23`

### Case 3:
You just want to know how to increase evenly from stitchcount A to stitchcount B.
In that case you don't care about any angle or sinus.
Start the script with argument `-n` for "no sinus":
 
`python3 knittomat.py -n`
