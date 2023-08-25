from .getObj import Objects
from django.http import HttpResponse
def obj_view(request, id):
    #data = request.GET(id) # Получение данных из GET-запросa
    
    # ... здесь вы можете начать обрабатывать полученные данные ...
    return HttpResponse(Objects.get_Obj(id))