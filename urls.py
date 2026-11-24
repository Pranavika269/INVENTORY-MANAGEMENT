from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/edit/<int:pk>/", views.edit_product, name="edit_product"),
    path("products/delete/<int:pk>/", views.delete_product, name="delete_product"),
    # CATEGORY
    path("categories/", views.category_list, name="category_list"),
    path("categories/add/", views.add_category, name="add_category"),
    path("categories/edit/<int:pk>/", views.edit_category, name="edit_category"),
    path("categories/delete/<int:pk>/", views.delete_category, name="delete_category"),

    # SUPPLIER
    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("suppliers/add/", views.add_supplier, name="add_supplier"),
    path("suppliers/edit/<int:pk>/", views.edit_supplier, name="edit_supplier"),
    path("suppliers/delete/<int:pk>/", views.delete_supplier, name="delete_supplier"),

]
