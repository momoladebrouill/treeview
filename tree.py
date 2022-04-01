"""Simple structure d'arbre"""
from random import choice,randrange
class Node:

    def __init__(self,value):
        self.v=value
        self.childs=list()

    def add(self,other):
        assert isinstance(other,type(self))
        self.childs.append(other)

    __repr__=lambda s:"N"+s.v.__repr__()

    def _leaves(self):
        if self.childs:
            l=[]
            for c in self.childs:
                l+=c._leaves()
            return l
        else:
            return [self]

class Tree:
    def __init__(self,typ=Node):
        self.root=typ(None)

    @property
    def leaves(self):
        return self.root._leaves()

    @property
    def height(self):
        current=[self.root]
        height=0
        while current:
            next_=list()
            for elem in current:
                for c in elem.childs:
                    next_.append(c)
            height+=1
            current=next_[:]
        return height

def standard_tree(typ=Node):
    t=Tree(typ)
    t.root.add(typ("JS"))
    t.root.add(typ("nasal"))
    t.root.add(typ(1))
    t.root.childs[0].add(typ(True))
    return t

def random_tree(typ=Node):
    t=Tree(typ)
    nodes=[t.root]
    namegenerator= lambda n:''.join(chr(randrange(65,90)) for i in range(n))
    for i in range(randrange(1,10)*5):
        n=typ(namegenerator(2))
        choice(nodes).add(n)
        nodes.append(n)
    return t

def main():
    t=Tree(Node)
    t.root.add(Node("JS"))
    t.root.add(Node("nasal"))
    t.root.add(Node(1))
    t.root.childs[0].add(Node(True))
    print(t.leaves,t.root.childs)
    return t

if __name__ == '__main__':
    main()
