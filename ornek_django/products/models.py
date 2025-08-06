# Django veritabanı modelleri için gerekli modülü import ediyoruz
# models modülü, Django ORM (Object-Relational Mapping) için kullanılır
# Bu modül ile veritabanı tablolarını Python sınıfları olarak tanımlayabiliriz
from django.db import models

# =============================================================================
# DJANGO MODELS.PY VERİTABANI MODEL TANIMLAMA DOSYASI
# =============================================================================
#
# Bu dosya, Django uygulamasının veritabanı modellerini tanımlar.
# Modeller, veritabanı tablolarını Python sınıfları olarak temsil eder.
# Django ORM, bu modelleri kullanarak veritabanı işlemlerini otomatikleştirir.
#
# Model Sınıflarının Özellikleri:
# - Veritabanı tablolarını temsil eder
# - Otomatik CRUD işlemleri sağlar (Create, Read, Update, Delete)
# - Veri doğrulama ve kısıtlamaları içerir
# - İlişkisel veritabanı özelliklerini destekler
# - Django admin paneli ile entegre çalışır
#
# Bu dosyada tanımlanan modeller:
# - Product: Ürün bilgilerini saklayan ana model
# =============================================================================

# =============================================================================
# PRODUCT MODEL SINIFI
# =============================================================================
#
# Bu sınıf, ürün bilgilerini saklamak için kullanılan veritabanı modelidir.
# Django, bu sınıfı kullanarak otomatik olarak bir veritabanı tablosu oluşturur.
# Model sınıfları, Django'nun models.Model sınıfından türetilmelidir.
class Product(models.Model):
    # =============================================================================
    # MODEL ALANLARI (VERİTABANI KOLONLARI)
    # =============================================================================

    # Ürün adı alanı
    # CharField: Metin verisi için kullanılır
    # max_length=100: Maksimum 100 karakter uzunluğunda
    # Bu alan, veritabanında VARCHAR(100) olarak oluşturulur
    name = models.CharField(max_length=100)

    # Ürün fiyatı alanı
    # DecimalField: Ondalıklı sayı verisi için kullanılır
    # max_digits=10: Toplam 10 basamak (nokta dahil)
    # decimal_places=2: Ondalık kısımda 2 basamak
    # Örnek: 12345678.90 (8+2=10 basamak)
    # Bu alan, veritabanında DECIMAL(10,2) olarak oluşturulur
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Stok miktarı alanı
    # IntegerField: Tam sayı verisi için kullanılır
    # default=0: Varsayılan değer 0
    # Bu alan, veritabanında INTEGER DEFAULT 0 olarak oluşturulur
    stock = models.IntegerField(default=0)

    # Oluşturulma tarihi alanı
    # DateTimeField: Tarih ve saat verisi için kullanılır
    # auto_now_add=True: Kayıt oluşturulduğunda otomatik olarak şu anki tarih/saat atanır
    # Bu alan, veritabanında DATETIME olarak oluşturulur
    # Değiştirilemez (sadece oluşturulma anında set edilir)
    created_at = models.DateTimeField(auto_now_add=True)

    # =============================================================================
    # MODEL METODLARI
    # =============================================================================

    # String temsil metodu
    # Bu metod, model nesnesinin string olarak nasıl görüneceğini belirler
    # Django admin panelinde, form'larda ve shell'de görüntülenir
    # Örnek: Product.objects.first() çağrıldığında ürün adını döndürür
    def __str__(self):
        return self.name

    # =============================================================================
    # OPSİYONEL ÖZELLİKLER (Şu anda kullanılmıyor)
    # =============================================================================
    #
    # Diğer yaygın model özellikleri:
    #
    # class Meta:
    #     verbose_name = 'Ürün'
    #     verbose_name_plural = 'Ürünler'
    #     ordering = ['-created_at']  # Varsayılan sıralama
    #     db_table = 'custom_products'  # Özel tablo adı
    #
    # # Özel metodlar
    # def is_in_stock(self):
    #     return self.stock > 0
    #
    # def get_display_price(self):
    #     return f"₺{self.price}"
    #
    # # Özel alanlar
    # description = models.TextField(blank=True, null=True)
    # is_active = models.BooleanField(default=True)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tag')
    #
    # # Dosya alanları
    # image = models.ImageField(upload_to='products/', blank=True)
    # file = models.FileField(upload_to='documents/', blank=True)
    # =============================================================================