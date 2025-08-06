# Django REST Framework - Derinlemesine Mimari Rehberi

Bu proje, Django REST Framework'ün temel bileşenlerinin (Models, Serializers, Views, Database) nasıl birlikte çalıştığını ve veri akışının nasıl gerçekleştiğini derinlemesine açıklar.

## 📋 İçindekiler

1. [Proje Yapısı](#proje-yapısı)
2. [Veri Akışı Mimarisi](#veri-akışı-mimarisi)
3. [Models (Modeller)](#models-modeller)
4. [Serializers (Serileştiriciler)](#serializers-serileştiriciler)
5. [Views (Görünümler)](#views-görünümler)
6. [Database Bağlantıları](#database-bağlantıları)
7. [URL Routing](#url-routing)
8. [Pratik Örnekler](#pratik-örnekler)
9. [Gelişmiş Konular](#gelişmiş-konular)

## 🏗️ Proje Yapısı

```
ornek_django/
├── core/                    # Ana proje ayarları
│   ├── settings.py         # Django ayarları
│   ├── urls.py            # Ana URL yönlendirmeleri
│   ├── asgi.py            # ASGI konfigürasyonu
│   └── wsgi.py            # WSGI konfigürasyonu
├── products/              # Ürünler uygulaması
│   ├── models.py          # Veritabanı modelleri
│   ├── serializers.py     # API serileştiricileri
│   ├── views.py           # API görünümleri
│   ├── urls.py            # Uygulama URL'leri
│   ├── admin.py           # Admin panel konfigürasyonu
│   └── tests.py           # Test dosyaları
├── manage.py              # Django yönetim aracı
└── db.sqlite3             # SQLite veritabanı
```

## 🔄 Veri Akışı Mimarisi

Django REST Framework'te veri akışı şu şekilde gerçekleşir:

```
HTTP Request → URL Router → View → Serializer → Model → Database
                ↓
HTTP Response ← Serializer ← View ← Model ← Database
```

### Detaylı Veri Akışı:

1. **HTTP Request** → Kullanıcı API'ye istek gönderir
2. **URL Router** → İsteği uygun view'a yönlendirir
3. **View** → İsteği işler ve serializer'ı kullanır
4. **Serializer** → Veriyi dönüştürür (JSON ↔ Model)
5. **Model** → Veritabanı işlemlerini gerçekleştirir
6. **Database** → Veriyi saklar veya getirir
7. **Response** → Sonuç JSON formatında döndürülür

## 🗄️ Models (Modeller)

### Model Nedir?

Model, veritabanı tablolarını Python sınıfları olarak temsil eden Django ORM bileşenidir.

### Product Model Analizi:

```python
class Product(models.Model):
    name = models.CharField(max_length=100)           # VARCHAR(100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # DECIMAL(10,2)
    stock = models.IntegerField(default=0)            # INTEGER DEFAULT 0
    created_at = models.DateTimeField(auto_now_add=True)  # DATETIME
```

### Model Alanları ve Veritabanı Karşılıkları:

| Django Field | Veritabanı Türü | Açıklama |
|--------------|-----------------|----------|
| `CharField` | VARCHAR | Metin verisi |
| `DecimalField` | DECIMAL | Ondalıklı sayı |
| `IntegerField` | INTEGER | Tam sayı |
| `DateTimeField` | DATETIME | Tarih ve saat |
| `TextField` | TEXT | Uzun metin |
| `BooleanField` | BOOLEAN | True/False |
| `ForeignKey` | FOREIGN KEY | İlişkisel bağlantı |

### Model İşlemleri:

```python
# Oluşturma
product = Product.objects.create(name="Laptop", price=999.99, stock=10)

# Okuma
products = Product.objects.all()  # Tüm ürünler
product = Product.objects.get(id=1)  # Tek ürün
filtered = Product.objects.filter(price__gte=100)  # Filtreleme

# Güncelleme
product.price = 899.99
product.save()

# Silme
product.delete()
```

## 🔄 Serializers (Serileştiriciler)

### Serializer Nedir?

Serializer, Django modellerini JSON/XML formatına dönüştüren ve tersine dönüştüren bileşendir.

### ProductSerializer Analizi:

```python
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Tüm alanları dahil et
```

### Serializer İşlemleri:

#### 1. Serialization (Model → JSON):
```python
# Model nesnesini JSON'a dönüştürme
product = Product.objects.get(id=1)
serializer = ProductSerializer(product)
json_data = serializer.data
# Sonuç: {"id": 1, "name": "Laptop", "price": "999.99", "stock": 10, "created_at": "2024-01-01T10:00:00Z"}
```

#### 2. Deserialization (JSON → Model):
```python
# JSON verisini model nesnesine dönüştürme
json_data = {"name": "Mouse", "price": "29.99", "stock": 50}
serializer = ProductSerializer(data=json_data)
if serializer.is_valid():
    product = serializer.save()  # Veritabanına kaydet
```

### Gelişmiş Serializer Özellikleri:

```python
class ProductSerializer(serializers.ModelSerializer):
    # Hesaplanmış alan
    is_in_stock = serializers.SerializerMethodField()

    # Özel alan doğrulama
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Fiyat 0'dan büyük olmalıdır.")
        return value

    # Hesaplanmış alan metodu
    def get_is_in_stock(self, obj):
        return obj.stock > 0

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'is_in_stock', 'created_at']
```

## 👁️ Views (Görünümler)

### View Nedir?

View, HTTP isteklerini işleyen ve uygun yanıtları döndüren Django bileşenidir.

### API View Türleri:

#### 1. Generic Views (Hazır View'lar):

```python
# ListCreateAPIView - Liste ve oluşturma
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # GET: Tüm ürünleri listeler
    # POST: Yeni ürün oluşturur

# RetrieveUpdateDestroyAPIView - Detay, güncelleme, silme
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # GET: Tek ürün detayı
    # PUT/PATCH: Ürün günceller
    # DELETE: Ürün siler
```

#### 2. View İşlem Akışı:

```python
# GET /api/products/ isteği geldiğinde:
class ProductListCreateAPIView(generics.ListCreateAPIView):
    def get(self, request):
        # 1. Queryset'i al
        products = Product.objects.all()

        # 2. Serializer ile JSON'a dönüştür
        serializer = ProductSerializer(products, many=True)

        # 3. JSON yanıtı döndür
        return Response(serializer.data)

# POST /api/products/ isteği geldiğinde:
    def post(self, request):
        # 1. JSON verisini al
        serializer = ProductSerializer(data=request.data)

        # 2. Veriyi doğrula
        if serializer.is_valid():
            # 3. Veritabanına kaydet
            product = serializer.save()
            # 4. Başarılı yanıt döndür
            return Response(serializer.data, status=201)
        else:
            # 5. Hata yanıtı döndür
            return Response(serializer.errors, status=400)
```

### Gelişmiş View Özellikleri:

```python
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Filtreleme
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'price']
    search_fields = ['name']

    # Sayfalama
    pagination_class = PageNumberPagination

    # İzin kontrolü
    permission_classes = [IsAuthenticated]

    # Özel metodlar
    def get_queryset(self):
        """Özel filtreleme"""
        return Product.objects.filter(stock__gt=0)

    def perform_create(self, serializer):
        """Oluşturma sırasında özel işlemler"""
        serializer.save(created_by=self.request.user)
```

## 🗃️ Database Bağlantıları

### Django ORM (Object-Relational Mapping):

Django ORM, Python nesnelerini veritabanı tablolarına dönüştüren sistemdir.

### Veritabanı Konfigürasyonu:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Veritabanı motoru
        'NAME': BASE_DIR / 'db.sqlite3',         # Veritabanı dosyası
    }
}
```

### ORM Sorguları:

#### 1. Temel Sorgular:
```python
# Tüm kayıtları al
Product.objects.all()

# Tek kayıt al
Product.objects.get(id=1)

# Filtreleme
Product.objects.filter(price__gte=100)
Product.objects.filter(name__icontains='laptop')

# Sıralama
Product.objects.order_by('-created_at')
Product.objects.order_by('name')
```

#### 2. Karmaşık Sorgular:
```python
# Q nesneleri ile karmaşık filtreleme
from django.db.models import Q
Product.objects.filter(Q(price__gte=100) | Q(stock__gt=0))

# Annotate ile hesaplamalar
from django.db.models import Avg, Count
Product.objects.annotate(
    avg_price=Avg('price'),
    product_count=Count('id')
)

# Aggregation
from django.db.models import Sum
total_value = Product.objects.aggregate(
    total=Sum('price')
)
```

#### 3. Raw SQL Sorguları:
```python
# Ham SQL sorgusu
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT name, price FROM products
        WHERE price > %s AND stock > %s
    """, [100, 0])
    results = cursor.fetchall()
```

### Migration Sistemi:

```bash
# Migration oluştur
python manage.py makemigrations

# Migration uygula
python manage.py migrate

# Migration durumunu kontrol et
python manage.py showmigrations
```

## 🛣️ URL Routing

### URL Yapısı:

```python
# core/urls.py (Ana URL'ler)
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),  # API URL'lerini dahil et
]

# products/urls.py (Uygulama URL'leri)
urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
]
```

### URL Parametreleri:

```python
# <int:pk> - Integer parametre
# URL: /api/products/1/
# View'da: self.kwargs['pk'] = 1

# <str:slug> - String parametre
# URL: /api/products/laptop/
# View'da: self.kwargs['slug'] = 'laptop'
```

## 🧪 Pratik Örnekler

### 1. Tam CRUD İşlemi:

```python
# 1. Model tanımla
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

# 2. Serializer oluştur
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 3. View tanımla
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# 4. URL yapılandır
router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = router.urls
```

### 2. Özel API Endpoint:

```python
# Özel view
class ProductStatsAPIView(generics.GenericAPIView):
    def get(self, request):
        total_products = Product.objects.count()
        avg_price = Product.objects.aggregate(Avg('price'))
        low_stock = Product.objects.filter(stock__lt=10).count()

        return Response({
            'total_products': total_products,
            'average_price': avg_price['price__avg'],
            'low_stock_count': low_stock
        })
```

## 🚀 Gelişmiş Konular

### 1. Nested Serializers:

```python
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category']
```

### 2. Custom Model Manager:

```python
class ProductManager(models.Manager):
    def in_stock(self):
        return self.filter(stock__gt=0)

    def expensive_products(self):
        return self.filter(price__gte=1000)

class Product(models.Model):
    # ... alanlar ...
    objects = ProductManager()
```

### 3. Signal Kullanımı:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Product)
def update_product_cache(sender, instance, created, **kwargs):
    if created:
        print(f"Yeni ürün oluşturuldu: {instance.name}")
```

### 4. Caching:

```python
from django.core.cache import cache

class ProductListCreateAPIView(generics.ListCreateAPIView):
    def get(self, request):
        # Cache'den veri al
        cached_data = cache.get('products_list')
        if cached_data is None:
            # Cache'de yoksa veritabanından al
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            cached_data = serializer.data
            # 5 dakika cache'le
            cache.set('products_list', cached_data, 300)

        return Response(cached_data)
```

## 📚 Öğrenme Kaynakları

- [Django REST Framework Dokümantasyonu](https://www.django-rest-framework.org/)
- [Django ORM Dokümantasyonu](https://docs.djangoproject.com/en/stable/topics/db/)
- [Django Model Fields](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [Django Serializer Fields](https://www.django-rest-framework.org/api-guide/fields/)

## 🔧 Kurulum ve Çalıştırma

```bash
# 1. Virtual environment oluştur
python -m venv .venv

# 2. Virtual environment'ı aktifleştir
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 3. Bağımlılıkları yükle
pip install django djangorestframework

# 4. Veritabanını oluştur
python manage.py makemigrations
python manage.py migrate

# 5. Admin kullanıcısı oluştur
python manage.py createsuperuser

# 6. Sunucuyu başlat
python manage.py runserver
```

## 🌐 API Endpoint'leri

- `GET /api/products/` - Tüm ürünleri listele
- `POST /api/products/` - Yeni ürün oluştur
- `GET /api/products/{id}/` - Ürün detayı
- `PUT /api/products/{id}/` - Ürün güncelle
- `DELETE /api/products/{id}/` - Ürün sil

Bu rehber, Django REST Framework'ün temel bileşenlerinin nasıl birlikte çalıştığını ve veri akışının nasıl gerçekleştiğini derinlemesine açıklar. Her bileşenin rolü ve birbirleriyle nasıl etkileşim kurduğu detaylı olarak incelenmiştir.