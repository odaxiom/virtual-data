from vdata import Data
import time


N = 50_000
SUM_UPDATE = 0
SUM_GET = 0

# instantiate a virtual data
variable = Data(name='variable', namespace='raw')

for i in range(N):
    t1 = time.time()
    variable.update(data=i)
    t2 = time.time()

    delta = t2 - t1
    SUM_UPDATE += delta

for i in range(N):
    t1 = time.time()
    a = variable.get(revision=i)
    t2 = time.time()

    delta = t2 - t1
    SUM_GET += delta


print(SUM_UPDATE)
print(SUM_GET)

print(SUM_UPDATE / N)
print(SUM_GET / N)
