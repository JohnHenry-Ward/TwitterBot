import tweepy
import logging

logger = logging.getLogger()

# Strore authentication credentials
def create_api():
    consumer_key = "yr8JszgNjmhizjmq1jMXmcoS2"
    consumer_secret = "x77un5VKszl2dYQeZkXZzju68346Iz3olgCAIEhbOb5aoQ4Wcv"
    access_token = "1171920714867204096-IWvwfOljOyQyPQdacrwIvC4AuZtC2S"
    access_token_secret = "gGKgVr7Rb3upOQ4yu65mxbDHuXFEiLD1erfqXuSPD3Fne"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api        
        
