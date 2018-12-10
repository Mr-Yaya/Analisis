from functions import *
from datos import *

data = dataTest
print(data)

print([select(data, i) for i in range(10)])
print([rec_select(data, i,0,9) for i in range(10)])