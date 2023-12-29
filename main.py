from lib.other.download_v_a import download
from lib.marge.stefnk import merge
from lib.other.name_gen import create_filename
from lib.other.getdata import start,data,link_data,res



name_gen = create_filename('youtube')
audio_file= f"./storage/temp-store/{name_gen}.mp3"
video_file =f"./storage/temp-store/{name_gen}.mp4"
output_name = f"./storage/output/output{name_gen}.mp4"



video_url = 'https://youtu.be/vSo6Opp_kg0?si=QWITAPSxc3dxf85l'

start(video_url)
print(res[0]['resolution'])
print(link_data[0])

resolution_choice = '2160p'

#download(video_url, resolution_choice,video_file,audio_file)


#merge(video_file, audio_file, output_name)
