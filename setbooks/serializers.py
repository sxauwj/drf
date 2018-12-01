from rest_framework import serializers
from .models import BookInfo

"""
# 定义序列化器类
class BookInfoSerializer(serializers.ModelSerializer):
    # 图书序列化器

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

"""


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField(
        required=False,
        min_value=5,
        max_value=20,
        error_messages={
            'min_value': '最小值为10'
        }
    )
    bcomment = serializers.IntegerField(required=False)

    # 一 针对一个属性进行验证
    # validate_属性名 ， value 为btitle属性的值
    def validate_btitle(self, value):
        # 定义验证，进行验证
        # 要求书名包含python
        if 'python' not in value:
            # 验证条件不满足，抛异常
            raise serializers.ValidationError('书名必须包含python')
        # 验证通过后，需要返回这个数据
        return value

    # 二 针对多个属性进行验证
    # validate
    def validate(self, attrs):
        # 在该方法中，可以获取所有请求的数据，attrs是个字典
        bread = attrs.get('bread')
        bcomment = attrs.get('bcomment')
        if bread < bcomment:
            raise serializers.ValidationError('阅读量不能小于评论量')
        return attrs
