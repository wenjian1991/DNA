from math import pi, sin, cos

width, height = 30, 100
w, a = 8, 8
for i in range(height):
    ang = pi/12*i
    s0 = int(a*sin(ang))
    s0 = ' '*int(width/2+s0) + '0'*w + ''*int(width/2-s0-w)
    s1 = int(a*cos(ang))
    s1 = ' '*int(width/2+s1) + '1'*w + ''*int(width/2-s1-w)

    what = None
    if sin(ang) > 0:
        what = lambda x, y:x if x!=' ' else y
    else:
        what = lambda x, y:y if y!=' ' else x

    s = [what(x,y) for x, y in zip(s0, s1)]
    print(''.join(s))

