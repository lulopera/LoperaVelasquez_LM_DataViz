import matplotlib.pyplot as plt


labels = (["SUI", "CAN", "TCH", "USA", "SWE", "NOR", "FIN", "AUT", "BEL","FRA", "GBR", "HUN", "ITA"])

values = ([28, 20, 17, 16, 13, 13, 9, 8, 6, 5, 2, 2,1])

plt.bar(labels, values, color = ['yellow', 'red', 'green', 'blue', 'red', 'purple', 'pink', 'lightblue', 'lightgreen', 'blue', 'green', 'yellow', 'orange'])

plt.title("Countries and medals in 1948 Winter Games")

plt.show()