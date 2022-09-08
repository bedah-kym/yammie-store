from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

CATEGORY_CHOICES=[
    ('cow products','for cows'),
    ('chicken products','for chicken'),
    ('pig products','for pigs'),
    ('general feeds','for any')
]
class Item(models.Model):
    title = models.CharField(max_length=50)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=30)
    description = models.TextField(default=True)
    in_stock = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    item_image = models.ImageField(null=False,upload_to="product_pics")


    def __str__(self):
        return self.title

    def get_add_to_cart_url(self):
        return reverse('Shop:add_to_cart', kwargs={'product_id' : self.pk})

    def get_remove_from_cart_url(self):
        return reverse('Shop:remove_from_cart', kwargs={'product_id' : self.pk})

    def save(self):
        super().save()
        img = Image.open(self.item_image.path)
        if img.width > 100 or img.height > 100:
            outputsize=(200,200)
            img.thumbnail(outputsize)
            img.save(self.item_image.path)



class CartItem (models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} bag(s) of {self.item.weight}kg {self.item}"

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
