class Agente:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.habilidades = {}

    def adicionar_habilidade(self, habilidade):
        self.habilidades[habilidade.nome] = habilidade

    def usar_habilidade(self, nome_habilidade):
        if nome_habilidade in self.habilidades:
            habilidade = self.habilidades[nome_habilidade]
            habilidade.usar()
        else:
            print(f"Habilidade {nome_habilidade} não encontrada.")

    def mostrar_status(self):
        print(f"Agente: {self.nome}, Tipo: {self.tipo}")
        for habilidade in self.habilidades.values():
            print(f"Habilidade: {habilidade.nome}, Cargas: {habilidade.carga_atual}/{habilidade.carga_maxima}")

    def usar_habilidade_por_numero(self, numero):
        if 0 <= numero < len(self.habilidades):
            habilidade_nome = list(self.habilidades.keys())[numero]
            self.usar_habilidade(habilidade_nome)
        else:
            print("Número de habilidade inválido.")