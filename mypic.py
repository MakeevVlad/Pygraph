from graph import *
import numpy as np
import random as rm

c = canvas()

# def ellipsis(a, b, x0, y0):
#     p = ([])
#     for x in np.arange(-np.sqrt(a) + x0, np.sqrt(a) + x0, 1):
#         p.append([x, np.sqrt(b*(1-(x-x0)**2/a))+y0])
#     for x in np.arange(np.sqrt(a) + x0, -np.sqrt(a) + x0, -1):
#         p.append([x, -np.sqrt(b*(1-(x-x0)**2/a))+y0])
#     return polygon(p)

pol = []
global p
for i in range(5):
    pol.append(polygon([[0, 0]]))

def invert_col(col):
    col = col[1:]
    res = '#'

    for i in range(3):
        comp = int(col[2 * i:2 * i + 2], base=16)
        comp = 255 - comp
        res += ('0' + hex(comp)[2:])[-2:]

    return res

ghost_content = list()
def ghost():
    global ghost_content

    '''
    brushColor('#000000')
    penColor('#000000')
    rectangle(400, 600, 700, 400)
    '''

    for obj in ghost_content:
        deleteObject(obj)
    ghost_content = list()

    brushColor('#E5E5E5')
    penColor('#E5E5E5')
    #ellipsis(625, 625, 550, 400)
    ghost_content.append(c.create_oval(
        525, 375, 525 + 51, 375 + 47, fill='#E5E5E5', outline='#E5E5E5'
    ))

    p = [([])]
    for i in range(5):
        p.append(([]))
        deleteObject(pol[i])
        p[i].append([550-25  , 400])
        p[i].append([550-25*3+rm.uniform(-5, 6), 400+25*3+rm.uniform(-5, 6)])
        p[i].append([550-25*4+rm.uniform(-5, 6), 400+25*5+rm.uniform(-5, 6)])
        p[i].append([550-25*3+rm.uniform(-5, 6), 400+25*4+rm.uniform(-5, 6)])
        p[i].append([500-25*2+rm.uniform(-5, 6), 400+25*6+rm.uniform(-5, 6)])
        p[i].append([550-25*1+rm.uniform(-5, 6), 400+25*7+rm.uniform(-5, 6)])
        p[i].append([550     +rm.uniform(-5, 6), 400+25*6+rm.uniform(-5, 6)])
        p[i].append([550-25*1+rm.uniform(-5, 6), 400+25*8+rm.uniform(-5, 6)])
        p[i].append([550+25  +rm.uniform(-5, 6), 400+25*6+rm.uniform(-5, 6)])
        p[i].append([550+25*2+rm.uniform(-5, 6), 400+25*7+rm.uniform(-5, 6)])
        p[i].append([550+25*2+rm.uniform(-5, 6), 400+25*6+rm.uniform(-5, 6)])
        p[i].append([550+25*3+rm.uniform(-5, 6), 400+25*7+rm.uniform(-5, 6)])
        p[i].append([550+25*4+rm.uniform(-5, 6), 400+25*5+rm.uniform(-5, 6)])
        p[i].append([550+25*5+rm.uniform(-5, 6), 400+25*6+rm.uniform(-5, 6)])
        p[i].append([550+25*4+rm.uniform(-5, 6), 400+25*4+rm.uniform(-5, 6)])
        p[i].append([550+25*3+rm.uniform(-5, 6), 400+25*3+rm.uniform(-5, 6)])
        p[i].append([550+25*4+rm.uniform(-5, 6), 400+25*3+rm.uniform(-5, 6)])
        p[i].append([550+25, 400])
        pol[i] = (polygon(p[i]))



    # brushColor('#B2001D')
    # penColor('#B2001D')
    # ellipsis(25, 25, 550 - 10, 400 - 10)
    # ellipsis(25, 25, 550 + 10, 400 - 10)
    ghost_content.append(c.create_oval(
        535, 385, 535 + 11, 385 + 11, fill='#B2001D', outline='#B2001D'
    ))
    ghost_content.append(c.create_oval(
        555, 385, 555 + 11, 385 + 11, fill='#B2001D', outline='#B2001D'
    ))

    brushColor('#000000')
    penColor('#000000')
    cd = rm.uniform(-2, 2)
    d = rm.uniform(-2, 2)
    # ellipsis(15, 10, 550 - 10+cd,  400 - 10 +d)
    # ellipsis(15, 10, 550 + 10 +cd, 400 - 10 +d)

    ghost_content.append(c.create_oval(
        538 + cd, 389 + d, 538 + cd + 5, 389 + d + 5,
        fill='black', outline='black'
    ))
    ghost_content.append(c.create_oval(
        558 + cd, 389 + d, 558 + cd + 5, 389 + d + 5,
        fill='black', outline='black'
    ))

    ghost_content.append(polygon([
        (538 + cd, 389 + d), (539 + cd, 389 + d), (538 + cd - d, 460 + d),
        (537 + d - cd, 550 + d), (536 + cd - d, 460 + d)
    ]))
    ghost_content.append(polygon([
        (558 + cd, 389 + d), (559 + cd, 389 + d), (558 + cd - d, 460 + d),
        (557 + cd - d, 550 + d), (556 + cd - d, 460 + d)
    ]))

