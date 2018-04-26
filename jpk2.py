#! python3
from utils.files import get_full_path

with open('1.txt') as f:
    read_data = f.read()
    print(read_data)

for filename in os.listdir(input_dir):
    with open(filename, 'rb') as f:
        if filename.endswith(".gz"):
            f = gzip.open(fileobj=f)
        words = (line.split(delimiter) for line in f)
        ... my logic ...







path_to_map = get_full_path('res', 'map.png')
