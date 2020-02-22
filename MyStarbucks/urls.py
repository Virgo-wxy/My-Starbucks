from django.urls import re_path

from MyStarbucks import views

app_name = 'MyStarbucks'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/', views.login, name='login'),
    re_path(r'^regist/', views.regist, name='regist'),
    re_path(r'^logout/', views.logout, name='logout'),
    re_path(r'^drink/', views.drink, name='drink'),
    re_path('^coffee/', views.coffee, name='coffee'),
    re_path('^food/', views.food, name='food'),
    re_path('^guest_book/', views.guest_book, name='guest_book'),
    re_path('^newview/', views.newview, name='newview'),
    re_path('^product_list/', views.product_list, name='product_list'),
    re_path(r'^shopping/', views.shopping, name='shopping'),
    re_path(r'^add(\d+)_(\d+)/', views.add,name='add'),     #加入购物车  分别为商品的id和数量
    re_path(r'^edit/',views.edit,name='edit'),   #修改购物车中商品的数量 分别为商品的id和数量
    re_path(r'^edit1/',views.edit1,name='edit1'),   #修改购物车中商品的数量 分别为商品的id和数量
    re_path(r'^delete(\d+)/',views.delete,name='delete'),      #删除购物车中的某个商品
    re_path(r'^result/', views.result, name='result'),


    re_path(r'^manage_index/', views.manage_index, name='manage_index'),
    re_path(r'^add_user/', views.add_user, name='add_user'),
    re_path(r'^show_user/', views.show_user, name='show_user'),
    re_path(r'^del_user(\d+)/', views.del_user, name='del_user'),
    re_path(r'^show_news/', views.shownews, name='show_news'),
    re_path(r'^show2_news/', views.shownews2, name='show2_news'),
    re_path(r'^update_news(\d+)/', views.update_news, name='update_news'),
    re_path(r'^del_news(\d+)/', views.del_news, name='del_news'),
    re_path(r'^showguestbook/', views.showguestbook, name='showguestbook'),
    re_path(r'^answer_guestbook(\d+)/', views.answer_guestbook, name='answer_guestbook'),
    re_path(r'^ask_guestbook/', views.ask_guestbook, name='ask_guestbook'),
    re_path(r'^detail(\d+)/', views.detail, name='detail'),
    re_path(r'^shopping/', views.shopping, name='shopping'),

]
