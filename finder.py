with open('spool-teste.txt', 'r') as infile:
    true_values = infile.readlines()
with open('detectado.txt', 'r') as infile:
    predictions = infile.readlines()


for i in range(len(true_values)):
    if(len(true_values[i]) != len(predictions[i])):
        print(i)
