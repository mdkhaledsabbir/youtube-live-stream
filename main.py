import os

# ভিডিও ফাইলের নাম (GitHub থেকে pull হয়ে Render এ থাকবে)
video_file = "LiveClip.mp4"

# YouTube RTMP URL এবং Stream Key
stream_url = "rtmp://a.rtmp.youtube.com/live2"
stream_key = "kay3-aefp-uht1-uvbq-dem1"  # আপনার লাইভ স্ট্রিমিং key

# FFmpeg command: ভিডিও push করা
ffmpeg_command = f"""
ffmpeg -re -i "{video_file}" \
-c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k \
-pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 \
-f flv "{stream_url}/{stream_key}"
"""

# Execute FFmpeg
os.system(ffmpeg_command)
