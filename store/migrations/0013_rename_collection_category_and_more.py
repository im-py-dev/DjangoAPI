# Generated by Django 4.0.5 on 2022-06-22 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_customer_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collection',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='collection',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='store.order'),
        ),
    ]