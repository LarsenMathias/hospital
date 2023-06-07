from django.db import models
import io
import os
import qrcode

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Document(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='')
    qr_code = models.ImageField(upload_to='', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.file and not self.qr_code:
            qr_code_image = self.generate_qr_code()
            self.qr_code.save(f'{self.file.name}.png', qr_code_image, save=True)

    def generate_qr_code(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.file.url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill='black', back_color='white')

        # Create a BytesIO object to store the image data
        qr_image_bytes = io.BytesIO()
        qr_image.save(qr_image_bytes, format='PNG')
        qr_image_bytes.seek(0)

        return qr_image_bytes
    def __str__(self) -> str:
        return self.name