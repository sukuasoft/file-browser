#Node é uma classe que representa um ficheiro ou pasta resultante da busca
class Node:
    name:str='',
    isFile:bool=False,
    childs=[]

    def __init__(self, name, isFile):
        self.name= name 
        self.isFile=isFile
        self.childs=[]
        
    def appendNode(self, node):
        self.childs.append(node)
