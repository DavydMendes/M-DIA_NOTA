# Função para calcular a média do aluno
def calcular_media(nota1, nota2):
    """Recebe duas notas e retorna a média do aluno."""
    media = (nota1 + nota2) / 2
    return media


# Função para verificar a aprovação
def verificar_aprovacao(media):
    """Verifica se o aluno atingiu a média mínima 6.0."""
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


# Função para gerar o relatório
def gerar_relatorio(nome, nota1, nota2):
    """Calcula a média e exibe o relatório do aluno."""
    media = calcular_media(nota1, nota2)
    situacao = verificar_aprovacao(media)

    print("\n--- RELATÓRIO DO ALUNO ---")
    print("Nome:", nome)
    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Média:", media)
    print("Situação:", situacao)


# Dados de exemplo
nome = "João"
nota1 = 8.0
nota2 = 6.0

# Gera o relatório
gerar_relatorio(nome, nota1, nota2)