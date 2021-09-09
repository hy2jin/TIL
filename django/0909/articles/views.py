from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
# GET 요청만 통과하도록 decorator를 사용
@require_safe
def index(request):
    # 모델명.매니저.queryset API
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    # render 함수의 2번째 인자 문자열 경로는
    # 실제 파일이 저장되너있응 경로를 의미하며, templates는 생략되어 있다.
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    # print(help(ArticleForm))
    # 내가 작성한 데이터로 글 생성해줘(POST)
    if request.method == 'POST':
        # 사용자가 보낸 모든 정보는 request
        # 파일을 함께 요청 보낼때는 파일은 request.FILES에 들어있다.
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            # redirect의 인자로 직접 경로를 작성해 줘도 정상 작동은 되지만,
            # app_name:pattern_name 형태로 사용할 수 있도록 하자.
            return redirect('articles:detail', article.pk)
    # 글 작성할 수 있는 페이지 보여줘(GET)
    else:
        form = ArticleForm()
    '''
    print(form) -> html element  문자열 출력 -> 이것이 의미하는 바는?
    ModelForm의 매직매서드 __str__에는 Model에 정의된 필드에 해당하는
    label, input element의 형태를 만들어서 출려갛도록 설정되어 있을 것이다.
    <label for="title">title : </label>
    -> context를 통해서 create.html에게 넘겨 줬을 때, {{ form }}으로 출력하면 나오는 내용은?
    <label for="title">title : </label>
    {{ article.title }} --> 제목
    __str__을 설정한 후, {{ article }} --> 제목
    '''
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    # 만약 해당하는 게시물이 없으면 404 not found를 보여주기 위해 get_object_or_404
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 데코레이터를 사용하면 POST가 아닌경우 오류페이지를 띄운다.
@require_POST
def delete(request, pk):
    # POST 요청일 때만 삭제하도록 만들고 싶다.
    # POST 요청이 아니면 그냥 detail 문서에 남아있게 하고싶다.
    article = get_object_or_404(Article, pk=pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # ModelForm(data=None, files=None, ..., instance=None)
        # 기억이 안나면 print(help(ArticleForm))
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 단, 수정을 하고자 할 때는 어느 게시글을 수정하려고 하는지
        # 처음 form 인스턴스 생성할때 같이 article 정보 넘겨주면서 생성
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)