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

## Examples
```python
from vdata import Data

meaning_of_life = Data(name='meaning_of_life', namespace='raw')
a = 42

meaning_of_life.update(data=a) # this will create a pickle in ./.data/raw/meaning_of_life.0.vdata

del a
assert meaning_of_life.get() == 42

b = 43
meaning_of_life.update(data=43)

assert meaning_of_life.get() == 43
assert meaning_of_life.get(revision='latest') == 43
assert meaning_of_life.get(revision=1) == 43
assert meaning_of_life.get(revision=0) == 42
```

## Todo
- [ ] Able to update the default PATH = 'data'
- [ ] Add version with GCP Bucket
- [ ] Add version with Amazon Bucket
