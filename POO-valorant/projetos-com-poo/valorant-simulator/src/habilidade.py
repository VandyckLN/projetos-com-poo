class Habilidade:
    def __init__(self, nome, descricao, carga_maxima, tempo_recarga):
        self.nome = nome
        self.descricao = descricao
        self.carga_maxima = carga_maxima
        self.carga_atual = carga_maxima
        self.tempo_recarga = tempo_recarga
        self.proxima_recarga = 0

    def usar(self):
        if self.carga_atual > 0:
            self.carga_atual -= 1
            print(f'Habilidade {self.nome} usada! Cargas restantes: {self.carga_atual}')
        else:
            print(f'Habilidade {self.nome} sem cargas disponíveis!')

    def verificar_recarga(self, tempo_atual):
        if tempo_atual >= self.proxima_recarga:
            self.recarregar()

    def recarregar(self):
        self.carga_atual = self.carga_maxima
        self.proxima_recarga += self.tempo_recarga
        print(f'Habilidade {self.nome} recarregada! Cargas disponíveis: {self.carga_atual}')