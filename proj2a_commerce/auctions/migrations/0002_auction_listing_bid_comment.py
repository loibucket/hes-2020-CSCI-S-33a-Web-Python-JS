# Generated by Django 3.0.3 on 2020-07-08 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction_Listing',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_bid', models.DecimalField(decimal_places=2, max_digits=9)),
                ('curr_bid', models.DecimalField(decimal_places=2, max_digits=9)),
                ('n_bids', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=300)),
            ],
        ),
    ]
