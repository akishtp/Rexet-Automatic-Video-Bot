from cv2 import VideoWriter, VideoWriter_fourcc
from moviepy.editor import *
import cv2


class CreateOneVid():
    def __init__(self, i):
        self.i = i
        for x in range(self.i):
            self.createSingleVid(x)
        self.createFullVid()

    def createSingleVid(self, i):
        audio = AudioFileClip(f'Audio/audio{i}.mp3')
        clip = ImageClip(f'images/{i}.png').set_duration(audio.duration)
        clip = clip.set_audio(audio)
        clip.write_videofile(f'Video/part{i}.mp4', fps=30)

    def createFullVid(self):
        clips = []

        for i in range(self.i):
            clips.append(VideoFileClip(f'Video/part{i}.mp4'))

        final_video = concatenate_videoclips(clips, method='compose')
        final_video.write_videofile('final_video.mp4', fps=30)
        # videos = []
        # for i in range(self.i):
        #     videos.append(f'Video/part{i}.mp4')

        # # Create a new video
        # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        # video = cv2.VideoWriter(
        #     "new_video.mp4", fourcc, 1, (1080, 1920))

        # # Write all the frames sequentially to the new video
        # for v in videos:
        #     curr_v = cv2.VideoCapture(v)
        #     while curr_v.isOpened():
        #         r, frame = curr_v.read()    # Get return value and curr frame of curr video
        #         if not r:
        #             break
        #         video.write(frame)          # Write the frame

        # video.release()
