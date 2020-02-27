import numpy as np
import random
from vdata import Data

from sklearn.ensemble import RandomForestRegressor


dataset_X = Data(name='dataset_X', namespace='raw')
dataset_y = Data(name='dataset_y', namespace='raw')
data_model = Data(name='my_model', namespace='models')
prediction = Data(name='prediction', namespace='metrics')


X = np.array([random.randint(0, 100) for _ in range(0, 1000)])
X = X.reshape(-1, 1)
y = [x * 2 for x in X]

dataset_X.update(data=X)
dataset_y.update(data=y)

model = RandomForestRegressor()
model.fit(dataset_X.get(), dataset_y.get())

data_model.update(data=model)

del model
model = data_model.get()

x = [[5]]
p = model.predict(x)

prediction.update({'x': x, 'predicted': p})

print(x)
print(p)
