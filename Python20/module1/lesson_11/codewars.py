# def noonerize(numbers):
#
#     for i in numbers:
#         if not str(i).isdigit():
#             return "invalid array"
#     num1 , num2 = map(str , numbers)
#     result = abs(int(num2[0]+num1[1:]) - int(num1[0]+num2[1:]))
#     return result
#
#
# print(noonerize([120, "120"]))


# def sort_grades(lst):
#
#
#     lst = sorted(lst , key=lambda x  : int(x[1:]) if x[1:].isdigit() else -1 if x[1:].isalpha() else 0.01)
#     return lst
#
# tests = [
#             [[], []],
#             [['V1'], ['V1']],
#             [['V7', 'V12', 'V1'], ['V1', 'V7', 'V12']],
#             [['V13', 'V14', 'VB', 'V0'], ['VB', 'V0', 'V13', 'V14']],
#             [['V0+', 'V0', 'V16', 'V2', 'VB', 'V6'], ['VB', 'V0', 'V0+', 'V2', 'V6', 'V16']]]
# m = sort_grades(['V0+', 'V0', 'V16', 'V2', 'VB', 'V6'])
# print(m)



# def to_csv_text(array):
#     result = ''
#     for row in array:
#         l = ','.join(map(str , row))+"\n"
#         result += l
#
#     return result.rstrip("\n")
# matrix = [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]]
# to_csv_text(matrix)

# m = [ 23, 2, 3, 4, 5 ]
# def sort_by_value_and_index(arr):
#     arr = list(enumerate(arr,1))
#     arr = sorted(arr , key = lambda x: x[0]*x[1])
#     return [i[1] for i in arr]
#
# sort_by_value_and_index(m)

# def multiple_of_index(arr):
#
#     result = [0] if arr[0] == 0 else []
#     # if arr[0] == 0:
#     #     result = [0]
#     # else:
#     #     result = []
#     for i , v in enumerate(arr[1:],1):
#         if v % i == 0:
#             result.append(v)
#     return result
#
#
# m = [22, -6, 32, 82, 9, 25]
# print(multiple_of_index(m))
#


# def fizzbuzz(n):
#         return ['FizzBuzz' if not i % 3 and not i % 5 else 'Fizz' if not i % 3 else 'Buzz' if not i % 5 else i for i in
#                range(1, n + 1)]


# fizzbuzz(100)


# def seqlist(start , step , n):
    # result = []
    # c = start
    # for _ in range(n):
    #     result.append(c)
    #     c  = c + step
#     return [c:=step] + [c := c + step for _ in range(n-1)]
#
# print(seqlist(0, 2, 20))

