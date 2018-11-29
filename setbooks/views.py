import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from setbooks.models import BookInfo, HeroInfo


# Create your views here.

class BookInfoView(View):
    def get(self, request):
        # 得到所有图书的查询集
        blist = BookInfo.objects.all()
        book_list = []
        for book in blist:
            dict = {
                'id': book.id,
                'name': book.btitle,
                # 查询得到的对象的bpub_date字段为日期类型，需要先转成字符串类型
                'bpub_date': book.bpub_date.strftime("%Y-%m-%d")
            }
            book_list.append(dict)
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        # 创建新的图书对象
        # 接受
        book_str = json.loads(request.body.decode())
        # 详细校验省略
        # 创建
        book_obj = BookInfo.objects.create(**book_str)
        book_info = {
            'id': book_obj.id,
            'name': book_obj.btitle,
            # 直接赋值生成的对象其bpub_date为字符串类型，不需要类型转换
            'bpub_date': book_obj.bpub_date,
        }
        return JsonResponse(book_info, safe=False, status=201)
