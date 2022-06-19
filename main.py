from Rexet.FetchReddit import FetchReddit


subreddit = 'AskReddit'
limit = 20  # max 100
timeframe = 'day'  # hour, day, week, month, year, all
listing = 'top'  # controversial, best, hot, new, random, rising, top

FetchReddit(subreddit, listing, limit, timeframe)
