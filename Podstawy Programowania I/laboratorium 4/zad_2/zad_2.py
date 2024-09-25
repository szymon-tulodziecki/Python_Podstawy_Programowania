class Salary:
    def __init__(self, amount_brutto, tax=18, deductions=0, bonus=0):
        self.amount_brutto = amount_brutto
        self.tax = tax
        self.deductions = deductions
        self.bonus = bonus

    def calculate_netto(self):
        tax_amount = self.amount_brutto * (self.tax / 100)
        bonus_amount = self.amount_brutto * (self.bonus / 100)
        return self.amount_brutto - tax_amount - self.deductions + bonus_amount

def enter_data():
    while True:
        try:
            amount_brutto = float(input("Enter gross amount: "))
            tax = float(input("Enter tax percentage (default: 18): ") or 18)
            deductions = float(input("Enter amount of deductions (default 0): ") or 0)
            bonus = float(input("Enter bonus percentage (default 0): ") or 0)
            return Salary(amount_brutto, tax, deductions, bonus)
        except ValueError:
            print("You entered incorrect data, try again.")

def enter_current_month():
    while True:
        try:
            month = int(input("Enter current month (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("You entered incorrect data, try again.")
        except ValueError:
            print("You entered incorrect data, try again.")

def enter_new_bonus():
    while True:
        try:
            bonus = float(input("Enter new bonus percentage (default 0): ") or 0)
            if 0 <= bonus <= 100:
                return bonus
            else:
                print("Bonus percentage must be between 0 and 100.")
        except ValueError:
            print("You entered incorrect data, try again.")

def main():
    salary_xyz = enter_data()

    print(f"Gross salary before bonus: {salary_xyz.amount_brutto}")
    print(f"Net salary before bonus: {salary_xyz.calculate_netto()}")

    current_month = enter_current_month()
    new_bonus_percentage = enter_new_bonus()

    new_salary_xyz = Salary(
        salary_xyz.amount_brutto,
        salary_xyz.tax,
        salary_xyz.deductions,
        new_bonus_percentage
    )

    print(f"Gross salary after bonus: {new_salary_xyz.amount_brutto}")
    print(f"Net salary after bonus: {new_salary_xyz.calculate_netto()}")

    if current_month == 1:
        print("You won't get any compensation!")
    else:
        compensation = (current_month - 1) * (new_salary_xyz.calculate_netto() - salary_xyz.calculate_netto())
        print(f"You will also get {compensation:.2f} compensation!")

if __name__ == '__main__':
    main()
