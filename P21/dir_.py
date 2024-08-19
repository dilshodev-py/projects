from pathlib import Path
from os.path import join

BASE_PATH = Path(__file__).parent

DATABASE_PATH = join(BASE_PATH , 'dir1' , 'test' , 'database')
print(DATABASE_PATH)



