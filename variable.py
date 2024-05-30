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
i, j = 0, 1
i = j
j = i + j
print(f"{i}\t{j}")
k = (1,)
l = ('k',)
m, = k
n, = l
print(f"{k}\t{l}\t{m}\t{n}")


# 變數(全域, 區域)
def func3():
    i = 3
    print(f"{i}\t{j}")


func3()


def func4():
    print(i + 1)


func4()
print(i)


def func5():
    global i
    i = 0


print(i)
func5()
print(i)


def func6():
    global h
    h = [2, 1, 0]


print(f"{h}")
func6()
print(f"{h}")


def func7():
    i = 0
    print(locals())
    print(globals())


func7()
print(f"{i}")
print(locals())
