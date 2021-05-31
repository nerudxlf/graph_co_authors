class Edge:
    def __init__(self, id_source: str, id_target: str):
        self.id_source = int(id_source)
        self.id_target = int(id_target)
        self.value = 1

    def __eq__(self, other):
        if isinstance(other, Edge):
            if self.id_source == other.id_source or self.id_source == self.id_target:
                self.value += 1
                return True
            return False
        return NotImplemented

    def __hash__(self):
        return self.id_target

    def __str__(self):
        return f'\t\tsource {self.id_source}\n' \
               f'\t\ttarget {self.id_target}\n' \
               f'\t\tvalue {self.value}'
