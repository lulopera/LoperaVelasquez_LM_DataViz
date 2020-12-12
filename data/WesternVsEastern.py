import matplotlib.pyplot as plt



values = [764, 810]
colors = ['purple', 'green']

labels = ["EASTERN BLOCK", "WESTERN BLOCK"]

explode = [0, 0.1]

plt.title("Eastern Bloc Vs Western Bloc at the Winter Games during the Cold War", pad="20")

plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()