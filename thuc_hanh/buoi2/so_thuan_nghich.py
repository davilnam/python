def is_palindrome(number_str):
    return number_str == number_str[::-1]

def count_palindromic_numbers(a, b, M):
    count = 0
    
    for num in range(int(a), int(b) + 1):
        is_palindromic = True
        for base in range(2, M + 1):
            num_str_in_base = ''
            temp_num = num
            while temp_num > 0:
                temp_num, remainder = divmod(temp_num, base)
                num_str_in_base = str(remainder) + num_str_in_base
            if not is_palindrome(num_str_in_base):
                is_palindromic = False
                break
        if is_palindromic:
            count += 1
                
    return count

# Đọc input
a, b, M = input().split()

# Tính và in ra kết quả
result = count_palindromic_numbers(a, b, int(M))
print(result)
