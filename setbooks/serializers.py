from rest_framework import serializers
from .models import BookInfo, HeroInfo

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
            'min_value': '最小值为10',
            'max_value': '最大值为20'
        }
    )
    bcomment = serializers.IntegerField(required=False)
    heros = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

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

    def create(self, validated_data):
        # 创建对象
        # 当调用序列化器对象的save()方法时执行
        book = BookInfo.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        # 修改对象
        # instance 被修改的对象
        # validated_data　接受的验证后的数据，是一个类型已经转换过字典，
        # 对于必传属性，直接获取赋值
        instance.btitle = validated_data.get('btitle')
        instance.bpub_date = validated_data.get('bpub_date')
        # 对于可传属性，判断再赋值
        if validated_data.get('bread'):
            instance.bread = validated_data.get('bread')
        if validated_data.get('bcomment'):
            instance.bcomment = validated_data.get('bcomment')
        instance.save()
        return instance


# 使用模型类序列化器
class HeroSerializer(serializers.ModelSerializer):
    # 隐藏属性,输出需要明确定义
    hbook_id = serializers.IntegerField()
    hbook = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HeroInfo
        # fields = '__all__'
        # fields = ['hname', 'hcomment','hbook_id','hbook']
        exclude = ['is_delete']
        # 嵌套表示
        # depth = 1
        # # 自定义验证方法 ,验证方法需要自己来写
        # def validate_hname(self,value):
        #     if not value.startswith('刘'):
        #         return serializers.ValidationError("必须姓刘")
        #     else:
        #         return value
