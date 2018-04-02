from django.shortcuts import render, Http404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from adsrental.models.lead_account import LeadAccount


class BundlerReportView(View):
    @method_decorator(login_required)
    def get(self, request):
        bundler = request.user.bundler
        if not bundler:
            raise Http404

        lead_accounts_by_qualified_date = LeadAccount.objects.filter(lead__bundler=bundler)

        return render(request, 'bundler_dashboard.html', dict(
            user=request.user,
            bundler=bundler,
        ))