import make_sandwiches

make_sandwiches.make_sandwich('butter', 'sardine')
make_sandwiches.make_sandwich('jam', 'peanut butter')
make_sandwiches.make_sandwich('tomato', 'lettuce', 'tofu')

from make_sandwiches import make_sandwich
make_sandwich('avocado', 'spinach', 'mayo')

from make_sandwiches import make_sandwich as ms
ms('turkey', 'bacon', 'lettuce', 'tomato', 'mayo')

import make_sandwiches as ms
ms.make_sandwich('ham', 'cheese', 'mustard')

from make_sandwiches import *
make_sandwich('roast beef', 'horseradish', 'lettuce', 'tomato')
