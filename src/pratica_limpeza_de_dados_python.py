import pandas as pd
import seaborn as srn
import statistics as sts
import matplotlib.pyplot as plt

# Importar dados
dataset = pd.read_csv("tempo.csv", sep=";")

# Visualizar
print(dataset.head())

# Explorar dados categóricos
# Aparencia
agrupado_aparencia = dataset.groupby(['Aparencia']).size()
agrupado_aparencia.plot.bar(color='gray')
plt.title('Distribuição de Aparencia')
plt.show()

# Vento
agrupado_vento = dataset.groupby(['Vento']).size()
agrupado_vento.plot.bar(color='gray')
plt.title('Distribuição de Vento')
plt.show()

# Jogar
agrupado_jogar = dataset.groupby(['Jogar']).size()
agrupado_jogar.plot.bar(color='gray')
plt.title('Distribuição de Jogar')
plt.show()

# Explorar colunas numéricas
# Temperatura
print(dataset['Temperatura'].describe())

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
srn.boxplot(dataset['Temperatura']).set_title('Boxplot - Temperatura')
plt.subplot(1, 2, 2)
srn.histplot(dataset['Temperatura']).set_title('Histograma - Temperatura')
plt.show()

# Umidade
print(dataset['Umidade'].describe())

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
srn.boxplot(dataset['Umidade']).set_title('Boxplot - Umidade')
plt.subplot(1, 2, 2)
srn.histplot(dataset['Umidade']).set_title('Histograma - Umidade')
plt.show()

# Contar valores NaN
print(dataset.isnull().sum())

# Tratar valores inválidos em 'Aparencia'
agrupado_aparencia = dataset.groupby(['Aparencia']).size()
dataset.loc[dataset['Aparencia'] == 'menos', 'Aparencia'] = "Sol"
agrupado_aparencia = dataset.groupby(['Aparencia']).size()
print(agrupado_aparencia)

# Tratar valores fora do domínio em 'Temperatura'
print(dataset['Temperatura'].describe())
outliers_temperatura = dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)]
print(outliers_temperatura)

mediana_temperatura = sts.median(dataset['Temperatura'])
dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130), 'Temperatura'] = mediana_temperatura

print(dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)])

# Tratar 'Umidade': domínio e NaNs
agrupado_umidade = dataset.groupby(['Umidade']).size()
print(agrupado_umidade)

total_nas_umidade = dataset['Umidade'].isnull().sum()
print(f'Total de NaNs em Umidade: {total_nas_umidade}')

mediana_umidade = sts.median(dataset['Umidade'])
dataset['Umidade'].fillna(mediana_umidade, inplace=True)

print(dataset['Umidade'].isnull().sum())

print(dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)])

dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100), 'Umidade'] = mediana_umidade

print(dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)])

# Tratar 'Vento': NaNs
agrupado_vento = dataset.groupby(['Vento']).size()
print(agrupado_vento)

total_nas_vento = dataset['Vento'].isnull().sum()
print(f'Total de NaNs em Vento: {total_nas_vento}')

dataset['Vento'].fillna('FALSO', inplace=True)

print(dataset['Vento'].isnull().sum())

# Visualizar o resultado final do tratamento
print(dataset.head())
