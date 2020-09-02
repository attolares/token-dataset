
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt  
import pandas
import numpy as np

with open('f1.txt', 'r') as infile:
    true_values = infile.read()
    true_values = list(true_values)
with open('f2.txt', 'r') as infile:
    predictions = infile.read()
    predictions = list(predictions)

labels = ['a','b','c','t','e'] #PREENCHER COM O ALFABETO CORRESPONDENTE

cm = confusion_matrix(true_values, predictions, labels)

print(cm)


fig, ax = plt.subplots()
im = ax.imshow(cm)


ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

# labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# por o valor nas celulas
for i in range(len(labels)):
    for j in range(len(labels)):
        text = ax.text(j, i, cm[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Matriz")
fig.tight_layout()

plt.show()