import os
import threading
import requests
import time
import sys

# ===============================
# Logging
# ===============================
log_file = "stream.log"
sys.stdout = open(log_file, "a")
sys.stderr = sys.stdout

# ===============================
# Configuration
# ===============================
video_file = "LiveClip.mp4"
stream_url = "rtmp://a.rtmp.youtube.com/live2"
stream_key = "kay3-aefp-uht1-uvbq-dem1"
keep_alive_url = "https://your-uptimerobot-url"  # optional ping URL
# ===============================

# ===============================
# Keep-alive ping thread
# ===============================
def keep_alive():
    while True:
        try:
            requests.get(keep_alive_url)
        except:
            pass
        time.sleep(300)  # প্রতি ৫ মিনিটে ping

threading.Thread(target=keep_alive, daemon=True).start()

# ===============================
# 24/7 livestream loop with auto-restart
# ===============================
while True:
    ret = os.system(f'ffmpeg -re -i "{video_file}" '
                    f'-c:v libx264 -preset veryfast '
                    f'-maxrate 500k -bufsize 1000k '
                    f'-vf "scale=-2:144" -pix_fmt yuv420p -g 50 '
                    f'-c:a aac -b:a 64k -ar 44100 '
                    f'-f flv "{stream_url}/{stream_key}"')
    if ret != 0:
        print("FFmpeg crashed, restarting in 5 seconds...")
        time.sleep(5)
