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

print('\n')

def getTree(dir_path: Path, prefix: str='', ignore_files: list=ignore_files):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """    
    contents = [path for path in dir_path.iterdir() if path.name not in ignore_files]
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): 
            extension = branch if pointer == tee else space 
            yield from getTree(path, prefix=prefix+extension,ignore_files=ignore_files)

def formatTree(dir_path: Path, dsc_spacing: int=4, base_spacing: int=2):
    tree_contents = [line for line in getTree(Path().absolute())]
    max_string_length = max(tree_contents, key=len)
    tree_contents = [' '*base_spacing + line + ' '*int(dsc_spacing + len(max_string_length) - len(line)) + '<= DSC' for line in tree_contents]
    for i in tree_contents:
        print(i)


formatTree(Path().absolute())