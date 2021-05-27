from pathlib import Path
import os



# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '
# files to ignore:
ignore_files = ['.git']


def getTree(dir_path: Path, prefix: str='', ignore_files: list=ignore_files):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """    
    contents = [path for path in dir_path.iterdir() if path.stem not in ignore_files]
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): 
            extension = branch if pointer == tee else space 
            yield from getTree(path, prefix=prefix+extension,ignore_files=ignore_files)

for line in getTree(Path().absolute()):
    print(line)