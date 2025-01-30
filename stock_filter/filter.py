import pandas as pd
from ..agent_manager.models import FilteredStock, FilteredStockList

class StockFilter:
    """
    수집된 주가 데이터에서 '눌림목'으로 보이는 종목들을 필터링하는 로직을 담당합니다.
    """

    def filter_pullback(self, stock_data):
        """
        간단히 예시로 20일 이동평균 대비 단기 하락 종목을 뽑는 식으로 구현 가능.
        실제로는 범위, 거래량, 외부 이슈 등을 반영하여 추가 필터링이 필요.
        """
        candidate_symbols = []
        for symbol, df in stock_data.items():
            df["MA20"] = df["Close"].rolling(window=20).mean()
            if len(df) >= 20:
                # 마지막 종가가 MA20보다 낮고, 최근 5영업일 줄어든 경우를 예로 듦
                recent_df = df.iloc[-5:]
                is_pullback = (recent_df["Close"] < recent_df["MA20"]).all()
                if is_pullback:
                    candidate_symbols.append(FilteredStock(symbol=symbol))

        return FilteredStockList(stocks=candidate_symbols) 