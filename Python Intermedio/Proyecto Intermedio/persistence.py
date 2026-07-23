import json    # python--json
import os      
from models import Category, Movement

class Persistence:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.categories_path = os.path.join(self.data_dir, "categories.json")
        self.movements_path = os.path.join(self.data_dir, "movements.json")
    
    #--Categories
    def save_categories(self, categories: dict) -> None:
        data = [c.to_dict() for c in categories.values()]
        self._write(self.categories_path, data)

    
    def load_categories(self) -> dict:
        data = self._read(self.categories_path)
        categories = {}
        for item in data:
            cat = Category.from_dict(item)
            categories[cat.name] = cat
        return categories
    
    #--Movements
    def save_movements(self, movements: list) -> None:
        data = [m.to_dict() for m in movements]
        self._write(self.movements_path, data)

    def load_movements(self, categories: dict) -> list:
        data = self._read(self.movements_path)
        return [Movement.from_dict(item, categories) for item in data]
    #--Private methods
    @staticmethod
    def _write(path: str, data: list) -> None:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def _read(path: str) -> list:
        if not os.path.exists(path):
            return []
        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except (json.JSONDecodeError, OSError):
            return []