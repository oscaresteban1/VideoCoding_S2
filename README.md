# VideoCoding_S2
## Seminar 2 of Video Coding: More ffmpeg

### Parts

**Exercise 1:** Cut 10 seconds of the BBB video.

**Exercise 2:** Extract the YUV histogram from the previous BBB video you’ve done and create a new video with both images at the same time.

**Exercise 3** Resize the previous video into 4 different resolutions:
- 720p
- 480p
- 360x240
- 160x120

**Exercise 4:** Integrate everything inside a Python script. 

**Exercise 5:** Change the audio into mono output and in a different audio codec.

### Code

This code uses the ffmpeg package for python. It is necessary to have the Big Buck Bunny video as BBB.avi to execute it. The video is then converted to mp4 inside to compute all the code.

Change the option in the ```choose_exercise()``` function to select a task from 2 to 4. Task 1 is not selectionable.
