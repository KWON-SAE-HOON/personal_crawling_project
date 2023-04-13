from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . models import Posting, Reply
from . forms import PostingForm, ReplyForm
from account.models import SteamUser 


@require_http_methods(['POST','GET'])
def index(request):
    posts = Posting.objects.all()
   
    
    return render(request, 'community/index.html', {
        'posts' : posts,
        
    })


@login_required
@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():

            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()

            return redirect('community:detail', posting.pk)

    else:
        form = PostingForm()
    return render(request, 'community/create.html',{
        'form' : form,
    })

@require_safe
def detail(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)

    return render(request, 'community/detail.html', {
        'posting' : posting,
    })

@login_required
@require_http_methods(['GET','POST'])
def update(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)

    if request.user != posting.user:
        return redirect('community:index')

    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid:
            posting = form.save()
            return redirect('account:detail', posting.pk)

    else:
        form = PostingForm()
    return render(request, 'account/create.html',{
        'form' : form,
    })

@login_required
@require_POST
def delete(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    posting.delete()
    return redirect('community:index')

@login_required
@require_POST
def create_reply(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
                        # 저장하기 직전에 멈추고 reply객체는 잡을 수 있음
                        # 데이터베이스에 저장하지 않기 위해 이거 안하면 한번 덧씌우고 되버림
        reply.posting = posting # 비어있는 컬럼 => FK
        reply.user = request.user
        reply.save()
        return redirect('community:detail', posting_pk)

@login_required
@require_POST
def delete_reply(request, posting_pk, reply_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    
    if request.user == reply.user:
        reply.delete()
        
    return redirect('community:detail', posting.pk)