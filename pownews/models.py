from django.db import models
from hashlib import sha256

class LinkEntry(models.Model):
  link = models.CharField(max_length=200)
  nonce = models.CharField(max_length=200)
  hashed = models.CharField(max_length=200)

  def __unicode__(self):
    return str(self.link)
