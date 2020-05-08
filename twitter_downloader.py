class TwitterDownloader:
  def __init__(self, twitter_api, url_helper):
    self.twitter_api = twitter_api
    self.url_helper = url_helper

  def call(self, url):
    status_id = self.get_status_id(url)
    tweet_data = self.twitter_api.get_tweet(status_id)
    video_media = self.get_video_media(tweet_data)
    if not video_media:
      return None

    video_data = self.get_appropriate_video(video_media)
    return video_data['url']

  def get_video_media(self, tweet_data):
    medias = tweet_data.get('extended_entities', {}).get('media')

    if not medias:
      return None

    return next((media for media in medias if media.get('type') == 'video'), None)

  def get_appropriate_video(self, video_media):
    return max(video_media['video_info']['variants'], key=lambda variant: variant.get('bitrate', 0))

  def get_status_id(self, url):
    path = self.url_helper.get_path(url)
    return path.split('status/')[1]
