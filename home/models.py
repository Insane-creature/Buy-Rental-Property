from django.db import models

# Create your models here.
# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations


class Contact(models.Model):
        name = models.CharField(max_length=122)
        email = models.CharField(max_length=122)
        query = models.TextField()
        date = models.DateField()

        # def __str__(self):
        #     return self.name
              
        

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})