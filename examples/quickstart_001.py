from vdata import Data


# instantiate some variables
a = 42
b = 43

# instantiate a virtual data
meaning_of_life = Data(name='meaning_of_life', namespace='raw')

meaning_of_life.update(data=a) # this will create a pickle in ./.vdata/raw/meaning_of_life.0.vdata

del a
assert meaning_of_life.get() == 42 # we are able to retrieve the previous variable

# update with another variable value
meaning_of_life.update(data=43) # this will create a pickle in ./.vdata/raw/meaning_of_life.1.vdata

assert meaning_of_life.get() == 43
assert meaning_of_life.get(revision='latest') == 43
assert meaning_of_life.get(revision=1) == 43
assert meaning_of_life.get(revision=0) == 42
