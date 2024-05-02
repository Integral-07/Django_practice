from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import FriendForm
from .forms import SessionForm
from .models import Friend
from django.db.models import QuerySet

class HelloView(TemplateView):

    def __init__(self):
        self.params={
            'title':'Hello',
            'form':SessionForm(),
            'result':None
        }

    def get(self, request):

        self.params['result'] = request.session.get('last_msg', 'No message')
        return render(request, 'hello/index.html', self.params)
    
    
    def post(self, request):

        ses = request.POST['session']
        self.params['result'] = 'send:' + ses + ' .'
        request.session['last_msg'] = ses
        self.params['form'] = SessionForm(request.POST)

        return render(request, 'hello/index.html', self.params)
"""
def sample_middleware(get_response):

        def middleware(request):
            counter = request.session.get('counter', 0)
            request.session['counter'] = counter + 1
            response = get_response(request)
            print("count: " + str(counter))
            return response
        
        return middleware
"""

def __new_str__(self):
    
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        
        result += '</tr>'
    
    return result


QuerySet.__str__ = __new_str__


def index(request):

    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }

    return render(request, 'hello/index.html', params)

def create(request):

    if(request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()

        return redirect(to='/hello')
    
    params={
        'title':'Hello',
        'form':FriendForm(),
    }

    return render(request, 'hello/create.html', params)

def edit(request, num):

    obj = Friend.objects.get(id=num)
    if(request.method == "POST"):

        friend = FriendForm(request.POST, instance=obj)
        friend.save()

        return redirect(to="/hello")
    
    params = {

        'title':'Hello',
        'id':num,
        'form':FriendForm(instance=obj),
    }

    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == "POST"):
        friend.delete()
        return redirect(to="/hello")
    
    params = {

        "title":"Hello",
        "id":num,
        "obj":friend,
    }

    return render(request, "hello/delete.html", params)