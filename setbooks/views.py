import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from setbooks.models import BookInfo, HeroInfo

#
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


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


class BookOptionsView(View):
    def get(self, request, pk):
        # 查 接受参数，查询图书
        try:
            book_obj = BookInfo.objects.get(pk=pk)
        except Exception as e:
            return JsonResponse({'errmsg': '该书走丢了'})
        book_dict = {
            'id': book_obj.id,
            'name': book_obj.btitle,
            'bpub_date': book_obj.bpub_date.strftime("%Y-%m-%d"),
        }

        return JsonResponse(book_dict)

    def put(self, request, pk):
        # 改 接受参数修改数据
        update_dict = json.loads(request.body.decode())
        # 获得修改对象
        try:
            book_obj = BookInfo.objects.get(pk=pk)
        except:
            return JsonResponse({'errmsg': '该书走丢了'})
        # 更新数据
        book_obj.bpub_date = update_dict['bpub_date']
        book_obj.btitle = update_dict['btitle']
        book_obj.save()
        book_dict = {
            'id': book_obj.id,
            'bname': book_obj.btitle,
            'bpub_date': book_obj.bpub_date,
        }
        return JsonResponse(book_dict, status=201)

    def delete(self, request, pk):
        # 删 获取参数
        try:
            book_obj = BookInfo.objects.get(pk=pk).delete()
        except:
            return JsonResponse({'errmsg':'该图书跑丢了'})
        return JsonResponse({}, status=204)



