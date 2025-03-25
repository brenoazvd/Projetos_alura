import pandas as pd

dados_creditcard = pd.read_csv('arvores_decisao/creditcard.csv')

#print(dados_creditcard.head())  # mostra as primeiras 5 linhas

n_transacoes = dados_creditcard['Class'].count()
n_fraudes = dados_creditcard['Class'].sum() #Faz a contagem do número total de transações realizadas
n_normais = n_transacoes - n_fraudes
fraudes_porc = n_fraudes / n_transacoes
normais_porc = n_normais / n_transacoes


print('Número de transações: ', n_transacoes)
print('Número de fraudes: ', n_fraudes, "%.2f" %(fraudes_porc*100))
print('Número de transações normais: ', n_normais, "%.2f" %(normais_porc*100))
#O que foi feito acima é apenas uma analise dos dados, onde nos trás o num. de transações, fraudes e transações normais

#-------------------------------------

X = dados_creditcard.drop('Class', axis=1).values
y = dados_creditcard['Class'].values

from sklearn.model_selection import StratifiedShuffleSplit

# Divisor de conjuntos
validador = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=0)


#É feita a separação dos dados testes(90%) e treinos(10%)
for treino_id, teste_id in validador.split(X, y): 
    X_train, X_test = X[treino_id], X[teste_id]
    y_train, y_test = y[treino_id], y[teste_id]

from sklearn import tree
classificador_arvore_decisao = tree.DecisionTreeClassifier()
arvore = classificador_arvore_decisao.fit(X_train, y_train)
y_pred = arvore.predict(X_test)