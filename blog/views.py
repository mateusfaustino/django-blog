from django.shortcuts import render

def home(request):
    
    hero_texts = [
        'La Trilha',
        'Aproveite a Paisagem',
        'Ela Passa'
    ]
    context= {
        'hero_texts': hero_texts,
    }
    return render(request,'blog/home.html',context)
