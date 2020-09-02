from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt  
import pandas

with open('f1.txt', 'r') as infile:
    true_values = infile.read()
    true_values = list(true_values)
with open('f2.txt', 'r') as infile:
    predictions = infile.read()
    predictions = list(predictions)

labels = ['l','a','r','i','s','g','o','m','e','0']

cm = confusion_matrix(true_values, predictions, labels)

print(cm)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()