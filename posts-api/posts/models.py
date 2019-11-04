from django.db import models

class Profile(models.Model):
    name = models.CharField(max_lenght=255)
    email = models.EmailField()

    class Meta:
        db_table = "profile"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_lenght=255)
    body = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_lenght=255)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return self.name
