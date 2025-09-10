import os

# ভিডিও ফাইলের নাম
video_file = "MusclePainRelief_DrRavi.mp4"

# Stream URL এবং Stream Key
stream_url = "rtmp://a.rtmp.youtube.com/live2"
stream_key = "kay3-aefp-uht1-uvbq-dem1"

# FFmpeg লাইভ স্ট্রিম কমান্ড
ffmpeg_command = f"""
ffmpeg -re -i "{video_file}" -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k \
-pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 -f flv "{stream_url}/{stream_key}"
"""

# কমান্ড রান করা
os.system(ffmpeg_command)
