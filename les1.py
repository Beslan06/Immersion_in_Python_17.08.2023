try:
    input_number = int(input("Введите целое число: "))
    hex_result = hex(input_number)[2:]
    print("Шестнадцатеричное представление:", hex_result)

    hex_check = hex(input_number)[2:]
    print("Проверка с использованием hex:", hex_check)

except ValueError:
    print("Ошибка: Введите целое число.")




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