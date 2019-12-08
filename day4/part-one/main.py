from collections import Counter

def check_num(num):
    if num != sorted(num): return False
    counts = Counter(num)
    for value in counts.values():
        if value >= 2: return True
    return False

def possible_passwords(min, max):
    count = 0
    for i in range(min, max):
        if check_num(str(i)):
            count += 1
    return count

if __name__ == "__main__":
    print(possible_passwords(158126,624574))