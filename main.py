import os
import sys
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 로컬 환경에서만 .env 파일 로드, Lambda 환경에서는 시스템 변수를 사용
if os.environ.get("AWS_LAMBDA_FUNCTION_NAME") is None:
    logger.info("Loading local .env file")
    load_dotenv()
else:
    logger.info("Running in AWS Lambda environment; skipping .env loading")

# 필요한 모듈 임포트
from stock_filter.data_fetcher import DataFetcher
from stock_filter.filter import StockFilter
from stock_filter.analysis import StockAnalysis
from stock_filter.report_generator import ReportGenerator

from agent_manager.manager import AgentManager

def lambda_handler(event=None, context=None):
    """
    AWS Lambda 진입점 함수.
    하루 1회 트리거하여 미국 주식 스크리닝 및 종합 보고를 수행.
    """
    # 1. 데이터 가져오기
    fetcher = DataFetcher()
    raw_data = fetcher.fetch_daily_data()

    # 2. 누림목 기반 필터링
    stock_filter = StockFilter()
    filtered_stocks = stock_filter.filter_pullback(raw_data)

    # 3. 종목 분석
    analyzer = StockAnalysis()
    analyzed_stocks = analyzer.perform_analysis(filtered_stocks)

    # 4. 에이전트(LLM) 활용 뉴스/블로그 수집
    agent_manager = AgentManager()
    enriched_data = agent_manager.collect_news_and_blogs(analyzed_stocks)

    # 5. 최종 레포트 생성
    report_gen = ReportGenerator()
    report = report_gen.generate_report(enriched_data)

    # 6. 최종 레포트 전송
    agent_manager.send_report(report)

def main():
    """
    로컬에서 테스트를 위해 실행되는 메인 함수.
    AWS Lambda 환경이 아니라면 직접 호출.
    """
    lambda_handler()

if __name__ == "__main__":
    main() 