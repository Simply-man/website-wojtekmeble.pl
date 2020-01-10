from django.db import models
from django.utils.html import format_html
from django.utils import timezone

# Add some picture


class Pictures(models.Model):
    picture = models.ImageField(upload_to="images/")
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.picture)
