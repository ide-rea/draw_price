from django.conf.urls import url
from . import views
urlpatterns=[url(r'^(?P<person>[^/]+)$',views.yes_or_not_draw_prize,name='judge'),
             url(r'^result/(?P<person>[^/]+)$',views.get_draw_prize_res,name='prize'),
             url(r'^type/(?P<person>[^/]+)$',views.real_or_virtual_good,name='type'),
             url(r'^send/virtual/(?P<person>[\w]+)$',views.take_virtual_good,name='send_virtual'),
             url(r'^send/real/(?P<person>[\w]+)$',views.take_real_good,name='send_real')
             ]

