from django.shortcuts import render


def blog_index(request):
    blogs = [
        {
            'name': 'The first blog',
            'author': {'name': 'admin'},
            'publication_date': '16.04.2022'
        }, 
        {
            'name': 'The second blog',
            'author': {'name': 'admin'},
            'publication_date': '12.04.2022'
        }
        ]
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blog_index.html', context=context)


def user_page(request):
    user_data = {
        'user_name': 'Emir',
        'user_age': 14
    }
    context = {
        'user_data': user_data
    }
    return render(request,  'blogs/user_page.html', context=context)


def first_blog(request):
    context = {

    }
    return render(request, 'blogs/first_blog.html', context=context)

def cards_page(request):
    context = {

    }
    return render(request, 'blogs/cards_page.html', context=context)


def cards_page2(request):
    context = {

    }
    return render(request, 'blogs/cards_page2.html', context=context)


def card_details(request):
    context = {
        
    }
    return render(request, 'blogs/card_details.html', context=context)
