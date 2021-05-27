from __init__ import __version__ as version
import sys
from docopt import docopt

sys.dont_write_bytecode = True

class GetArgumentParser:
   
    """
    Argument Parser class for repostruc:
    
    @functions
    __init__     => Initializes docopt
    getArguments => Returns docopt
    
    """

    def __init__(self):
        """
        Initializes Usage of arguments for Docopt

        """
        doc = """repostruc.

                Usage:
                    main.py 
                    main.py (-c | --clip)
                    main.py (-r | --readme) <filepath>
                    main.py (-h | --help)
                    main.py --version
                
                Options:
                    -r --readme   Add to readme file.
                    -c --clip     Copy to clipboard.
                    --version     Show version.

                """
        self.doc = doc
        self.version = version
        self.name = "repostruc"

    def getArguments(self):
        """
        Initializes Docopt.

        @return
        Docopt object for Argument Parsing 
        """
        return docopt(self.doc, version=f'{self.name}_{self.version}')


if __name__ == '__main__':
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    print(arguments)
