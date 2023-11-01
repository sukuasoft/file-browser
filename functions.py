from pathlib import Path
from node import Node

def browse(path:Path):

    node_current = Node(path.name, False)

    #Pega os ficheiros
    files =  list(path.glob('*')) 

    for file in files:
        if file.is_file():
            node_current.appendNode(Node(file.name, True))
        else:
            node_current.appendNode(browse(file.absolute()))   
            pass

    return node_current

def show_files(node:Node, level=0):
   print (generator_spaces(level) + node.name+ '/')

   for node_child in node.childs:
        if  node_child.isFile:
            print(generator_spaces(level+1) + node_child.name)
        else:
            show_files(node_child, level+1)

def generator_spaces(count:int):
    text:str =''
    for x in range(count):
        text +='   '

    return text


