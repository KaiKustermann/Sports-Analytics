import os

directory_in_str = "J:/Kai Kustermann/HDM/Semester 7/Sports Analytics/mp4_2/mp4_2/"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mp4"): 
        print("ffmpeg -i \"{}{}\" \"{}converted{}\"".format(directory_in_str, filename, directory_in_str, filename))
        os.system("ffmpeg -i \"{}{}\" \"{}converted{}\"".format(directory_in_str, filename, directory_in_str, filename))
        continue
    else:
        continue