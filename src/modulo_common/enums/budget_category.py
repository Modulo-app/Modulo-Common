from enum import Enum

class BudgetCategory(str, Enum):
    NEEDED = "needed"
    WANTED = "wanted"
    SAVINGS = "savings"