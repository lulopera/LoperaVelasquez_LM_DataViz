import matplotlib.pyplot as plt



labels = (["URS", "USA", "CAN", "SWE", "FIN", "AUT", "SUI", "ITA", "NOR","HUN", "EUA", "JAP", "POL"])

values = ([37, 26, 20, 15, 12, 12, 10, 8, 4, 2, 2, 1, 1])

plt.bar(labels, values, color = ['blue', 'red', 'purple', 'red', 'pink', 'blue', 'yellow', 'green', 'purple', 'orange', 'lightblue', 'red', 'lightgreen'])

plt.title("Countries and medals in 1956 Winter Games")

plt.show()