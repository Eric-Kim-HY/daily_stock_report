class ReportGenerator:
    """
    최종 보고서를 생성하는 클래스. 
    예: 종목명, 점수, 이유분석, 전망 등을 요약하여 문자열로 생성.
    """
    def generate_report(self, analysis_data):
        """
        analysis_data: [{ symbol, momentum_score, value_score, growth_score, pullback_reason, ... }]
        """
        lines = ["[Daily Stock Pullback Report]"]
        for item in analysis_data:
            lines.append(
                f"종목: {item.get('symbol')} | "
                f"모멘텀: {item.get('momentum_score'):.2f}, "
                f"가치평가: {item.get('value_score'):.2f}, "
                f"성장성: {item.get('growth_score'):.2f}, "
                f"눌림목 사유: {item.get('pullback_reason')}"
            )
        report_str = "\n".join(lines)
        return report_str 