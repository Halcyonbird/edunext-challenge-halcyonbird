# Generated by Django 3.2.3 on 2021-06-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerdataapi', '0003_auto_20210607_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdata',
            name='CREATION_DATE',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='customerdata',
            name='LAST_PAYMENT_DATE',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customerdata',
            name='SUBSCRIPTION',
            field=models.CharField(choices=[('free', 'Free'), ('basic', 'Basic'), ('premium', 'Premium')], default='1', max_length=9, null=True),
        ),
    ]
