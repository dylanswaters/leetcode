# leetcode 1305
#  complete
class treeNode:
    def __init__(self, vals):
        self.val = None
        self.left = None
        self.right = None
        for v in vals:
            self.insert(v)
        # self.printTree()

    def getElem(self):
        # print(self.val)
        return self.val

    def insert(self, val):
        if self.val == None:
            self.val = val
        else:
            if val < self.val:
                if self.left == None:
                    self.left = treeNode([val])
                else:
                    self.left.insert(val)
            else:
                if self.right == None:
                    self.right = treeNode([val])
                else:
                    self.right.insert(val)

    def printTree(self):
        print(self.val)
        if self.left != None:
            self.left.printTree(self.left)
        if self.right != None:
            self.right.printTree(self.right)

def getElems(tree, newList):
    # print(newList)
    if(tree.getElem() != None):
        newList.append(tree.getElem())
    if(tree.left != None):
        getElems(tree.left, newList)
    if(tree.right != None):
        getElems(tree.right, newList)
    # print(newList)
    return newList

def getAllElems(tree1, tree2):
    # get all values from trees
    finalList = getElems(tree1, []) + getElems(tree2, [])
    # sort final list
    finalList.sort()
    return finalList

def main():
    x = treeNode([2,1,4])
    y = treeNode([1,0,3])
    print(getAllElems(x,y))
    x = treeNode([0,-10,10])
    y = treeNode([5,1,7,0,2])
    print(getAllElems(x,y))
    x = treeNode([])
    y = treeNode([5,1,7,0,2])
    print(getAllElems(x,y))
    x = treeNode([0,-10,10])
    y = treeNode([])
    print(getAllElems(x,y))
    x = treeNode([1,8])
    y = treeNode([8,1])
    print(getAllElems(x,y))

if __name__ == "__main__":
    main()
