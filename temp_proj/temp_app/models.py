from django.db import models

# Create your models here.

from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

# class Place(models.Model):
#     name = models.CharField(max_length=200)
#     # featured_image = models.ImageField(upload_to="places/images/")
#     Place = models.CharField(max_length=200)
#     category = models.ForeignKey("places.Category", on_delete=models.CASCADE)
#     description = models.TextField()
#     is_deleted = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = "places_place"
#
#     def __str__(self):
#         return self.name
#
#
# class Category(models.Model):
#     # image = models.ImageField(upload_to="categories/images/")
#     name = models.CharField(max_length=200)
#
#     class Meta:
#         db_table = "places_category"
#         verbose_name_plural = "categories"
#
#     def __str__(self):
#         return self.name


# class Gallery(models.Model):
#     place = models.ForeignKey("places.Place",on_delete=models.CASCADE)
#     # image = models.ImageField(upload_to="places/images/")
#
#     class Meta:
#         db_table = "places_gallery"
#         verbose_name_plural = "gallery"
#
#     def __str__(self):
#         return str(self.id)


# class Comment(models.Model):
#     name = models.CharField(max_length=200)
#     date = models.DateTimeField(auto_now=True)
#     description = models.TextField()
#     id_com = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = "places_comments"
#         verbose_name_plural = "comments"
#
#     def __str__(self):
#         return str(self.id)
