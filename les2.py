from fractions import Fraction

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

sum_result = Fraction(fraction1) + Fraction(fraction2)
multiply_result = Fraction(fraction1) * Fraction(fraction2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", multiply_result)




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