import matplotlib.pyplot as plt


labels = (["SUI", "CAN", "FRG", "USA", "SWE", "NOR", "FIN", "NED", "GBR", "ITA"])

values = ([6, 20, 12, 30, 23, 19, 12, 3, 1, 2])

plt.bar(labels, values, color = ['yellow', 'red', 'green', 'blue', 'red', 'purple', 'pink', 'lightblue', 'lightgreen', 'blue'])

plt.title("Countries and medals in 1952 Winter Games")

plt.show()