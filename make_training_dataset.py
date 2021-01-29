import pandas as pd

training_dataset = pd.read_csv('./datasets/disease-prediction-using-machine-learning/Training.csv')
symptoms_list = []
dataset = {'symptoms': [], 'prognosis': []}

with open('list.txt') as f:
    lines = f.readlines()
    for line in lines:
        symptoms_list.append(line.strip())


for index, row in training_dataset.iterrows():
    symptoms = 0
    for sym in symptoms_list:
        symptoms = symptoms | (int(row[sym]) << symptoms_list.index(sym))

    dataset['symptoms'].append(symptoms)
    dataset['prognosis'].append(row['prognosis'])

new_training_df = pd.DataFrame(dataset)
new_training_df.to_csv('training_dataset.csv')
