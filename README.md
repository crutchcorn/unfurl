# Unfurl

The concept of `unfurl`ing is to take all items from within a given tree and move them as far up the tree as possible.
```
folder
└───subfolder1
│   └───subfolder2
│   │   └───subfolder3
│   │   │   │   file.txt
│   │   │   └───subfolder4
│   │   │   │   │   file.txt
```

Should end up turning into something looking like using a respectful unful:

```
folder
│   file.txt
└───subfolder4
│   │   file.txt
```

Or, by using a non-respectful furl:

```
folder
│   file.txt
│   file.txt
```

## Installation

Because this program uses the [docopt](https://github.com/docopt/docopt) library, to use this program you have to install the library by running:
```
pip install docopt==0.6.2
```

## Usage

* `unfurl -h` or `unfurl --help`    - Show program help
* `unfurl -v` or `unfurl --version` - Show program version
* `unfurl -r` or `unfurl --respect` - Respect the tree structure
* `unfurl <folder>`                 - Unfurl everything in given folder only
    * *EG: unfurl asdf*

## Errors
Why does:
`Destination path 'C:\Users\user\folder\asdf' already exists`
Occur when there is no file/folder with the same name?
>Python does not see a difference between files and folders; therefore - it is impossible to move a file to a directory where a folder has the same name.