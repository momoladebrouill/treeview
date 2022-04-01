"""Simple tkinter representation of a tree"""
import tkinter as tk
from tree import *
from colorsys import hsv_to_rgb
from random import random
class PrettyNode(Node):
    def __init__(self,v):
        super().__init__(v)
        self._x=None
        self._y=None
        self.parent=None
        self.radius=20
        self.coul="#%02x%02x%02x" % tuple(int(c) for c in hsv_to_rgb(random(),1,255))

    def x():
        doc = "The x property."

        def fget(self):
            if self._x:
                return self._x
            else:
                self._x=sum(c.x for c in self.childs)//len(self.childs)
            return self._x

        def fset(self, value):
            self._x = value

        def fdel(self):
            del self._x

        return locals()

    x = property(**x())

    def y():
        doc = "The y property."

        def fget(self):
            if self.parent:
                self.y=self.parent.y+1
            else:
                self.y=1
            return self._y

        def fset(self, value):
            self._y = value

        def fdel(self):
            del self._y

        return locals()

    y = property(**y())

    def add(self,other):
        super().add(other)
        other.parent=self

    def draw(self,can,step):
        #can.create_text(self.x,self.y+self.radius+10,text=str(self.v))
        self.radius=step/8
        if self.parent:
            can.create_line(self.x,self.y*step,
                            self.parent.x,self.parent.y*step,
                            width=2,fill=self.coul)
        for c in self.childs:
            c.draw(can,step)

        can.create_oval(self.x-self.radius,self.y*step-self.radius,
                        self.x+self.radius,self.y*step+self.radius,
                        fill=self.coul,outline="white",width=self.y)



class Fen(tk.Tk):

    def __init__(s):
        super().__init__()
        s.title("Tree representation")
        s.can=tk.Canvas(s,width=500,height=500,bg="black")
        s.can.pack()
        s.but=tk.Button(s,command=s.generate,text="Show me how")
        s.but.pack()

    def generate(self):
        self.can.delete("all")
        self.tree=random_tree(typ=PrettyNode)
        self.draw()
        #self.after(2000,self.generate)

    def draw(self):
        x=50
        s=450//self.tree.height
        for son in self.tree.leaves:
            son.y=450
            son.x=x
            son.radius=s/8
            x+=400//(len(self.tree.leaves)-1)
        self.tree.root.draw(self.can,s)


if __name__=="__main__":
    Fen().mainloop()
