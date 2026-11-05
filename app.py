import streamlit as st
import cv2
import numpy as np
from PIL import Image

from detector import StructuralInspector
from agent import InspectorAgent
from hardware import EdgeHardwareController

st.set_page_config(page_title="Edge-VLA スマート点検システム", layout="wide")

st.title("🤖 Edge-VLA スマート・ロボティック点検エージェント")
st.markdown("コンピュータビジョン、生成AIエージェント、およびエッジコンピューティングを統合したリアルタイム構造物・インフラ異常検知システム。")

@st.cache_resource
def load_modules():
    detector = StructuralInspector()
    agent = InspectorAgent()
    hardware = EdgeHardwareController()
    return detector, agent, hardware

detector, agent, hardware = load_modules()

st.sidebar.header("コントロールパネル")
uploaded_file = st.sidebar.file_uploader("点検対象の画像をアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("元画像 (Original Image)")
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("AI 検出結果 (AI Detection)")
        with st.spinner("画像解析および異常検知を実行中..."):
            annotated_img, detections = detector.detect_anomalies(image_np)
            st.image(annotated_img, channels="BGR", use_column_width=True)

    st.markdown("---")
    st.subheader("🧠 LangChain AI エージェント＆ハードウェア連携")
    
    if st.button("AIエージェントによる詳細分析を実行"):
        with st.spinner("レポートを生成しています..."):
            report = agent.analyze_issue(detections)
            hardware_status = hardware.send_signal("中")

            st.success("分析が完了しました！")
            st.write(report)
            st.info(f"**エッジデバイス状態:** {hardware_status}")
else:
    st.info("左側のサイドバーから点検用の画像をアップロードしてください。")