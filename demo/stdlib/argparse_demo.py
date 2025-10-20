from argparse import ArgumentParser

p = ArgumentParser("Description")
p.add_argument("-d", type=str, default="oasis", help="Help Text")
args = p.parse_args()

print(args.d)
