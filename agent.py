import os
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model

class InspectorAgent:
    def __init__(self):
        try:
            self.llm = init_chat_model("gemini-1.5-flash", model_provider="google_genai")
        except Exception:
            self.llm = None

    def analyze_issue(self, detections: list):
        if not detections:
            return "異常は検出されませんでした。構造物は正常な状態です。"

        prompt = f"""
        以下のコンピュータビジョンの検出結果に基づき、構造物点検レポート（日本語）を作成してください。
        検出データ: {detections}

        以下の項目を必ず含めてください：
        1. 異常の深刻度 (低・中・高 / Critical)
        2. 即座に行うべき対応 (Immediate Action)
        3. 推奨される補修・メンテナンス方針 (Repair Recommendation)
        """

        if self.llm:
            try:
                response = self.llm.invoke([HumanMessage(content=prompt)])
                return response.content
            except Exception as e:
                return f"AIエージェントによる分析エラーが発生しました (API Error): {str(e)}"
        else:
            return "【モック分析】重大なひび割れが検出されました。直ちに構造補強が必要です。"
