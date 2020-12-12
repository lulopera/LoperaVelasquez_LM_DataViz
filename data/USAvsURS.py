import matplotlib.pyplot as plt

#generate a pie chart with our Olympic data

values = [422, 169]
colors = ['red', 'blue']

labels = ["URS", "USA"]

explode = [0, 0.1]

plt.title("Soviet Union Vs  United States of America at the Winter Games during the Cold War", pad="20")

plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()