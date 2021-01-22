from django.shortcuts import render
from .forms import ImageForm


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'photo_gallery/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'photo_gallery/index.html', {'form': form})

def display(request): 
  
    if request.method == 'GET': 
        Images = Image.objects.all()  
        return render((request, 'display_images.html', 
                     {'display_image' : Images}))