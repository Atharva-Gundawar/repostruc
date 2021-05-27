from pathlib import Path
import os
import pyperclip



# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '
# files to ignore:
ignore_files = ['.git']

print('\n')

class TreeHandler(object):

    @staticmethod
    def getTree(dir_path: Path, prefix: str='', ignore_files: list=ignore_files):
        """
        A recursive generator function,
        which yeilds a visual tree structure line by line.

        @param dir_path: Path object of targeted directory 
        @param prefix: Prefix for every level of the tree structure 
        @param ignore_files: Files and directories to ignore

        """    
        contents = [path for path in dir_path.iterdir() if path.name not in ignore_files]
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            yield prefix + pointer + path.name
            if path.is_dir(): 
                extension = branch if pointer == tee else space 
                yield from TreeHandler.getTree(path, prefix=prefix+extension,ignore_files=ignore_files)

    @staticmethod
    def formatTree(dir_path: Path, dsc_spacing: int=4, base_spacing: int=2):
        """
        Adds spacing before and after every file.

        @param dir_path: Path object of targeted directory.
        @param dsc_spacing: Spacing between file and discription.
        @param base_spacing: Spacing before file. 

        """
        tree_contents = [line for line in getTree(Path().absolute())]
        max_string_length = max(tree_contents, key=len)
        tree_contents = [' '*base_spacing + line + ' '*int(dsc_spacing + len(max_string_length) - len(line)) + '<= DSC' for line in tree_contents]
        for i in tree_contents:
            print(i)
        TreeHandler.copyToClipboard(tree_contents)

    @staticmethod
    def copyToClipboard(tree_contents: list):
        """
        Saves Tree contents to clipboard.

        @param tree_contents: List object containing tree contents.
        """
        text = '\n'.join(map(str, tree_contents))
        pyperclip.copy(text)

    formatTree(Path().absolute())
