from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    gluOrtho2D(0, 500.0, 500.0, 0)

class mutableFloat(float):
    "create pseudo pointer class so that arithmetic is easier work with "
    def __init__(self, val = 0):
        self._val = val
    def __int__(self):
        return self._val
    def __index__(self):
        return self._val
    def __str__(self):
        return str(self._val)
    def __repr__(self):
        return repr(self._val)
    def __iter__(self):
        self._iter_cnt = 0
        return self
    def __iadd__(self,value):
        self._val+=value
        return self
    def __isub__(self,value):
        self._val-=value
        return self
    def __imul__(self,value):
        self._val*=value
        return self
    def __idiv__(self,value):
        self._val/=value
        return self
    def __add__(self, value):
        return mutableFloat(self._val+value)
    def __sub__(self, value):
        return mutableFloat(self._val-value)
    def __mul__(self, value):
        return mutableFloat(self._val*value)
    def __div__(self, value):
        return mutableFloat(self._val/value)
    def __le__(self, value):
        return bool(self._val<=value)
    def __lt__(self, value):
        return bool(self._val<value)
    def __ge__(self, value):
        return bool(self._val>=value)
    def __gt__(self, value):
        return bool(self._val>value)
    def __eq__(self, value):
        return bool(self._val==value)
    def __or__(self, value):
        return bool(self._val or value)
    def __and__(self, value):
        return bool(self._val and value)

class point(list):
    def __init__(self,*args:"either one point or a a set of numbers",**kwargs):
        """make the constructor to be able to handle 0 arguments,1 argument (integer and iterable),2 argument and 3 argument"""
        self.x = mutableFloat(0)
        self.y = mutableFloat(0)
        self.z = mutableFloat(0)
        if len(args)==1:
            try :
                args =[*args[0]]
                self.x = mutableFloat(args[0])
            except TypeError:
                self.x = mutableFloat(args[0])
        if len(args)>=2:
            self.x = mutableFloat(args[0])
            self.y = mutableFloat(args[1])
            if len(args)>=3:
                self.z = mutableFloat(args[2])
        self.list = [self.x,self.y,self.z]
        super().__init__(self.list)


    def drawpoint(self,color=[1.0, 0.0, 0.0]):
        glColor3f(*color)
        glVertex2f(x, y)


def drawDDA(x1,y1,x2,y2):
    glColor3f(0.0, 1.0, 0.0)
    dx = x2-x1
    dy = y2-y1
    x,y = x1,y1
    length = abs(dx) if abs(dx)>abs(dy) else abs(dy)
    if dx == dy == 0:
        return
    xinc = dx/float(length)
    yinc = dy/float(length)
    glVertex2f(x,y)

    for i in range(int(length)):
        x += xinc
        y += yinc
        glVertex2f(x,y)
    glColor3f(1.0, 0.0, 0.0)

    def translate(self,tx=0,ty=0,tz=0):
        self.x+=tx
        self.y+=ty
        self.z+=tz



def write_text(point):
    glColor3f(0, 1, 1)
    glWindowPos2d(point.x,500-point.y)
    string = [point.x,point.y]
    string = str(string)
    for ch in string:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(ch)))
    glColor3f(1.0, 0.0, 0.0)


def Display():
    global points1,p,drawn1,points2,drawn2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    for i in range(len(points1)):
        write_text(points1[i])
    glBegin(GL_POINTS)



    glEnd()
    glFlush()
    glutPostRedisplay()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'bezier curve')
    glutDisplayFunc(Display)
    init()
    glutMainLoop()


main()