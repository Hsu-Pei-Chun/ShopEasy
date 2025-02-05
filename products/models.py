from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 這個會自動在新增產品時記錄時間
    updated_at = models.DateTimeField(auto_now=True)  # 這個會在每次修改產品時更新時間

    def __str__(self):
        return self.name
