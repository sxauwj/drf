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
                'id':book.id,
                'name':book.btitle,
            }
            book_list.append(dict)
        return JsonResponse(book_list,safe=False)

