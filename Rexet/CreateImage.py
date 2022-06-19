import textwrap
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from Rexet.CreateAudio import CreateAudio


class CreateTitle():
    def __init__(self, subreddit, text, author):
        self.subreddit = subreddit
        self.text = text
        self.author = author

        self.image = Image.new('RGB', (1080, 1920), color=(24, 25, 26))

        self.fetchIcon()
        self.drawTitle()
        self.drawAuthorTitle()
        self.drawIcon()

    def fetchIcon(self):
        try:
            icon_url = f'https://www.reddit.com/r/{self.subreddit}/about.json'
            request = requests.get(icon_url, headers={'User-agent': 'yourbot'})
            icon = request.json()['data']['icon_img']
            response = requests.get(str(icon))
            img = Image.open(BytesIO(response.content))
            img = img.resize((100, 100), Image.ANTIALIAS)
            img.save('images/icons/icon.png')
            self.removeIconBg(img)
        except:
            print('could not fetch subreddit icon')

    def removeIconBg(self, img):
        # stolen from Mark Setchell to crop image in circle
        # Open the input image as numpy array, convert to RGB
        img.convert("RGB")
        npImage = np.array(img)
        h, w = img.size
        # Create same size alpha layer with circle
        alpha = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, h, w], 0, 360, fill=255)
        npAlpha = np.array(alpha)  # Convert alpha Image to numpy array
        npImage = np.dstack((npImage, npAlpha))  # Add alpha layer to RGB
        Image.fromarray(npImage).save(
            'images/icons/icon.png')  # Save with alpha

    def drawTitle(self):
        draw = ImageDraw.Draw(self.image)
        y_text = 975
        lines = textwrap.wrap(self.text, width=45)
        font = ImageFont.truetype("Font/Font.ttf", 48)
        for line in lines:
            draw.text((50, y_text),
                      line, font=font, fill=(200, 200, 200))
            y_text += 54
        self.image.save('images/0.png')

    def drawAuthorTitle(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("Font/Font.ttf", 48)
        draw.text((165, 825), f'r/{self.subreddit}',
                  fill=(200, 200, 200), font=font)
        font = ImageFont.truetype("Font/Font.ttf", 32)
        draw.text((165, 885), f'u/{self.author}',
                  fill=(200, 200, 200), font=font)
        self.image.save('images/0.png')

    def drawIcon(self):
        icon = Image.open('images/icons/icon.png').convert("RGBA")
        image = Image.open('images/0.png').convert("RGBA")
        image.paste(icon, (50, 825), icon)
        image.save("images/0.png")


class CreateComments():
    def __init__(self, comments, comment_authors, title):
        self.comments = comments
        self.comment_authors = comment_authors

        n = len(self.comments)
        for i in range(n):
            self.drawComment(comments[i], i)

        to_read = [title]
        for i in range(n):
            to_read.append(comments[i])

        CreateAudio(to_read)

    def drawDoots(self, i, h):
        upvote = Image.open('images/icons/upvote.png').convert("RGBA")
        downvote = Image.open('images/icons/downvote.png').convert("RGBA")
        backimg = Image.open(f'images/{i+1}.png').convert("RGBA")
        backimg.paste(upvote, (20, h-35), upvote)
        backimg.paste(downvote, (20, h+15), downvote)
        backimg.save(f'images/{i+1}.png')
        self.image = Image.open(f'images/{i+1}.png')
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("Font/Font.ttf", 32)
        draw.text((90, h-36), f'u/{self.comment_authors[i]}',
                  font=font, fill=(57, 57, 257))
        self.image.save(f'images/{i+1}.png')

    def drawComment(self, comment, i):
        self.image = Image.new('RGB', (1080, 1920), color=(24, 25, 26))
        draw = ImageDraw.Draw(self.image)
        lines = textwrap.wrap(comment, width=40)
        y_text = 1920
        font = ImageFont.truetype("Font/Font.ttf", 48)
        hgt = (y_text-(54*len(lines)))//2
        for line in lines:
            h = (y_text-(54*len(lines)))/2
            # print(y_text, line_height , len(lines))
            draw.text((90, h),
                      line, font=font, fill=(200, 200, 200))
            y_text += 54*2
        self.image.save(f'images/{i+1}.png')
        self.drawDoots(i, hgt)
