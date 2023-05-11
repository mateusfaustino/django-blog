from django.shortcuts import render

def index(request):
    user={
        'name':'Mateus Faustino',
        'avatar':'adminlte/dist/img/user2-160x160.jpg'
    }
    side_menu = [
        {
            'icon':'nav-icon fas fa-book',
            'description':'Post',
            'link':'',
            'children': [
                {
                    'icon':'fa-sharp fa-solid fa-plus',
                    'description':'New Post',
                    'link':'',
                    'children': []
                },       
                {
                    'icon':'fa-sharp fa-regular fa-border-all',
                    'description':'All Post',
                    'link':'',
                    'children': []
                },       
            ]
        }
    ]
    context = {
        'side_menu': side_menu,
        'user':user
    }
    return render(request,'manager/index.html',context)
