#En Python, la fonction exponentielle peut être calculée en utilisant la fonction math.exp(). Cette fonction prend un nombre réel en argument et renvoie l'exponentielle du nombre, c'est-à-dire e à la puissance de l'argument. Par exemple, pour calculer l'exponentielle de 2, on peut utiliser la syntaxe suivante :


import math

x = 2
result = math.exp(x)
print(result)  # affiche "7.38905609893065"

#Notez que e est une constante mathématique avec une valeur approchée de 2,71828. La fonction math.exp() est utile pour calculer des exponentielles de nombres réels, mais elle ne peut pas être utilisée pour calculer des exponentielles de nombres complexes. Pour ce faire, vous devrez utiliser une bibliothèque de calculs numériques telle que numpy.