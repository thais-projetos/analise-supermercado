import pandas as pd
import matplotlib.pyplot as plt

# Dados de estoque do supermercado
dados_estoque = {
    'Produto': ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Óleo', 'Leite', 'Pão', 'Café', 'Sabão', 'Detergente',
                'Shampoo', 'Condicionador', 'Sabonete', 'Creme Hidratante'],
    'Categoria': ['Grãos', 'Grãos', 'Massas', 'Açúcar', 'Óleo', 'Laticínios', 'Padaria', 'Bebidas', 'Limpeza', 'Limpeza',
                  'Beleza', 'Beleza', 'Beleza', 'Beleza'],
    'Quantidade': [150, 100, 80, 90, 60, 120, 70, 110, 40, 50,
                   30, 25, 45, 20]
}

estoque = pd.DataFrame(dados_estoque)

# Exibindo o DataFrame
print(estoque)

# Agrupar estoque por categoria para gráfico de pizza
estoque_categoria = estoque.groupby('Categoria')['Quantidade'].sum()

# Criar gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(estoque_categoria, labels=estoque_categoria.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribuição do Estoque por Categoria no Supermercado')
plt.axis('equal')  # Para garantir que o gráfico fique circular
plt.show()
