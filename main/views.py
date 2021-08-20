from django.shortcuts import render, HttpResponse
from django.db.models.base import Model
from django.shortcuts import redirect, render, HttpResponse
from .models import tv_show
from django.contrib import messages

def home(request):
    tv_shows = tv_show.objects.all()
    
    context = {
        'tv': tv_shows,
      
    }
    return render(request, 'home.html', context)


def create_new_show(request):
    if request.method == 'GET':
        return render(request,'form.html')
    else:
        errors = tv_show.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/new_show')
        
        else: 
            title1 = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['date_show']
            desc = request.POST['desc']
            new_show = tv_show.objects.create(
                title=title1, network=network, release_date=release_date, desc=desc)
            messages.success(request,'the show has been created!')
            return redirect('/home')


def delete_show(requets, id_show):
    get2delete = tv_show.objects.get(id=id_show)
    get2delete.delete()
    return redirect('/home')


def edit_show(request, id_show):
    if request.method == 'GET':
        edit_show = tv_show.objects.get(id=id_show)
        time_str = edit_show.release_date.strftime('%Y-%m-%d')

        context = {
            '2edit': edit_show,
            'time_str': time_str
        }
        return render(request,'form_edit.html',context)
       
    else:
        edit_show = tv_show.objects.get(id=id_show)

        title_recieve = request.POST['title']
        network_recieve = request.POST['network']
        release_recieve = request.POST['date_show']
        desc_recieve = request.POST['desc']
        zelda_recieve = request.POST['zelda']

        edit_show.title = title_recieve
        edit_show.network = network_recieve
        edit_show.release_date = release_recieve
        edit_show.desc = desc_recieve
        edit_show.zelda = zelda_recieve

        edit_show.save()
        messages.success(request,'the show has been edited!')
        return redirect('/home')

def show_show (request,tv_id):
    show = tv_show.objects.get(id = tv_id)
    context = {
        'show':show
    }
    return render(request,'show_tv.html',context)

def search_show(request):
    title2find = request.POST['title']
    title2find = title2find.capitalize()
    find_show = tv_show.objects.get(title = title2find)
    id_show = find_show.id
    return redirect(f'home/show_tv/{id_show}')



