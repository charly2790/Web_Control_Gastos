from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import Template, Context


path_raiz_proyecto = r"C:\Users\charl\Documents\Proyectos\Web_Control_Gastos"


def probando_template(request):
    mi_html = open(r"C:\Users\charl\Documents\Cursos\Python - Coderhouse\Django_1\proyecto1\templates\template1.html")

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def alta_tipo_operacion(request):

    #Django por default busca dentro del proyecto el directorio templates. Por lo que no es necesario
    #pasarle la ruta completa.
    path_alta_tipo_oper_html = open('templates/Web_Control_Gastos/form_alta_tipo_operacion.html')
    
    template_alta_tipo_oper = Template(path_alta_tipo_oper_html.read())

    path_alta_tipo_oper_html.close()

    context = Context()

    doc_template = template_alta_tipo_oper.render(context)

    return HttpResponse(doc_template)


def mostrar_datos(request,tipo_operacion_name,tipo_operacion_descripcion):
    #return HttpResponse("Hola intentaremosmostrar los datos del post")
    tp_oper_name = request.POST['tipo_operacion_name']
    tp_oper_desc = request.POST['tipo_operacion_descripcion']

    return HttpResponseRedirect(reverse(mostrar_datos))








