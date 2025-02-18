string = input().split()
palindrome = input()

only_palindromes = [x for x in string if x[::-1] == x]
count_of_palindrome = only_palindromes.count(palindrome)

print(only_palindromes)
print(f"Found palindrome {count_of_palindrome} times")
