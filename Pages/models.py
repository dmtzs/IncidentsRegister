from django.db import models
import ckeditor.fields as ck

# Create your models here.
class PageModel(models.Model):
    title= models.CharField(max_length=50, verbose_name="Title")
    content= ck.RichTextField(verbose_name="Content")
    slug= models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    order= models.IntegerField(default=0, verbose_name="Order")
    visible= models.BooleanField(verbose_name="Visible?")
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta():
        verbose_name= "URL page"
        verbose_name_plural= "URL pages"
    
    def __str__(self):
        return self.title
        #Con esto imprime el título de cada una de las páginas del panel de admon.