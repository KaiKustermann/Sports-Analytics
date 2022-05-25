import os

def mov_to_mp4(directory_str: str):
    directory_in_str = directory_str
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".mp4"): 
            print("ffmpeg -i \"{}{}\" \"{}converted{}\"".format(directory_in_str, filename, directory_in_str, filename))
            os.system("ffmpeg -i \"{}{}\" \"{}converted{}\"".format(directory_in_str, filename, directory_in_str, filename))
            continue
        else:
            continue