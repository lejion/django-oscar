from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from oscar.core.application import Application
from oscar.core.loading import get_class


class BasketApplication(Application):
    name = 'basket'
    summary_view = get_class('basket.views', 'BasketView')
    saved_view = get_class('basket.views', 'SavedView')
    add_view = get_class('basket.views', 'BasketAddView')
    add_voucher_view = get_class('basket.views', 'VoucherAddView')
    remove_voucher_view = get_class('basket.views', 'VoucherRemoveView')

    def get_urls(self):
        urls = [
            url(r'^$', self.summary_view.as_view(), name='summary'),
            url(_(r'^add/(?P<pk>\d+)/$'), self.add_view.as_view(), name='add'),
            url(_(r'^vouchers/add/$'), self.add_voucher_view.as_view(),
                name='vouchers-add'),
            url(_(r'^vouchers/(?P<pk>\d+)/remove/$'),
                self.remove_voucher_view.as_view(), name='vouchers-remove'),
            url(_(r'^saved/$'), login_required(self.saved_view.as_view()),
                name='saved'),
        ]
        return self.post_process_urls(urls)


application = BasketApplication()
