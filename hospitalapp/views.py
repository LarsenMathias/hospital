from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document, Patient
from django.http import HttpResponse
import qrcode
import io
def upload_success(request):
    if request.method == 'POST':
        # Handle the file upload and save the document
        
        # Generate the QR code for the uploaded file
        document = Document.objects.last()  # Assuming the latest uploaded document is the one to generate the QR code for
        qr_code = generate_qr_code(document.file.url)

        return render(request, 'upload_success.html', {'qr_code': qr_code})
    
    return redirect('upload')  # Redirect to the upload page if the request method is not POST
def generate_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')

    # Create a BytesIO object to store the image data
    qr_img_bytes = io.BytesIO()
    qr_img.save(qr_img_bytes, format='PNG')
    qr_img_bytes.seek(0)

    return qr_img_bytes

def upload(request):
    if request.method == 'POST':
        posts=Document.objects.all()
        form = DocumentForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
        context={'form':form,
                 'posts':posts}
        return render(request,'upload.html',context)    
    form=DocumentForm()
    posts=Document.objects.all()       
    context={'form':form,
                 'posts':posts}
    return render(request,'upload.html',context)


