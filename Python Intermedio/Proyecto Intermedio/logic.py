from models import Category,Income,Expense
from persistence import Persistence

class CategoryAlreadyExistsError(Exception):
    """Raised when trying to create a category that already exists"""


class NoCategoriesError(Exception):
    """Raised when trying to add a movement without any categories created"""

class FinanceManager:
    def __init__(self,persistence:Persistence=None):
        self.persistence = persistence or Persistence()
        self.categories:dict={}  # {normalized_name: Category}
        self.movements:list=[]   # list of Income/Expense
        self._load_data()

    #--save/load
    def _load_data(self)->None:
        self.categories=self.persistence.load_categories()
        self.movements=self.persistence.load_movements(self.categories)
    
    def save_all(self)->None:
        """Persist the current state. Called after each change (autosave)."""
        self.persistence.save_categories(self.categories)
        self.persistence.save_movements(self.movements)

    #--Categories

    def add_category(self,name:str)->Category:
        category=Category(name)
        if category.name in self.categories:
            raise CategoryAlreadyExistsError(f"The category '{category.name}' already exists")
        self.categories[category.name]=category
        self.save_all()
        return category
    
    def category_names(self)->list:
        return sorted(self.categories.keys())
    
    def _get_category(self,name:str)->Category:
        key=name.strip().capitalize() if name else ""
        category=self.categories.get(key)
        if category is None:
            raise ValueError(f"The category '{name}' does not exist")
        return category
    
    def _validate_categories_exist(self)->None:
        if not self.categories:
            raise NoCategoriesError(
                "No categories available. Create a category before continuing."
            )
    #--Movemts

    def add_income(self, tittle:str, amount:float, category_name:str)->Income:
        self._validate_categories_exist()
        category=self._get_category(category_name)
        income =Income(titlle,amount,category)
        self.movements.append(income)
        self.save_all()
        return income
    
    def add_expense(self, tittle:str,amount:float, category_name:str)->Expense:
        self._validate_categories_exist()
        category=self._get_category(category_name)
        expense=Expense(tittle,amount,category)
        self.movements.append(expense)
        self.save_all()
        return expense
    
    #--Reports
    def calculate_balance(self)->float:
        return sum(m.amount*m.sign() for m in self.movements)
    
    def calculate_totals_by_category(self)->tuple:
        income_total=suma(m.amount for m in self.movements if isinstance(m,Income))
        expense_total=sum(m.amount for m in self.movements if isinstance(m,Expense))
        return income_total,expense_total
    
    def movements_for_table(self)->list:
        return [
            {
                "type": m.TIPO,
                "tittle": m.tittle,
                "amount": m.amount,
                "category": m.category.name,
                "date": m.date
            }
            for m in self.movements
        ]
    