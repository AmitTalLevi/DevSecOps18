# # #q1
# # number1 = int(input("Please enter number: "))
# # for i in range(1,number1):
# #     if (number1 % i) == 0:
# #         print(i)
# #
# # #q2
# #
# # sum2 = 0
# # avg2 = 0
# # i = 0
# #
# # while True:
# #     if i == 0:
# #         number2 = int(input(f'Please enter number #{i + 1}: '))
# #     else:
# #         number2 = int(input(f'Please enter number #{i + 1}: (avg= {avg2}, Sum= {sum2}) '))
# #     if number2 < 0:
# #         break
# #
# #     sum2 += number2
# #     i += 1
# #     avg2 = sum2 / i
# #
# # print("Thank you. Goodbye")
# #
# #
# # # number2 = 0
# # # sum2 = 0
# # # avg2 = 0
# # # i = 1
# # # while number2 >= 0:
# # #     if i == 1:
# # #         number2 = int(input(f'Please enter number #{i}: '))
# # #     sum2 = sum2 + number2
# # #     avg2 = sum2 / i
# # #     number2 = int(input(f'Please enter number #{i}: (avg= {avg2}, Sum= {sum2}) : '))
# # #     i += 1
# # #
# # # i+=1
# # # print(f'Please enter number #{i}: (avg= {avg2}, Sum{sum2}) ')
# # # print("Thank you. Goodbye")
# #
# # #q3
# #
# # words_list = []
# # while True:
# #     word = input("Please type a word: ")
# #     if word in words_list:
# #         print(f'You entered the work {word} twice. Good bye...')
# #         break
# #     words_list.append(word)
# #
# # #q3-challenge
# # words_list2 = {}
# # while True:
# #     word = input("Please type a word: ").lower()
# #     if word in words_list2:
# #         words_list2[word] += 1
# #     else:
# #         words_list2[word] = 1
# #
# #     if words_list2[word] == 3:
# #         print(f'You entered the word "{word}" three times. Goodbye...')
# #         break
# #
# #
#
#
# words_count3 = {}
#
# word = input("Please type a word: ").lower()
# words_count3[word] = 1
#
# while words_count3[word] < 3:
#     word = input("Please type a word: ").lower()
#     if word in words_count3:
#         words_count3[word] += 1
#     else:
#         words_count3[word] = 1
#
#     if words_count3[word] == 3:
#         print(f'You entered the word "{word}" three times. Goodbye...')
#         break
#
#q4

list1 = [1, 2, 'a', 4, 5, 6.5]
list2 = [7, 'b', 3, 10, 'hello', 12]
count1 = 0
count2 = 0

for item in list1:
    if isinstance(item, (int, float)):
        count1 += 1
for item in list2:
    if isinstance(item, (int, float)):
        count2 += 1

if count1 > count2:
    print(f"List 1 contains more numbers ({count1}) than List 2 ({count2}).")
elif count1 < count2:
    print(f"List 2 contains more numbers ({count2}) than List 1 ({count1}).")
else:
    print(f"Both lists contain the same number of numbers ({count1}).")


