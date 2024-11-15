# Generated by Django 5.1.3 on 2024-11-15 05:11

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChemicalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Chemical Categories',
                'db_table': 'chemical_categories',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('movable', 'Movable'), ('fixed', 'Fixed')], max_length=10)),
                ('quantity_available', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('maintenance', 'Maintenance'), ('out_of_stock', 'Out of Stock')], max_length=15)),
                ('image_url', models.URLField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'equipments',
            },
        ),
        migrations.CreateModel(
            name='EquipmentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Equipment Categories',
                'db_table': 'equipment_categories',
            },
        ),
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity_available', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('unit', models.CharField(default='ml', max_length=20)),
                ('status', models.CharField(choices=[('in_stock', 'In Stock'), ('low_stock', 'Low Stock'), ('out_of_stock', 'Out of Stock')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='br_app.chemicalcategory')),
            ],
            options={
                'db_table': 'chemicals',
            },
        ),
        migrations.CreateModel(
            name='ChemicalWithdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdrawal_date', models.DateTimeField()),
                ('quantity_withdrawn', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('remaining_quantity', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chemical', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='br_app.chemical')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chemical_withdrawals',
            },
        ),
        migrations.CreateModel(
            name='BorrowEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('actual_return_date', models.DateTimeField(blank=True, null=True)),
                ('fine', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('status', models.CharField(choices=[('borrowed', 'Borrowed'), ('returned', 'Returned'), ('overdue', 'Overdue')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='br_app.equipment')),
            ],
            options={
                'db_table': 'borrow_equipments',
            },
        ),
        migrations.AddField(
            model_name='equipment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='br_app.equipmentcategory'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('staff', 'Staff'), ('admin', 'Admin')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profiles',
            },
        ),
    ]
