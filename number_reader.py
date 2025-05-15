def read_numbers():
    input_str = input("Введите список чисел через запятую: ")
    numbers = [int(num.strip()) for num in input_str.split(',')]
    return numbers

def find_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def find_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

def sort_list(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def main():
    numbers = read_numbers()
    even_numbers = find_even_numbers(numbers)
    max_num, min_num = find_max_min(numbers)
    sorted_numbers = sort_list(numbers)

    print(f"Четные числа: {even_numbers}")
    print(f"Максимальное число: {max_num}")
    print(f"Минимальное число: {min_num}")
    print(f"Отсортированный список: {sorted_numbers}")

if __name__ == "__main__":
    main()
