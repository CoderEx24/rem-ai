with open('./datasets/disease-prediction-using-machine-learning/Training.csv', 'r') as f:
    line = f.readline()
    symptoms = line.split(',')[:-2]
    list_file = open('symptoms_list.txt', 'w')
    for symptom in symptoms:
        list_file.write(f'{symptom}\n')
    list_file.flush()
    list_file.close()
    diseases = []
    for line in f.readlines():
        disease = line.split(',')[-2]
        disease = disease.lower().strip().replace(' ', '_')
        diseases.append(disease)
    diseases = set(diseases)
    list_file = open('disease_list.txt', 'w')
    for disease in diseases:
        list_file.write(f"{disease}\n")
    list_file.flush()
    list_file.close()
