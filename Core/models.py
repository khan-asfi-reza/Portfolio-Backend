from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=200, verbose_name="Sender Name")
    email = models.EmailField(verbose_name="Sender Email")
    message = models.TextField(verbose_name="Message")
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ["-time_stamp"]
        verbose_name = "Client Message"
        verbose_name_plural = "Client Messages"
