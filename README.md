# Análise de Vendas Integradas - Capstone Project (LojinhaTech)

Este projeto demonstra o domínio do ecossistema de dados do Python (Pandas e Matplotlib) ao simular a análise de desempenho de vendas de uma loja de e-commerce.

A aplicação realiza o ciclo completo da Análise Exploratória de Dados (EDA): Carregar → Limpar → Modelar → Analisar → Visualizar.

## ✨ Funcionalidades e Habilidades Demonstradas

- **Carregamento Multi-Fonte:** Lê simultaneamente dados de três ficheiros .csv distintos (`pedidos`, `clientes`, `produtos`).
- **Limpeza de Dados (Nível 2):** Aplica as técnicas de limpeza de dados mais comuns:
    - Uso de `.str.replace().astype(float)` para limpar strings de moeda e convertê-las para o tipo numérico (`float`).
    - Uso de `.fillna()` para preencher valores ausentes em colunas categóricas (`Regiao`) e numéricas.
- **Modelagem de Dados (pd.merge):**
    - Executa duas operações de junção (`pd.merge`) para ligar todas as informações (Produto + Pedido + Cliente) numa única tabela mestra.
    - Utiliza a junção à esquerda (`how='left'`) para garantir que todos os dados de RH sejam mantidos.
- **Análise e Agregação:**
    - Cria a métrica chave: `Valor_Total_Venda` (Preço * Quantidade).
    * Utiliza **`groupby().sum()`** para calcular o total de vendas por Região e por Produto.
    * Aplica o encadeamento **`.sort_values().head(5)`** para gerar o ranking dos Top 5 Clientes por valor gasto.
- **Visualização de Impacto:** Cria um gráfico de barras com `matplotlib` para exibir as vendas regionais, tornando os dados mais acessíveis a stakeholders não técnicos.

## ⚙️ Como Rodar o Projeto

1.  Certifique-se de que os três ficheiros (.csv) estão na mesma pasta que o script Python.
2.  Tenha as bibliotecas `pandas` e `matplotlib` instaladas e o ambiente virtual ativado.
3.  Execute o script: `python seu_arquivo_principal.py`
