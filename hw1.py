#q1
print("#q1: ")
number1 = int(input("Please enter number: "))
divisors_list = []
for i in range(1,number1 + 1):
    if (number1 % i) == 0:
        divisors_list.append(i)
print(divisors_list)

#q2
print("#q2: ")
sum2 = 0
avg2 = 0
i = 0

while True:
    if i == 0:
        number2 = int(input(f'Please enter number #{i + 1}: '))
    else:
        number2 = int(input(f'Please enter number #{i + 1}: (avg= {avg2}, Sum= {sum2}) '))
    if number2 < 0:
        break

    sum2 += number2
    i += 1
    avg2 = sum2 / i

print("Thank you. Goodbye")

#q3
print("#q3: ")
words_count2 = []
while True:
    word = input("Please type a word: ")
    if word in words_count2:
        print(f'You entered the work {word} twice. Good bye...')
        break
    words_count2.append(word)

#q3-challenge
print("#q3-challenge: ")
words_count3 = {}
word = input("Please type a word: ").lower()
words_count3[word] = 1
while words_count3[word] < 3:
    word = input("Please type a word: ").lower()
    if word in words_count3:
        words_count3[word] += 1
    else:
        words_count3[word] = 1
    if words_count3[word] == 3:
        print(f'You entered the word "{word}" three times. Goodbye...')
        break

#q4
print("#q4: ")
list1 = [3, 5, 30, 0]
list2 = [1000, 5, 29, -5]
count1 = 0
count2 = 0
greater_numbers_list1 = []
greater_numbers_list2 = []

for i in range(len(list1)):
    if list1[i] > list2[i]:
        count1 += 1
        greater_numbers_list1.append((list1[i], list2[i]))
    elif list1[i] < list2[i]:
        count2 += 1
        greater_numbers_list2.append((list2[i], list1[i]))

if count1 > count2:
    print(f"List 1 has more greater numbers:")
    for greater, smaller in greater_numbers_list1:
        print(f"{greater} is greater than {smaller} from List 2")
elif count1 < count2:
    print(f"List 2 has more greater numbers:")
    for greater, smaller in greater_numbers_list2:
        print(f"{greater} is greater than {smaller} from List 1")
else:
    print(f"Both lists have the same number of greater numbers ({count1}).")

#q4-challenge
print("#q3-challenge: ")
list1 = [3, 5, 30, 0]
list2 = [1000, 5, 29, -5, 100]

count1 = 0
count2 = 0
greater_numbers_list1 = []
greater_numbers_list2 = []

min_length = min(len(list1), len(list2))

for i in range(min_length):
    if list1[i] > list2[i]:
        count1 += 1
        greater_numbers_list1.append((list1[i], list2[i]))
    elif list1[i] < list2[i]:
        count2 += 1
        greater_numbers_list2.append((list2[i], list1[i]))

if count1 > count2:
    print(f"List 1 has more greater numbers:")
    for greater, smaller in greater_numbers_list1:
        print(f"{greater} is greater than {smaller} from List 2")
elif count1 < count2:
    print(f"List 2 has more greater numbers:")
    for greater, smaller in greater_numbers_list2:
        print(f"{greater} is greater than {smaller} from List 1")
else:
    print(f"Both lists have the same number of greater numbers ({count1}).")

