import validators
from tld import get_tld

class UrlHelper:
  def __init__(self, supported_domains):
    self.supported_domains = supported_domains

  def is_url_valid(self, url):
    return validators.url(url)

  def is_supported_domain(self, url):
    domain = self.get_domain(url)
    return any(domain == supported_domain for supported_domain in self.supported_domains)

  def get_domain(self, url):
    return get_tld(url, as_object=True).fld

  def get_path(self, url):
    return get_tld(url, as_object=True).parsed_url.path
