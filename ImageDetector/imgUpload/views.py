from django.shortcuts import render
from .forms import ImageUploadForm
import keras
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image


def handle_uploaded_file(f):
    with open('uploaded_image.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def imageprocess(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])

        model = ResNet50(weights='imagenet')
        img_path = 'uploaded_image.jpg'

        # prediction
        image_file = keras.utils.load_img(img_path, target_size=(224, 224))
        x = keras.utils.img_to_array(image_file)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        html = decode_predictions(preds, top=3)[0]
        res = []
        for e in html:
            res.append((e[1], np.round(e[2]*100, 2)))
        return render(request, 'results.html', {'results': res})


    return render(request, 'home.html')