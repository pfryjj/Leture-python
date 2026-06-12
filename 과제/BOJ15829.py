def hash():
    s = input().strip()      

    r = 31
    M = 1234567891

    ans = 0
    for i in range(len(s)):
        ans = (ans + (ord(s[i]) - ord('a') + 1) * pow(r, i, M)) % M
    print(ans)
hash()