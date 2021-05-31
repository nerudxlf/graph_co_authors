from get_graph.dictionary import Dictionary
from get_graph.graph import CreateGraphFromScopus


def main():
    dict_data = Dictionary("dictionary.xlsx", "list_of_employees.xlsx")
    graph = CreateGraphFromScopus("scopus2020.xlsx", dict_data)
    list_node = graph.get_nodes_list()
    list_edge = graph.get_edge_list()
    graph.to_gml(list_node, list_edge)
