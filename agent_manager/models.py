from pydantic import BaseModel
from typing import List

class FilteredStock(BaseModel):
    """
    누림목 필터 과정을 통과한 종목을 표현하는 모델.
    """
    symbol: str

class FilteredStockList(BaseModel):
    """
    여러 종목의 목록을 보관하는 모델.
    """
    stocks: List[FilteredStock] 