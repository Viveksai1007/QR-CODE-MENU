from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings



def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            # This is where you'll add logic to generate the QR code
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            # Pass the data or a success message back to the template

            #generate qr code
            qr= qrcode.make(url)
            print(qr)
            file_name= restaurant_name.replace(" ","_").lower()+'_menu.png'
            file_path=os.path.join(settings.MEDIA_ROOT,file_name)  #media/rathan_restaurant_menu.png
            qr.save(file_path)
             
           #image url
            qr_url=os.path.join(settings.MEDIA_URL,file_name)
            print('media url==>', qr_url)

        
            context = {
                        'restaurant_name': restaurant_name,
                         'qr_url': qr_url,
                           'file_name':file_name,
                      }
        return render(request, 'qr_result.html', context)
         
    else:
        form = QRCodeForm()

    context = {
        'form': form,
    }
    return render(request, 'generate_qr_code.html', context)