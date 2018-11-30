from rest_framework import serializers
from .models import BookInfo


# 定义序列化器类
class BookInfoSerializer(serializers.ModelSerializer):
    """图书序列化器"""

    class Meta:
        model = BookInfo
        fields = '__all__'

class HerosSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hname = serializers.CharField()
# 定义序列化器类
class BookSerializer(serializers.Serializer):
    # 该字段只允许序列化输出
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(
        min_length=1,
        max_length=15,
        error_messages={
            'min_length': '书名要大于3个字符',
            'max_length': '书名要小于15个字符'
        }
    )
    # 该字段只允许反序列化输入
    bpub_date = serializers.DateField(write_only=True)
    bread = serializers.IntegerField()

    # 输出书籍的关系属性hero的内容
    # 形式一
    # heros = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # 形式二
    # heros = serializers.StringRelatedField(read_only=True,many=True)
    # 形式三
    heros = HerosSerializer(read_only=True,many=True)


class HeroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hname = serializers.CharField()
    # 关系属性必须指定read_only=True
    # 形式一 输出关联对象的主键
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # 形式二 输出关联对象的字符串表示形式
    # hbook = serializers.StringRelatedField(read_only=True)
    # 形式三 使用关联对象的序列化器
    hbook = BookSerializer(read_only=True)


