#19/03/2020
if __name__ == "__main__":
    count = int(input())
    s = set()
    for i in range(0,count):
        ans = input()
        s.add(ans)
    print(len(s))
