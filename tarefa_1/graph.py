import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Aracaju', 'Belo Horizonte', 'Boa Vista', 'Campo Grande', 'Curitiba', 'São Luis', 'São Paulo', 'Rio Branco', 'Cuiabá', 'Porto Alegre']
oleo_diesel = [6.24, 5.68, 6.64, 5.8, 5.69, 5.3, 5.8, 7.11, 5.92, 5.96]
oleo_diesel_s10 = [5.92, 5.81, 6.68, 5.96, 5.96, 5.48, 6.07, 7.18, 5.94, 5.92]


x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots()
fig.set_size_inches(14, 8)
fig.set_dpi(100)

rects1 = ax.bar(x - width/2 - 0.05, oleo_diesel, width, label='Óleo Diesel', color='#30b8d1')
rects2 = ax.bar(x + width/2 + 0.05, oleo_diesel_s10, width, label='Óleo Diesel S10', color='#ed5858')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Preço (R$)')
ax.set_title('Comparação do Preço de Revenda Médio de Combustíveis Entre Capitais Brasileiras')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('R${}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout(pad=1)

plot_filename = './plot.svg'
plt.savefig(plot_filename, dpi=100)
plt.close()