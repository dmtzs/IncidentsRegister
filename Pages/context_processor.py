from Pages.models import PageModel

def get_pages(request):
    pages= PageModel.objects.filter(visible= True).values_list("id", "title", "slug")

    return{
        "pages": pages
    }
    #Este context processor es apra poder mostrar en el panel de administración lo que deseo de los campos de la base de datos.