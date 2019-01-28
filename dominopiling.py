# codeforces
def dominoPiling():
    m, n = map(int,input().strip().split())
    if not m or not n:
        return 0
    p = m * n
    dominos = p // 2
    return dominos


if __name__ == "__main__":
    print(dominoPiling())
