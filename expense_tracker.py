import json
from pathlib import Path

expense_list = {"name": [], "category": [], "amount": []}

def load_expenses():
    if Path("expenses.json").exists():
        with open("expenses.json", "r", encoding="utf-8") as file:
            loaded_expenses = json.load(file)
            expense_list["name"] = loaded_expenses.get("name", [])
            expense_list["category"] = loaded_expenses.get("category", [])
            expense_list["amount"] = loaded_expenses.get("amount", [])
    else:
        if not Path("expenses.json").exists():
            with open("expenses.json", "w", encoding="utf-8") as file:
                json.dump(expense_list, file, ensure_ascii=False, indent=4)

def changes():
    if len(expense_list["name"]) == 0:
        expenses = {"name": [], "category": [], "amount": []}
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(expenses, file, ensure_ascii=False, indent=4)
    else:
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(expense_list, file, ensure_ascii=False, indent=4)

def enterance():
    print("=== EXPENSE TRACKER ===")
    print("")
    print("1. Добавить расход")
    print("2. Просмотреть расходы")
    print("3. Общая сумма")
    print("4. Удалить расход")
    print("5. Выход")

def add_expense():
    flag = False
    while not flag:
        name = input("Введите название расхода: ").strip()
        if name.strip() == "":
            print("Ошибка! Название расхода не может быть пустым.")
        else:
            flag = True
    category = input("Введите категорию расхода: ")
    amount_is_valid = False

    while not amount_is_valid:
        try:
            amount = float(input("Введите сумму расхода: "))
            if amount <= 0:
                print("Ошибка! Сумма расхода не может быть отрицательной или нулевой.")
                continue
            amount_is_valid = True
        except ValueError:
            print("Ошибка! Введите число.")

    expense_list["name"].append(name)
    expense_list["category"].append(category)
    expense_list["amount"].append(amount)
    print("Расход успешно добавлен!")

def delete_expense():
    print("=== УДАЛЕНИЕ РАСХОДА ===")
    for i in range(len(expense_list["name"])):
        print(f"{i + 1}. {expense_list['name'][i]} - {expense_list['category'][i]} - {expense_list['amount'][i]}")
    index = int(input("Введите номер расхода для удаления: ")) - 1
    if 0 <= index < len(expense_list["name"]):
        del expense_list["name"][index]
        del expense_list["category"][index]
        del expense_list["amount"][index]
        print("Расход успешно удален!")
    else:
        print("Некорректный номер расхода.")
choice = 0
load_expenses()
while choice != 5:
    enterance()
    choice = int(input("Выберите действие (1-5): "))
    if choice == 1:
        add_expense()
        changes()
    elif choice == 2:
        print("=== СПИСОК РАСХОДОВ ===")
        for i in range(len(expense_list["name"])):
            print(f"{i + 1}. {expense_list['name'][i]} - {expense_list['category'][i]} - {expense_list['amount'][i]}")
    elif choice == 3:
        total_amount = sum(expense_list["amount"])
        print(f"Общая сумма расходов: {total_amount}")
    elif choice == 4:
        delete_expense()
        changes()
    elif choice == 5:
        print("Выход из программы.")
    else:
        print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 5.")
