from django.db import models
from io import BytesIO
import qrcode
from django.core.files import File
from django.core.validators import URLValidator

class QRCodeModel(models.Model):
    link = models.URLField(max_length=200, validators=[URLValidator()])
    name = models.CharField(max_length=100, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.link)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        self.qr_code.save(f'{self.name}.png', File(img_io), save=False)

    class Meta:
        permissions = [
            ("can_update_qrcode", "Can update QR code"),
            ("can_delete_qrcode", "Can delete QR code"),
        ]
