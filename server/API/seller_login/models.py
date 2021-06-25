from django.db import models

# Create your models here.


from django.conf import settings


class categories(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=2)
    Category_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Category_Name + ' | ' + self.Seller.email
        # return self.Category_Name


def ss(instance, filename):
    ext = filename.split('.')[-1]
    new_ext = 'jpg'
    prev = instance.Product_Name + '_' + str(instance.Seller)
    if instance:
        return 'products/{}.{}'.format(prev, new_ext)


class products(models.Model):
    Product_Name = models.CharField(max_length=200)
    Price = models.IntegerField()
    Category = models.ForeignKey(categories, on_delete=models.CASCADE)
    Seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=2)
    Image = models.ImageField(blank=False, null=False, upload_to=ss)

    def __str__(self):
        return self.Product_Name

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)
