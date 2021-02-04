"""
Given a lexically graphically sorted list of alien words, return the order of
the alphabet that fits the assortment.

Alphabet (in no particular order): <b f g q>

TestCase 1:
bgg
fbq
fqf
ffq
gfg

b -> q - > f -> g

TestCase 2:
bgg
fbq
ffq
fqf
gfg

b - > f -> g -> q


class G:
    def add(self, c1, c2) #adds edge
    def remove(self, c1, c2) #removes edge
    def outgoing(self, c) #returns list of characters
    def incoming(self, c) #return list of characters
    def nodes(self) #returns list of characters
    def empty(self) # returns boolean
"""

class Graph(object):
     def __init__(self):
         self.dict = {}

     def nodes(self):
         return(list(self.dict))

     def add(self, n1, n2):
         try:
             self.dict[n1].add(n2)
         except:
             self.dict[n1] = set()
             self.dict[n1].add(n2)
     def remove(self, n1, n2):
         try:
             self.dict[n1].remove(n2)
         except:
             return -1

     def outgoing(self, n):
         return(list(self.dict.get(n, [])))

     def incoming(self, n):
         inc = []
         for n1,n2s in self.dict.items():
             if n in n2s:
                 inc.append(n1)
         return(inc)

     def print(self):
         for k,v in self.dict.items():
             print(k, " ", v)

class OrderedGraph(object):

    def __init__(self):
        self.g = Graph()

    def processEdge(self, nodeA, nodeB):
        if nodeA != nodeB:
            self.g.add(nodeA, nodeB)
        pass

    def samePrefix(self, wordA, wordB, index):
        #obsolete
        for k in range(index+1):
            if wordA[k] != wordB[k]:
                return False
        return True

    def genGraph(self, wordList):
        #main function
        for i, word in enumerate(wordList):
            word_lst = []
            if i == 0:
                continue
            elif i > 0:
                samePrefix = True
                for j, ch in enumerate(word):
                    if j == 0:
                        self.processEdge(wordList[i-1][j], ch)
                    elif j > 0:
                        samePrefix = samePrefix and wordList[i-1][j-1] == word[j-1]
                        if samePrefix:
                            self.processEdge(wordList[i-1][j], ch)

    def pullAlphabet(self):
        zeroNode = None
        output = []
        for n in self.g.nodes():
            if len(self.g.incoming(n)) == 0:
                zeroNode = n
                break
        zeroNodes = [zeroNode]
        while zeroNodes:
            zeroNode = zeroNodes.pop()
            output.append(zeroNode)
            toRemove = self.g.outgoing(zeroNode)
            for n in toRemove:
                self.g.remove(zeroNode, n)
                if len(self.g.incoming(n)) == 0:
                    zeroNodes.append(n)
        return output

if __name__ == "__main__":
    g = Graph()
    lst = ["bgg", "fbq", "fqf", "ffq", "gfg"] #TestCase 1
    lst2 = ["bgg", "fbq", "ffq", "fqf", "gfg"] #TestCase 2

    orderedG = OrderedGraph()
    orderedG.genGraph(lst)
    print(orderedG.pullAlphabet())
