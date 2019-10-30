from django.urls import path, include
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),  # 如果url中含有hello_world，则把他转发到blog.views.hello_world函数中
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page),
    # path('detail', blog.views.get_detail_page),
    path('detail/<int:article_id>', blog.views.get_detail_page),

]