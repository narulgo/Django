from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Element(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.SlugField(max_length=255,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2, default=6.10) # 12345678.10
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Element, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('store:detail', args=[self.url_clean])

    def get_discount(self, coupon):
        return (coupon.discount / Decimal(100)) * self.price # 10 /100 = 0.1 * 10$ = 1$

    def get_price_after_discount(self, coupon):
        return self.price - self.get_discount(coupon)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    element = models.ForeignKey(Element, related_name='comments', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Comentario #{}'.format(self.id)
