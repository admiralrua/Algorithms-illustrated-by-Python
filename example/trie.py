import sys
sys.setrecursionlimit(10000000)


class Node:
    def __init__(self):
        self.value = 0
        self.child = dict()


def trie_insert(root, st):
    tmp   = root
    
    for ch in st:
        if not (ch in tmp.child):
            tmp.child[ch] = Node()
            
        tmp = tmp.child[ch]
    
    tmp.value += 1
     
 
def trie_search(root, st):
    tmp = root
    for ch in st:
        if not (ch in tmp.child):
            return False
        tmp = tmp.child[ch]
    return tmp.value > 0
        
        
def is_word(node):
    return (node.nword > 0)


def is_empty(node):
    return (len(node.child) == 0)
    

def trie_delete(root, st, level, length):
    if (root == None):
        return False

    if (level == length):
        if (root.value > 0):
            root.value -= 1
            return True
        return False

    ch   = st[level]
    flag = trie_delete(root.child[ch], st, level+1, length)

    if (flag) and (not is_word(root.child[ch])) and (is_empty(root.child[ch])):
        del root.child[ch]
        root.child[ch] = None

    return flag


def trie_print(root, st):
    if is_word(root):
        print(st)

    for ch in root.child:
        trie_print(root.child[ch], st + ch)
       
            
            
            
            
            