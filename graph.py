
class graph:
    def __init__(self,gdict=None) -> None:
        if gdict is None:
            gdict=[]
        
        self.gdict=gdict
    
    
    # getting vertices of graphs
    def getVertices(self):
            return list(self.gdict.keys())
        
    def getedges(self):
        edges=[]
        for i in self.gdict:
            for j in self.gdict[i]:
                if {j,i} not in edges:
                    edges.append({i,j})
                
        return edges
    
    def add_vertices(self,vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx]=[]
            
    def add_edge(self,edge):
        pass
    

graph_elements={
    "a": ['b','c'],
    "b": ['a','d'],
    "c": ['a','d'],
    "d": ['e'],
    "e": ['d'],
}
g=graph(graph_elements)
print(g.getVertices())
print(g.getedges())
