# 變數
a = "Hello World!"
b = c = a
print(f"{a}\t{b}\t{c}")
d, e, f = 1, 2, 3
print(f"{d}\t{e}\t{f}")
g = [1]
h = g
g.append(0)
print(f"{g}\t{h}")


def func1():
    g.append(-1)
    h = [-1, 0, 1]
    print(f"{g}\t{h}")


def func2():
    print(f"{g}\t{h}")


func1()
func2()

g = [0, 1, 2]
print(f"{g}\t{h}")
d, e, f = f, e, d
print(f"{d}\t{e}\t{f}")
