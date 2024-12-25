from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
import pandas as pd
from pandas.errors import EmptyDataError
import json
from .models import Data


# Create your views here.
def hello(request):
    # return HttpResponse('Hello There')
    # return HttpResponse('<h1>Hello There</h1>')  
    # name = 'Aru'
    # context = {
    #     'name' : name
    # }
    # print(request.method)
    # if(request.method=='POST'):
    #     print('This is a POST request')
    #     name = request.POST.get('name')
    #     print(name)
    # else:
    #     print('This is a GET request')
    try:
        if(request.method=='POST'):
            # print(request.FILES['file'])
            history = Data.objects.all()
            history.delete()
            filename = request.FILES['file']
            # print(pd.read_csv(filename))
            df = pd.read_csv(filename)
            json_records = df.reset_index().to_json(orient='records')
            data = []
            data = json.loads(json_records)
            # print(data)
            # print(json_records)
            for d in data:
                name = d['property_name']
                price = d['property_price']
                rent = d['property_rent']
                emi = d['emi']
                tax = d['tax']
                exp = d['other_exp']
                monthly_expenses = emi + tax + exp
                monthly_income = rent - monthly_expenses
                dt = Data(name=name,price=price,rent=rent,emi=emi,tax=tax,exp=exp,monthly_expenses=monthly_expenses,monthly_income=monthly_income)
                dt.save()
                # print('File Uploaded successfully')
            data_objects = Data.objects.all()
            context = {'data_objects' : data_objects}
            return render(request, 'myapp/index.html', context)
        else:
            print('This is a GET request')
    except EmptyDataError:
        print(f"No columns to parse from file {filename}")
    return render(request, 'myapp/index.html')

def thirukkural(request):
    import json
    import os
    json_file_path = os.path.join(settings.BASE_DIR, 'detail.json')
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return render(request, 'myapp/thirukkural.html', {'data': data})
    except FileNotFoundError:
        e_message = f"File not found: {json_file_path}"
        print(e_message)
        return JsonResponse({'error': e_message}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Error decoding JSON'}, status=400)