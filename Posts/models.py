from django.db import models
from PIL import Image
from django.db import models

# from uuid import uuid4
# Create your models here.
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')



class Post(models.Model):
    title=models.CharField( max_length=50)
    caption=models.TextField()
    field_name=models.ImageField( upload_to="post_files/")
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.field_name.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.field_name.path)
            

    # field_name = models.FileField(upload_to='post_files/', max_length=254, validators=[validate_file_extension])
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    posted_time=models.DateField(auto_now_add=True)
    like=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Tags(models.Model):
    title=models.ForeignKey(Post, on_delete=models.CASCADE)
    # title=models.CharField( max_length=50)
    
    def __str__(self):
        return self.title