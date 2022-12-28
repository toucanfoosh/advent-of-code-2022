import sys

def get_sum(stack):
    out = 0
    while (len(stack) > 0):
        out += stack.pop()
    return out

def get_largest(stack):
    max = -1
    while(len(stack) > 0):
        val = stack.pop()
        if val > max:
            max = val
    return max

def remove_new_line(file_name):
    with open(file_name) as f:
        for line in f:
            line = line.strip()
    return line

def main():
    with open("1/1-dataset.txt", "r") as lines:
        lines = [i.strip() for i in lines.readlines()]
        x = [[int(num) for num in i.split()] for i in lines]
    arr = []
    stack = []
    x = 0
    for i in lines:
        if i == "":
            arr.append(get_sum(stack))
            stack = []
            x = 0
        else:
            stack.append(int(i))
            x += 1
    print(get_largest(arr))

if __name__ == "__main__":
    main()