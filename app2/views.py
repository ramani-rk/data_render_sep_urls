from django.shortcuts import render

# Create your views here.

def data2_render(request):
    data = 'Kohli Breaks the sachin highest Centuries record in worldcup semifinal infront of the Sachin Tendulkar'
    d = {'kohli': data}
    return render (request,'data2_render.html',context=d)