import pandas as pd

training_dataset = pd.read_csv('./datasets/disease-prediction-using-machine-learning/Training.csv')
symptoms_list = []
diseases_list = []
with open('disease_list.txt') as f:
    lines = f.readlines()
    for line in lines:
        diseases_list.append(line.strip())

dataset = {'symptoms': [], 'prognosis': []}

with open('symptoms_list.txt') as f:
    lines = f.readlines()
    for line in lines:
        symptoms_list.append(line.strip())


for index, row in training_dataset.iterrows():
    symptoms = 0
    for sym in symptoms_list:
        symptoms = symptoms | (int(row[sym]) << symptoms_list.index(sym))

    dataset['symptoms'].append(symptoms)
    dataset['prognosis'].append(diseases_list.index(row['prognosis'].strip().lower().replace(' ', '_')))

new_training_df = pd.DataFrame(dataset)
new_training_df.to_csv('training_dataset.csv')
