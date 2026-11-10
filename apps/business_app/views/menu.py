from django.shortcuts import render
from django.apps import apps

def business_menu(request):
    app_label = 'business_app'
    models_info = []
    for model in apps.get_app_config(app_label).get_models():
        admin_url = f"/admin/{app_label}/{model._meta.model_name}/"
        models_info.append({
            'name': model._meta.verbose_name_plural,
            'model_name': model._meta.model_name,
            'admin_url': admin_url,
        })
    return render(request, 'business_app/menu.html', {'models': models_info})
