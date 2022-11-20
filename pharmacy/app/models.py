from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Address(models.Model):
    country = models.CharField(verbose_name="Страна", max_length=20)
    city = models.CharField(verbose_name="Город", max_length=20)
    street = models.CharField(verbose_name="Улица", max_length=20)
    number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.number}"

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адресы"


class Pharmacy(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=50)
    address = models.ForeignKey(Address,
                                verbose_name="Адрес",
                                related_name="address_pharmacy",
                                on_delete=models.SET_NULL,
                                null=True)
    state_number = models.CharField(verbose_name="Государственный номер", max_length=20)

    employee = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name} {self.state_number}"

    class Meta:
        verbose_name = "Аптека"
        verbose_name_plural = "Аптеки"


class ReleaseForm(models.Model):
    name = models.CharField(verbose_name="Форма выпуска", max_length=30)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Форма выпуска"
        verbose_name_plural = "Формы выпуска"


class Manufacturer(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=50)
    address = models.ForeignKey(Address,
                                verbose_name="Адрес",
                                related_name="address_manufacturer",
                                on_delete=models.SET_NULL,
                                null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Disease(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=50)
    treatment = models.CharField(verbose_name="Лечение", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Дозировка"
        verbose_name_plural = "Дозировки"


class Medicament(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=50)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=12)
    description = models.TextField(verbose_name="Описание")
    form_release = models.ForeignKey(ReleaseForm, verbose_name="Форма выпуска", on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, verbose_name="Заболевание", on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", on_delete=models.CASCADE)
    dosage = models.CharField(verbose_name="Дозировка", max_length=30)

    def __str__(self):
        return f"{self.name} {self.form_release} {self.disease} {self.price}"

    class Meta:
        verbose_name = "Лекарственное средство"
        verbose_name_plural = "Лекарственные средства"


class MedicamentInPharmacy(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, verbose_name="Аптека", on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, verbose_name="Лекарственное средство", on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0, verbose_name="Количество", validators=[MinValueValidator(0)])
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=12)
    expiration_date = models.DateField(verbose_name="Срок годности",)

    def __str__(self):
        return f"{self.pharmacy} {self.medicament} {self.price} {self.expiration_date}"

    class Meta:
        verbose_name = "Лекарственные средства в аптеке"
        verbose_name_plural = "Лекарственные средства в аптеке"


class Order(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, verbose_name="Аптека", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="дата заявки", auto_now_add=True)
    reason = models.CharField(verbose_name="Основние", max_length=100)
    total_price = models.DecimalField(verbose_name="Общая цена", decimal_places=2, max_digits=12)
    medicines = models.ManyToManyField(Medicament)
    writeoff = models.BooleanField(verbose_name="Списана", default=False)

    def __str__(self):
        return f"{self.pharmacy} {self.total_price} {self.writeoff}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Invoice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    reason = models.CharField(verbose_name="Основние", max_length=100)
    medicines = models.ManyToManyField(Medicament)
    total_price = models.DecimalField(verbose_name="Общая цена", decimal_places=2, max_digits=12)

    def __str__(self):
        return f"{self.order} {self.reason} {self.total_price}"

    class Meta:
        verbose_name = "Накладная"
        verbose_name_plural = "Накладные"


class Application(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Дата", auto_now_add=True)
    reason = models.CharField(verbose_name="Основние", max_length=100)
    total_price = models.DecimalField(verbose_name="Общая цена", decimal_places=2, max_digits=12)
    medicines = models.ManyToManyField(MedicamentInPharmacy)

    def __str__(self):
        return f"{self.date} {self.reason} {self.total_price}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
