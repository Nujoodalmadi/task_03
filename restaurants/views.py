from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list": [{"restaurant_name": "B1B2","food_type": "Burgers" },{"restaurant_name": "BestPizza","food_type": "Italian" },{"restaurant_name":"Sushii" ,"food_type":"Sushi" }]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object": {"restaurant_name":"B1B2", "food_type":"Burgers"}

    }
    return render(request, 'detail.html', context)
