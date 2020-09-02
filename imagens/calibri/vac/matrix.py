from sklearn.metrics import confusion_matrix

# Read the data
with open('out1.txt', 'r') as infile:
    true_values = [str(i) for i in infile]
with open('gt1.txt', 'r') as infile:
    predictions = [str(i) for i in infile]

# Make confusion matrix
confusion = confusion_matrix(true_values, predictions)

print(confusion)