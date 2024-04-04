# Generated by Django 4.2.4 on 2024-03-25 20:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mmablog.models.BlogPostModel
import mmablog.models.BlogSubPostModel
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogContact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('message', models.CharField(max_length=400)),
                ('contacted_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('ip_information', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('topic_image', models.ImageField(blank=True, null=True, upload_to=mmablog.models.BlogPostModel.topic_image_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])),
                ('topic', models.CharField(blank=True, max_length=250, null=True)),
                ('article', models.TextField(blank=True, null=True)),
                ('total_clicks', models.BigIntegerField(default=0)),
                ('total_comments', models.BigIntegerField(default=0)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(related_name='%(class)s_author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmablog.blogcategory')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_publisher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSubPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('topic_image', models.ImageField(blank=True, null=True, upload_to=mmablog.models.BlogSubPostModel.topic_image_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])),
                ('topic', models.CharField(blank=True, max_length=250, null=True)),
                ('article', models.TextField(blank=True, null=True)),
                ('total_clicks', models.BigIntegerField(default=0)),
                ('total_comments', models.BigIntegerField(default=0)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(related_name='%(class)s_author', to=settings.AUTH_USER_MODEL)),
                ('blogheadline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmablog.blogpost')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmablog.blogcategory')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_publisher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('message', models.CharField(max_length=400)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('ip_information', models.JSONField(blank=True, null=True)),
                ('blogheadline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmablog.blogpost')),
            ],
        ),
    ]