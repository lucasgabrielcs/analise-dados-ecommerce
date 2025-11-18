import matplotlib.pyplot as plt
import pandas as pd


df_produto = pd.read_csv("produtos.csv")
df_clientes = pd.read_csv("clientes.csv")
df_pedidos = pd.read_csv("pedidos.csv")

print("-----------------Produtos mais vendidos--------------------------")
df_produto["Preco_Unitario"] =df_produto['Preco_Unitario'].str.replace("R$ ", " ").astype(float)

df_prod_vend = pd.merge(df_produto,df_pedidos, on="ID_Produto")
total_vend = (df_prod_vend['Preco_Unitario'] * df_prod_vend["Quantidade"])

prod_vend = df_prod_vend.groupby("Nome_Produto")["Quantidade"].sum()
print(prod_vend)
print("--------------------------Tabela Geral com Total de Vendas--------------------")
df_prod_vend = df_prod_vend.dropna()
df_prod_vend["Valor_Total_Venda"] = (total_vend)


print(df_prod_vend)

print("---------------------Qual Região Compra mais---------------------")

df_client_ped = pd.merge(df_clientes, df_prod_vend, on="ID_Cliente")
df_client_ped["Regiao"] = df_client_ped["Regiao"].fillna("Desconhecido")
venda_regiao = df_client_ped.groupby("Regiao")["Valor_Total_Venda"].sum()
print(venda_regiao)

print("--------------------------------------LIsta TOTAL--------------------------------")
print(df_client_ped)
print("---------------------Nossos Top 5 Clientes--------------------------")

top_5 = df_client_ped.groupby("Nome_Cliente")["Valor_Total_Venda"].sum()

top_5_final = top_5.sort_values(ascending=False).head(5)

print(top_5_final)

print("===================VISUALIZAÇÃO============================")

venda_regiao.plot(kind="bar")
plt.title("Vendas Por Região")
plt.ylabel("Valor Total Gasto em R$")
plt.xlabel("Regiões")



plt.figure()
top_5_final.plot(kind="bar")
plt.title("Top 5 Clientes")
plt.ylabel("Valor Gasto")
plt.xlabel("Nome dos Clientes")
plt.show()