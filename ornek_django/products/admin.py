# Django admin paneli için gerekli modülü import ediyoruz
# admin modülü, Django'nun yerleşik admin panelini yapılandırmak için kullanılır
from django.contrib import admin

# =============================================================================
# DJANGO ADMIN.PY KONFİGÜRASYON DOSYASI
# =============================================================================
#
# Bu dosya, Django'nun yerleşik admin panelini yapılandırmak için kullanılır.
# Admin paneli, Django projelerinde veritabanı verilerini yönetmek için
# kullanılan güçlü bir web arayüzüdür.
#
# Admin Panelinin Özellikleri:
# - Veritabanı kayıtlarını görüntüleme, ekleme, düzenleme, silme
# - Kullanıcı dostu web arayüzü
# - Otomatik form oluşturma
# - Arama ve filtreleme özellikleri
# - Kullanıcı yetkilendirme sistemi
# - Özelleştirilebilir görünüm ve davranış
#
# Bu dosyada yapılacak işlemler:
# - Modelleri admin paneline kaydetme
# - Admin panel görünümünü özelleştirme
# - Admin panel davranışını yapılandırma
# - Özel admin sınıfları oluşturma
# =============================================================================

# =============================================================================
# MODEL KAYIT İŞLEMLERİ
# =============================================================================
#
# Modelleri admin paneline kaydetmek için aşağıdaki yöntemler kullanılır:
#
# 1. Basit Kayıt:
#    admin.site.register(Product)
#
# 2. Özelleştirilmiş Admin Sınıfı ile Kayıt:
#    admin.site.register(Product, ProductAdmin)
#
# 3. Özel Admin Sınıfı Tanımlama:
#    class ProductAdmin(admin.ModelAdmin):
#        list_display = ['name', 'price', 'created_at']
#        list_filter = ['category', 'is_active']
#        search_fields = ['name', 'description']
#        ordering = ['-created_at']
#
# =============================================================================

# =============================================================================
# ÖRNEK KULLANIM (Şu anda yorum satırı olarak bırakılmıştır)
# =============================================================================
#
# Aşağıdaki kodlar, products uygulamasındaki modelleri
# admin paneline kaydetmek için kullanılabilir:
#
# from .models import Product, Category
#
# # Basit kayıt
# admin.site.register(Product)
# admin.site.register(Category)
#
# # Özelleştirilmiş admin sınıfı
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'category', 'is_active']
#     list_filter = ['category', 'is_active', 'created_at']
#     search_fields = ['name', 'description']
#     list_editable = ['price', 'is_active']
#     ordering = ['-created_at']
#
#     fieldsets = (
#         ('Temel Bilgiler', {
#             'fields': ('name', 'description', 'price')
#         }),
#         ('Kategori ve Durum', {
#             'fields': ('category', 'is_active')
#         }),
#     )
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'product_count']
#     search_fields = ['name']
#
#     def product_count(self, obj):
#         return obj.products.count()
#     product_count.short_description = 'Ürün Sayısı'
#
# =============================================================================

# Register your models here.
# Bu satır, modellerinizi admin paneline kaydetmek için kullanılır.
# Şu anda boş bırakılmıştır çünkü henüz modeller tanımlanmamıştır.
# Modeller oluşturulduktan sonra buraya kayıt kodları eklenmelidir.
