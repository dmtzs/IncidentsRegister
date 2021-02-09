from django.db import models
from django.contrib.auth.models import User
import ckeditor.fields as ck, django_countries.fields as countries
#Buscar django-countries para mas info de ese campo.

# Create your models here.
class RegIncident(models.Model):
    CompleteDate= models.DateField(verbose_name= "Date")
    Application= models.CharField(verbose_name= "Application Name", max_length= 30)
    SealID= models.CharField(verbose_name= "SealID", max_length= 10)
    Severity= models.CharField(verbose_name= "Severity", max_length= 4)
    TicketNum= models.CharField(verbose_name= "Ticket", unique= True, max_length= 13)
    StartTime= models.TimeField(verbose_name= "Start Hour")
    EndTime= models.TimeField(verbose_name= "End Hour")
    IssueDesc= ck.RichTextField(verbose_name= "Issue description")
    ReportTo= models.CharField(verbose_name= "Report to regulator?", max_length= 3)
    Impact= ck.RichTextField(verbose_name= "Impact")
    RegBy= models.ForeignKey(User, verbose_name= "Registered by", on_delete= models.PROTECT)
    ReportedBy= models.CharField(verbose_name= "Reported by")
    Country= countries.CountryField(verbose_name= "Country")
    Extras= models.FileField(verbose_name= "Another extras", upload_to= "ExtrasEv")
    #Checar si se necesita relación de muchos a muchos entre la tabla de usuarios default y esta tabla.

    class Meta():
        verbose_name= "Incident"
        verbose_name_plural= "Incidents"

    def __str__(self):
        return self.TicketNum