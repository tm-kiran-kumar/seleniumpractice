# Factorial of number
def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result
print(f'factorial: {factorial(5)}')
print('----'*10)

# Fibonacci Series
def fibonacci(n):
    res = []
    a, b = 0, 1
    for _ in range(n):
        res.append(a)
        # print(a, end=' ')
        a, b = b, a + b
    return res
print(fibonacci(10))


# Palindrome
def palindrome(s):
    if s == s[::-1]:
        return f'palindrome: {s}'
    else:
        return f'Not a palindrome: {s}'
print(palindrome('racecar'))
print('----'*10)

# Anagram Check
def anagram(s1, s2):
    if "".join(sorted(s1)) == "".join(sorted(s2)):
        return 'Anagram'
    else:
        return 'Not a anagram'
print(anagram('listen', 'silent'))

# angram check alternate way
from collections import Counter
def is_anagram(s1, s2):
    # Counter creates a dictionary of character frequencies
    return Counter(s1) == Counter(s2)
print(is_anagram('listen', 'silent')) # True
# return 'Anagram' if sorted(s1) == sorted(s2) else 'Not an anagram'


# Sum of two integers
def sum_of_two(numbers):
    count = []
    for i in range(0, len(numbers)-1):
        result = numbers[i] + numbers[i+1]
        count.append(result)
    return count
num_list = [36,46,43,21,34,45]
print(sum_of_two(num_list))
print('----'*10)

# Sum of two integers with first and second highest numbers
def sum_of_two(numbers):
    count = []
    first, second = 0, 0
    for i in range(0, len(numbers)-1):
        result = numbers[i] + numbers[i+1]
        count.append(result)
        if result>=first:
            second = first
            first=result
        elif result>=second and result <= first:
            second = result
    return count, first, second
num_list = [36,46,43,21,34,45]
sum_count, highest, second_highest = sum_of_two(num_list)
print(f'Sum of two integers: {sum_count}\nhighest number: {highest}\nsecond highest number: {second_highest}')
print('----'*10)

# Sum of two integers with highest numbers indices
def highest_num_index(numbers):
    count = []
    highest = 0
    indices = (0, 0)
    for i in range(0, len(numbers)-1):
        result = numbers[i] + numbers[i+1]
        count.append(result)
        if result >= highest:
            highest = result
            indices = i, i+1
        else:
            continue

    return count, highest, indices
numbers_list = [36,20,93,20,34,45]
sum_count, highest, highest_indices = highest_num_index(numbers_list)
print(f'Sum of two integers: {sum_count}\nhighest number: {highest}\nhighest_indices are: {highest_indices}')
print('----'*10)

# Two sum for target value
def find_target_sum(numbers, target):
    seen = {} # val : index
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return "No pair found"

nums = [10, 20, 30, 40]
print(find_target_sum(nums, 50))


# Nested list to flatten list
def flatten(nested):
    flat_list = []
    for i in nested:
        if isinstance(i, list):
            #flat_list.extend(i)
            flat_list.extend(flatten(i))    # recursive function
        else:
            flat_list.append(i)
    return flat_list
nested_list = [23,32,[45,64,[77,44],56,],34,66]
result = flatten(nested_list)
print(f'flatten list: {result}\nsum of flatten list: {sum(result)}')
print('----'*10)

# Sum of missing number
def missing_num(numbers):
    n = len(numbers)+1
    expected_sum = n * (n+1) // 2   # formula
    actual_sum = sum(numbers)
    return expected_sum - actual_sum
numbers_list = [1,2,3,4,5,7,8]
print(f'missing number from list: {missing_num(numbers_list)}')
print('----'*10)

# Count number of characters
def char_count(words):
    count = {}
    for char in words.lower():  # .lower() handles case sensitivity
        if char in count:
            count[char] += 1
        elif char != ' ':   # for removing whitespaces
            count[char] = 1
        else:
            continue
    return count

string_of_words = 'Hello python, this is practice character count'
print(char_count(string_of_words))
print('----'*10)

# Alternate way
def char_count(words):
    count = {}
    for char in words.lower(): # .lower() handles case sensitivity
        if char != ' ':
            count[char] = count.get(char, 0) + 1
    return count
print(char_count('Hello python, this is practice'))

# Word Count
def char_count(words):
    word = words.split()
    print(word)
    count = {}
    for w in word:
        count[w] = count.get(w, 0) + 1
    return count

string_of_words = 'Python is great and Python is fast"'
print(char_count(string_of_words))
print('----'*10)


