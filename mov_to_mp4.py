import os

#converts the videos in the given directory from mov to mp4, ffmpeg must be installed
def mov_to_mp4(directory_str: str):
    directory_in_str = directory_str
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".mov"): 
            os.system("ffmpeg -i \"{}{}\" \"{}converted{}\"".format(directory_in_str, filename, directory_in_str, filename[:-4] + ".mp4"))
            continue
        else:
            continue