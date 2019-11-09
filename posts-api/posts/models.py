from django.db import models


class Company(models.Model):
    catchPhrase = models.CharField(max_length=255)
    bs = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.name


class Adress(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    class Meta:
        db_table = "adress"

    def __str__(self):
        return self.street + " " + self.suite


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    Adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "post"

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return self.name
