from django.db import models
from django.db.models import Sum
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Test(models.Model):
    name = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=200,verbose_name='姓名')
    gender_choice = sorted((item, item) for item in ['男','女'])
    gender = models.CharField(max_length=10,choices=gender_choice,verbose_name='性别',null=True)
    age = models.IntegerField(default=0,verbose_name='年龄',null=True)
    address = models.CharField(max_length=200,verbose_name='地址',null=True)
    phone = models.CharField(max_length=20,verbose_name='手机号',null=True)
    email = models.EmailField(verbose_name='邮箱',null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Income(models.Model):
    year = models.IntegerField(verbose_name=u'年份')
    income = models.IntegerField(verbose_name=u'营业额')
    def __str__(self):
        return str(self.year)
    class Meta:
        verbose_name = '营业额'
        verbose_name_plural = verbose_name

class CodeDic(models.Model):
    name = models.CharField(max_length=100,verbose_name='显示值')
    # code = models.CharField(max_length=100,verbose_name='编码')
    type = models.CharField(max_length=100,verbose_name='字典类型')
    order = models.IntegerField(verbose_name='排序')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '数据字典'
        verbose_name_plural = verbose_name

class ProductProject(models.Model):
    use = models.CharField(max_length=20,verbose_name='用途')
    env = models.CharField(max_length=20, verbose_name='使用环境')
    lenth = models.CharField(max_length=20, verbose_name='环境长')
    width = models.CharField(max_length=20, verbose_name='环境宽')
    audio_req = models.CharField(max_length=20, verbose_name='音响要求')
    line = models.CharField(max_length=20, verbose_name='布线')
    machine = models.CharField(max_length=20, verbose_name='投影机')
    mac_price = models.IntegerField( verbose_name='投影价格')
    mubu = models.CharField(max_length=20, verbose_name='幕布')
    mb_price = models.IntegerField( verbose_name='幕布价格')
    audio = models.CharField(max_length=100, verbose_name='音响')
    audio_price = models.IntegerField( verbose_name='音响价格')
    media = models.CharField(max_length=100, verbose_name='播放器')
    media_price = models.IntegerField( verbose_name='播放器价格')
    other = models.CharField(max_length=200, verbose_name='其他设备')
    other_price = models.IntegerField( verbose_name='其他价格')
    total_price = models.IntegerField( verbose_name='总价')

    class Meta:
        verbose_name = '投影方案'
        verbose_name_plural = verbose_name

class Order(models.Model):
    # province_choice = sorted([(item.name,item.name) for item in CodeDic.objects.filter(type='province')])
    # customer_source_choice = sorted([(item.name,item.name) for item in CodeDic.objects.filter(type='cus_source')])
    # useage_choice = sorted([(item.name,item.name) for item in CodeDic.objects.filter(type='usage')])
    # useage_detail_choice = sorted([(item.name,item.name) for item in CodeDic.objects.filter(type='usage_detail')])
    sales_choice = [(item.name,item.name) for item in CodeDic.objects.filter(type='sales')]

    # order_num = models.CharField(max_length=100,verbose_name='订单号',null=True,blank=True)
    order_date = models.DateField(verbose_name='订单日期',null=True,blank=True)
    sales = models.CharField(max_length=150,verbose_name='销售员',choices=sales_choice)
    # sales = models.CharField(max_length=150,verbose_name='销售员')
    customer = models.CharField(max_length=100,verbose_name='客户名')
    customer_source = models.CharField(max_length=100,verbose_name='客户来源')
    useage = models.CharField(max_length=100,verbose_name='产品用途')
    useage_detail = models.CharField(max_length=100,verbose_name='用途细分')
    # customer_source = models.CharField(max_length=100,verbose_name='客户来源',choices=customer_source_choice)
    # useage = models.CharField(max_length=100,verbose_name='产品用途',choices=useage_choice)
    # useage_detail = models.CharField(max_length=100,verbose_name='用途细分',choices=useage_detail_choice)
    place = models.CharField(max_length=100,verbose_name='使用场所',null=True,blank=True)
    series_num = models.CharField(max_length=100,verbose_name='产品序列号',null=True,blank=True)
    province = models.CharField(max_length=100,verbose_name='省份')
    # province = models.CharField(max_length=100,verbose_name='省份',choices=province_choice)
    city = models.CharField(max_length=100,verbose_name='城市',null=True,blank=True)
    sale_source =models.CharField(max_length=100,verbose_name='销售渠道',null=True)
    wangwang = models.CharField(max_length=100,verbose_name='客户旺旺号',null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10,verbose_name='应收总价',null=True,blank=True)
    reciever = models.CharField(max_length=100, verbose_name='收件人',null=True)
    phone = models.CharField(max_length=100, verbose_name='收件人联系方式',null=True)
    address = models.TextField(verbose_name='收件地址',null=True)
    remark = models.CharField(max_length=255,verbose_name='订单备注',null=True,blank=True)
    def __str__(self):
        return str(self.id)
    def total_price(self):
        total_price = OrderDetail.objects.filter(order_id=self.id).aggregate(total_price=Sum('price'))
        return total_price['total_price']
    total_price.short_description = u'总价'
    class Meta:
        verbose_name = '销售报表'
        verbose_name_plural = verbose_name

class OrderDetail(models.Model):
    product_name = models.CharField(max_length=100,verbose_name='产品名称')
    product_model = models.CharField(max_length=100,verbose_name='产品型号')
    num = models.IntegerField(verbose_name='数量')
    price = models.FloatField(verbose_name='价格')
    order_id = models.ForeignKey(to='Order',to_field='id')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '订单物品明细'
        verbose_name_plural = verbose_name

class PayDetail(models.Model):
    pay_date = models.DateField(verbose_name='付款日期')
    source = models.CharField(max_length=50,verbose_name='付款渠道')
    money = models.FloatField(verbose_name='金额')
    order_id = models.ForeignKey(to='Order',to_field='id')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '付款明细'
        verbose_name_plural = verbose_name

