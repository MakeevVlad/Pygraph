from graph import *
import numpy as np
import random as rm

def ellipsis(a, b, x0, y0):
    p = ([])
    for x in np.arange(-np.sqrt(a) + x0, np.sqrt(a) + x0, 1):
        p.append([x, np.sqrt(b*(1-(x-x0)**2/a))+y0])
    for x in np.arange(np.sqrt(a) + x0, -np.sqrt(a) + x0, -1):
        p.append([x, -np.sqrt(b*(1-(x-x0)**2/a))+y0])
    return polygon(p)

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

def ghost():
    '''
    brushColor('#000000')
    penColor('#000000')
    rectangle(400, 600, 700, 400)
    '''
    brushColor('#E5E5E5')
    penColor('#E5E5E5')
    ellipsis(625, 625, 550, 400)
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



    brushColor('#B2001D')
    penColor('#B2001D')
    ellipsis(25, 25, 550 - 10, 400 - 10)
    ellipsis(25, 25, 550 + 10, 400 - 10)

    brushColor('#000000')
    penColor('#000000')
    c = rm.uniform(-1, 2)
    d = rm.uniform(-1, 2)
    ellipsis(15, 10, 550 - 10+c,  400 - 10 +d)
    ellipsis(15, 10, 550 + 10 +c, 400 - 10 +d)

per = 3 #phase counter
def lightning():
    global lightning_obj, per

    per += 1
    per %= 10

    if per == 0:
        points = list()

        points.append((420, 0))
        points.append((400, 75))
        points.append((440, 75))
        points.append((390, 225))
        points.append((410, 96))
        points.append((370, 96))
        points.append((390, 0))

        brushColor('white')
        penColor('white')
        lightning_obj = polygon(points)

    elif per == 1:
        for object in content:
            changePenColor(object, invert_col(content[object]))
            changeFillColor(object, invert_col(content[object]))



    elif per == 3:
        deleteObject(lightning_obj)

        for object in content:
            changePenColor(object, content[object])
            changeFillColor(object, content[object])

def house(x,y): #x,y=left bottom; default x=50,y=500
    #hounted house
    brushColor('#552200')
    penColor('#552200')
    content[rectangle(x, y, x+250, y-340)] = '#552200'
    #roof
    brushColor('#000000')
    penColor('#000000')
    content[polygon([[x-25, y-340], [x+25, y-370], [x+225,y-370],[x+275, y-340]])] = '#000000'
    #columns
    brushColor('#554433')
    penColor('#554433')
    for i in range(4):
        content[rectangle(x+10 + i*65, y-200, x+40+ i*65, y-340)] = '#554433'
    ##Bottom windws
    brushColor('#554433')
    penColor('#554433')
    for i in range(2):
        content[rectangle(x+20 + i*85, y-50, x+60+ i*85, y-100)] = '#554433'
    brushColor('#FFCC33')
    penColor('#FFCC33')
    content[rectangle(x+20 + 2*85, y-50, x+60+ 2*85, y-100)] = '#FFCC33'
    #Balcony
    brushColor('#371700')
    penColor('#371700')
    content[rectangle(x-25, y-185, x+270, y-200)] = '#371700'


content = dict()

windowSize(700, 600)
canvasSize(700, 600)
penColor('grey')
brushColor('grey')
ellipsis(10000, 1000, 600, 100)

#background
brushColor('#99999C')
penColor('#99999C')
content[rectangle(0, 250, 700, 0)] = '#99999C'

brushColor('#000000')
penColor('#000000')
content[rectangle(0, 700, 700, 250)] = '#000000'

house(50,500)

#Sky
##moon
brushColor('#EEEEEE')
penColor('#EEEEEE')
content[ellipsis(4000, 4000, 600, 50)] = '#EEEEEE'

##clouds
brushColor('#444444')
penColor('#444444')
content[ellipsis(30000, 550, 350, 80)] = '#444444'

brushColor('#888888')
penColor('#888888')
content[ellipsis(20000, 500, 510, 60)] = '#888888'

brushColor('#333333')
penColor('#333333')
content[ellipsis(30000, 400, 700, 120)] = '#333333'


onTimer(ghost, 200)
onTimer(lightning, 200)

run()
