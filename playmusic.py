import yt_dlp

def get_youtube_data(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            result = {
                'id': info.get('id'),
                'title': info.get('title'),
                'thumbnail': info.get('thumbnail'),
                'audio': info.get('url'),
                'video': info.get('formats')[0]['url']
            }
            return result
        except Exception as e:
            return None
