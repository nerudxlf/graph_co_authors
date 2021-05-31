import pandas as pd

from get_graph.article import Article
from get_graph.dictionary import Dictionary


class CreateGraphFromScopus:
    def __init__(self, path_to_scopus_file: str, dictionary: Dictionary):
        self.data_scopus = pd.read_excel(path_to_scopus_file)
        self.dict_data = dictionary

        self.authors = self.data_scopus['Authors'].to_list()
        self.authors_id = self.data_scopus['Author(s) ID'].to_list()
        self.title = self.data_scopus['Title'].to_list()
        self.year = self.data_scopus['Year'].to_list()
        self.source_title = self.data_scopus['Source title'].to_list()
        self.volume = self.data_scopus['Volume'].to_list()
        self.issue = self.data_scopus['Issue'].to_list()
        self.affiliations = self.data_scopus['Affiliations'].to_list()
        self.authors_with_affiliations = self.data_scopus['Authors with affiliations'].to_list()

    def get_articles(self) -> list:
        list_article = []
        for i in range(len(self.authors)):
            article = Article(self.authors[i], self.authors_id[i], self.title[i], self.year[i], self.source_title[i],
                              self.volume[i], self.issue[i], self.affiliations[i], self.authors_with_affiliations[i])
            list_article.append(article)
        return list_article

    def get_nodes_list(self) -> list:
        list_articles = self.get_articles()
        list_nodes = []
        for article in list_articles:
            for node in article.create_node(self.dict_data):
                list_nodes.append(node)
        return list(set(list_nodes))

    def get_edge_list(self) -> list:
        list_articles = self.get_articles()
        list_edge = []
        for article in list_articles:
            for edge in article.create_edges():
                list_edge.append(edge)
        return list(set(list_edge))

    @staticmethod
    def to_gml(list_nodes: list, list_edges: list):
        """
        ФУнкция формирует gml файл из 2 списков объектов
        :param list_nodes: список с нодами
        :param list_edges: список связей нод
        :return:
        """
        str_to_write = "graph\n[\n"
        for node in list_nodes:
            str_to_write += f"\tnode\n\t[\n{node.__str__()}\n\t]\n"
        for edge in list_edges:
            str_to_write += f"\tedge\n\t[\n{edge.__str__()}\n\t]\n"
        str_to_write += "]"
        f = open("graph.gml", "w", encoding="utf-8", )
        f.write(str_to_write)
        f.close()

