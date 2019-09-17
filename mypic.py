from graph import *
import numpy as np

def ellipsis(a, b, x0, y0):
    p = ([])
    for x in np.arange(-np.sqrt(a) + x0, np.sqrt(a) + x0, 1):
        p.append([x, np.sqrt(b*(1-(x-x0)**2/a))+y0])
    for x in np.arange(np.sqrt(a) + x0, -np.sqrt(a) + x0, -1):
        p.append([x, -np.sqrt(b*(1-(x-x0)**2/a))+y0])
    polygon(p)

windowSize(700, 600)
canvasSize(700, 600)
penColor('grey')
brushColor('grey')
ellipsis(10000, 1000, 600, 100)

#background
brushColor('#99999C')
penColor('#99999C')
rectangle(0, 250, 700, 0)

brushColor('#000000')
penColor('#000000')
rectangle(0, 700, 700, 250)

#hounted house
brushColor('#552200')
penColor('#552200')
rectangle(50, 500, 300, 160)

polygon(([]))

#Sky
##moon
brushColor('#EEEEEE')
penColor('#EEEEEE')
ellipsis(4000, 4000, 600, 50)

##clouds
brushColor('#444444')
penColor('#444444')
ellipsis(30000, 550, 350, 80)

brushColor('#888888')
penColor('#888888')
ellipsis(20000, 500, 510, 60)

brushColor('#333333')
penColor('#333333')
ellipsis(30000, 400, 700, 120)




run()
