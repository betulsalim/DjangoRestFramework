# Django REST Framework serializers modülünü import ediyoruz
# serializers modülü, Django modellerini JSON/XML formatına dönüştürmek için kullanılır
# Bu modül, API'lerde veri alışverişini kolaylaştırır
from rest_framework import serializers

# Kendi uygulamamızdan Product modelini import ediyoruz
# Bu model, serializer'ın dönüştüreceği veri kaynağıdır
from .models import Product

# =============================================================================
# DJANGO REST FRAMEWORK SERIALIZERS.PY DOSYASI
# =============================================================================
#
# Bu dosya, Django REST Framework (DRF) serializers'ını tanımlar.
# Serializers, Django modellerini JSON/XML formatına dönüştürmek ve
# tersine dönüştürmek için kullanılan sınıflardır.
#
# Serializer'ların Görevleri:
# - Model verilerini JSON/XML formatına dönüştürme (Serialization)
# - JSON/XML verilerini model nesnelerine dönüştürme (Deserialization)
# - Veri doğrulama (Validation)
# - API response'larını formatlama
# - Nested (iç içe) veri yapılarını yönetme
#
# Bu dosyada tanımlanan serializer'lar:
# - ProductSerializer: Product modeli için JSON dönüşümü
# =============================================================================

# =============================================================================
# PRODUCT SERIALIZER SINIFI
# =============================================================================
#
# Bu sınıf, Product modelini JSON formatına dönüştürmek için kullanılır.
# ModelSerializer, Django modellerini otomatik olarak serialize eden
# özel bir serializer türüdür.
class ProductSerializer(serializers.ModelSerializer):
    # =============================================================================
    # META SINIFI KONFİGÜRASYONU
    # =============================================================================

    # Meta sınıfı, serializer'ın davranışını yapılandırmak için kullanılır
    class Meta:
        # Hangi modelin serialize edileceğini belirtiyoruz
        # Bu, serializer'ın hangi model sınıfını kullanacağını belirler
        model = Product

        # Hangi alanların serialize edileceğini belirtiyoruz
        # '__all__': Modeldeki tüm alanları serialize et
        # Alternatif: ['name', 'price', 'stock', 'created_at'] şeklinde liste
        # Bu ayar, API response'unda hangi alanların görüneceğini belirler
        fields = '__all__'

        # =============================================================================
        # OPSİYONEL META AYARLARI (Şu anda kullanılmıyor)
        # =============================================================================
        #
        # Diğer yaygın Meta ayarları:
        #
        # # Belirli alanları hariç tutma
        # exclude = ['created_at']
        #
        # # Sadece okuma için alanlar (API'de değiştirilemez)
        # read_only_fields = ['created_at']
        #
        # # Ekstra alanlar ekleme
        # extra_fields = ['is_in_stock']
        #
        # # Alan doğrulama kuralları
        # extra_kwargs = {
        #     'name': {'min_length': 2, 'max_length': 100},
        #     'price': {'min_value': 0},
        #     'stock': {'min_value': 0}
        # }
        # =============================================================================

    # =============================================================================
    # OPSİYONEL ÖZEL ALANLAR VE METODLAR (Şu anda kullanılmıyor)
    # =============================================================================
    #
    # Serializer'a özel alanlar ve metodlar eklenebilir:
    #
    # # Hesaplanmış alan
    # is_in_stock = serializers.SerializerMethodField()
    #
    # def get_is_in_stock(self, obj):
    #     return obj.stock > 0
    #
    # # Özel alan doğrulama
    # def validate_price(self, value):
    #     if value <= 0:
    #         raise serializers.ValidationError("Fiyat 0'dan büyük olmalıdır.")
    #     return value
    #
    # # Model doğrulama
    # def validate(self, data):
    #     if data['price'] > 1000 and data['stock'] == 0:
    #         raise serializers.ValidationError("Yüksek fiyatlı ürünler stokta olmalıdır.")
    #     return data
    #
    # # Özel alan formatı
    # formatted_price = serializers.SerializerMethodField()
    #
    # def get_formatted_price(self, obj):
    #     return f"₺{obj.price}"
    #
    # # Nested serializer örneği (Category modeli varsa)
    # category = CategorySerializer(read_only=True)
    # =============================================================================