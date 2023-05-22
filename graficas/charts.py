import matplotlib.pyplot

def generar_pie_chart():
    labels = ["A", 'B', 'C']
    values = [123, 78, 94]

    fig, ax = matplotlib.pyplot.subplots()
    ax.pie(values, labels=labels)
    matplotlib.pyplot.savefig("grafica.png")
    matplotlib.pyplot.close()