import tweepy
import logging
from config import create_api
import time
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def daysToChristmas():
    logger.info("Calculating days til December 25")
    today = datetime.date.today()
    christmas = datetime.date(2019, 12, 25)
    daysTil = christmas - today
    return daysTil.days

def main():
    api = create_api()
    while True:
        daysTil = daysToChristmas()
        api.update_status(str(daysTil) + " days til Christmas.")
        logger.info("Tweeted: " + str(daysTil) + " days til Christmas.")
        logger.info("Be back in 24 hours...")
        time.sleep(86400)

if __name__ == "__main__":
    main()
