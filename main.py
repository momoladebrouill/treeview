"""Simple tkinter representation of a tree"""
import tkinter as tk
from tree import *

class PrettyNode(Node):
    def __init__(self,v):
        super().__init__(v)
        self.x=None
        self.y=None
        self.parent=None
        self.radius=20
        self.coul="#{0:03x}".format(hash(self.v)%0xfff)

    def add(self,other):
        super().add(other)
        other.parent=self

    def getpos(self,step):
        if self.x is None:
            self.x=sum(c.getpos(step)[0] for c in self.childs)//len(self.childs)
        if self.y is None:
            self.y=min(c.getpos(step)[1] for c in self.childs)-step
        self.radius=step/8
        return self.x,self.y

    def draw(self,can,step):
        self.x,self.y=self.getpos(step)
        #can.create_text(self.x,self.y+self.radius+10,text=str(self.v))
        if self.parent:
            can.create_line(self.x,self.y,
                            self.parent.x,self.parent.y,
                            width=2,fill=self.coul)
        for c in self.childs:
            c.draw(can,step)
        can.create_oval(self.x-self.radius,self.y-self.radius,
            self.x+self.radius,self.y+self.radius,
            fill=self.coul)

class Fen(tk.Tk):
    def __init__(s):
        super().__init__()
        s.title("Tree representation")
        s.can=tk.Canvas(s,width=500,height=500,bg="white")
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
