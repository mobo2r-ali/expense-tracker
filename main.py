from colorama import Fore, init

from expense_manager import (
    add_expense,
    view_expenses,
    show_total,
    show_category_summary,
    load_expenses
)

init(autoreset=True)


def main():
    load_expenses()

    while True:
        print(Fore.CYAN+"\n=====  EXPENSE TRACKER =====")
        print(Fore.GREEN+"1.add expense ")
        print(Fore.GREEN+"2.view expense")
        print(Fore.GREEN+"3.show total")
        print(Fore.GREEN+"4.category summary")
        print(Fore.RED+"5.exit")

        choice = input(Fore.YELLOW+"choose an option:")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_category_summary()
        elif choice == "5":
            print(Fore.CYAN+"goodbye!")
            break
        else:
            print(Fore.RED+"invalid choice!")


if __name__ == "__main__":
    main()
