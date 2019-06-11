# Generated by Django 2.2 on 2019-06-11 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('plan_type', models.CharField(choices=[('Enterprise', 'ent'), ('Professional', 'pro'), ('Free', 'free')], default='Free', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stripe_plan_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(max_length=40)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.Plan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=True)),
                ('user_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.UserPlan')),
            ],
        ),
    ]
