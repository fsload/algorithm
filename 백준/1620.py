import sys

poke, toSolve = map(int, sys.stdin.readline().split())

dic1 = {}
dic2 = {}
for i in range(poke):
    mons = sys.stdin.readline().strip()
    dic1[i+1] = mons
    dic2[f'{mons}'] = i+1

for _ in range(toSolve):
    cmd = sys.stdin.readline().strip()
    if cmd.isdigit():
        print(dic1[int(cmd)])
    else:
        print(dic2[f'{cmd}'])
