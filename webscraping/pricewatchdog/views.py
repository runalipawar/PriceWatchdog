# views.py

import subprocess
import subprocess
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import AmazonTb
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')

def Login(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                pass1 = request.POST.get('pass')
                user = authenticate(request, username=username, password=pass1)
                if user is not None:
                    login(request, user)
                    # Store the user's email in the session
                    request.session['user_email'] = user.email
                    return redirect('main')
                else:
                    return HttpResponse("Username or Password is incorrect!!!")

            send_mail(
                "Subject here",
                "Welcome to PriceWatchdog!",
                "pricewatchdogofficial@gmail.com",
                ["runalipawar27@gmail.com"],
                fail_silently=False,
            )

            return render(request, 'login.html')



def LogoutPage(request):
            logout(request)
            return redirect('login')


from django.core.management import call_command
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .management.commands.run_spider import run_spider

from .models import AmazonTb

import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import render



# def track_price1(request):
#     if request.method == 'POST':
#         selected_product = request.POST.get('selected_product', '')  # Extract selected product name
#         if selected_product:
#             user_email = request.session.get('user_email', None)
#             if user_email:
#                 print("View function - track_price1 - started.")
#                 logger.info("View function - track_price1 - started.")
#                 # Call the function to run the Scrapy spider with the selected product name
#                 run_spider(selected_product, user_email)
#                 return HttpResponse("Price tracking initiated.")
#             else:
#                 return HttpResponse("User email not found in session.")  # Return an appropriate response
#
#         else:
#             return HttpResponse("No product selected.")  # Return an appropriate response
#
#     else:
#         return render(request,'track_price.html')

# from django.http import HttpResponse
# from django.shortcuts import render
# from myapp.crawler import crawl
# from myapp.spiders import MobilePriceSpider

def track_price1(request):
    if request.method == 'POST':
        selected_product = request.POST.get('selected_product', '')  # Extract selected product name
        if selected_product:
            print("View function - track_price1 - started.")
            logger.info("View function - track_price1 - started.")
            # Call the function to run the Scrapy spider with the selected product name
            run_spider(selected_product)
            return HttpResponse("Price tracking initiated.")
        else:
            return HttpResponse("No product selected.")  # Return an appropriate response
    else:
        return render(request, 'track_price.html')

def track_price(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        search_results = AmazonTb.objects.filter(name__icontains=search_query)
        return render(request, 'track_price.html', {'search_results': search_results})
    else:
        return render(request, 'track_price.html')


def index(request):
    return render(request,'main.html')

def main(request):
    return render(request,'main.html')

# def track(request):
#     return render(request,'track.html')

def compare1(request):
    # product = get_object_or_404(Product, id = id)
    # context = {
    #      'product': product
    #  }
    return render(request, 'compare1.html')
    # return render(request,'compare1.html', context)

def get_product_details(request):
    product_ids = request.GET.getlist('id')
    products = []
    for product_id in product_ids:
        try:
            product = AmazonTb.objects.get(id=product_id)
            products.append(product)
        except AmazonTb.DoesNotExist:
            pass

    # Render a template fragment with the product details for both products
    return render(request, 'get_product_details.html', {'products': products})


def compare2(request, id1=None, id2=None):
    product1 = None
    product2 = None

    # Fetch product details based on IDs provided in the URL parameters
    if id1:
        product1 = get_object_or_404(AmazonTb, id=id1)
    if id2:
        product2 = get_object_or_404(AmazonTb, id=id2)

    # Pass the product details to the template for rendering
    context = {'product1': product1, 'product2': product2}
    return render(request, 'compare2.html', context)


def search(request):
    # search = AmazonTb.objects.all()

    if request.method == 'POST':
        query1 = request.POST.get('query1', None)
        if query1 is not None:
            # query1 = request.POST.get('query1')
            print(query1)
            products = AmazonTb.objects.filter(name__icontains=query1)
            for product in products:
                print(product.id)
            return render(request, 'search.html', {'products': products})
        else:
            query2 = request.POST.get('query2')
            print(query2)
            products2 = AmazonTb.objects.filter(name__icontains=query2)
            for product in products2:
                print(product.id)
            return render(request, 'search.html', {'products': products2})

    else:
        return render(request, 'search.html', {'search': search})


def view(request):
    return render(request, 'view.html')

def store(request):
    store_items = AmazonTb.objects.all()  # Retrieve all items from the Amazon model
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        products = AmazonTb.objects.filter(name__icontains=query).values('name', 'price')
        print('Filtered Products:', products)
        products_data = [{'name': product['name'], 'price': product['price']} for product in products]
        # names = [AmazonTb.name for product in products]
        return JsonResponse({'products': products_data})
        # return render(request, 'search.html', {'search': search})
    else:
        # return render(request, 'search.html', {'search': search})
        return render(request, 'store.html', {'store': store_items})


def scrape_amazon(request):
    subprocess.run(['scrapy','crawl','amazon_spider'])

    amazon_spider = AmazonTb.objects.all()

    return render(request, 'store.html',{'amazon_spider': amazon_spider})