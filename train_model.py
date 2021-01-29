import numpy as np
from sklearn import model_selection, preprocessing, neighbors
import pandas as pd

df = pd.read_csv('./training_dataset.csv')

x = np.array(df['symptoms']).reshape((-1, 1))
y = np.array(df['prognosis'])

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

model = neighbors.KNeighborsClassifier()
model.fit(x_train, y_train)
score = model.score(x_test, y_test)

print(f"score = {score}")

import pickle
pickle.dump(model, open('model.bin', 'wb'))
