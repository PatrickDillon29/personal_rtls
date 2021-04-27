from django.http import HttpResponse
from django.http.request import HttpRequest
from django.template import loader
from django.shortcuts import render, get_list_or_404
from django.http import Http404
# from django.db.models.loading import get_model
from django.apps import apps


from .models import Tag_table

def index(request):
    # tag_list = tags.objects.order_by('tag_id')
    # template = loader.get_template('webapp/index.html')
    # context = {'tag_list': tag_list}
    return render(request, 'webapp/index.html')

    # return HttpResponse(template.render(context, request))
    # output = ', '.join([str(t.tag_id) for t in tag_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the Viasat RTLS Project Homepage.")

def live_data(request):
    return HttpResponse("Live data page (more to come)")

def hist_data(request):
    print("HI")
    avail_tag_set = Tag_table.objects.order_by('tag_id').distinct()
    print(avail_tag_set)
    return render(request, 'webapp/hist_data.html', {'avail_tag_set': avail_tag_set})
    # return render(request, 'webapp/hist_data.html')
    # return HttpResponse("Historical data page (more to come)")

def get_tag_data(request, requested_id):
    tag_data = get_list_or_404(Tag_table, tag_id=requested_id)
    print(tag_data)
    print("hi")
    return render(request, 'webapp/ind_tag_data.html', {'tag_data': tag_data})
    # tag_model_str = "Tag_" + str(tag_id)
    # try:
    #     tag_model = apps.get_model("webapp", tag_model_str, require_ready=False)
    # except LookupError:
    #     raise Http404("couldn't find model for tag_id" + str(tag_id))


def tag_config(request):
    return HttpResponse("Tag configuration page (more to come)")

def move_transactions(request):
    return HttpResponse("Move transactions page (more to come)")

def demo_mode(request):
    return HttpResponse("Demo mode page (more to come)")

def conveyor_config(request):
    return HttpResponse("Conveyor config page (more to come)")


 