from datetime import datetime


class Category:

    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Cannot be empty")
        self.name = name.strip().capitalize()

    def to_dict(self) -> dict:
        return {"name": self.name}

    @classmethod
    def from_dict(cls, data: dict) -> "Category":
        return cls(data["name"])

    def __eq__(self, other):
        return isinstance(other, Category) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Category({self.name!r})"


class Movement:

    TYPE = "Movement"
    DATE_FORMAT = "%Y-%m-%d"  

    def __init__(self, title: str, amount: float, category: Category, date: str = None):
        self._validate(title, amount, category)
        self.title = title.strip()
        self.amount = float(amount)
        self.category = category
        self.date = (
            datetime.now().strftime(self.DATE_FORMAT)
            if date is None
            else self._validate_date(date)
        )

    @staticmethod
    def _validate(title, amount, category):
        if not title or not str(title).strip():
            raise ValueError("Title cannot be empty")
        try:
            amount_f = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Amount must be a valid number")
        if amount_f <= 0:
            raise ValueError("The amount must be greater than 0")
        if not isinstance(category, Category):
            raise ValueError("Must indicate a valid category")

    @classmethod
    def _validate_date(cls, date_str: str) -> str:
        if not date_str or not str(date_str).strip():
            raise ValueError("Date cannot be empty")
        try:
            parsed = datetime.strptime(str(date_str).strip(), cls.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Date must be in {cls.DATE_FORMAT} format (e.g. 2026-01-15)")
        if parsed.date() > datetime.now().date():
            raise ValueError("Date cannot be in the future")
        return parsed.strftime(cls.DATE_FORMAT)

    def sign(self) -> int:
        raise NotImplementedError("This method should be implemented in subclasses")

    def to_dict(self) -> dict:
        return {
            "type": self.TYPE,
            "title": self.title,
            "amount": self.amount,
            "category": self.category.name,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: dict, categories: dict) -> "Movement":
        category_name = data["category"]
        category_obj = categories.get(category_name)
        if category_obj is None:
            category_obj = Category(category_name)

        subclass = Income if data["type"] == "Income" else Expense
        instance = subclass.__new__(subclass)  # skip re-validating already-valid data
        instance.title = data["title"]
        instance.amount = float(data["amount"])
        instance.category = category_obj
        instance.date = data["date"]
        return instance

    def __repr__(self):
        return f"{self.TYPE}({self.title!r}, {self.amount}, {self.category.name!r})"


class Income(Movement):
    TYPE = "Income"

    def sign(self) -> int:
        return 1


class Expense(Movement):
    TYPE = "Expense"

    def sign(self) -> int:
        return -1
