from django.http import request
from django.shortcuts import render, HttpResponse
from django.db.models.base import Model
from django.shortcuts import redirect, render, HttpResponse
from .models import tv_show, User
from django.contrib import messages
import bcrypt


def home(request):
    tv_shows = tv_show.objects.all()
    context = {
        'tv': tv_shows,
    }
    return render(request, 'home.html', context)


def create_new_show(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    else:
        errors = tv_show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new_show')
        else:
            title1 = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['date_show']
            desc = request.POST['desc']
            new_show = tv_show.objects.create(
                title=title1, 
                network=network, 
                release_date=release_date, 
                desc=desc)
            messages.success(request, 'the show has been created!')
            return redirect('/shows')


def delete_show(request, id_show):
    get2delete = tv_show.objects.get(id=id_show)
    get2delete.delete()
    messages.info(request, 'the show has been deleted!')
    return redirect('/shows')


def delete_by_ajax(request, id_show):
    if request.method == 'POST':
        get2delete = tv_show.objects.get(id=id_show)
        get2delete.delete()
        return redirect('/shows')


def edit_show(request, id_show):
    if request.method == 'GET':
        edit_show = tv_show.objects.get(id=id_show)
        time_str = edit_show.release_date.strftime('%Y-%m-%d')
        context = {
            '2edit': edit_show,
            'time_str': time_str
        }
        return render(request, 'form_edit.html', context)

    else:

        title_recieve = request.POST['title']
        network_recieve = request.POST['network']
        release_recieve = request.POST['date_show']
        desc_recieve = request.POST['desc']
        zelda_recieve = request.POST['zelda']

        errors = tv_show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'../edit_show/{id_show}')
        edit_show = tv_show.objects.get(id=id_show)

        edit_show.title = title_recieve
        edit_show.network = network_recieve
        edit_show.release_date = release_recieve
        edit_show.desc = desc_recieve
        edit_show.zelda = zelda_recieve
        edit_show.save()
        messages.warning(request, 'the show has been edited!')
        return redirect('/shows')


def show_show(request, tv_id):
    show = tv_show.objects.get(id=tv_id)
    context = {
        'show': show
    }
    return render(request, 'show_tv.html', context)


def search_show(request):
    title2find = request.POST['title']
    title2find = title2find.capitalize()
    find_show = tv_show.objects.get(title=title2find)
    id_show = find_show.id
    return redirect(f'shows/show_tv/{id_show}')


def signup(request):
    if request.method == 'GET':
        return render(request, 'user_form.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        birth = request.POST['birthday']

        errors = User.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/signup')
        else:
            new_user = User.objects.create(
                name=name,
                email=email,
                password=bcrypt.hashpw(
                    password.encode(), bcrypt.gensalt()).decode(),
                birthdat=birth
            )
            request.session['user'] = {
                'id': new_user.id,
                'name': new_user.name,
                'email': new_user.email
            }
            messages.success(request, 'Usuario creado con exito')
            return redirect('/shows')


def login(request):
    email = request.POST['email']
    password = request.POST['password']

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, 'Usuario o contraseña incorrecta')
        return redirect('/signup')

    if not bcrypt.checkpw(password.encode(), user.password.encode()):
        messages.error(request, 'Usuario inexistente o contraseña incorrecta')
        return redirect('/signup')

    request.session['user'] = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
    }
    messages.success(request, f'Hola {user.name}')
    return redirect('/shows')


def logout(request):
    try:
        del request.session['user']
    except KeyError:
        messages.error(request, 'Ooops algo sucedio')
    return redirect('/signup')
