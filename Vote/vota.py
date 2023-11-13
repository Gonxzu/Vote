class EleicaoPresidencial:
    def __init__(self, candidatos):
        self.candidatos = candidatos
        self.votos = {candidato: 0 for candidato in candidatos}

    def votar(self, eleitor):
        print("Candidatos disponíveis:")
        for i, candidato in enumerate(self.candidatos, 1):
            print(f"{i}. {candidato}")

        escolha = int(input(f"\n{eleitor}, selecione o número do candidato em quem deseja votar (1-{len(self.candidatos)}): "))

        if 1 <= escolha <= len(self.candidatos):
            candidato_escolhido = self.candidatos[escolha - 1]
            self.votos[candidato_escolhido] += 1
            print(f"\n{eleitor} votou em {candidato_escolhido}.")
        else:
            print(f"\n{eleitor}, escolha inválida. Por favor, escolha um número válido.")

    def realizar_eleicao(self, numero_eleitores):
        for i in range(1, numero_eleitores + 1):
            self.votar(f"Eleitor {i}")

    def mostrar_resultados(self):
        print("\nResultado da Eleição Presidencial:")
        for candidato, votos in self.votos.items():
            print(f"{candidato}: {votos} votos")

        vencedor = max(self.votos, key=self.votos.get)
        total_votos_vencedor = self.votos[vencedor]

        print(f"\nO vencedor é {vencedor} com {total_votos_vencedor} votos!")

# Lista de candidatos
candidatos = ["Candidato A", "Candidato B", "Candidato C"]

# Perguntar ao usuário quantos eleitores participarão
numero_eleitores = int(input("Informe o número de eleitores: "))

# Inicialização da eleição
eleicao = EleicaoPresidencial(candidatos)

# Realizar a eleição
eleicao.realizar_eleicao(numero_eleitores)

# Mostrar resultados
eleicao.mostrar_resultados()
