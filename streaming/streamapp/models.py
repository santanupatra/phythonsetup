# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Role(models.Model):
    role = models.CharField(max_length=10)
    def __str__(self):
        return (str(self.role))

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    ROLES_LIST = (
        ('Moderator', 'Moderator'),
        ('Streamer', 'Streamer'),
        ('Viewer', 'Viewer'),
        ('Subscriber', 'Subscriber'),
    )
    # role = models.CharField(max_length=10,
    # 								choices=ROLES_LIST,
    #                                 default='Moderator')
    role = models.ForeignKey(Role)

    def __str__(self):
        return (str(self.user))

class PointResult(models.Model):
    user = models.ForeignKey(User, unique=True)
    serial_number = models.IntegerField()
    on_viewer_now = models.BooleanField(default=False)
    chat_weekly = models.IntegerField(default=False)
    chat_total = models.IntegerField()
    weekly = models.IntegerField()
    total = models.IntegerField()
    weekly_streams = models.IntegerField()
    total_streams = models.IntegerField()

    def __str__(self):
        return (str(self.user))

class BlogCategorie(models.Model):
	category = models.CharField(max_length=30)

	def __str__(self):
		return (str(self.category))

class Blog(models.Model):
	blog_id = models.AutoField(primary_key=True)
	blog_category = models.ForeignKey(BlogCategorie)
	blog_content = models.TextField()
	added_by = models.ForeignKey(User, unique=False)
	created_at = models.DateTimeField(default=datetime.now, blank=False)
	last_edited = models.DateTimeField(default=datetime.now, blank=False)

	def __str__(self):
		return (str(self.blog_id))

class BlogComment(models.Model):
	comment_id = models.AutoField(primary_key=True)
	blog = models.ForeignKey(Blog, unique=False)
	comment = models.TextField()
	is_approved = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=datetime.now, blank=False)
	last_edited = models.DateTimeField(default=datetime.now, blank=False)

	def __str__(self):
		return (str(self.comment_id))