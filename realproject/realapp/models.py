from django.utils import timezone
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

class Contact(models.Model):
    message=models.TextField()
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)

    class Meta:
        db_table='Contact'
# Create your models here.

class Admin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)

    class Meta:
        db_table='Admin'

class AddNotification(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Notification'


class Registration(models.Model):
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # better to prevent duplicates at DB level too
    mobile_number = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    status = models.CharField(max_length=20, default="Pending")
    otp = models.CharField(max_length=6, null=True, blank=True)

    class Meta:
        db_table = 'Register'


class Designer(models.Model):
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pincode = models.IntegerField()
    gender = models.CharField(max_length=20)
    experience = models.IntegerField()
    specialization = models.CharField(max_length=200)
    aboutme = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    otp = models.CharField(max_length=6, null=True, blank=True)
    class Meta:
        db_table = 'Designer'

class DesignerGallery(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='designer_gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'DesignerGallery'
        verbose_name_plural = 'Designer Galleries'


from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

class DesignerService(models.Model):
    designer = models.ForeignKey(
        "Designer",
        on_delete=models.CASCADE,
        related_name="services"
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    timeperiod = models.PositiveIntegerField(
        help_text="Estimated completion time in days"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    image = models.ImageField(
        upload_to="service_images/",
        blank=True,
        null=True,
        help_text="Upload an image representing the service"
    )

    class Meta:
        db_table = "DesignerService"

class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),       # ✅ new
        ("picked_up", "Picked Up"),     # ✅ new
        ("in_progress", "In Progress"), # ✅ new
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name="bookings")
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name="bookings")
    service = models.ForeignKey(DesignerService, on_delete=models.CASCADE, related_name="bookings")

    booking_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.DateField(help_text="Date when service should start")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    actual_start_date = models.DateField(null=True, blank=True)
    expected_end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "Booking"
        ordering = ["-booking_date"]

class Review(models.Model):
    booking = models.OneToOneField(
        "Booking",
        on_delete=models.CASCADE,
        related_name="review"
    )
    customer = models.ForeignKey(
        "Registration",
        on_delete=models.CASCADE,
    )
    designer = models.ForeignKey(
        "Designer",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.PositiveSmallIntegerField(default=0)  # range 0–5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Review"
        ordering = ["-created_at"]
