def load(filename):
    with open(filename) as f:
        l = f.readlines()
    entries = [x.split() for x in l[1:]]
    entries = [(x[0], set(x[2:])) for x in entries]

load('dataset/a_example.txt')
