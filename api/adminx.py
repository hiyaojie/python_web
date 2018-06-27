import xadmin
from django.contrib import admin

from xadmin.layout import Main, Fieldset, Row
from xadmin import views
# from api.models import Test,Contact,Tag,Snippet,Income,ProductProject
from api.models import *


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class ContactAdmin(object):
    list_display = ('name','gender','age','address','phone','email')
    ordering = ('id',)
xadmin.site.register(Contact,ContactAdmin)

# class SnippetAdmin(object):
#     list_display = ('id', 'title', 'code', 'language', 'style')
#     list_per_page = 20
#     ordering = ('id',)
#     list_filter = ('language',)
#     search_fields = ('code', 'language', 'style')
#
#     data_charts = {
#         "user_count": {'title': u"User Register Raise", "x-field": "id", "y-field": ("language",),
#                        "order": ('id',)},
#         # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
#     }
# xadmin.site.register(Snippet,SnippetAdmin)



class GlobalSetting(object):
    # site_title = '立影科技后台管理系统'
    site_footer = 'http://127.0.0.1:8000/xadmin/'
    # menu_style = 'accordion'

class IncomeAdmin(object):
    list_display = ('year','income')
    data_charts = {
        "user_count": {'title': u"User Register Raise", "x-field": "year", "y-field": ("income",),
                       "order": ('year',)},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }

# xadmin.site.register(Income,IncomeAdmin)

class CodeDicAdmin(object):
    pass
xadmin.site.register(CodeDic,CodeDicAdmin)



# xadmin.site.register(Snippet,SnippetAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


class ProductProjectAdmin(object):
    list_display = ('id','machine','mac_price','mubu','mb_price','audio','audio_price',
                    'media','media_price','other','other_price','total_price')
    ordering = ('id',)
    search_fields = ('machine','mubu')
    list_per_page = 15
    list_filter = ('use','env','lenth','width','audio_req','line')
xadmin.site.register(ProductProject,ProductProjectAdmin)


class OrderDetailInline(object):
    model = OrderDetail
    extra = 2


class PayDetailInline(object):
    model = PayDetail
    extra = 2

class OrderAdmin(object):
    # exclude = ('order_date',)
    list_display = ('id','order_date','sales','customer','province','city','sale_source','series_num','total_price','goods_des',)
    search_fields = ('order_num','customer')
    # readonly_fields = ('order_num',)
    list_per_page = 15
    list_filter = ('sales','province','city','customer_source','useage',)
    inlines = (OrderDetailInline,PayDetailInline,)
    show_detail_fields = ['order_num']
    # form = MyForm


    # fields = ('order_date','order_num','customer')
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('订单基本信息',
                             'order_date',
                             'sales','sale_source',
                             'useage', 'useage_detail',
                             'place','series_num','price'
                             ),
                    Fieldset('客户基本信息',
                             'customer',
                             'customer_source',
                             'province', 'city',
                             'wangwang'
                             ),
                    Fieldset('收件信息',
                             Row('reciever', 'phone'),
                             'address',
                             'remark'
                             ),
                ),
            )
        return super(OrderAdmin, self).get_form_layout()

xadmin.site.register(Order,OrderAdmin)

class OrderDetailAdmin(object):
    list_display = ('order_id','product_name','product_model','num','price',)
    list_per_page = 15
    list_filter = ('order_id',)
    # readonly_fields = ('order_id','product_name','product_model','num','price',)
    ordering = ('order_id',)
xadmin.site.register(OrderDetail,OrderDetailAdmin)

class PayDetailAdmin(object):
    list_display = ('order_id','pay_date','source','money',)
    list_per_page = 15
    list_filter = ('order_id',)
    ordering = ('order_id',)
xadmin.site.register(PayDetail,PayDetailAdmin)

