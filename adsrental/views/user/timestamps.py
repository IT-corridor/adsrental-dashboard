import datetime

from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect

from adsrental.models.lead import Lead
from adsrental.models.lead_history import LeadHistory


class UserTimestampsView(View):
    @staticmethod
    def last_day_of_month(any_day):
        next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
        return next_month - datetime.timedelta(days=next_month.day)

    def get(self, request):
        leadid = request.session.get('leadid')
        lead = Lead.objects.filter(leadid=leadid).first()
        if not lead:
            return redirect('user_login')

        date = datetime.datetime.strptime(request.GET.get('date', '2018-01-01'), settings.SYSTEM_DATE_FORMAT)
        date_start = date.replace(day=1)
        date_end = self.last_day_of_month(date)

        return render(request, 'user/timestamps.html', dict(
            lead=lead,
            lead_accounts=lead.lead_accounts.all(),
            date_start=date_start,
            date_end=date_end,
            raspberry_pi=lead.raspberry_pi,
            lead_histories=LeadHistory.objects.filter(
                lead=lead,
                date__gte=date_start,
                date__lte=date_end,
            ).order_by('-date'),
        ))