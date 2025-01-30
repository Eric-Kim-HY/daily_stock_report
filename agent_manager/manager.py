import os
from .tasks.news_collector import NewsCollector
from .tasks.final_report_generator import FinalReportGenerator
import requests

class AgentManager:
    """
    smolagent 라이브러리를 관리하고, 
    GPT-4o-mini나 o1-mini 등을 활용한 multi-agent 작업을 orchestration하는 클래스.
    """
    def __init__(self):
        self.news_collector = NewsCollector()
        self.final_report_generator = FinalReportGenerator()
        self.webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")

    def collect_news_and_blogs(self, stock_analysis_data):
        """
        GPT-4o-mini 에이전트를 활용하여 뉴스/블로그 정보를 수집하고 데이터에 추가.
        """
        enriched_data = self.news_collector.collect_for_stocks(stock_analysis_data)
        return enriched_data

    def send_report(self, report_str):
        """
        최종 레포트를 Discord 등으로 전송
        """
        if not self.webhook_url:
            print("No webhook URL provided. Report not sent.")
            return

        payload = {
            "content": report_str
        }
        try:
            response = requests.post(self.webhook_url, json=payload)
            if response.status_code != 204:
                print(f"Error sending message to Discord: {response.text}")
        except Exception as e:
            print(f"Exception while sending to Discord: {e}") 