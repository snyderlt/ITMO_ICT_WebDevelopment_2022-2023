# Generated by Django 4.1.3 on 2022-12-03 10:58

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.AutoField(primary_key=True, serialize=False, verbose_name='ID_книги')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=70, verbose_name='ФИО автора')),
                ('publisher', models.CharField(max_length=30, verbose_name='Издательство')),
            ],
        ),
        migrations.CreateModel(
            name='BookRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id_instance', models.AutoField(primary_key=True, serialize=False, verbose_name='ID_экземпляра')),
                ('section', models.CharField(max_length=20, verbose_name='Раздел')),
                ('code', models.CharField(max_length=20, verbose_name='Артикул')),
                ('year', models.IntegerField(verbose_name='Год издания')),
                ('condition', models.CharField(choices=[('х', 'хорошее'), ('у', 'удовлетворительное'), ('с', 'старое')], max_length=1, verbose_name='Состояние экземпляра')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='Книга')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=20, verbose_name='Номер читательского билета')),
                ('name', models.CharField(max_length=70, verbose_name='ФИО')),
                ('passport', models.CharField(max_length=20, verbose_name='Номер паспорта')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('education', models.CharField(choices=[('н', 'начальное'), ('с', 'среднее'), ('в', 'высшее')], max_length=1, verbose_name='Образование')),
                ('degree', models.BooleanField(default=False, verbose_name='Наличие ученой степени')),
                ('registration_date', models.DateField(verbose_name='Дата регистрации')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('capacity', models.IntegerField(verbose_name='Вместимость')),
                ('books', models.ManyToManyField(related_name='book_room', through='library.BookRoom', to='library.instance', verbose_name='Книги')),
            ],
        ),
        migrations.CreateModel(
            name='ReaderRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата закрепления зала')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.reader', verbose_name='Читатель')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.room', verbose_name='Зал')),
            ],
        ),
        migrations.CreateModel(
            name='ReaderBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата выдачи экземпляра книги')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.instance', verbose_name='Книга')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.reader', verbose_name='Читатель')),
            ],
        ),
        migrations.AddField(
            model_name='reader',
            name='instances',
            field=models.ManyToManyField(related_name='reader_book', through='library.ReaderBook', to='library.instance', verbose_name='Взятые книги'),
        ),
        migrations.AddField(
            model_name='reader',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.room', verbose_name='Зал, за которым закреплен читатель'),
        ),
        migrations.AddField(
            model_name='bookroom',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.instance', verbose_name='Книга'),
        ),
        migrations.AddField(
            model_name='bookroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.room', verbose_name='Зал'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]