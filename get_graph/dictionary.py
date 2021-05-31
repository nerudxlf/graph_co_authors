import pandas as pd


class Dictionary:
    """
    Класс для работы со словарем и со списком сотрудником
    """
    def __init__(self, path_to_dictionary: str, path_to_list_employee: str):
        self.pd_dict = pd.read_excel(path_to_dictionary)
        self.employee = self.pd_dict["Сотрудник"].to_list()
        self.names = self.pd_dict["names"].to_list()

        self.pd_list_of_employee = pd.read_excel(path_to_list_employee)
        self.name_author = self.pd_list_of_employee['Сотрудник']
        self.work_place = self.pd_list_of_employee['Место работы']

    def get_author_form_dictionary(self, name: str) -> tuple:
        for i in range(len(self.employee)):
            try:
                if self.names[i].find(name.lower()) != -1:
                    return self.employee[i], True
            except AttributeError:
                pass
        return name, False

    def get_author_from_list_of_employees(self, name: str) -> tuple:
        for i in range(len(self.name_author)):
            if self.name_author[i].lower() == name.lower():
                return self.__get_unit_name(self.work_place[i])
        return "None", "None"

    @staticmethod
    def __get_unit_name(unit: str) -> tuple:
        """
        Делит строку с местом работы на кафедру и факультет
        :param unit:
        :return:
        """
        unit_list = unit.split('/')
        if len(unit_list) == 2:
            return unit_list[0], unit_list[1]
        return unit_list[0], "None"
