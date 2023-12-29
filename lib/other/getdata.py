from lib.downloader.__main__ import YouTube

data = []
link_data=[]
res =[]

def start(video_url):
    yt = YouTube(video_url)
    video_streams = yt.streams.all()

    resolutions_sit = [stream.resolution for stream in video_streams if stream.resolution]
    resolutions = sorted(list(set(resolutions_sit)))
    v_res ={
        'resolution':resolutions
    }
    
    video_data = {
        'title': yt.title,
        'thumbnail': yt.thumbnail_url,
        'views': yt.views,
        'publish_date': yt.publish_date,
        'caption': yt.captions,
    }
    download ={
        'streams_data':yt.fmt_streams
    }

    link_data.append(download)
    data.append(video_data)
    res.append(v_res)
    return data,link_data,res

