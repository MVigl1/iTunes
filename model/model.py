import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._albumObjectList = []
        self._grafo = nx.Graph()
        self._idMap = {}


    def creaGrafo(self, durata):
        durataMillisecindi = int(durata)*60*1000
        self.addNodes(durataMillisecindi)
        self.addEdges()

    def addNodes(self, durata):

        self._grafo.clear_edges()
        self._albumObjectList = DAO.getAllObjects(durata)
        self._grafo.add_nodes_from(self._albumObjectList)

        for v in self._albumObjectList:
            self._idMap[v.albumId] = v

    def addEdges(self):

        self._grafo.clear_edges()
        allEdges = DAO.getAllConnessioni(self._idMap)

        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2)

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]

        #Modo1: successori di v0 in DFS
        successors = nx.dfs_successors(self._grafo, v0)
        allSucc = []
        for v in successors.values():
            allSucc.extend(v)

        print(f"Metodo 1 (pred): {len(allSucc)}")

        #Modo2: predecessori di v0 in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(f"Metodo 2 (succ): {len(predecessors.values())}")

        #Modo3: conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, v0)
        print(f"Metodo 3 (tree): {len(tree.nodes)}")

        #Modo4: node_connected_component
        connComp = nx.node_connected_component(self._grafo, v0)
        print(f"Metodo 4 (connected comp): {len(connComp)}")

        return len(connComp)





    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
