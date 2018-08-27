import datetime

from django.views import View
from django.utils import timezone
from django.shortcuts import render, Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from adsrental.models.lead_account import LeadAccount
from adsrental.models.lead import Lead


class AutoBanSoonView(View):
    template_name = 'report/autoban_soon.html'

    @method_decorator(login_required)
    def get(self, request):
        if not request.user.is_superuser:
            raise Http404

        now = timezone.localtime(timezone.now())
        wrong_password_lead_accounts = LeadAccount.objects.filter(
            wrong_password_date__lte=now - datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_WRONG_PASSWORD - 3),
            status=LeadAccount.STATUS_IN_PROGRESS,
            active=True,
            auto_ban_enabled=True,
        ).order_by('wrong_password_date').select_related('lead')
        for lead_account in wrong_password_lead_accounts:
            lead_account.ban_timedelta = lead_account.wrong_password_date + datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_WRONG_PASSWORD) - now

        offline_lead_accounts = LeadAccount.objects.filter(
            lead__raspberry_pi__last_seen__lte=now - datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_OFFLINE - 3),
            status=LeadAccount.STATUS_IN_PROGRESS,
            active=True,
            auto_ban_enabled=True,
        ).order_by('lead__raspberry_pi__last_seen').select_related('lead', 'lead__raspberry_pi')
        for lead_account in offline_lead_accounts:
            lead_account.ban_timedelta = lead_account.lead.raspberry_pi.last_seen + datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_OFFLINE) - now

        sec_checkpoint_lead_accounts = LeadAccount.objects.filter(
            security_checkpoint_date__lte=now - datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_SEC_CHECKPOINT - 3),
            status=LeadAccount.STATUS_IN_PROGRESS,
            active=True,
            auto_ban_enabled=True,
        ).order_by('security_checkpoint_date').select_related('lead')
        for lead_account in sec_checkpoint_lead_accounts:
            lead_account.ban_timedelta = lead_account.security_checkpoint_date + datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_SEC_CHECKPOINT) - now

        not_used_lead_accounts = LeadAccount.objects.filter(
            status=Lead.STATUS_QUALIFIED,
            lead__delivery_date__lte=now - datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_NOT_USED - 4),
            active=True,
            auto_ban_enabled=True,
        ).order_by('lead__delivery_date').select_related('lead')
        for lead_account in not_used_lead_accounts:
            lead_account.ban_timedelta = datetime.datetime.combine(lead_account.lead.delivery_date, datetime.datetime.min.time()).replace(tzinfo=timezone.get_default_timezone()) + datetime.timedelta(days=LeadAccount.AUTO_BAN_DAYS_NOT_USED + 1) - now

        context = dict(
            wrong_password_lead_accounts=wrong_password_lead_accounts,
            sec_checkpoint_lead_accounts=sec_checkpoint_lead_accounts,
            not_used_lead_accounts=not_used_lead_accounts,
            offline_lead_accounts=offline_lead_accounts,
        )

        return render(request, self.template_name, context)
