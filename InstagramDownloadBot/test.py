# import instaloader
# from instaloader import Post
#
# loader = instaloader.Instaloader()
# l = 'https://www.instagram.com/reel/C-T8-i4oPed/?utm_source=ig_web_copy_link'
#
#
# code = l.split('/')[-2]
# p = Post.from_shortcode(loader.context , code)
# print(p)
import logging
import threading

import yt_dlp
def download_and_send_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info_dict)

url = 'https://www.youtube.com/watch?v=ZorffyLHmVE'
threading.Thread(target=download_and_send_video, args=(url,)).start()
print(10)

