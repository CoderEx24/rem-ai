with open('./datasets/disease-prediction-using-machine-learning/Training.csv', 'r') as f:
    line = f.readline()
    symptoms = line.split(',')[:-2]
    list_file = open('list.txt', 'w')
    for symptom in symptoms:
        list_file.write(f'{symptom}\n')
    list_file.flush()
    list_file.close()
