"""Simple tkinter representation of a tree"""
import tkinter as tk
from tree import *

class PrettyNode(Node):
    def __init__(self,v):
        super().__init__(v)
        self.x=None
        self.y=None
        self.parent=None

    def add(self,other):
        super().add(other)
        other.parent=self

    def getpos(self):
        if self.childs:
            return (sum(c.getpos()[0] for c in self.childs)//len(self.childs),
                    self.childs[0].getpos()[1]-20)
        else:
            return self.x,self.y

    def draw(self,can):
        self.x,self.y=self.getpos()
        can.create_oval(self.x-2,self.y-2,self.x+2,self.y+2)
        can.create_text(self.x,self.y+10,text=str(self.v))
        if self.parent:
            can.create_line(self.x,self.y,self.parent.x,self.parent.y)
        for c in self.childs:
            c.draw(can)

class Fen(tk.Tk):
    def __init__(s):
        super().__init__()
        s.title("Tree representation")
        s.can=tk.Canvas(s,width=500,height=500)
        s.can.pack()
        s.tree=random_tree(typ=PrettyNode)
        print(s.tree.root,type(s.tree.root))
        s.draw()
    def draw(self):
        x=50
        for son in self.tree.leaves:
            son.y=450
            son.x=x
            x+=400//len(self.tree.leaves)
        self.tree.root.draw(self.can)

if __name__=="__main__":
    Fen().mainloop()
