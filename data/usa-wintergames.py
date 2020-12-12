import matplotlib.pyplot as plt


labels = ([1948, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,1988, 1992])

values = ([16, 26, 27, 8, 7, 25, 11, 30, 9, 7, 14])

plt.plot(labels, values, color = 'blue')

plt.title("Olympic medals won by USA during the Cold War", pad = 20)

plt.show()