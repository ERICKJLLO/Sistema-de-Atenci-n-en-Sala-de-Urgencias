class Paciente:
    __slots__ = ("id_paciente", "categoria", "nivel_triage")

    def __init__(self, id_paciente, categoria, nivel_triage):
        self.id_paciente = id_paciente
        self.categoria = categoria
        self.nivel_triage = nivel_triage

    def __str__(self):
        return f"{self.id_paciente} | {self.categoria} | Triage {self.nivel_triage}"