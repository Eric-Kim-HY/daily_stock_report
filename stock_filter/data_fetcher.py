import os
import yfinance as yf
import datetime

class DataFetcher:
    """
    주식 데이터를 yfinance 등을 이용해 가져오는 클래스.
    """
    def __init__(self):
        self.start_date = datetime.datetime.now() - datetime.timedelta(days=365)
        self.end_date = datetime.datetime.now()

    def fetch_daily_data(self, symbols=None):
        """
        일봉 데이터를 가져와서 반환합니다.
        symbols가 None이면, 기본 종목 리스트를 사용할 수도 있습니다.
        """
        if symbols is None:
            # 예시: 간단한 종목 리스트
            symbols = ["AAPL", "MSFT", "TSLA", "GOOGL"]

        all_data = {}
        for symbol in symbols:
            df = yf.download(symbol, start=self.start_date, end=self.end_date)
            all_data[symbol] = df
        return all_data 