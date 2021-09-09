from django.db import models

# Create your models here.
# # 유저별로 이미지 따로 저장
# def articles_image_path(instance, filename):
#     return f'user_{instance.user.pk}/{filename}'


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    # upload_to 옵션이 없으면? --> settings.py의 MEDIA_ROOT에 설정한 폴더에 저장된다.
    # upload_to 옵션이 있으면? --> upload_to = 'uploaded_files'
    # /media/uploaded_files/ 에 저장된다.
    # upload_to = '%Y/%m/%d/' --> media/2021/09/09/ 날짜별로 저장
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title