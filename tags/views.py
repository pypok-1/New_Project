from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from tags.forms import TagForm
from tags.models import Tag


@login_required
@require_GET
def tags_list(request):
    tags = Tag.objects.all()
    form = TagForm()
    return render(request, 'tags/tag_list.html', {'tags': tags, 'form': form})


@login_required
@require_POST
def create_tag (request):
    form = TagForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/tags/')
    return render(request, 'tags/tag_list.html', {'form': form})