per = 4
def lightning():
    global lightning_obj, per, raining

    if per == 0:
        x = rm.choice(range(-60, 60))
        sy = rm.choice(range(7, 15)) / 10

        points = list()

        points.append((420 + x, 0 * sy))
        points.append((400 + x, 75 * sy))
        points.append((440 + x, 75 * sy))
        points.append((390 + x, 225 * sy))
        points.append((410 + x, 96 * sy))
        points.append((370 + x, 96 * sy))
        points.append((390 + x, 0 * sy))

        brushColor('white')
        penColor('white')
        lightning_obj = polygon(points)

        per = 1

    elif per == 1:
        for object in content:
            changePenColor(object, invert_col(content[object]))
            changeFillColor(object, invert_col(content[object]))

        per = 2

    elif per == 2:
        per = 3

    elif per == 3:
        deleteObject(lightning_obj)

        for object in content:
            changePenColor(object, content[object])
            changeFillColor(object, content[object])

        per = 4

        raining = True

    elif rm.choice([False] * 10 + [True]):
        per = 0

drops = dict()
raining = False  # it will be raining after the first lightning, just make sense
def rain():
    global drops

    if not raining:
        return 0

    col = '#222222'

    x = rm.choice(range(width))
    v = rm.choice(range(3)) + 1
    new_drop = c.create_oval(x, -2 * v, x + 1.5 * v, 0, fill=col, outline=col)

    drops[new_drop] = v

    deleting_drops = set()

    for drop in drops:
        moveObjectBy(drop, 0, drops[drop] * 2)

        x, y = xCoord(drop), yCoord(drop)
        if y > height * (1 + 0.2 * (drops[drop] - 3)):
            deleting_drops.add(drop)

        if drops[drop] < 3 and y >= roof_y and house_x1 < x < house_x2:
            deleting_drops.add(drop)

    for drop in deleting_drops:
        drops.pop(drop)
        deleteObject(drop)


width, height = 700, 600

content = dict()

windowSize(width, height)
canvasSize(width, height)
penColor('grey')
brushColor('grey')
#ellipsis(10000, 1000, 600, 100)

#background
brushColor('#99999C')
penColor('#99999C')
content[rectangle(0, 250, 700, 0)] = '#99999C'

brushColor('#000000')
penColor('#000000')
content[rectangle(0, 700, 700, 250)] = '#000000'

#hounted house
roof_y = 130
brushColor('#000000')
penColor('#000000')
content[polygon([
    [25, 160], [75, roof_y], [275, roof_y],[325, 160]
])] = '#000000'

house_x1 = 50
house_x2 = 300
brushColor('#552200')
penColor('#552200')
content[rectangle(house_x1, 500, house_x2, 160)] = '#552200'

#Top windws
brushColor('#554433')
penColor('#554433')
for i in range(4):
    content[rectangle(60 + i*65, 300, 90+ i*65, 160)] = '#554433'

##Bottom windws
brushColor('#554433')
penColor('#554433')
for i in range(2):
    content[rectangle(70 + i*85, 450, 110+ i*85, 400)] = '#554433'
brushColor('#FFCC33')
penColor('#FFCC33')
content[rectangle(70 + 2*85, 450, 110+ 2*85, 400)] = '#FFCC33'

#Balcony
brushColor('#110000')
penColor('#110000')
content[rectangle(25, 315, 320, 300)] = '#110000'




#Sky
##moon
# brushColor('#EEEEEE')
# penColor('#EEEEEE')
# content[ellipsis(4000, 4000, 600, 50)] = '#EEEEEE'
content[c.create_oval(
    537, -14, 537 + 127, -14 + 128, fill='#EEEEEE', outline='#EEEEEE')
] = '#EEEEEE'

##clouds
# brushColor('#444444')
# penColor('#444444')
# content[ellipsis(30000, 550, 350, 80)] = '#444444'
content[c.create_oval(
    176, 57, 176 + 348, 57 + 47, fill='#444444', outline='#444444')
] = '#444444'

# brushColor('#888888')
# penColor('#888888')
# content[ellipsis(20000, 500, 510, 60)] = '#888888'
content[c.create_oval(
    369, 38, 369 + 284, 38 + 45, fill='#888888', outline='#888888')
] = '#888888'

# brushColor('#333333')
# penColor('#333333')
# content[ellipsis(30000, 400, 700, 120)] = '#333333'
content[c.create_oval(
    527, 100, 527 + 354, 100 + 41, fill='#333333', outline='#333333')
] = '#333333'


onTimer(ghost, 200)
onTimer(lightning, 200)
onTimer(rain, 13)

run()
