def sumArray(numbers):
    ret = 0
    for x in numbers:
        ret += x
    return ret

def multiplyArray(numbers):
    ret = 1
    for x in numbers:
        ret = ret * x
    return ret

def main():
    numbers = []
    for x in range(5):
        numbers.append(int(input("Enter a number: ")))
    print(sumArray(numbers))
    print(multiplyArray(numbers))

#hello
if __name__ == "__main__":
    main()