import math

graph = {
    "A": [(2, "B"), (5, "C")],
    "B": [(10, "E")],
    "C": [(3, "D")],
    "D": [(2, "E")],
    "E": [],
}
results = {x: "inf" for x in graph.keys()}
print(results)
node_to_visit = ["A"]
if node_to_visit:
    graph[node_to_visit[0]]
