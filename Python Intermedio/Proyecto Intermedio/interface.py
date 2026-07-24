
import FreeSimpleGUI as sg

from logic import FinanceManager, CategoryAlreadyExistsError, NoCategoriesError

sg.theme("SystemDefaultForReal")

HEADINGS = ["Date", "Type", "Title", "Category", "Amount"]


class FinanceInterface:
    def __init__(self):
        self.manager = FinanceManager()
        self.window = self._create_main_window()

    # ---------- Window construction ----------

    def _create_main_window(self) -> sg.Window:
        layout = [
            [sg.Text("Personal Finance Manager", font=("Arial", 16))],
            [sg.Text("Balance:"), sg.Text("0.00", key="-BALANCE-", font=("Arial", 12, "bold"))],
            [sg.Table(
                values=self.manager.movements_for_table(),
                headings=HEADINGS,
                key="-TABLE-",
                auto_size_columns=True,
                expand_x=True,
                expand_y=True,
                num_rows=15,
                justification="left",
            )],
            [
                sg.Button("Add Category", key="-CAT-"),
                sg.Button("Add Income", key="-INC-"),
                sg.Button("Add Expense", key="-EXP-"),
                sg.Button("Exit", key="-EXIT-"),
            ],
        ]
        return sg.Window("Personal Finances", layout, finalize=True, resizable=True)

    def _add_category_window(self) -> None:
        layout = [
            [sg.Text("Category name:"), sg.Input(key="-NAME-", focus=True)],
            [sg.Button("Save"), sg.Button("Cancel")],
        ]
        window = sg.Window("New Category", layout, modal=True)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancel"):
                break
            if event == "Save":
                try:
                    self.manager.add_category(values["-NAME-"])
                    break 
                except (ValueError, CategoryAlreadyExistsError) as error:
                    sg.popup_error(str(error), title="Error")
        window.close()

    def _add_movement_window(self, kind: str) -> None:
        """kind: 'Income' or 'Expense'. We reuse the same form for both."""
        if not self.manager.categories:
            sg.popup_error(
                "No categories available. Create a category first.",
                title="No categories",
            )
            return

        category_options = self.manager.category_names()
        layout = [
            [sg.Text("Title:"), sg.Input(key="-TITLE-", focus=True)],
            [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
            [sg.Text("Category:"), sg.Combo(category_options, key="-CATEGORY-", readonly=True)],
            [sg.Button("Save"), sg.Button("Cancel")],
        ]
        window = sg.Window(f"New {kind}", layout, modal=True)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancel"):
                break
            if event == "Save":
                try:
                    if kind == "Income":
                        self.manager.add_income(
                            values["-TITLE-"], values["-AMOUNT-"], values["-CATEGORY-"]
                        )
                    else:
                        self.manager.add_expense(
                            values["-TITLE-"], values["-AMOUNT-"], values["-CATEGORY-"]
                        )
                    break
                except (ValueError, NoCategoriesError) as error:
                    sg.popup_error(str(error), title="Error")
        window.close()

    

    def _update_table(self) -> None:
        self.window["-TABLE-"].update(values=self.manager.movements_for_table())
        income_total, expense_total = self.manager.calculate_totals()
        balance = self.manager.calculate_balance()
        self.window["-BALANCE-"].update(
            f"{balance:.2f}   (Income: {income_total:.2f}  /  Expenses: {expense_total:.2f})"
        )

    

    def run(self) -> None:
        self._update_table()
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "-EXIT-"):
                break
            elif event == "-CAT-":
                self._add_category_window()
                self._update_table()
            elif event == "-INC-":
                self._add_movement_window("Income")
                self._update_table()
            elif event == "-EXP-":
                self._add_movement_window("Expense")
                self._update_table()

        self.manager.save_all()  # final autosave, though it also saves after every change
        self.window.close()