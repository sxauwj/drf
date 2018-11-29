from rest_framework import serializers
from .models import BookInfo


# 定义序列化器类
class BookInfoSerializer(serializers.ModelSerializer):
    """图书序列化器"""

    class Meta:
        model = BookInfo
        fields = '__all__'


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