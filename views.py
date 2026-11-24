from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Product, Category, Supplier


# Create your views here.
@login_required
def dashboard(request):
    total_products = Product.objects.count()
    low_stock = Product.objects.filter(
        quantity__lte=F("reorder_level")
    ).count()

    return render(request, "inventory/dashboard.html", {
        "total_products": total_products,
        "low_stock": low_stock
    })
@login_required
def product_list(request):
    products = Product.objects.select_related(
        "category", "supplier"
    ).all()

    return render(request, "inventory/product_list.html", {
        "products": products
    })
@login_required
def add_product(request):
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        Product.objects.create(
            name=request.POST["name"],
            category_id=request.POST["category"],
            supplier_id=request.POST.get("supplier"),
            quantity=int(request.POST["quantity"]),
            price=request.POST["price"]
        )
        return redirect("product_list")

    return render(request, "inventory/add_product.html", {
        "categories": categories,
        "suppliers": suppliers
    })
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.name = request.POST["name"]
        product.quantity = request.POST["quantity"]
        product.price = request.POST["price"]
        product.save()
        return redirect("product_list")

    return render(request, "inventory/edit_product.html", {
        "product": product
    })
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "inventory/confirm_delete.html", {
        "product": product
    })
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, "category/category_list.html", {
        "categories": categories
    })
@login_required
def add_category(request):
    if request.method == "POST":
        Category.objects.create(
            name=request.POST["name"]
        )
        return redirect("category_list")

    return render(request, "category/add_category.html")
@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.name = request.POST["name"]
        category.save()
        return redirect("category_list")

    return render(request, "category/edit_category.html", {
        "category": category
    })
@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    return render(request, "category/confirm_delete.html", {
        "object": category,
        "type": "Category"
    })
@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, "supplier/supplier_list.html", {
        "suppliers": suppliers
    })
@login_required
def add_supplier(request):
    if request.method == "POST":
        Supplier.objects.create(
            name=request.POST["name"],
            phone=request.POST["phone"],
            email=request.POST["email"]
        )
        return redirect("supplier_list")

    return render(request, "supplier/add_supplier.html")
@login_required
def edit_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == "POST":
        supplier.name = request.POST["name"]
        supplier.phone = request.POST["phone"]
        supplier.email = request.POST["email"]
        supplier.save()
        return redirect("supplier_list")

    return render(request, "supplier/edit_supplier.html", {
        "supplier": supplier
    })
@login_required
def delete_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == "POST":
        supplier.delete()
        return redirect("supplier_list")

    return render(request, "supplier/confirm_delete.html", {
        "object": supplier,
        "type": "Supplier"
    })
