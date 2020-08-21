from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db.models import Q
from django.utils.text import slugify


class PublisherManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(state__icontains=query) |
                         Q(country__icontains=query) 
                        )
            qs = qs.filter(or_lookup).distinct()
        return qs


class Publisher(models.Model):
	name = models.CharField(max_length = 100)
	address_line = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	state = models.CharField(max_length = 200)
	country = models.CharField(max_length = 200)
	pincode = models.CharField(max_length = 200)
	slug = AutoSlugField(unique = True, populate_from='name', db_index=True, editable = True, null=True, blank=True)

	created_by = models.TextField(null=True, blank=True) # User related
	updated_by = models.TextField(null=True, blank=True) # User related

	created_on = models.DateTimeField(auto_now_add=True)
	last_updated_on = models.DateTimeField(auto_now=True)

	objects = PublisherManager()

	class Meta:
		pass

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse("publisher:publisher_detail", args=[str(self.slug)])


	def get_update_url(self):
		return reverse("publisher:publisher_update", args=[str(self.slug)])