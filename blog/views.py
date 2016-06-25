import logging

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .models import Post
from .forms import PostNormalForm, PostForm
from instablog.sample_exceptions import HelloWorldError

logger = logging.getLogger('django')

def list_posts(request):
    logger.warning('경고, 경고!')
    #raise HelloWorldError('맘대로')
    per_page = 3
    page = request.GET.get('page', 1)
    #if 'page' in request.GET:
    #    page = request.GET['page']
    #else:
    #    page = 1
    #try:
    #    page = int(page)
    #except ValueError:
    #    return redirect('blog:list')
    #page = page if page >= 1 else 1
    #posts = Post.objects.all()[(page-1)*per_page:page*per_page]

    posts = Post.objects.all().order_by('-pk')
    pg = Paginator(posts, per_page)

    try:
        contents = pg.page(page)
    except PageNotAnInteger:
        contents = pg.page(1)
    except EmptyPage:
        contents = []

    context = {
        'posts': contents,
    }

    return render(request, 'list.html', context)

def detail_post(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post
    }

    return render(request, 'detail.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid() is True:
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            #new_post = Post()
            #new_post.title = form.cleaned_data['title']
            #new_post.content = form.cleand_data['conetent']
            #new_post.save()

            url = reverse('blog:detail', kwargs={'pk': new_post.pk})
            return redirect(url)
    else:
        form = PostForm()


    context = {'form': form,}

    return render(request, 'edit.html', context)