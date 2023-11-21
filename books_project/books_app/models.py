from django.db import models

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=100,null=True)
    zipcode = models.IntegerField(null=True)
    telephone = models.CharField(max_length=20,null=True)
    recommended_by = models.ForeignKey('Author',on_delete=models.CASCADE,related_name='recommended_author',related_query_name='rec_authors',null=True)
    joindate = models.DateField()
    followers = models.ManyToManyField('User',related_name='followed_authors',related_query_name='followed_authors',)
    popularity_score = models.IntegerField()
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
class Books(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE,related_name='books',related_query_name='books')
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE,related_name='books',related_query_name='books')
    def __str__(self):
        return self.title

class Publisher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()
    def __str__(self):
        return self.firstname + ' ' + self.lastname
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)