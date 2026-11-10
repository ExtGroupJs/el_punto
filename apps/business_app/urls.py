from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.business_app.views.classification import ClassificationViewSet
from apps.business_app.views.gallery import GalleryViewSet
from apps.business_app.views.menu import business_menu
from apps.business_app.views.dashboard import DashboardViewSet
from apps.business_app.views.product import ProductViewSet
from apps.business_app.views.sell_group import PaymentMethodsViewSet, SellGroupViewSet
from apps.business_app.views.shop import ShopViewSet
from apps.business_app.views.input_group import (
    InputGroupViewSet,
)
from apps.business_app.views.input import InputViewSet
from apps.business_app.views.shop_products import ShopProductsViewSet
from apps.business_app.views.sell import SellViewSet
from apps.business_app.views.shop_products_logs import ShopProductsLogsViewSet
from apps.business_app.views.group_sell import GroupSellViewSet
from apps.business_app.views.pallet import PalletViewSet


router = SimpleRouter()


router.register(
    "classifications",
    ClassificationViewSet,
    basename="classifications",
)
router.register(
    "products",
    ProductViewSet,
    basename="products",
)
router.register(
    "shops",
    ShopViewSet,
    basename="shop",
)
router.register(
    "shop-products",
    ShopProductsViewSet,
    basename="shop-products",
)
router.register(
    "shop-products-logs",
    ShopProductsLogsViewSet,
    basename="shop-products-logs",
)
router.register(
    "sell-products",
    SellViewSet,
    basename="sell-products",
)
router.register(
    "sell-groups",
    SellGroupViewSet,
    basename="sell-groups",
)
router.register(
    "group-sells",
    GroupSellViewSet,
    basename="group-sells",
)
router.register(
    "dashboard",
    DashboardViewSet,
    basename="dashboard",
)
router.register(
    "payment-methods",
    PaymentMethodsViewSet,
    basename="payment-methods",
)
router.register(
    "input-groups",
    InputGroupViewSet,
    basename="input-groups",
)
router.register(
    "input-products",
    InputViewSet,
    basename="input-products",
)
router.register(
    "pallets",
    PalletViewSet,
    basename="pallets",
)
router.register(
    "galleries",
    GalleryViewSet,
    basename="galleries",
)
router.register(
    "gallery",
    GalleryViewSet,
    basename="gallery",
)

urlpatterns = [
    path("business-menu/", business_menu, name="business-menu"),
]

urlpatterns += router.urls
