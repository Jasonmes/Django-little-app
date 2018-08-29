from django.http import HttpResponse

"""
1.这是我的第一个django应用
"""
def index(request):
    return HttpResponse("这是我的第一个django应用，路径：/polls/views.py")

"""
2.这是 Django 中最简单的视图。如果想看见效果，我们需要将一个 URL 映射到它——这就是我们需要 URLconf 的原因了。

为了创建 URLconf，请在 polls 目录里新建一个 urls.py 文件。你的应用目录现在看起来应该是这样：
"""