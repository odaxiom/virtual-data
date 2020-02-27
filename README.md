# Vdata
This package aims to provide an abstraction about the management of any types of data : boolean, int, float, string, array, dict, json, file, ... .

Principles :
- never lose data
- historic of any data
- simple calling


## Quickstart
```
git clone https://github.com/odaxiom/vdata
cd vdata
pip install .
```

## Starting examples
```python
from vdata import Data


# instantiate some variables
a = 42
b = 43

# instantiate a virtual data
meaning_of_life = Data(name='meaning_of_life', namespace='raw')

meaning_of_life.update(data=a) # this will create a pickle in ./.data/raw/meaning_of_life.0.vdata

del a
assert meaning_of_life.get() == 42 # we are able to retrieve the previous variable

# update with another variable value
meaning_of_life.update(data=43) # this will create a pickle in ./.data/raw/meaning_of_life.1.vdata

assert meaning_of_life.get() == 43
assert meaning_of_life.get(revision='latest') == 43
assert meaning_of_life.get(revision=1) == 43
assert meaning_of_life.get(revision=0) == 42
```

## Advanced examples
### Machine learning
```python
import random
from vdata import Data

from sklearn.ensemble import RandomForestRegressor


dataset_X = Data(name='dataset_X', namespace='raw')
dataset_y = Data(name='dataset_y', namespace='raw')
data_model = Data(name='my_model', namespace='models')
prediction = Data(name='prediction', namespace='metrics')


X = [random.randint(0, 100) for _ in range(0, 1000)]
y = [x * 2 for x in X]

dataset_X.update(data=X)
dataset_y.update(data=y)

model = RandomForestRegressor()
model.fit(dataset_X.get(), dataset_y.get())

data_model.update(data=model)

del model
model = data_model.get()

x = [5]
p = model.predict(x)

prediction.update({'x': x, 'predicted': p})
```

This system will reach its full potential when data will be saved online ;-)

## Todo
- [ ] Able to update the default PATH = 'data'
- [ ] Add version with GCP Bucket
- [ ] Add version with Amazon Bucket
