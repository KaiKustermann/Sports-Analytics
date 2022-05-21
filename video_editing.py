from scipy.io.wavfile import read 
import numpy as np
import moviepy.editor as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
import os


#ffmpeg -i "Cutting Crew - (I Just) Died In Your Arms (Official Music Video).mp3" -sample_fmt s16 output.wav

def get_time_of_max_volume(wav_file: str):
    samplerate, data = read(wav_file)
    #only needed for 2 channel audio data
    data_flatten = data.flatten()
    index_max = np.argmax(data_flatten)
    time_max = index_max/samplerate
    return time_max

def get_duration(wav_file: str):
    samplerate, data = read(wav_file)
    return len(data)/samplerate

def get_data(wav_file: str):
    samplerate, data = read(wav_file)
    return data

def get_samplerate(wav_file: str):
    samplerate, data = read(wav_file)
    return samplerate

def get_time_vector(wav_file: str, duration, samplerate):
    time_vector = np.arange(0,duration,1/samplerate) #time vector
    return time_vector

def extract_subclip_from_video(directory: str, mp4_file_name: str):
    clip = mp.VideoFileClip(directory + mp4_file_name + ".mp4")
    clip.audio.write_audiofile(directory + mp4_file_name + ".wav")

    time_max_volume = get_time_of_max_volume(directory + mp4_file_name + ".wav")
    duration = get_duration(directory + mp4_file_name + ".wav")

    if time_max_volume < 15:
        with VideoFileClip(directory + mp4_file_name + ".mp4") as video:
            new = video.subclip(time_max_volume, time_max_volume + 60)
            new.write_videofile(directory + mp4_file_name + "_cut.mp4", audio_codec='aac')
    else:
        print("The time of the maximum volume in the video is higher than 15 seconds, so the video" + mp4_file_name + "was not cut")
        
    if os.path.exists(directory + mp4_file_name + ".wav"):
        os.remove(directory + mp4_file_name + ".wav")
    else:
        print("The file does not exist")


directory_in_str = "J:/Kai Kustermann/HDM/Semester 7/Sports Analytics/mp4_1/mp4_1/"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filename = filename[:-4]
    if (filename.endswith("H") or filename.endswith("S")) and filename.startswith("converted"): 
        extract_subclip_from_video(directory_in_str, filename)
        continue
    else:
        continue