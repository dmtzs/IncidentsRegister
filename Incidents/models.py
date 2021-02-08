from django.db import models
import ckeditor.fields as ck

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
    Extras= models.FileField(verbose_name= "Another extras", upload_to= "ExtrasEv")