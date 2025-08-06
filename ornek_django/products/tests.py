# Django test framework'ü için gerekli modülü import ediyoruz
# TestCase, Django'da unit test'ler yazmak için kullanılan temel sınıftır
# Bu sınıf, test veritabanı yönetimi ve test yardımcı metodları sağlar
from django.test import TestCase

# =============================================================================
# DJANGO TESTS.PY TEST DOSYASI
# =============================================================================
#
# Bu dosya, Django uygulamasının test'lerini tanımlar.
# Test'ler, kodun doğru çalıştığını doğrulamak ve hataları önlemek
# için yazılan otomatik kontrollerdir.
#
# Test'lerin Önemi:
# - Kod kalitesini artırır
# - Hataları erken tespit eder
# - Refactoring güvenliği sağlar
# - Dokümantasyon görevi görür
# - Kod değişikliklerinin güvenliğini sağlar
#
# Test Türleri:
# - Unit Tests: Tek fonksiyon/sınıf testleri
# - Integration Tests: Bileşenler arası testler
# - API Tests: API endpoint'lerinin testleri
# - Model Tests: Veritabanı model testleri
# - View Tests: Django view'larının testleri
#
# Bu dosyada yazılacak test'ler:
# - Product model testleri
# - Product API testleri
# - Product view testleri
# - Serializer testleri
# =============================================================================

# =============================================================================
# TEST SINIFLARI (Şu anda boş - örnekler yorum satırı olarak verilmiştir)
# =============================================================================
#
# Aşağıdaki test sınıfları, products uygulaması için yazılabilir:
#
# # Product Model Testleri
# class ProductModelTest(TestCase):
#     def setUp(self):
#         """Test verilerini hazırla"""
#         self.product = Product.objects.create(
#             name="Test Ürün",
#             price=99.99,
#             stock=10
#         )
#
#     def test_product_creation(self):
#         """Ürün oluşturma testi"""
#         self.assertEqual(self.product.name, "Test Ürün")
#         self.assertEqual(self.product.price, 99.99)
#         self.assertEqual(self.product.stock, 10)
#
#     def test_product_str_method(self):
#         """__str__ metodu testi"""
#         self.assertEqual(str(self.product), "Test Ürün")
#
#     def test_product_price_validation(self):
#         """Fiyat doğrulama testi"""
#         with self.assertRaises(ValidationError):
#             Product.objects.create(
#                 name="Negatif Fiyat Ürün",
#                 price=-10.00,
#                 stock=5
#             )
#
# # Product API Testleri
# class ProductAPITest(TestCase):
#     def setUp(self):
#         """Test verilerini hazırla"""
#         self.client = APIClient()
#         self.product = Product.objects.create(
#             name="API Test Ürün",
#             price=149.99,
#             stock=20
#         )
#
#     def test_get_products_list(self):
#         """Ürün listesi API testi"""
#         response = self.client.get('/api/products/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
#
#     def test_create_product(self):
#         """Ürün oluşturma API testi"""
#         data = {
#             'name': 'Yeni Ürün',
#             'price': 199.99,
#             'stock': 15
#         }
#         response = self.client.post('/api/products/', data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Product.objects.count(), 2)
#
#     def test_get_product_detail(self):
#         """Ürün detay API testi"""
#         response = self.client.get(f'/api/products/{self.product.id}/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['name'], 'API Test Ürün')
#
# # Product View Testleri
# class ProductViewTest(TestCase):
#     def setUp(self):
#         """Test verilerini hazırla"""
#         self.product = Product.objects.create(
#             name="View Test Ürün",
#             price=79.99,
#             stock=8
#         )
#
#     def test_home_view(self):
#         """Ana sayfa view testi"""
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'View Test Ürün')
#
#     def test_product_list_view(self):
#         """Ürün listesi view testi"""
#         response = self.client.get('/products/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'products/product_list.html')
#
# # Serializer Testleri
# class ProductSerializerTest(TestCase):
#     def setUp(self):
#         """Test verilerini hazırla"""
#         self.product_data = {
#             'name': 'Serializer Test Ürün',
#             'price': 129.99,
#             'stock': 12
#         }
#         self.product = Product.objects.create(**self.product_data)
#         self.serializer = ProductSerializer(instance=self.product)
#
#     def test_contains_expected_fields(self):
#         """Serializer alan testi"""
#         data = self.serializer.data
#         self.assertCountEqual(data.keys(), ['id', 'name', 'price', 'stock', 'created_at'])
#
#     def test_name_field_content(self):
#         """Ürün adı alanı testi"""
#         data = self.serializer.data
#         self.assertEqual(data['name'], self.product_data['name'])
#
#     def test_price_field_content(self):
#         """Fiyat alanı testi"""
#         data = self.serializer.data
#         self.assertEqual(str(data['price']), str(self.product_data['price']))
#
# # Test Yardımcı Fonksiyonları
# def create_test_product(name="Test Ürün", price=99.99, stock=10):
#     """Test ürünü oluşturan yardımcı fonksiyon"""
#     return Product.objects.create(name=name, price=price, stock=stock)
#
# # Test Fixtures (Test verileri)
# class ProductFixturesTest(TestCase):
#     fixtures = ['products_test_data.json']  # Test verilerini JSON dosyasından yükle
#
#     def test_fixtures_loaded(self):
#         """Fixture verilerinin yüklendiğini test et"""
#         self.assertEqual(Product.objects.count(), 5)  # JSON'da 5 ürün varsa
# =============================================================================

# Create your tests here.
# Bu satır, test'lerinizi yazmak için kullanılır.
# Şu anda boş bırakılmıştır çünkü henüz test'ler yazılmamıştır.
# Yukarıdaki örnekler, nasıl test yazılacağını göstermektedir.
