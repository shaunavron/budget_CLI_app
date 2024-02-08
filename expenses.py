class Expense:

    def __init__(self, item, item_type, item_amount) -> None:
        self.item = item
        self.item_type = item_type
        self.item_amount = item_amount

    def enter_expense():
        expense_types = ["Bills", "Food", "Transportation", "Entertainment", "Other"]
        NUM_CATEGORIES = len(expense_types)
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: $"))
        
        while True:
            print("What kind of expense is this?")
            for i, expense_type in enumerate(expense_types):
                print(f"    {i+1}. {expense_type}")
            
            try:
                expense_type_index = int(input("Enter the number that corresponds to the expense type: ")) - 1
                if 0 <= expense_type_index < NUM_CATEGORIES:
                    expense_type = expense_types[expense_type_index]
                    new_expense = Expense(expense_name, expense_type, expense_amount)
                    return new_expense
                    break
                else:
                    print(f"Invalid selection. Please try again.")
            except ValueError:
                print(f"Invalid entry. Please enter a number from 1 to {NUM_CATEGORIES}")
    

    def write_expense_to_file(user):
        pass

    def generate_report():
        pass
