from django.shortcuts import redirect, render, HttpResponse

def login_required(funct):
    def wrapper(request,*args):
        if 'user' not in request.session:
            return redirect('/signup')
        resp = funct(request,*args)
        return resp
    return wrapper
