from django.shortcuts import redirect, render
from .models import Post, Category1, Category2, Comment
from django.contrib import messages

# Create your views here.

def HomePage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    context  = {
        'posts':get_all_posts,
        'cat1': get_all_categories_in_category_1,
        'cat2': get_all_categories_in_category_2
    }
    return render(request, 'blogapp/index.html', context)

def ArticleDetail(request, slug):
    get_post = Post.objects.get(slug=slug)
    get_all_comments = Comment.objects.filter(post_name=get_post)

    number_of_comments = 0
    for i in get_all_comments:
        number_of_comments +=1

    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']

        new_comment = Comment(name=name, post_name=get_post, body=body)
        new_comment.save()

        messages.success(request, 'Comment was added successfully!')
        return redirect('detail', slug=slug)

    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    get_all_posts = Post.objects.all()
    
    get_cat_1 = get_post.first_category
    get_cat_2 = get_post.second_category
    context = {
        'posts': get_all_posts,
        'post': get_post,
        'category1': get_cat_1,
        'category2': get_cat_2,
        'cat1': get_all_categories_in_category_1,
        'cat2': get_all_categories_in_category_2,
       'comments': get_all_comments,
       'number_of_comments': number_of_comments
    }
    return render(request, 'blogapp/article.html', context)