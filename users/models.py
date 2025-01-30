import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import mimetypes


def user_avatar_path(instance, filename):
    """
    讓檔案名稱維持 `userID_原始檔名`
    """
    ext = filename.split(".")[-1]  # 取得副檔名 (jpg, png, etc.)
    filename = f"{instance.user.id}_{filename}"  # 確保包含 user.id
    return os.path.join("avatars", str(instance.user.id), filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=user_avatar_path, null=True, blank=True
    )  # 指定正確的 upload_to

    def __str__(self):
        return self.user.username


@receiver(pre_save, sender=UserProfile)
def update_avatar_content_type(sender, instance, **kwargs):
    """
    確保上傳到 S3 的圖片擁有正確的 Content-Type
    """
    if instance.avatar:
        content_type, _ = mimetypes.guess_type(instance.avatar.name)
        if content_type:
            instance.avatar.file.content_type = content_type
