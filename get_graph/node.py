class Node:
    def __init__(self, author_id: str, name: str, faculty: str, department: str, country: str, is_omstu: bool,
                 value_affiliations: int, university: str):
        self.author_id = int(author_id)
        self.name = name
        self.faculty = faculty
        self.department = department.replace('"', '')
        self.country = country
        self.university = university
        self.is_omstu = is_omstu
        self.value_affiliations = value_affiliations

    def __str__(self):
        return f'\t\tid {self.author_id}\n' \
               f'\t\tlabel "{self.name}"\n' \
               f'\t\tfaculty "{self.faculty}"\n' \
               f'\t\tcountry "{self.country}"\n' \
               f'\t\tdepartment "{self.department}"\n' \
               f'\t\tis_omstu "{self.is_omstu}"\n' \
               f'\t\tvalue_affiliations "{self.value_affiliations}"\n' \
               f'\t\tuniversity "{self.university}"\n'

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.author_id == other.author_id
        return NotImplemented

    def __hash__(self):
        return self.author_id
