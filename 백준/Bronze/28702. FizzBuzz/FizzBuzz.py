# 최대 길이: 100만
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz,
# 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz
# --> 위  패턴 반복, 숫자가 아닌 문자열이 세 개 연속으로 등장하는 경우는 없다. --> 최소 하나의 숫자는 등장, 그 숫자를 활용하기

arr = [input() for _ in range(3)]


def fizzbuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0) and (num % 5 != 0):
        return "Fizz"
    elif (num % 3 != 0) and (num % 5 == 0):
        return "Buzz"
    else:
        return num


for i in range(len(arr)):
    if arr[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        answer = int(arr[i]) + (3 - i)
        print(fizzbuzz(answer))
        break