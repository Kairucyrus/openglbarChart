import OpenGL.GLUT as glut
import OpenGL.GL as gl
import numpy as np

class FruitData:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

fruitData = [
    FruitData("Avocados", 36),
    FruitData("Oranges", 41),
    FruitData("Bananas", 19),
    FruitData("Kiwi Fruit", 28),
    FruitData("Mangoes", 30),
    FruitData("Grapes", 16)
]

Color = np.array

fruitColors = {
    "Avocados": Color([0.0, 0.5, 0.0]),
    "Oranges": Color([1.0, 0.5, 0.0]),
    "Bananas": Color([1.0, 1.0, 0.0]),
    "Kiwi Fruit": Color([0.6, 0.3, 0.0]),
    "Mangoes": Color([1.0, 0.95, 0.0]),
    "Grapes": Color([0.5, 0.0, 0.5])
}

def drawAxes():
    gl.glColor3f(0.0, 0.0, 0.0)
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(0.1, 0.1)
    gl.glVertex2f(0.1, 0.9)
    gl.glEnd()
    
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(0.1, 0.1)
    gl.glVertex2f(0.9, 0.1)
    gl.glEnd()
    
    gl.glColor3f(1.0, 0.0, 0.0)
    labelY = 0.1
    for i in range(0, 56, 13):
        gl.glRasterPos2f(0.05, labelY)
        label = str(i)
        for r in label:
            glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_10, ord(r))
        labelY += 0.2

def drawBars():
    barWidth = 0.08
    startX = 0.18
    startY = 0.1
    maxHeight = 0.8
    for i in range(len(fruitData)):
        color = fruitColors[fruitData[i].name]
        gl.glColor3fv(color)
        barHeight = fruitData[i].quantity / 50.0
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2f(startX + i * 0.10, startY)
        gl.glVertex2f(startX + i * 0.10, startY + barHeight * maxHeight)
        gl.glVertex2f(startX + i * 0.10 + barWidth, startY + barHeight * maxHeight)
        gl.glVertex2f(startX + i * 0.10 + barWidth, startY)
        gl.glEnd()

def drawLabels():
    labelX = 0.2
    labelY = 0.05
    for i in range(len(fruitData)):
        gl.glColor3f(0.0, 0.0, 0.0)
        gl.glRasterPos2f(labelX + i * 0.10, labelY)
        for c in fruitData[i].name:
            glut.glutBitmapCharacter(glut.GLUT_BITMAP_TIMES_ROMAN_10, ord(c))

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    drawAxes()
    drawBars()
    drawLabels()
    gl.glFlush()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(800, 600)
    glut.glutCreateWindow(b"Fruit Preference Bar Chart")
    glut.glutDisplayFunc(display)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()

#ran in a virtual environment