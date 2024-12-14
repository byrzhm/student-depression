import matplotlib.pyplot as plt


def hist_plot(data, bins, title, xlabel, ylabel, figsize=(10, 6), color='lightblue', alpha=0.75):
    plt.figure(figsize=figsize)
    plt.hist(data, bins, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=alpha)
    plt.show()