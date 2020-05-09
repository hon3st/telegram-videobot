import os
import telebot
from enum import Enum
from twitter_api import TwitterApi
from twitter_downloader import TwitterDownloader
from url_helper import UrlHelper

SUPPORTED_DOMAINS = {
  'twitter': 'twitter.com'
}

bot = telebot.TeleBot(os.getenv('TELEGRAM_KEY'))
url_helper = UrlHelper(SUPPORTED_DOMAINS.values())
twitter_downloader = TwitterDownloader(
  TwitterApi(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET')),
  url_helper
)

@bot.message_handler(content_types=['text'])
def handle_message(message):
  if not url_helper.is_url_valid(message.text):
    return bot.send_message(message.from_user.id, "Send me some url!")

  if not url_helper.is_supported_domain(message.text):
    supported_domains_formatted = ', '.join(SUPPORTED_DOMAINS.values())
    return bot.send_message(
      message.from_user.id,
      'This website is not supported :( I only support {}'.format(supported_domains_formatted)
    )

  send_video(message)

def send_video(message):
  url = message.text
  video_downloader = get_video_downloader(url)
  video_url = video_downloader.call(url)

  if video_url:
    bot.send_video(message.from_user.id, video_url)
  else:
    bot.send_message(message.from_user.id, 'Could not extract video')

def get_video_downloader(url):
  domain = url_helper.get_domain(url)

  if domain == SUPPORTED_DOMAINS['twitter']:
    return twitter_downloader

bot.polling(none_stop=True, interval=0)
