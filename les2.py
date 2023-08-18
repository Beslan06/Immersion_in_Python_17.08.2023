def parse_fraction(fraction_str):
    parts = fraction_str.split('/')
    if len(parts) == 2:
        numerator = int(parts[0])
        denominator = int(parts[1])
        return numerator, denominator
    else:
        raise ValueError("Неверный формат дроби. Используйте формат a/b.")

def add_fractions(fraction1, fraction2):
    num1, den1 = fraction1
    num2, den2 = fraction2
    common_denominator = den1 * den2
    new_numerator = num1 * den2 + num2 * den1
    return new_numerator, common_denominator

def multiply_fractions(fraction1, fraction2):
    num1, den1 = fraction1
    num2, den2 = fraction2
    new_numerator = num1 * num2
    new_denominator = den1 * den2
    return new_numerator, new_denominator

fraction1_str = input("Введите первую дробь в формате a/b: ")
fraction2_str = input("Введите вторую дробь в формате a/b: ")

try:
    fraction1 = parse_fraction(fraction1_str)
    fraction2 = parse_fraction(fraction2_str)

    sum_result = add_fractions(fraction1, fraction2)
    multiply_result = multiply_fractions(fraction1, fraction2)

    print("Сумма дробей:", sum_result[0], "/", sum_result[1])
    print("Произведение дробей:", multiply_result[0], "/", multiply_result[1])

except ValueError as e:
    print("Ошибка:", e)












# from fractions import Fraction

# fraction1 = input("Введите первую дробь в формате a/b: ")
# fraction2 = input("Введите вторую дробь в формате a/b: ")

# sum_result = Fraction(fraction1) + Fraction(fraction2)
# multiply_result = Fraction(fraction1) * Fraction(fraction2)

# print("Сумма дробей:", sum_result)
# print("Произведение дробей:", multiply_result)








# from fractions import Fraction

# def add_fractions(fraction1, fraction2):
#     result = Fraction(fraction1) + Fraction(fraction2)
#     return result

# def multiply_fractions(fraction1, fraction2):
#     result = Fraction(fraction1) * Fraction(fraction2)
#     return result

# try:
#     fraction1 = input("Введите первую дробь в формате a/b: ")
#     fraction2 = input("Введите вторую дробь в формате a/b: ")

#     sum_result = add_fractions(fraction1, fraction2)
#     multiply_result = multiply_fractions(fraction1, fraction2)

#     print("Сумма дробей:", sum_result)
#     print("Произведение дробей:", multiply_result)

# except ValueError:
#     print("Ошибка: Введите дроби в правильном формате (например, 3/4).")