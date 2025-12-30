import sys 
sys.path.append("../")
from utils import clean_ranges

input_file = "data.in" if len(sys.argv) == 1 else "test.in" if len(sys.argv[1]) == 1 else sys.argv[1]

with open(input_file) as f:
	inp = f.read().strip()
	ranges, food = inp.split("\n\n")

ranges = ranges.splitlines()
ranges = [x.split("-") for x in ranges]
ranges = [(int(a), int(b)) for a, b in ranges]

food = food.splitlines()
food = [int(x) for x in food]

cleaned_ranges = clean_ranges(ranges, debug = True)

counts = 0
for a, b in cleaned_ranges: 
	counts += b - a + 1	


print(counts)