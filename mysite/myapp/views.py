from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
import pandas as pd
from pandas.errors import EmptyDataError
import json
from .models import Data
from .forms import ImageUploadForm
from .models import UploadedImage
import os
from .utils import format_image
import pytesseract
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from .models import Document
from django.core.files.storage import FileSystemStorage
# Specify the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
    


# def upload_image(request):
#     if request.method == 'POST':
#         history = UploadedImage.objects.all()
#         history.delete()
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_image = form.save(commit=False)
#             original_path = os.path.join(settings.MEDIA_ROOT, str(uploaded_image.original_image))
#             print(f"Printing original path - {original_path}")

#             # Format the image and save it to a formatted directory
#             formatted_path = os.path.join(settings.MEDIA_ROOT, 'formatted_uploads', str(uploaded_image.original_image))
#             os.makedirs(os.path.dirname(formatted_path), exist_ok=True)
#             format_image(original_path, formatted_path)

#             # Update the formatted_image field and save the model
#             uploaded_image.formatted_image.name = f'formatted_uploads/{uploaded_image.original_image.name}'
#             uploaded_image.save()


#             # return redirect('display_images')
#             images = UploadedImage.objects.all()
#             return render(request, 'myapp/upload.html', {'images': images})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'myapp/upload.html', {'form': form})

def upload_image(request):
    try:
        if request.method == 'POST':
            UploadedImage.objects.all().delete()
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_image = form.save()

                original_path = os.path.join(settings.MEDIA_ROOT, str(uploaded_image.original_image))
                original_dir = os.path.dirname(original_path)
                original_name, original_ext = os.path.splitext(os.path.basename(original_path))

                formatted_name = f"{original_name}_formatted{original_ext}"
                formatted_path = os.path.join(original_dir, formatted_name)

                print(f"Original path: {original_path}")
                print(f"Formatted path: {formatted_path}")
                # os.makedirs(os.path.dirname(formatted_path), exist_ok=True)
                format_image(original_path, formatted_path)

                # uploaded_image.formatted_image.name = f'formatted_uploads/{uploaded_image.original_image.name}'
                uploaded_image.formatted_image.name = os.path.join(os.path.dirname(uploaded_image.original_image.name), formatted_name)

                uploaded_image.save()
                images = UploadedImage.objects.all()
                return render(request, 'myapp/upload.html', {'form': form, 'images': images})
        else:
            form = ImageUploadForm()
    except Exception as e:
        print(f"Error processing formatted image: {e}")
        return render(request, 'myapp/upload.html', {
            'form': ImageUploadForm(),
            'error_message': 'An error occurred while processing the image. Please try again.'
        })
    except EmptyDataError:
        print(f"No columns to parse from file {images}")
    return render(request, 'myapp/upload.html', {'form': form})

def display_images(request):
    images = UploadedImage.objects.all()
    # print(images)
    return render(request, 'myapp/display.html', {'images': images})


def ocr_scan(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('document'):
        file = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        # Open the image using PIL
        img = Image.open(f'media/{filename}')

        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(img)

        # Pass details to the template
        context = {
            'image_url': file_url,
            'extracted_text': extracted_text
        }

    return render(request, 'myapp/ocr_scan.html', context)
