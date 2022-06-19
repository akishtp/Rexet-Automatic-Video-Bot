from gtts import gTTS
from Rexet.CreateOneVid import CreateOneVid


class CreateAudio():
    def __init__(self, to_read, subreddit):
        self.to_read = to_read

        for i in range(len(to_read)):
            self.readrexit(to_read[i], i)
        i = len(to_read)
        CreateOneVid(i, to_read[0], subreddit)

    def readrexit(self, to_read, i):
        myobj = gTTS(text=to_read, lang='en', slow=False)
        myobj.save(f'Audio/audio{i}.mp3')
