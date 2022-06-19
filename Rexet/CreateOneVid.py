from moviepy.editor import *


class CreateOneVid():
    def __init__(self, i, title, subreddit):
        self.i = i
        self.title = title
        self.subreddit = subreddit
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
        final_video.write_videofile(
            f'{self.title} | {self.subreddit} | Rexet #shorts.mp4', fps=30)
