from django.db import models


class User(models.Model):
    '''
    Таблица пользователей системы
    '''
    login = models.CharField(max_length=20, 
                    unique=True, verbose_name="Логин") # Логин пользователя
    password = models.CharField(max_length=15,
                    unique=False, verbose_name="Пароль") # Пароль
    user_name = models.CharField(max_length=60,
                    verbose_name="ФИО пользователя") # ФИО Пользователя
    position = models.CharField(max_length=70, 
                    blank=True, null=True, verbose_name="Должность") # Должность пользователя

    ACCESSES = (
        ('1', 'Редактировать, добавлять и просматривать'),
        ('2', 'Добавлять и просматривать'),
        ('3', 'Только просматривать'),
     ) # Возможные уровни доступа к редакции таблиц

    access = models.CharField(
        max_length=50,
        choices=ACCESSES,
        default='2',
        verbose_name="Уровень доступа"
    )

    def __srt__(self):
        return str(self.user_name)


class Patient(models.Model):
    '''
    Таблица онкобольных детей
    '''
    last_name = models.CharField(max_length=30,
                    verbose_name='Фамилия') # Фамилия ребенка
    first_name = models.CharField(max_length=30,
                    verbose_name='Имя') # Имя ребенка
    father_name = models.CharField(max_length=30,
                    verbose_name='Отчество') # Отчество ребенка
    date_birthday = models.DateField(verbose_name='Дата рождения') # Дата рождения ребенка
    address = models.CharField(max_length=255,
                    verbose_name='Адрес проживания') # Адресс ребенка
    diagnosis = models.CharField(max_length=255,
                    verbose_name='Диагноз') # Диагноз
    dosage = models.TextField(verbose_name='МНН Дозировка') # МНН Дозировка
    therapy = models.TextField(verbose_name='Схема лечения') # Схема лечения
    monthly_need = models.TextField(verbose_name='Месячная потребность') # Месячная потребность
    annual_need = models.TextField(verbose_name='Годовая потребность') # Годовая потребность

    REGISTERS = (
        ('1', 'Регистр больных детей, страдающих гемофилией, болезнью Вилльбранда и другими наследственными коагулопатиями'),
        ('2', 'Регистр больных детей, страдающих тромбоцитопенией и тромбоцитопатией'),
        ('3', 'Регистр больных детей, страдающих наследственной анемией'),
        ('4', 'Регистр больных детей, страдающих приобретенной апластической анемией')
    )
    type_register = models.CharField(max_length=255, choices=REGISTERS, verbose_name='Тип регистра') # Указываем тип регистра
    last_editor = models.OneToOneField(User, on_delete=models.SET_NULL, verbose_name='Последнее изменение', 
                    blank=True, null=True) # Указывает юзера, который последний проводил изменения
    archive = models.FileField(upload_to='archives/', verbose_name='Архив документов', null=True, blank=True)
    
    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.father_name

    def fio(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.father_name
