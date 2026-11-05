class EdgeHardwareController:
    def __init__(self, port="/dev/ttyUSB0", baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.connected = False

    def send_signal(self, severity: str):
        """
        深刻度に応じて、エッジデバイスやロボットアームへ制御信号を送信するシミュレーション
        """
        if severity.lower() == "critical" or severity.lower() == "高":
            print("[HARDWARE] 警告: ロボットアームへ緊急停止信号を送信しました！")
            return "緊急停止作動 (Emergency Stop Triggered)"
        else:
            print("[HARDWARE] 情報: 通常運転を継続します。")
            return "通常運転継続 (Normal Operation)"