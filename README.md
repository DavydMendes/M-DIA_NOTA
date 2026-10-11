Markdown
# 📚 Sistema de Gestão de Notas Escolares

> **Disciplina:** Desenvolvimento de Sistemas — Agenda 10  
> **Estudante:** David Mendes Santos  
> **Linguagem:** Python 3  

---

## 🎯 Sobre o Projeto

Este projeto consiste na automação do cálculo de notas e verificação do status de aprovação de alunos de uma instituição de ensino. O objetivo principal é demonstrar a estruturação modular do código através de **funções** e **procedimentos**, aplicando o conceito de **separação de responsabilidades** (*Single Responsibility Principle*).

---

## 🛠️ Estrutura do Código

O programa é dividido em três funções principais:

| Função | Tipo | Descrição / Responsabilidade |
| :--- | :--- | :--- |
| `calcular_media(nota1, nota2)` | **Função** | Recebe duas notas e retorna a média aritmética simples. |
| `verificar_aprovacao(media)` | **Função** | Avalia a média recebida e retorna `"Aprovado"` ou `"Reprovado"` (média mínima: 6,0). |
| `gerar_relatorio(nome, nota1, nota2)` | **Procedimento** | Integra os cálculos e exibe o relatório consolidado formatado no terminal. |

---

## 💻 Código-Fonte (`sistema_notas.py`)

```python
# ==========================================
# SISTEMA DE GESTÃO DE NOTAS ESCOLARES
# Autor: David Mendes Santos
# ==========================================

# Função para calcular a média do aluno
def calcular_media(nota1, nota2):
    """Calcula a média aritmética de duas notas."""
    media = (nota1 + nota2) / 2
    return media


# Função para verificar a aprovação
def verificar_aprovacao(media):
    """Verifica a situação do aluno com base na média (mínima 6.0)."""
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


# Função para gerar o relatório do aluno
def gerar_relatorio(nome, nota1, nota2):
    """Calcula a média, verifica a situação e exibe o relatório."""
    media = calcular_media(nota1, nota2)
    situacao = verificar_aprovacao(media)

    print("\n--- RELATÓRIO DO ALUNO ---")
    print("Nome:", nome)
    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Média:", media)
    print("Situação:", situacao)


# Execução do programa com dados de teste
if __name__ == "__main__":
    nome = "João"
    nota1 = 8.0
    nota2 = 6.0

    gerar_relatorio(nome, nota1, nota2)