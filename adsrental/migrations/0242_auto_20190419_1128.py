# Generated by Django 2.1.7 on 2019-04-19 18:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0241_leadaccountissue_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadAccountIssueImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='leadaccountissue',
            name='image',
        ),
        migrations.AddField(
            model_name='leadaccountissueimage',
            name='lead_account_issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='image', to='adsrental.LeadAccountIssue'),
        ),
    ]
