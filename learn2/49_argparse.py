import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow")
args= parser.parse_args()
#w linijce 3 wartość default jest potrezbna bo inaczej bez podania arguentu n- program scrashuje
for _ in range(int(args.n)):
    print("meow")