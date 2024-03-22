import cowsay
import argparse


cowparser = argparse.ArgumentParser(prog="cow_say")
cowparser.add_argument("message", nargs="?")
cowparser.add_argument("-l", action="store_true")
cowargs = cowparser.parse_args()

if cowargs.l:
    print(cowsay.list_cows())
else:
    print(cowsay.cowsay(cowargs.message))
