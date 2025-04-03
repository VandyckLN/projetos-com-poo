import time
from datetime import datetime, timedelta


class Habilidade:
    """Representa uma habilidade de um agente"""

    def __init__(self, nome: str, descricao: str, carga: int = 1):
        self.nome = nome
        self.descricao = descricao
        self.carga_maxima = carga
        self.carga_atual = carga
        self.tempo_recarga = 120  # 2 minutos em segundos
        self.proxima_recarga = None

    def usar(self) -> bool:
        """Tenta usar a habilidade, retorna True se conseguiu usar"""
        if self.carga_atual > 0:
            self.carga_atual -= 1
            if self.proxima_recarga is None:
                self.proxima_recarga = datetime.now() + timedelta(
                    seconds=self.tempo_recarga
                )
            return True
        else:
            self.verificar_recarga()
            return False

    def verificar_recarga(self) -> bool:
        """Verifica se a habilidade pode ser recarregada e mostra contador"""
        if self.proxima_recarga and datetime.now() >= self.proxima_recarga:
            self.recarregar()
            return True
        elif self.proxima_recarga:
            tempo_restante = self.proxima_recarga - datetime.now()
            segundos_restantes = int(tempo_restante.total_seconds())
            minutos = segundos_restantes // 60
            segundos = segundos_restantes % 60
            print(f"⏳ Aguarde {minutos:02d}:{segundos:02d} para recarregar", end="\r")
            time.sleep(1)  # Atualiza a cada segundo
        return False

    def recarregar(self):
        """Recarrega a habilidade para sua carga máxima"""
        self.carga_atual = self.carga_maxima
        self.proxima_recarga = None
        print(f"✨ {self.nome} recarregada!")


class Agente:
    """Representa um agente do Valorant"""

    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo
        self.habilidades = {}  # Dicionário para guardar habilidades

    def adicionar_habilidade(self, habilidade: Habilidade):
        """Adiciona uma habilidade ao agente"""
        self.habilidades[habilidade.nome] = habilidade

    def usar_habilidade(self, nome_habilidade: str):
        """Usa uma habilidade específica do agente"""
        if nome_habilidade in self.habilidades:
            habilidade = self.habilidades[nome_habilidade]
            if habilidade.usar():
                print(f"🎮 {self.nome} usou {habilidade.nome}: {habilidade.descricao}")
                print(f"📊 Cargas restantes: {habilidade.carga_atual}")
                if habilidade.carga_atual == 0:
                    print(f"⏳ Recarga iniciada - Tempo restante: 02:00")
                    while not habilidade.verificar_recarga():
                        pass  # Aguarda a recarga terminar mostrando o contador
                    print("\n")  # Limpa a linha do contador
            else:
                while not habilidade.verificar_recarga():
                    pass  # Aguarda a recarga terminar mostrando o contador
                print("\n")  # Limpa a linha do contador
        else:
            print(f"❌ Habilidade '{nome_habilidade}' não encontrada!")

    def mostrar_status(self):
        """Mostra o status do agente e suas habilidades"""
        print(f"\n=== {self.nome} ({self.tipo}) ===")
        print("Habilidades:")
        for i, habilidade in enumerate(self.habilidades.values(), 1):
            print(
                f"{i}. {habilidade.nome}: {habilidade.carga_atual}/{habilidade.carga_maxima} cargas"
                f"\n   └─ {habilidade.descricao}"
            )

    def usar_habilidade_por_numero(self, numero: int):
        """Usa uma habilidade baseada no seu número de seleção"""
        try:
            habilidade = list(self.habilidades.values())[numero - 1]
            self.usar_habilidade(habilidade.nome)
        except IndexError:
            print("❌ Número de habilidade inválido!")


# Exemplo de uso
def main():
    # Criando agentes
    jett = Agente("Jett", "Duelista")
    sage = Agente("Sage", "Sentinela")
    reyna = Agente("Reyna", "Duelista")
    Omen = Agente("Omen", "Controlador")

    # Adicionando habilidades à Jett
    jett.adicionar_habilidade(
        Habilidade("Corrente Ascendente", "Impulsiona Jett para o alto", 2)
    )
    jett.adicionar_habilidade(Habilidade("Vento Afiado", "Lança projéteis de vento", 2))

    # Adicionando habilidades à Sage
    sage.adicionar_habilidade(Habilidade("Orbe de Cura", "Cura um aliado", 1))
    sage.adicionar_habilidade(Habilidade("Ressurreição", "Revive um aliado", 1))

    # Adicionando habilidades à Reyna
    reyna.adicionar_habilidade(Habilidade("Devorar", "Cura-se ao eliminar inimigos", 2))
    reyna.adicionar_habilidade(Habilidade("Dismissar", "Fica invulnerável", 2))
    reyna.adicionar_habilidade(Habilidade("Olhar Voraz", "Cega os inimigos", 2))
    reyna.adicionar_habilidade(
        Habilidade("Imperatriz", "Aumenta velocidade de disparo", 1)
    )
    Omen.adicionar_habilidade(
        Habilidade("teleporte", "Teleporta para um local próximo", 2)
    )
    Omen.adicionar_habilidade(Habilidade("Sombra da Morte", "Cega os inimigos", 2))
    Omen.adicionar_habilidade(
        Habilidade("Cegar", "Passa uma bola de cegueira por uma area", 2)
    )

    # Menu interativo
    agentes = {"1": jett, "2": sage, "3": reyna, "4": Omen}

    while True:
        print("\n=== VALORANT Simulator ===")
        print("1. Jett")
        print("2. Sage")
        print("3. Reyna")
        print("4. Omen")
        print("5. Sair")

        escolha = input("\nEscolha um agente (1-5): ")

        if escolha == "5":
            print("GG!")
            break

        if escolha in agentes:
            agente = agentes[escolha]
            agente.mostrar_status()

            try:
                hab = input("\nEscolha o número da habilidade (ou ENTER para voltar): ")
                if hab:
                    agente.usar_habilidade_por_numero(int(hab))
            except ValueError:
                print("❌ Por favor, digite um número válido!")
        else:
            print("Agente inválido!")


if __name__ == "__main__":
    main()
