def task1(x,y):
    x = int(input())
    y = int(input())
    print ((x + y) ** 2)

def task2(string):
    string = input()
    print (sum(letter.isupper() for letter in string))

def task3(string):
    string = input().split()
    bus = 0
    for word in string:
        if word[-3::] == "bus":
            bus += 1
    print(bus)

def task4(generator):
    return list(filter(lambda x: ("usu" not in x), generator))

def task5(list_of_smth):
    array1 = list(input().split())
    array2 = []
    for i in range(3, len(array1) - 2, 2):  # потому что до предпоследнего!
        array2.append(array1[i])
    print(*array2[::-1])

def task6(list1, list2, list3, list4):
    set1 = set(input().split())
    set2 = set(input().split())
    set3 = set(input().split())
    set4 = set(input().split())

    set1 |= set1.union(set4)
    set2 |= set2.union(set3)
    print(set1 & set2)

def task7():
    import numpy as np

    np.random.seed(1)
    arr = np.random.randint(36, size=36)
    arr = arr.reshape(6, 6)
    arr = arr[np.array([0, 1, 2, 3, 5])[:, np.newaxis], np.array([1, 2, 3, 4, 5])]
    print(arr, np.linalg.det(arr))

def task8(f, min_x, max_x, N, min_y, max_y):
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    x = np.linspace(min_x, max_x, N)
    y = f(x)

    plt.ylim([min_y, max_y])
    plt.yscale('log')
    plt.grid(True, linestyle="--")
    plt.plot(x, y, "--g", linewidth=1)
    plt.plot("--b", linewidth=1)  # derivative
    plt.show()

    plt.savefig('function.png')

def task9(data, x_array, y_array, threshold):
    # TODO: ...

def task10(list_of_smth, n):
    array2 = []
    m = 0
    n = len(list_of_smth)

    for i in range(n - 1):
        for j in range(i + 1, n):
            m += list_of_smth[j]
        array2.append(m / (n - 1 - i))
        m = 0
    array2.append(list_of_smth[n - 1])
    print(*array2)

def task11(filename="infile.csv"):
    df = pd.DataFrame({filename})
    x = pd.isnull(df["x"]).count()
    y = pd.isnull(df["y"]).count()
    x_err = pd.isnull(df["x_err"]).count()
    y_err = pd.isnull(df["y_err"]).count()
    print(bool(x), bool(y), bool(x_err), bool(y_err))

    df["x"] = df["x"].fillna(df["x"].mean())
    df["x_err"] = df["x_err"].fillna(df["x_err"].mean())

def task12(filename="video-games.csv"):
    # TODO: ...
