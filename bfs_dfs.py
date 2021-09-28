class Graph:
    def __init__(self):
        self.graph = {}

    # Lisätään verkon solmuun joukko muita solmuja johon se on yhdistetty, esim
    # "Tapiola" -> ["Matinkylä", "Aalto Yliopisto"])
    def addEdge(self, u, v):
        self.graph[u] = v

    def BFS(self, start, target):

        # Käydyt solmut, alussa se on tyhjä
        visited = set()

        # Jono joka sisältää solmun ja solmun so far käydyn reitin
        queue = [(start,[start])]

        while queue:
            # jatka kunnes jono ei ole tyhjä

            # valitaan jokin solmu ja poistetaan se jonosta
            vertex, path  = queue.pop(0)
            visited.add(vertex)
            print(f"Valittiin solmu {vertex},\n"
                  f"Reitti alkusolmusta tähän solmuun on: {path}\n")

            # Käydään valitun solmun naapurit läpi
            at_least_one_unvisited_neighbour = False
            for node in self.graph[vertex]:
                if node == target:
                    print(f"Löysimme kohdesolmun {node} {vertex}n naapureista! Reitti on valmis!")
                    return path + [node]
                if node not in visited:
                    at_least_one_unvisited_neighbour = True
                    print(f"Saavuimme {vertex}n naapurisolmun {node} kohdalle, jonka luona emme ole vielä käyneet!")
                    queue.append((node, path + [node]))
                    visited.add(node)
            if not at_least_one_unvisited_neighbour:
                print(f"Solmulla {vertex} ei ollut uusia naapureita :(")
            print()

    # DFS:n sisäinen funktio jota kutsutaan rekursiivisesti
    def DFS_inner(self, start, target, visited, path):
        visited.add(start)
        print(f"Valittiin solmu {start},\n"
              f"Reitti alkusolmusta tähän solmuun on: {path}\n")

        # Käydään valitun solmun naapurit läpi
        at_least_one_unvisited_neighbour = False
        for node in self.graph[start]:
            if node == target:
                print(f"Löysimme kohdesolmun {node} {start}n naapureista! Reitti on valmis!")
                return path + [node]

            if node not in visited:
                at_least_one_unvisited_neighbour = True
                print(f"Saavuimme {start}n naapurisolmun {node} kohdalle, jonka luona emme ole vielä käyneet!\n")

                # kutsutaan itseämme rekursiivisesti
                return_path = self.DFS_inner(node, target, visited, path + [node])
                if return_path is not None:
                    return return_path

        if not at_least_one_unvisited_neighbour:
            print(f"Solmulla {start} ei ollut uusia naapureita :(")
        print()

    def DFS(self, start, target):

        # Käydyt solmut, alussa se on tyhjä
        visited = set()

        # Kutsutaan sisäistä DFS funktiota
        return self.DFS_inner(start, target, visited, [start])


g = Graph()  # uusi (tyhjä) verkko
g.addEdge("Matinkylä", ["Tapiola"])  # lisätään jokaisen aseman naapuriasemat
g.addEdge("Tapiola", ["Matinkylä", "Aalto Yliopisto"])
g.addEdge("Aalto Yliopisto", ["Tapiola", "Helsingin päärautatieasema"])
g.addEdge("Helsingin päärautatieasema", ["Aalto Yliopisto", "Pasila", "Itäkeskus"])
g.addEdge("Itäkeskus", ["Helsingin päärautatieasema", "Mellunmäki", "Vuosaari"])
g.addEdge("Mellunmäki", ["Itäkeskus"])
g.addEdge("Vuosaari", ["Itäkeskus"])
g.addEdge("Pasila", ["Helsingin päärautatieasema", "Huopalahti", "Oulunkylä"])
g.addEdge("Huopalahti", ["Leppävaara", "Myyrmäki", "Pasila"])
g.addEdge("Myyrmäki", ["Huopalahti", "Lentoasema"])
g.addEdge("Leppävaara", ["Huopalahti", "Espoo"])
g.addEdge("Espoo", ["Leppävaara"])
g.addEdge("Oulunkylä", ["Pasila", "Malmi"])
g.addEdge("Malmi", ["Oulunkylä", "Tikkurila"])
g.addEdge("Tikkurila", ["Malmi", "Lentoasema"])
g.addEdge("Lentoasema", ["Tikkurila", "Myyrmäki"])

print("Matka Aalto-Yliopistosta Tikkurilaan käyttäen BFS-Algoritmia:")
print(g.BFS("Aalto Yliopisto", "Tikkurila"))

# Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# And https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# Original author: Neelam Yadav
# Edits by: Aarni Haapaniemi
