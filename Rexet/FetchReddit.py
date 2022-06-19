import requests
from Rexet.CreateImage import CreateTitle
from Rexet.CreateImage import CreateComments


class FetchReddit:
    def __init__(self, subreddit, listing, limit, timeframe):
        self.subreddit = subreddit
        self.listing = listing
        self.limit = limit
        self.timeframe = timeframe
        self.id()
        self.getComments()
        CreateTitle(self.subreddit, self.title, self.author)
        CreateComments(self.comments, self.comment_authors,
                       self.title, self.subreddit)

    def id(self):
        try:
            url = f'https://www.reddit.com/r/{self.subreddit}/{self.listing}.json?limit={self.limit}&t={self.timeframe}'
            request = requests.get(url, headers={'User-agent': 'rexet'})
            for i in range(self.limit):
                self.title = request.json(
                )['data']['children'][i]['data']['title']
                print(self.title)
                go = input('Use this title?[y/n]')
                if(go.lower() == 'y' or go.lower() == 'yes'):
                    break
            self.post_id = request.json()['data']['children'][i]['data']['id']
            self.author = request.json(
            )['data']['children'][i]['data']['author']
        except:
            print('Could not fetch post Post')

    def getComments(self):
        self.comments = []
        self.comment_authors = []
        n = int(input("How many comments do you want ?"))
        try:
            post_url = f'https://www.reddit.com/r/{self.subreddit}/comments/{self.post_id}.json'
            print(post_url)
            request = requests.get(post_url, headers={'User-agent': 'rexet'})
            i = x = 0
            while(i < n):
                comment = request.json()[
                    1]['data']['children'][x]['data']['body']
                comment_author = request.json()[
                    1]['data']['children'][x]['data']['author']
                x += 1
                print(comment, i+1)
                go = input('Use this comment?[y/n]')
                if(go.lower() == 'y' or go.lower() == 'yes'):
                    self.comments.append(comment)
                    self.comment_authors.append(comment_author)
                    i += 1
        except:
            print('Could not fetch comments')
