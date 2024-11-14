# urls.py в приложении recipe_project
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import CategoryViewSet, RecipeViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Автодокументация
schema_view = get_schema_view(
   openapi.Info(
      title="Recipe API",
      default_version='v1',
      description="API для рецептов",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@recipes.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

# Настроим роутинг для API
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]