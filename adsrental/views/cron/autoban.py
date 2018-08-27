import datetime

from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.utils import timezone

from adsrental.models.lead import Lead
from adsrental.models.lead_account import LeadAccount
from adsrental.models.user import User


class AutoBanView(View):
    '''
    Check every entry :model:`adsrental.LeadAccount` and ban in if auto_ban_enabled is True
    and password is worng for more than 2 weeks or :model:`adsrental.RaspberryPi` is offline for 2 weeks.

    Parameters:

    * execute - ban accounts, dry run otherwise
    '''
    def get(self, request):
        admin_user = User.objects.get(email=settings.ADMIN_USER_EMAIL)
        banned_wrong_password = []
        banned_offline = []
        banned_security_checkpoint = []
        banned_not_used = []
        now = timezone.localtime(timezone.now())
        execute = request.GET.get('execute', '') == 'true'
        days_wrong_password = LeadAccount.AUTO_BAN_DAYS_WRONG_PASSWORD
        days_offline = LeadAccount.AUTO_BAN_DAYS_OFFLINE
        days_checkpoint = LeadAccount.AUTO_BAN_DAYS_SEC_CHECKPOINT
        days_delivered = LeadAccount.AUTO_BAN_DAYS_NOT_USED
        for lead_account in LeadAccount.objects.filter(
                wrong_password_date__lte=now - datetime.timedelta(days=days_wrong_password),
                status=LeadAccount.STATUS_IN_PROGRESS,
                active=True,
                auto_ban_enabled=True,
        ):
            banned_wrong_password.append({
                'account': str(lead_account),
                'wrong_password_date': lead_account.wrong_password_date.date()
            })
            if execute:
                lead_account.ban(admin_user, reason=LeadAccount.BAN_REASON_AUTO_WRONG_PASSWORD)

        for lead_account in LeadAccount.objects.filter(
                lead__raspberry_pi__last_seen__lte=now - datetime.timedelta(days=days_offline),
                status=LeadAccount.STATUS_IN_PROGRESS,
                active=True,
                auto_ban_enabled=True,
        ):
            banned_offline.append({
                'account': str(lead_account),
                'last_seen': lead_account.lead.raspberry_pi.last_seen.date()
            })
            if execute:
                lead_account.ban(admin_user, reason=LeadAccount.BAN_REASON_AUTO_OFFLINE)

        for lead_account in LeadAccount.objects.filter(
                security_checkpoint_date__lte=now - datetime.timedelta(days=days_checkpoint),
                status=LeadAccount.STATUS_IN_PROGRESS,
                active=True,
                auto_ban_enabled=True,
        ):
            banned_security_checkpoint.append({
                'account': str(lead_account),
                'security_checkpoint_date': lead_account.security_checkpoint_date.date()
            })
            if execute:
                lead_account.ban(admin_user, reason=LeadAccount.BAN_REASON_AUTO_CHECKPOINT)

        for lead_account in LeadAccount.objects.filter(
                status=Lead.STATUS_QUALIFIED,
                lead__delivery_date__lte=now - datetime.timedelta(days=days_delivered),
                active=True,
                auto_ban_enabled=True,
        ).select_related('lead'):
            banned_not_used.append({
                'account': str(lead_account),
                'delivery_date': lead_account.lead.delivery_date,
            })
            if execute:
                lead_account.ban(admin_user, reason=LeadAccount.BAN_REASON_AUTO_NOT_USED)

        return JsonResponse({
            'execute': execute,
            'result': True,
            'banned_wrong_password': banned_wrong_password,
            'banned_offline': banned_offline,
            'banned_security_checkpoint': banned_security_checkpoint,
            'banned_not_used': banned_not_used,
        })
