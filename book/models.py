from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db.models import Q
from django.utils.text import slugify
from author.models import Author
from publisher.models import Publisher


class BookManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(author__name__icontains=query) |
                         Q(publisher__name__icontains=query) 
                        )
            qs = qs.filter(or_lookup).distinct()
        return qs


class Book(models.Model):
	name = models.CharField(max_length = 100)
	isbn = models.CharField(max_length = 20)
	pages = models.IntegerField()
	author = models.ForeignKey(Author, related_name='bookAuthor', on_delete=models.CASCADE, null=True, blank=True)
	publisher = models.ForeignKey(Publisher, related_name='bookPublisher', on_delete=models.CASCADE, null=True, blank=True)
	slug = AutoSlugField(unique = True, populate_from='name', db_index=True, editable = True, null=True, blank=True)

	created_by = models.TextField(null=True, blank=True) # User related
	updated_by = models.TextField(null=True, blank=True) # User related

	created_on = models.DateTimeField(auto_now_add=True)
	last_updated_on = models.DateTimeField(auto_now=True)

	objects = BookManager()

	class Meta:
		pass

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse("book:book_detail", args=[str(self.slug)])


	def get_update_url(self):
		return reverse("book:book_update", args=[str(self.slug)])

class Cost(models.Model):
	publisher = models.ForeignKey(Publisher, related_name='costPublisher', on_delete=models.CASCADE, null=True, blank=True)
	cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

	class Meta:
		pass

	def __str__(self):
		return str(self.cost)

	def get_absolute_url(self):
		return reverse("publisher:cost_detail", args=[str(self.slug)])


	def get_update_url(self):
		return reverse("publisher:cost_update", args=[str(self.slug)])