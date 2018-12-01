import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from setbooks.models import BookInfo, HeroInfo

from . import serializers

"""
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
        print('旧',book_obj.btitle)

        # 更新数据
        book_obj.bpub_date = update_dict['bpub_date']
        book_obj.btitle = update_dict['btitle']
        book_obj.save()
        book_dict = {
            'id': book_obj.id,
            'bname': book_obj.btitle,
            'bpub_date': book_obj.bpub_date,
        }
        print('新',book_obj.btitle)
        return JsonResponse(book_dict, status=201)

    def delete(self, request, pk):
        # 删 获取参数
        try:
            book_obj = BookInfo.objects.get(pk=pk).delete()
        except:
            return JsonResponse({'errmsg':'该图书跑丢了'})
        return JsonResponse({}, status=204)

class BookView(View):
    def get(self,request):
        """
"""        # one 序列化一个对象
        book = BookInfo.objects.get(pk=2)
        # 1 创建序列化器对象，以模型类对象为参数
        serializer = BookSerializer(book)
        # 2 调用属性data，获取转换后的字典
        book_dict = serializer.data
        # 3 响应
        return JsonResponse(book_dict)
        :param request:
        :return:"""

"""
        # two 序列化列表
        blist = BookInfo.objects.all()

        # 1创建序列化对象，以列表为参数（查询集当列表来用），列表中是模型类对象
        # 需要指定many=True
        serializer = BookSerializer(blist,many=True)
        # 2调用属性data，获取转换后的列表，列表中是字典
        blist_dict = serializer.data

        return  JsonResponse(blist_dict,safe=False)

class HeroView(View):
    def get(self,request):
        #多端关系属性输出
        # # 获取对象
        # hero = HeroInfo.objects.get(pk=1)
        # # 生成序列化器对象
        # serializer = HeroSerializer(hero)
        # hero_dict = serializer.data
        #
        # return JsonResponse(hero_dict)

        # 一端关系属性输出
        book = BookInfo.objects.get(pk=1)
        serializer = BookSerializer(book)
        book_dict = serializer.data

        return JsonResponse(book_dict)

"""


class BookView(View):
    # 序列化输出
    def get(self, request):
        blist = BookInfo.objects.all()
        serializer = serializers.BookSerializer(blist, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        # 1接受客户端传来的数据
        json_dict = json.loads(request.body.decode())

        # 交给序列化器实现，进行反序列化
        # 2验证创建对象
        serializer = serializers.BookSerializer(data=json_dict)
        if serializer.is_valid():
            # 验证通过
            # serializer.validated_data 为验证过后返回的字典数据，其内容已经经过类型转换，
            # 而json_dict的内容为字符串
            # 通过验证后调用此方法，保存数据
            # book为返回的对象
            book = serializer.save()
            # 进行序列化输出对象
            serializer = serializers.BookSerializer(book)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)


class BooksView(View):
    def put(self, request, pk):
        # 接受id
        json_dict = json.loads(request.body.decode())
        # 验证书籍是否存在
        try:
            book = BookInfo.objects.get(pk=pk)
        except:
            return JsonResponse({'errmsg': '该书走丢了'})
        # 定义反序列化器对象
        serializer = serializers.BookSerializer(book, data=json_dict)
        if serializer.is_valid():
            # 反序列化完成
            book = serializer.save()
            # 序列化
            serializer = serializers.BookSerializer(book)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
