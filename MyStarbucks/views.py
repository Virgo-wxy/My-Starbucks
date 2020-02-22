from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response, redirect

# Create your views h

from MyStarbucks.forms import UserForm
from MyStarbucks.models import guestbook, new_view, Detail_drink, CartInfo

# ---------------------------------------------前端-------------------------------------------------
# 首页
def index(request):
    return render_to_response('MyStarbucks/index.html')


# 饮料
def drink(request):
    products = Detail_drink.objects.all()
    return render(request, 'MyStarbucks/drink.html', {'products': products})


# 咖啡
def coffee(request):
    # return render(request,'MyStarbucks/coofee.html')
    return render_to_response('MyStarbucks/coofee.html')


# 美食
def food(request):
    return render(request, 'MyStarbucks/food.html')


# 联系我们
def guest_book(request):
    return render(request, 'MyStarbucks/guestbook.html')


# 新闻
def newview(request):
    return render(request, 'MyStarbucks/new_view.html')


# 季度精选
def product_list(request):
    return render(request, 'MyStarbucks/product_list.html')


# 登录
def login(request):
    # 实现登陆功能，返回user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 用户验证
        user_result = auth.authenticate(username=username, password=password)
        if user_result is not None:
            # 用户登陆
            auth.login(request, user_result)
            return render(request, 'MyStarbucks/index.html', {'user': user_result})
        else:
            return render(request, 'MyStarbucks/regist.html', {'login_error': 'username or password wrong'})
    else:
        # 访问登陆页面
        return render(request, 'MyStarbucks/login.html')


# 退出
def logout(request):
    auth.logout(request)
    return render(request, 'MyStarbucks/index.html')


# 注册
def regist(request):
    # 1,post提交注册信息
    if request.method == 'POST':
        # 实例化表单类
        uf = UserForm(request.POST)
        # 信息
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 判断是否用户存在
            ulist = User.objects.filter(username=username)
            # 如果存在
            if ulist:
                return render(request, 'MyStarbucks/regist.html',
                              {'message': 'username already exist', 'username': username})
            else:  # 用户不存在
                User.objects.create_user(username=username, password=password)
                return render(request, 'MyStarbucks/login.html', {'message': 'regist successfully'})
                # return HttpResponse("用户已经存在")
    else:
        # 2,显示空的注册页面
        uf = UserForm()
        return render(request, 'MyStarbucks/regist.html', {'uf': uf})


# 商品详情页
def detail(request, id):
    detail = Detail_drink.objects.get(id=id)
    return render(request, 'MyStarbucks/detail.html', {'datail': detail})


# 购物车
def shopping(request):
    uid = request.user.id
    if uid:
        carts = CartInfo.objects.filter(user_id=uid)
        id = User.objects.get(id=uid)
        prices = 0
        num = 0
        for i in carts:
            money = i.count * i.goods.price
            prices = i.count * i.goods.price + prices
            num = i.count + num
        return render(request, 'MyStarbucks/shopping.html', locals())
    else:
        return redirect('MyStarbucks:login')


def add(request, gid, count):  # 分别为商品的id和数量
    # 获取用户id
    uid = request.user.id
    if uid:
        if int(gid) == 0 and request.is_ajax() and int(count) == 0:
            count = CartInfo.objects.filter(user_id=uid).count()  # 查询当前登录用户购物车的商品类型数量
            return JsonResponse({'count': count})
        gid = int(gid)  # 转化为int型
        count = int(count)
        # 查询购物车中是已有该商品,如果有则数量增加,如果没有则新增一个商品
        carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
        if len(carts) >= 1:
            cart = carts[0]
            cart.count = cart.count + count
        else:
            cart = CartInfo()
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
        cart.save()
        # 如果是ajax请求则返回json,否则转向购物车  测试  正常都不转
        if request.is_ajax():
            count = CartInfo.objects.filter(user_id=uid).count()  # 查询当前登录用户购物车的商品类型数量
            return JsonResponse({'count': count})
        else:
            return redirect('/MyStarbucks/shopping/')  # 转到购物车
    else:
        return redirect('MyStarbucks:login')


def edit(request):
    ids = int(request.GET.get('id'))
    cart = CartInfo.objects.get(goods_id=ids)
    cart.count = cart.count + 1
    cart.save()
    return redirect('MyStarbucks:shopping')


def edit1(request):
    ids = int(request.GET.get('id'))
    cart = CartInfo.objects.get(goods_id=ids)
    cart.count = cart.count - 1
    cart.save()
    return redirect('MyStarbucks:shopping')


# 删除购物车
def delete(request, gid):
    cart = CartInfo.objects.get(id=int(gid))
    cart.delete()
    return redirect('/MyStarbucks/shopping/')


# 结算
def result(request):
    return  render_to_response('MyStarbucks/result.html')
# -----------------------------------------管理后台---------------------------------------------------
def manage_index(request):
    is_super = request.user.is_superuser
    if is_super:
        # return render_to_response('MyStarbucks/manage/manage_index.html')
        return render(request, 'MyStarbucks/manage/manage_index.html')
    else:
        return redirect('/MyStarbucks')


#用户管理
def add_user(request):
    # 1,post提交注册信息
    if request.method == 'POST':
        # 实例化表单类
        uf = UserForm(request.POST)
        # 信息
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 判断是否用户存在
            ulist = User.objects.filter(username=username)
            # 如果存在
            if ulist:
                return render(request, 'MyStarbucks/manage/add_user.html', {'message': 'UserName Already Exist !!'})
            else:  # 用户不存在
                User.objects.create_user(username=username, password=password)
                return render(request, 'MyStarbucks/manage/add_user.html', {'message': 'Regist successfully !!'})
    else:
        # 2,显示空的注册页面
        uf = UserForm()
        return render(request, 'MyStarbucks/manage/add_user.html', {'uf': uf})


def show_user(request):
    user = User.objects.all()
    return render(request, 'MyStarbucks/manage/del_user.html', {'user': user})


def del_user(request, user_id):
    users = User.objects.get(id=int(user_id))
    users.delete()
    return redirect('/MyStarbucks/show_user/')


# 新闻管理
def shownews(request):
    news = new_view.objects.all()
    return render(request, 'MyStarbucks/manage/del_news.html', {'news': news})


def shownews2(request):
    news = new_view.objects.all()
    return render(request, 'MyStarbucks/manage/del_news2.html', {'news': news})


def update_news(request, id):
    id = new_view.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        id.title = title
        id.content = content
        id.save()
        return redirect('/MyStarbucks/show2_news')
    else:
        return render(request, 'MyStarbucks/manage/update_news.html', {'id': id})


def del_news(request, news_id):
    news2 = new_view.objects.get(id=int(news_id))
    news2.delete()
    return redirect('/MyStarbucks/show_news/')


# -----------留言管理----------------
# 显示留言
def showguestbook(request):
    guestbooks = guestbook.objects.all()
    return render(request, 'MyStarbucks/manage/look_guestbook.html', {'guestbooks': guestbooks})


# 将前台留言部分保存到数据库
def ask_guestbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        titles = guestbook(title=title, content=None)
        titles.save()
        return redirect('/MyStarbucks/guest_book')


# def look(request):
#     return render(request, 'MyStarbucks/manage/answer_guestbook.html')
# return redirect('/MyStarbucks/ask_guestbook')
def answer_guestbook(request, id):
    id = guestbook.objects.get(id=id)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        id.content = answer
        id.save()
        return redirect('/MyStarbucks/showguestbook')
    else:
        return render(request, 'MyStarbucks/manage/answer_guestbook.html', {'id': id})
