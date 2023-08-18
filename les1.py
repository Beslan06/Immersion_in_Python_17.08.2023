try:
    is_valid_input = False
    while not is_valid_input:
        input_str = input("Введите целое число: ")
        if input_str.isdigit() or (input_str[0] == '-' and input_str[1:].isdigit()):
            input_number = int(input_str)
            is_valid_input = True
        else:
            print("Ошибка: Введите целое число.")

    hex_digits = "0123456789ABCDEF"
    hex_result = ""
    remainder = abs(input_number)

    if input_number == 0:
        hex_result = "0"
    else:
        while remainder > 0:
            digit = remainder % 16
            hex_result = hex_digits[digit] + hex_result
            remainder //= 16

    if input_number < 0:
        hex_result = "-" + hex_result

    print("Шестнадцатеричное представление:", hex_result)

except ValueError:
    print("Ошибка: Введите целое число.")






# try:
#     input_number = int(input("Введите целое число: "))
#     hex_result = hex(input_number)[2:]
#     print("Шестнадцатеричное представление:", hex_result)

#     hex_check = hex(input_number)[2:]
#     print("Проверка с использованием hex:", hex_check)

# except ValueError:
#     print("Ошибка: Введите целое число.")






# def int_to_hex_string(number):
#     hex_string = hex(number)[2:]  # Игнорируем префикс "0x"
#     return hex_string

# # Получаем ввод от пользователя
# try:
#     input_number = int(input("Введите целое число: "))
#     hex_result = int_to_hex_string(input_number)
#     print("Шестнадцатеричное представление:", hex_result)

#     # Проверка с использованием функции hex
#     hex_check = hex(input_number)[2:]
#     print("Проверка с использованием hex:", hex_check)

# except ValueError:
#     print("Ошибка: Введите целое число.")