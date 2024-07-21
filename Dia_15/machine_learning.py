import pandas as pd
import numpy as np
import matplotlib.pylot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import tree

#Columnas 1, Filas 0
X = df.drop('Sobreviviente', axis=1)
y = df['Sobreviviente']
X.head()
y.head()

clf = DecisionTreeClassifier(max_depth=2, random_state=42)
clf.fit(X,y)
#Predecimos sobre el set
pred_y = clf.predict(X);
#Comparacion con las etiquetas reales
print('Precision: ',accuracy_score(pred_y,y))
#Creacion de una matriz de confusion
confusion_matrix(y,pred_y)
#Creacion de un grafico para la matriz
graficMatrix = ConfusionMatrixDisplay.from_estimator(clf,X,y,cmap=plt.cm.Blues,values_format='.0f')
graficMatrix.plot()
plt.show()

#Creacion del grafico con los valores normalizados (mas precisos con decimales)
graficMatrix = ConfusionMatrixDisplay.from_estimator(clf,X,y,cmap=plt.cm.Blues,values_format='.2f',normalize='true')
graficMatrix.plot()
plt.show()
#Mostrar el arbol que uso para la toma de decisiones
plt.figure(figsize=(10,8))
tree.plot_tree(clf,filled=True,feature_names=X.columns)
plt.show()
#Graficar el grado de importancia de cada atributo de los datos
importancias = clf.feature_importances_
columnas = X.columns

sns.barplot(x=importancias,y=columnas)
plt.title("Grado de Importancia de cada atributo")
plt.show()