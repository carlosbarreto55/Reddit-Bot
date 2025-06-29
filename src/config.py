from dataclasses import dataclass
import os
@dataclass


class Config:
    USER_AGENT:str = os.getenv ('REDDIT_USER_AGENT','RedditBot/1.0')
    BASE_URL:str = 'https://www.reddit.com/search.json'
    DEFAULT_LMT : int = 50 # can change with the user will
    RATE_LMT_DELAY:float = 1.0

    