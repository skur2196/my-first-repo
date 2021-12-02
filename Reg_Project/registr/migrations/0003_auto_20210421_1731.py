# Generated by Django 2.1 on 2021-04-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registr', '0002_patient_last_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='archive',
            field=models.FileField(blank=True, null=True, upload_to='archives/', verbose_name='Архив документов'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='type_register',
            field=models.CharField(choices=[('1', 'Регистр больных детей, страдающих гемофилией, болезнью Вилльбранда и другими наследственными коагулопатиями'), ('2', 'Регистр больных детей, страдающих тромбоцитопенией и тромбоцитопатией'), ('3', 'Регистр больных детей, страдающих наследственной анемией'), ('4', 'Регистр больных детей, страдающих приобретенной апластической анемией')], max_length=255, verbose_name='Тип регистра'),
        ),
        migrations.AlterField(
            model_name='user',
            name='access',
            field=models.CharField(choices=[('1', 'Редактировать, добавлять и просматривать'), ('2', 'Добавлять и просматривать'), ('3', 'Только просматривать')], default='2', max_length=50, verbose_name='Уровень доступа'),
        ),
    ]
