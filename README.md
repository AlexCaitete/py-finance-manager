# 💰 PyFinance Manager

Aplicação de linha de comando (CLI) desenvolvida em **Python** para controle de fluxo de caixa pessoal. O sistema foca na **persistência de dados**, garantindo que as informações sejam salvas em disco e não se percam ao fechar o programa.

## 🚀 Funcionalidades

O sistema implementa operações essenciais de gestão de dados (CRUD):

* **Registrar Transações:** Entrada validada de Receitas e Despesas.
* **Persistência em Arquivo:** Uso da biblioteca `csv` para salvar dados automaticamente em um arquivo local (`financas.csv`).
* **Cálculo de Saldo:** Leitura e processamento do arquivo para gerar balanço financeiro em tempo real.
* **Exclusão de Registros:** Funcionalidade que permite remover transações específicas, reescrevendo a base de dados de forma segura.
* **Interface Limpa:** Comandos de limpeza de terminal para melhor experiência do usuário (UX).

## 🛠️ Tecnologias e Conceitos

* **Linguagem:** Python 3
* **Manipulação de Arquivos (File I/O):** Leitura (`r`), Escrita (`w`) e Anexação (`a`) de arquivos.
* **Biblioteca CSV:** Uso de `DictReader` e `DictWriter` para manipulação estruturada de dados.
* **Tratamento de Exceções:** Blocos `try/except` para blindar o input do usuário contra erros de digitação.
* **Modularização:** Código organizado em funções com responsabilidade única.

## 💻 Como executar

Certifique-se de ter o Python instalado.

1. Clone o repositório:
```bash
git clone [https://github.com/AlexCaitete/py-finance-manager.git](https://github.com/AlexCaitete/py-finance-manager.git)
