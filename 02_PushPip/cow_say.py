import cowsay
import argparse


cowparser = argparse.ArgumentParser(prog="cow_say")
cowparser.add_argument("message", nargs="?")
cowparser.add_argument("-e", "--eye_string", dest="eyes", default=cowsay.Option.eyes)
cowparser.add_argument("-f", "--cowfile")
cowparser.add_argument("-n", action="store_false", dest="wrap_text")
cowparser.add_argument("-T", "--tongue_string", dest="tongue", default=cowsay.Option.tongue)
cowparser.add_argument("-W", "--column", dest="width", default=40, type=int)
cowparser.add_argument("-bdgpstwy", dest="preset")
cowparser.add_argument("-l", action="store_true")
cowargs = cowparser.parse_args()

if cowargs.l:
    print(cowsay.list_cows())
else:
    print(cowsay.cowsay(cowargs.message, eyes=cowargs.eyes, cowfile=cowargs.cowfile, wrap_text=cowargs.wrap_text, tongue=cowargs.tongue, width=cowargs.width, preset=cowargs.preset))

