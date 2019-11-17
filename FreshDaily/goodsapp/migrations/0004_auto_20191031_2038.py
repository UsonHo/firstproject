# Generated by Django 2.2.4 on 2019-10-31 12:38

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0003_auto_20191030_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gbrief',
            field=models.CharField(max_length=100, verbose_name='商品简介'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(verbose_name='商品人气'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(verbose_name='详情内容'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='goodsPic', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gstock',
            field=models.IntegerField(verbose_name='商品库存'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=20, verbose_name='商品标题'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.TypeInfo', verbose_name='商品类型'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default='500g', max_length=10, verbose_name='单位'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='ttitle',
            field=models.CharField(max_length=10, verbose_name='商品类型'),
        ),
    ]