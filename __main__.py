# Fibonacci numbers module
import argparse 
from src.mymodule.task import fib, fib2

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--func")
    parser.add_argument("--n")
    args, _ = parser.parse_known_args()

    if args.func == "fib":
        fib(int(args.n))
    
    if args.func == "fib2":
        fib2(int(args.n))