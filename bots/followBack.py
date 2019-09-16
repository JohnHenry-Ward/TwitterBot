#followBack.py looks at who is following it every minute
#if it is not following the user, it will then follow it

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def followBack(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    running = True;
    while (running):
        followBack(api)
        logger.info("Waiting...")
        #time.sleep(60)
        running = False;

if __name__ == "__main__":
    main()
