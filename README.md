# Simple Python Package

This is a bare minimum structure of designing a python module 

## File Structure

```
$ tree
.
├── Makefile
└── src
    ├── __init__.py
    └── mymodule
        ├── __init__.py
        ├── __main__.py
        └── task.py
```

`mymodule` has the file `__main__.py`. This is the entry point to all the module functions defined in `task.py`. 

## Usage

From the directory `simplepyplg/`, run:

```py
 python -m src.mymodule --func fib2 --n 1000
 
 # output
 # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
 
 python -m src.mymodule --func fib --n 1000
 
 # output
 # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
```

**Bonus:** You can improve `__main__.py` such that it can accept `args` by reading `config.json`. 

To knore more on how python module works, please see this link:
1. [python module](https://keen-vegetarian-057.notion.site/Python-Advanced-Part-1-58791debe8544a0987c5ba72ab08301b)

Happy Coding !! ☘️

----

