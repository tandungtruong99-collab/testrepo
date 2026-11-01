import sys
from datetime import datetime

# Đảm bảo in tiếng Việt chuẩn trên mọi terminal Windows/Mac/Linux
if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

print("Xin chào! Môi trường của tôi đã sẵn sàng cho khóa học AI Agent 101!")
print(f"Thời gian hiện tại: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
