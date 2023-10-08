import random
from lib import List, UndirectedGraph, DirectedGraph, Tree, String
import settings

for i in range(settings.num_testcase):
    # ToDo: make testcase
    n = random.randrange(1, 1000)
    arr = List.gen_list(n, 0, 10**5)

    # Save the testcase to input dir.
    filepath = f"{settings.input_dir}{i:04d}.txt"
    with open(filepath, mode="w", encoding="utf-8") as f:
        # ToDo: depends on testcase
        print(n, file=f)
        print(*arr, file=f)
