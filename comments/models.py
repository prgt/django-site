from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone



class Comment(models.Model):
    comment_name = models.CharField('Username', max_length = 200)
    comment_email = models.CharField('Email', max_length = 200)
    comment_text = models.CharField('Text', max_length = 200)
    pub_date = models.DateTimeField('Date published')
	# If True comment enabled
    enabled = models.BooleanField('Enabled', default = False)
    user_id = models.IntegerField('User ID', default = 0)
    def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        out = 'Name: ' + self.comment_name + ' || Email: ' + self.comment_email
        return out
