from get_graph.dictionary import Dictionary
from get_graph.edge import Edge
from get_graph.node import Node


class Article:
    def __init__(self, authors, authors_id, title, year, source_title, value, issue, affiliations,
                 authors_with_affiliations):
        self.authors = authors
        self.authors_id = authors_id
        self.title = title
        self.year = year
        self.source_title = source_title
        self.value = value
        self.issue = issue
        self.affiliations = affiliations
        self.authors_with_affiliations = authors_with_affiliations

    def create_node(self, dictionary: Dictionary) -> list:
        """
        1 Узнаю аффилиацию
        2 Проверяю в словаре
        """
        count = 0
        list_node = []
        list_authors_with_affiliations = self.authors_with_affiliations.split('; ')
        list_affiliations = self.affiliations.split('; ')
        list_author_id = self.authors_id.split(';')
        for author_with_affil in list_authors_with_affiliations:
            name, faculty, university, department, country = "None", "None", "None", "None", "None"
            is_omstu = False
            value_affil = 0
            for affil in list_affiliations:
                # Считаю количество аффилиаций указанных автором и получаю данные для ноды
                # Получаю все аффилиации в статье и в цикле ищу эти аффилиации у автора
                # Если нахожу аффилиацию то записываю ее как основную
                # Если нахожу еще аффилиацию то добавляю в value_afff единицу
                name_author = author_with_affil.split('.,')[0].lower() + '.'
                if author_with_affil.find(affil) != -1 and author_with_affil.find('Omsk State Technical University') != -1:
                    value_affil += 1
                    if value_affil == 2:
                        continue
                    name, bool_value = dictionary.get_author_form_dictionary(name_author)
                    if bool_value:
                        faculty, department = dictionary.get_author_from_list_of_employees(name)
                    else:
                        faculty, department = 'OmSTU', 'OmSTU'
                    country = "Russian Federation"
                    university = "Omsk State Technical University"
                    is_omstu = True
                elif author_with_affil.find(affil) != -1:
                    value_affil += 1
                    if is_omstu:
                        continue
                    name = name_author
                    is_omstu = False
                    department = "None"
                    faculty = "None"
                    split_affil = affil.split(', ')
                    country = split_affil[-1]
                    university = ""
                    for university_get in split_affil:
                        if university_get.find("University") != -1:
                            university = university_get
                            break
                        elif university_get.find("Institute") != -1:
                            university = university_get
                            break
            author_id = list_author_id[count]
            node = Node(author_id, name, faculty, department, country, is_omstu, value_affil, university)
            list_node.append(node)
            count += 1
        return list_node

    def create_edges(self):
        list_edge = []
        for i in self.authors_id.split(';'):
            for j in self.authors_id.split(';'):
                if i == "" or j == "":
                    continue
                if i != j:
                    list_edge.append(Edge(i, j))
        return list_edge

    def __str__(self):
        return f"{self.authors} {self.authors_id} {self.title} {self.year} {self.source_title} {self.value} " \
               f"{self.issue} {self.affiliations} {self.authors_with_affiliations}"
