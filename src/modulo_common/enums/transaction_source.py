from enum import Enum

class TransactionSource(str, Enum):
    MANUAL = "manual"
    APPLE_PAY_IMPORT = "apple_pay_import"