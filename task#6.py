def apply_tax(amount, tax_rate):
    return amount - amount * tax_rate

balance, op_count = 0, 0

while True:
    print(f"Баланс: {balance} у.е.")
    action = input("Действие (пополнить/снять/выйти): ")

    if action == "пополнить":
        amount = int(input("Введите сумму для пополнения: "))
        if amount % 50 == 0:
            tax_rate = 0.10
            if op_count % 3 == 2:
                tax_rate += 0.03
            balance += apply_tax(amount, tax_rate)
            op_count += 1
    elif action == "снять":
        amount = int(input("Введите сумму для снятия: "))
        if amount % 50 == 0 and amount <= balance:
            fee = min(max(amount * 0.015, 30), 600)
            balance -= amount + fee
            op_count += 1
    elif action == "выйти":
        print("Программа завершена.")
        break
    else:
        print("Неверное действие. Попробуйте снова.")

    if balance > 5000000:
        balance = apply_tax(balance, 0.10)





# def apply_tax(amount, tax_rate=0.10):
#     return amount - amount * tax_rate

# balance, op_count = 0, 0

# while True:
#     print(f"Баланс: {balance} у.е.")
#     a = input("Действие (пополнить/снять/выйти): ")
#     if a in {"пополнить", "снять"}:
#         amount = int(input(f"Введите сумму для {a}: "))
#         if amount % 50 == 0:
#             fee = min(max(amount * 0.015, 30), 600)
#             if a == "снять" and amount <= balance:
#                 balance -= amount + fee
#             elif a == "пополнить":
#                 balance += apply_tax(amount)
#                 op_count += 1
#                 if op_count % 3 == 0:
#                     balance -= balance * 0.03
#     elif a == "выйти":
#         print("Программа завершена.")
#         break
#     else:
#         print("Неверное действие. Попробуйте снова.")
#     if balance > 5_000_000:
#         balance = apply_tax(balance)
