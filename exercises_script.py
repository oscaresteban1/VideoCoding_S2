from os import path, system

def launch(string, name):
    if not path.exists(name):
        system(string)

def choose_exercise(option):
    if option == 2:
        # ex2: extract the YUV histogram and create a video with both images
        # for some reason it does not sound
        system("ffplay BBB_cut.mp4 -vf 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay'")

    if option == 3:
        # ex3: resize the video
        launch("ffmpeg -i BBB_cut.mp4 -vf scale=1280:720 BBB_720.mp4", "BBB_720.mp4")
        launch("ffmpeg -i BBB_cut.mp4 -vf scale=854:480 BBB_480.mp4", "BBB_480.mp4")
        launch("ffmpeg -i BBB_cut.mp4 -vf scale=360:240 BBB_240.mp4", "BBB_240.mp4")
        launch("ffmpeg -i BBB_cut.mp4 -vf scale=160:120 BBB_120.mp4", "BBB_120.mp4")

    if option == 4:
        # ex4: change the audio into mono and use another codec
        launch("ffmpeg -i BBB_cut.mp4 -c:a libvorbis -ac 1 BBB_mono.mp4", "BBB_mono.mp4")

    else:
        print("Choose a valid option")

# ex1: cut 10 sec of the video BBB.avi and convert it to mp4
launch("ffmpeg -i BBB.avi -c copy -t 10 BBB_cut.mp4", "BBB_cut.mp4")

# exercises 2 to 4
choose_exercise(option = 4)
