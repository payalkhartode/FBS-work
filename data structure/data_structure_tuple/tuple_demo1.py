
tu = (10, 20, 30, 40)

tu = (10,)

tu = (10, 20, 30,'abc', 3.14, 10)


print(tu)


## ordered
## Immutable
## faster than list

print(type(tu))
print(tu)

import sys
print(sys.getsizeof(tu))

