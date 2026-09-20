def isperfect_number(n: int) -> bool:
    if n < 0:
        return False

    res = 0
    for i in range(1, n):
        if n % i == 0:
            res += i

    return True if res == n else False

print(isperfect_number(28))