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

class Country(models.Model):

    #  Fields
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 100, null=True, blank=True)
    phone_code = models.CharField(max_length = 100, null=True, blank=True)
    currency_code = models.CharField(max_length = 100, null=True, blank=True)
    currency_symbol = models.CharField(max_length = 100, null=True, blank=True)    
    slug = AutoSlugField(unique = True, populate_from='name', db_index=True, editable = True, null=True, blank=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("publisher:country_detail", args=[str(self.slug)])

    def get_update_url(self):
        return reverse("publisher:country_update", args=[str(self.slug)])

class State(models.Model):

    #  Fields
    country = models.ForeignKey(Country, related_name='stateCountry', on_delete=models.CASCADE, null=True, blank=True)
    state = models.CharField(max_length = 100)
    slug = AutoSlugField(unique = True, populate_from='state', db_index=True, editable = True, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        # return f"{self.state}"
        return f"{self.state}, {self.country}"

    def get_absolute_url(self):
        return reverse("publisher:state_detail", args=[str(self.slug)])

    def get_update_url(self):
        return reverse("publisher:state_update", args=[str(self.slug)])


class District(models.Model):

    #  Fields
    state = models.ForeignKey(State, related_name='districtState', on_delete=models.CASCADE, null=True, blank=True)
    district = models.CharField(max_length = 100)
    slug = AutoSlugField(unique = True, populate_from='district', db_index=True, editable = True, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return f"{self.district}, {self.state}"
        # return f"{self.state}, {self.country}"

    def get_absolute_url(self):
        return reverse("publisher:district_detail", args=[str(self.slug)])

    def get_update_url(self):
        return reverse("publisher:district_update", args=[str(self.slug)])



class Publisher(models.Model):
	name = models.CharField(max_length = 100)
	address_line = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	district = models.ForeignKey(District, related_name='publisherDistrict', on_delete=models.CASCADE, null=True, blank=True)
	state = models.ForeignKey(State, related_name='publisherState', on_delete=models.CASCADE, null=True, blank=True)
	country = models.ForeignKey(Country, related_name='publisherCountry', on_delete=models.CASCADE, null=True, blank=True)
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