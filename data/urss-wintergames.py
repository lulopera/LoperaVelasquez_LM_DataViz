import matplotlib.pyplot as plt


labels = ([1948, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,1988, 1992])

values = ([0, 37, 42, 46, 37, 45, 56, 54, 56, 67, 0])

plt.plot(labels, values, color = 'red')

plt.title("Olympic medals won by URS during the Cold War", pad = 20)

plt.show()