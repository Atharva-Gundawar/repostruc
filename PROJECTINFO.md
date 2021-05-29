# REPOSTRUC

>`repostruc` is a cross-platform library that returns the directory structure in a formated form. The structure can be copied to your clipboard or a .md file can be made available.[`.md example`](PROJECTINFO.md)

## File Structure

```markdown
  ├── .gitignore            <- Gitignore file
  ├── LICENSE               <- MIT LICENSE
  ├── Pipfile               <- Pipfile
  ├── PROJECTINFO.md        <- PROJECTINFO 
  ├── README.md             <- README
  ├── repostruc             <- Main folder
  │   ├── argHandler.py     <- Handles arguments
  │   ├── repostruc.py      <- Main file
  │   ├── returnUtils.py    <- Handles return types
  │   ├── treeUtils.py      <- Hanldes tree functions
  │   └── __init__.py       <- __init__.py
  ├── requirements.txt      <- requirements
  └── setup.py              <- setup for [pypi](https://pypi.org/project/repostruc/)

```

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
