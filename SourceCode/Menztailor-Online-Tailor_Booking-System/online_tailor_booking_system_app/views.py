from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import DatabaseError, models
from django.contrib.auth.hashers import make_password, check_password
from .models import Contact, Admin, AddNotification, Registration, Designer, Booking
from .forms import ContactForm, AdminForm, AddNotificationForm, RegistrationForm, DesignerForm, DesignerServiceForm,BookingForm, ReviewForm
from django.db.models import Q, Avg # Import Q and Avg
import random

# ------------------------------ General ------------------------------


def index(request):
    try:
        return render(request, 'index.html', {})
    except Exception as e:
        # In case the template fails to load
        return HttpResponse(f"Error loading page: {e}")

def about(request):
    try:
        return render(request, 'about.html', {})
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect('index')

def contact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'contact.html', {'msg': 'You have contacted successfully'})
            else:
                return render(request, 'contact.html', {'msg': 'There has been a mistake'})
        return render(request, 'contact.html', {})
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return render(request, 'contact.html', {'msg': 'Something went wrong'})


# ------------------------------ Admin ------------------------------
# ------------------------------ Admin ------------------------------
# ------------------------------ Admin ------------------------------
# ------------------------------ Admin ------------------------------


def admin_login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            exists = Admin.objects.filter(email=email, password=password).exists()
            if exists:
                request.session['email'] = email
                return redirect('admin_index')
            else:
                return render(request, 'admin_login.html', {'msg': 'Incorrect email or password'})
        return render(request, 'admin_login.html', {})
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return render(request, 'admin_login.html', {'msg': 'Something went wrong'})

def admin_logout(request):
    try:
        request.session.flush()
        return render(request, 'index.html', {'msg': 'Logout successfully'})
    except Exception as e:
        messages.error(request, f"Error during logout: {e}")
        return redirect('index')

def admin_index(request):
    try:
        return render(request, 'admin_index.html', {})
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect('admin_login')


from django.shortcuts import render, redirect  # Ensure redirect is imported
from django.contrib import messages


def add_notification(request):
    try:
        if request.method == 'POST':
            form = AddNotificationForm(request.POST)
            if form.is_valid():
                form.save()
                # 1. Use messages for the success alert
                messages.success(request, 'Notification added successfully')
                # 2. Redirect to the view_notification URL name
                return redirect('view_notification')
            else:
                return render(request, 'add_notification.html', {'form': form})
        else:
            form = AddNotificationForm()
            return render(request, 'add_notification.html', {'form': form})

    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return render(request, 'add_notification.html', {'form': AddNotificationForm()})

def view_notification(request):
    try:
        con = AddNotification.objects.all()
        return render(request, 'view_notification.html', {'con': con})
    except DatabaseError as e:
        messages.error(request, f"Error fetching notifications: {e}")
        return render(request, 'view_notification.html', {})

def admin_change_password(request):
    email = request.session.get('email')
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        try:
            user = Admin.objects.get(email=email)
            if user.password != old_password:
                messages.error(request, "Old password is incorrect!")
                return redirect("admin_change_password")
            if new_password == old_password:
                messages.error(request, "New password cannot be same as old password!")
                return redirect("admin_change_password")

            user.password = new_password
            user.save()
            messages.success(request, "Password changed successfully!")
            return redirect("admin_login")
        except DatabaseError as e:
            messages.error(request, f"Database error: {e}")
    return render(request, "admin_change_password.html", {"email": email})

def delete_notification(request, id):
    try:
        contact = get_object_or_404(AddNotification, id=id)
        contact.delete()
        messages.success(request, "Notification deleted successfully")
    except DatabaseError as e:
        messages.error(request, f"Error deleting notification: {e}")
    return redirect('view_notification')

def admin_view_customer(request):
    try:
        users = Registration.objects.all()
        return render(request, "admin_view_customer.html", {"reg": users})
    except DatabaseError as e:
        messages.error(request, f"Error fetching customers: {e}")
        return render(request, "admin_view_customer.html", {"reg": []})

def accept_customer(request, id):
    try:
        reg = get_object_or_404(Registration, id=id)
        reg.status = "accepted"
        reg.save()
        messages.success(request, f"Customer {reg.name} accepted successfully.")
    except DatabaseError as e:
        messages.error(request, f"Error updating customer: {e}")
    return redirect('admin_view_customer')

def decline_customer(request, id):
    try:
        reg = get_object_or_404(Registration, id=id)
        reg.status = "declined"
        reg.save()
        messages.success(request, f"Customer {reg.name} declined successfully.")
    except DatabaseError as e:
        messages.error(request, f"Error updating customer: {e}")
    return redirect('admin_view_customer')

def admin_view_designer(request):
    try:
        users = Designer.objects.all()
        return render(request, "admin_view_designer.html", {"reg": users})
    except DatabaseError as e:
        messages.error(request, f"Error fetching customers: {e}")
        return render(request, "admin_view_designer.html", {"reg": []})

from django.shortcuts import get_object_or_404, redirect
# Make sure to import Designer
from .models import Designer, Registration


def accept_designer(request, id):
    try:
        # Get the designer object
        designer = get_object_or_404(Designer, id=id)

        # Update status
        designer.status = "accepted"
        designer.save()

        messages.success(request, f"Designer {designer.fullname} accepted successfully.")

    except Exception as e:
        messages.error(request, f"Error updating designer: {e}")

    return redirect('admin_view_designer')


def decline_designer(request, id):
    try:
        # Get the designer object
        designer = get_object_or_404(Designer, id=id)

        # Update status
        designer.status = "declined"
        designer.save()

        messages.success(request, f"Designer {designer.fullname} declined.")

    except Exception as e:
        messages.error(request, f"Error updating designer: {e}")

    return redirect('admin_view_designer')

def view_contact(request):
    try:
        con = Contact.objects.all()
        return render(request, "view_contact.html" , {"con": con})
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return render(request, "view_contact.html", {"con": []})



# ------------------------------ Customer ------------------------------
# ------------------------------ Customer ------------------------------
# ------------------------------ Customer ------------------------------
# ------------------------------ Customer ------------------------------

def customer_index(request):
    return render(request, 'customer_index.html', {})

def customer_registration(request):
    try:
        if request.method == 'POST':
            form = RegistrationForm(request.POST, request.FILES)
            email = request.POST.get('email')
            password = request.POST.get('password')

            if Registration.objects.filter(email=email).exists():
                messages.error(request, 'This Email is already registered')
                return render(request, "customer_registration.html", {"form": form})

            if form.is_valid():
                customer = form.save(commit=False)
                customer.password = make_password(password)
                customer.status = "Pending"
                customer.save()

                # Send confirmation email
                try:
                    send_mail(
                        "Welcome to Our Store!",
                        f"Hi {customer.name}, thanks for registering with us!",
                        settings.EMAIL_HOST_USER,
                        [customer.email],
                        fail_silently=False
                    )
                except Exception as e:
                    print("Email send error:", e)

                return render(request, "customer_login.html", {
                    "msg": "✅ Successfully Registered! Please Login.."
                })
            else:
                return render(request, "customer_registration.html", {"form": form, "errors": form.errors})
        return render(request, "customer_registration.html", {"form": RegistrationForm()})
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return render(request, "customer_registration.html", {"form": RegistrationForm()})


def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Registration.objects.get(email=email)

            if user.status != "accepted":
                if user.status == "declined":
                    msg = "Your registration has been rejected."
                else:
                    msg = "Your registration is not approved yet."
                return render(request, "customer_login.html", {"msg": msg})

            if check_password(password, user.password):
                # --- OTP LOGIC ---

                # 1. Generate a random 4-digit OTP
                otp = str(random.randint(1000, 9999))

                # 2. Store OTP in the DATABASE (not session)
                user.otp = otp
                user.save()  # This updates the OTP in the DB

                # 3. Store email in session strictly for identification in next step
                request.session['temp_email'] = email

                # 4. Send OTP via Email
                try:
                    send_mail(
                        subject="Your Login OTP",
                        message=f"Hello {user.name},\n\nYour OTP for login is: {otp}\n\nDo not share this with anyone.",
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email],
                        fail_silently=False
                    )
                    messages.success(request, f"OTP sent to {email}")
                    return redirect('validate_otp')

                except Exception as e:
                    messages.error(request, f"Error sending email: {e}")
                    return render(request, "customer_login.html", {})

            else:
                return render(request, "customer_login.html", {"msg": "Invalid email or password"})

        except Registration.DoesNotExist:
            return render(request, "customer_login.html", {"msg": "Invalid email or password"})

    return render(request, 'customer_login.html', {})


def validate_otp(request):
    # Check if we have a temporary email in session
    if 'temp_email' not in request.session:
        messages.error(request, "Session expired. Please login again.")
        return redirect('customer_login')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        temp_email = request.session.get('temp_email')

        try:
            # 1. Fetch the user from the database
            user = Registration.objects.get(email=temp_email)

            # 2. Check if the entered OTP matches the one in the Database
            if user.otp == entered_otp:

                # --- SUCCESS ---
                request.session['email'] = temp_email  # Log the user in

                # Optional: Clear the OTP from DB so it can't be reused
                user.otp = None
                user.save()

                # Cleanup session
                del request.session['temp_email']
                return redirect('customer_index')

            else:
                # --- WRONG OTP ---
                messages.error(request, "Invalid OTP. Please try again.")
                return render(request, 'validate_otp.html')

        except Registration.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('customer_login')

    return render(request, 'validate_otp.html')


def initiate_forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = Registration.objects.get(email=email)

            # --- REUSING OTP GENERATION LOGIC ---
            otp = str(random.randint(1000, 9999))
            user.otp = otp
            user.save()

            # Store email in session for the next step
            request.session['temp_email'] = email

            # Send Email
            try:
                send_mail(
                    subject="Reset Password OTP",
                    message=f"Hello {user.name},\n\nYour OTP to reset password is: {otp}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False
                )
                messages.success(request, "OTP sent to your email.")
                # Redirect to the NEW validation view
                return redirect('validate_forgot_otp')

            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

        except Registration.DoesNotExist:
            messages.error(request, "Email not registered.")

    return render(request, 'initiate_forgot_password.html')


def validate_forgot_otp(request):
    # Check if we have the email from Step 1
    if 'temp_email' not in request.session:
        messages.error(request, "Session expired. Start over.")
        return redirect('initiate_forgot_password')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        temp_email = request.session.get('temp_email')

        try:
            user = Registration.objects.get(email=temp_email)

            if user.otp == entered_otp:
                # --- SUCCESS ---

                # 1. Clear OTP so it can't be used again
                user.otp = None
                user.save()

                # 2. Set a specific flag proving they passed the OTP check
                request.session['can_reset_password'] = True

                # 3. Redirect to the Set New Password view
                return redirect('customer_forgot_password')

            else:
                messages.error(request, "Invalid OTP. Please try again.")

        except Registration.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('initiate_forgot_password')

    return render(request, 'validate_otp.html')  # You can reuse the HTML template


def customer_forgot_password(request):
    # 1. Security Check: Did they pass the OTP validation?
    if not request.session.get('can_reset_password'):
        return redirect('initiate_forgot_password')

    # Get the email from the session (set in Step 1)
    email = request.session.get('temp_email')
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        try:
            user = Registration.objects.get(email=email)

            # Check if new password is same as old
            if check_password(new_password, user.password):
                messages.error(request, "New password cannot be the same as the old password.")
                return redirect("customer_forgot_password")

            # Update Password
            user.password = make_password(new_password)
            user.save()

            # --- CLEANUP ---
            # Remove session variables so they can't reset it again immediately
            if 'temp_email' in request.session:
                del request.session['temp_email']
            if 'can_reset_password' in request.session:
                del request.session['can_reset_password']

            messages.success(request, "Password changed successfully! Please login.")
            return redirect("customer_login")

        except Registration.DoesNotExist:
            messages.error(request, "User not found.")
        except Exception as e:
            messages.error(request, f"Error: {e}")

    return render(request, "customer_forgot_password.html")

# def customer_forgot_password(request):
#     email=request.session.get('email')
#     if request.method=="POST":
#         new_password=request.POST.get('new_password')
#         try:
#             user=Registration.objects.get(email=email)
#             if check_password(new_password,user.password):
#                 messages.error(request,"The password is same as old password")
#                 return redirect("customer_forgot_password")
#             user.password=make_password(new_password)
#             user.save()
#             messages.success(request, "Password changed successfully!")
#             return redirect("customer_login")
#         except DatabaseError as e:
#             messages.error(request, f"Database error: {e}")
#     return render(request, "customer_forgot_password.html", {"email": email})

def customer_change_password(request):
    email = request.session.get('email')
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        try:
            user = Registration.objects.get(email=email)
            if not check_password(old_password, user.password):
                messages.error(request, "Old password is incorrect!")
                return redirect("customer_change_password")
            if check_password(new_password, user.password):
                messages.error(request, "New password cannot be same as old password!")
                return redirect("customer_change_password")

            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password changed successfully!")
            return redirect("customer_login")
        except DatabaseError as e:
            messages.error(request, f"Database error: {e}")
    return render(request, "customer_change_password.html", {"email": email})

def profile(request):
    try:
        email = request.session.get("email")
        if email:
            user = Registration.objects.get(email=email)
            return render(request, "profile.html", {"reg": [user]})
        else:
            return render(request, "profile.html", {"msg": "⚠️ You must log in first."})
    except Registration.DoesNotExist:
        messages.error(request, "Profile not found")
        return redirect("customer_login")
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return redirect("customer_login")

def customer_profile_update(request, id):
    try:
        contact = get_object_or_404(Registration, id=id)
        if request.method == 'POST':
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.mobile_number = request.POST.get('mobile_number')
            contact.city = request.POST.get('city')
            contact.address = request.POST.get('address')
            contact.pincode = request.POST.get('pincode')

            if 'profile_image' in request.FILES:
                contact.profile_image = request.FILES['profile_image']

            contact.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')
        return render(request, 'customer_profile_update.html', {'contact': contact})
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return redirect('profile')

def delete_profile(request, id):
    try:
        contact = get_object_or_404(Registration, id=id)
        contact.delete()
        messages.success(request, "Profile deleted successfully")
    except DatabaseError as e:
        messages.error(request, f"Error deleting profile: {e}")
    return redirect('profile')

def customer_logout(request):
    try:
        request.session.flush()
        return render(request, 'customer_login.html', {'msg': 'Logout successfully'})
    except Exception as e:
        messages.error(request, f"Error during logout: {e}")
        return redirect('index')



from django.db.models import Q, Avg  # Ensure Q and Avg are imported


def customer_view_designer(request):
    query = request.GET.get('q')
    specialization_filter = request.GET.get('specialization_filter')
    gender_filter = request.GET.get('gender_filter')

    designers_queryset = Designer.objects.all()

    if query:
        designers_queryset = designers_queryset.filter(
            Q(fullname__icontains=query) |
            Q(city__icontains=query) |
            Q(specialization__icontains=query) |
            Q(gender__icontains=query) |
            Q(experience__icontains=query)
        )

    # ✅ FIXED specialization filter
    if specialization_filter:
        designers_queryset = designers_queryset.filter(
            specialization__regex=rf'(^|,){specialization_filter}(,|$)'
        )

    if gender_filter:
        designers_queryset = designers_queryset.filter(
            gender__iexact=gender_filter
        )

    designers = designers_queryset.distinct()

    for designer in designers:
        avg_rating = designer.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
        designer.avg_rating = round(avg_rating, 2)

    return render(request, "customer_view_designer.html", {
        "reg": designers,
        "query": query,
        "specialization_filter": specialization_filter,
        "gender_filter": gender_filter,
    })


def customer_view_notification(request):
    try:
        con = AddNotification.objects.all()
        return render(request, 'customer_view_notification.html', {'con': con})
    except DatabaseError as e:
        messages.error(request, f"Error fetching notifications: {e}")
        return render(request, 'customer_view_notification.html', {})

def customer_view_designer_detail(request, id):
    try:
        # Get designer by ID
        designer = get_object_or_404(Designer, id=id)

        # Get that designer's gallery images
        gallery = designer.gallery_images.all()

        return render(request, "customer_view_designer_detail.html", {
            "designer": designer,
            "gallery": gallery
        })

    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return redirect("customer_view_designer")




def customer_view_designer_services(request, id):
    try:
        designer = get_object_or_404(Designer, id=id)
        services = designer.services.all()  # thanks to related_name
        return render(request, "customer_view_designer_services.html", {
            "designer": designer,
            "services": services
        })
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return redirect("customer_view_designer")


def book_service(request, service_id):
    email = request.session.get("email")
    if not email:
        messages.error(request, "⚠️ You must log in to book a service.")
        return redirect("customer_login")

    customer = get_object_or_404(Registration, email=email)
    service = get_object_or_404(DesignerService, id=service_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = customer
            booking.service = service
            booking.designer = service.designer
            booking.total_price = service.price
            booking.save()

            # ✅ Send confirmation emails
            try:
                # To Customer
                send_mail(
                    subject="✅ Booking Confirmed!",
                    message=f"Hi {customer.name}, your booking for '{service.title}' has been placed successfully with designer {service.designer.fullname}.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[customer.email],
                    fail_silently=False,
                )

                # To Designer
                send_mail(
                    subject="🎨 New Booking Received!",
                    message=f"Hello {service.designer.fullname}, you have received a new booking from {customer.name} for '{service.title}'.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[service.designer.email],
                    fail_silently=False,
                )
            except Exception as e:
                print("Email send error:", e)

            messages.success(request, "✅ Booking successful! Email notifications sent.")
            return redirect("customer_view_designer")
    else:
        form = BookingForm()

    return render(request, "booking_form.html", {"form": form, "service": service})

def view_orders(request):
    email = request.session.get('email')
    if email:
        customer = get_object_or_404(Registration, email=email)
        orders = Booking.objects.filter(customer=customer)  # ✅ use Booking, not DesignerService
        return render(request, 'View_orders.html', {'reg': orders})
    else:
        messages.error(request, 'There is a problem with email')
        return redirect('index')


from .models import Booking, Review, Registration
from .forms import ReviewForm

from django.db import IntegrityError

def add_review(request, booking_id):
    email = request.session.get('email')
    if not email:
        messages.error(request, "You must log in to leave a review.")
        return redirect('customer_login')

    customer = get_object_or_404(Registration, email=email)
    booking = get_object_or_404(Booking, id=booking_id, customer=customer)

    # ✅ Check if this booking already has a review
    if hasattr(booking, 'review'):
        messages.warning(request, "You have already reviewed this booking.")
        return redirect('view_orders')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                review = form.save(commit=False)
                review.booking = booking
                review.customer = customer
                review.designer = booking.designer
                review.save()
                messages.success(request, "✅ Review submitted successfully!")
                return redirect('view_orders')
            except IntegrityError:
                messages.error(request, "You have already reviewed this booking.")
                return redirect('view_orders')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'booking': booking})


def customer_view_reviews(request, designer_id):
    designer = get_object_or_404(Designer, id=designer_id)
    reviews = designer.reviews.select_related('customer', 'booking').all()

    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 2)

    return render(request, 'customer_view_reviews.html', {
        'designer': designer,
        'reviews': reviews,
        'avg_rating': avg_rating
    })

#-----------------------------Designer------------------------------------------------------------------
#-----------------------------Designer------------------------------------------------------------------
#-----------------------------Designer------------------------------------------------------------------


def designer_index(request):
    email = request.session.get("email")
    designer = None
    if email:
        try:
            designer = Designer.objects.get(email=email)
        except Designer.DoesNotExist:
            pass
    return render(request, 'designer_index.html', {"designer": designer})


import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Designer  # Ensuring we import Designer


def designer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Designer.objects.get(email=email)

            # 1. Status Check
            if user.status != "accepted":
                if user.status == "declined":
                    msg = "Your registration has been rejected."
                else:
                    msg = "Your registration is not approved yet."
                return render(request, "designer_login.html", {"msg": msg})

            # 2. Password Check
            if check_password(password, user.password):

                # --- OTP LOGIC START ---
                # Generate a random 4-digit OTP
                otp = str(random.randint(1000, 9999))

                # Store OTP in the Designer DATABASE
                user.otp = otp
                user.save()

                # Store email in session strictly for identification in next step
                request.session['temp_email'] = email

                # Send OTP via Email
                try:
                    # UPDATED: Using user.fullname
                    send_mail(
                        subject="Designer Login OTP",
                        message=f"Hello {user.fullname},\n\nYour OTP for login is: {otp}\n\nDo not share this with anyone.",
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email],
                        fail_silently=False
                    )
                    messages.success(request, f"OTP sent to {email}")
                    return redirect('validate_designer_otp')

                except Exception as e:
                    messages.error(request, f"Error sending email: {e}")
                    return render(request, "designer_login.html", {})

                # --- OTP LOGIC END ---

            else:
                return render(request, "designer_login.html", {"msg": "Invalid email or password"})

        except Designer.DoesNotExist:
            return render(request, "designer_login.html", {"msg": "Invalid email or password"})
        except Exception as e:  # Catch generic DB errors
            messages.error(request, f"System error: {e}")
            return render(request, "designer_login.html", {})

    return render(request, 'designer_login.html', {})


def validate_designer_otp(request):
    """
    Validates OTP specifically for the Designer model.
    """
    # Check if we have a temporary email in session
    if 'temp_email' not in request.session:
        messages.error(request, "Session expired. Please login again.")
        return redirect('designer_login')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        temp_email = request.session.get('temp_email')

        try:
            # 1. Fetch the USER from the DESIGNER table
            user = Designer.objects.get(email=temp_email)

            # 2. Check if the entered OTP matches the one in the Database
            if user.otp == entered_otp:

                # --- SUCCESS ---
                request.session['email'] = temp_email  # Fully Log the designer in

                # Clear the OTP from DB so it can't be reused
                user.otp = None
                user.save()

                # Cleanup session
                del request.session['temp_email']

                return redirect('designer_index')

            else:
                # --- WRONG OTP ---
                messages.error(request, "Invalid OTP. Please try again.")
                return render(request, 'validate_designer_otp.html')

        except Designer.DoesNotExist:
            messages.error(request, "Designer not found.")
            return redirect('designer_login')

    return render(request, 'validate_designer_otp.html')


def initiate_designer_forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = Designer.objects.get(email=email)

            # --- OTP GENERATION ---
            otp = str(random.randint(1000, 9999))
            user.otp = otp
            user.save()

            # Store email in session for the next step
            request.session['temp_email'] = email

            # Send Email
            try:
                # Note: Using user.fullname as per your Designer model
                send_mail(
                    subject="Designer Reset Password OTP",
                    message=f"Hello {user.fullname},\n\nYour OTP to reset password is: {otp}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False
                )
                messages.success(request, "OTP sent to your email.")
                # Redirect to the NEW designer validation view
                return redirect('validate_designer_forgot_otp')

            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

        except Designer.DoesNotExist:
            messages.error(request, "Email not registered.")

    return render(request, 'initiate_designer_forgot_password.html')


def validate_designer_forgot_otp(request):
    # Check if we have the email from Step 1
    if 'temp_email' not in request.session:
        messages.error(request, "Session expired. Start over.")
        return redirect('initiate_designer_forgot_password')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        temp_email = request.session.get('temp_email')

        try:
            user = Designer.objects.get(email=temp_email)

            if user.otp == entered_otp:
                # --- SUCCESS ---

                # 1. Clear OTP so it can't be used again
                user.otp = None
                user.save()

                # 2. Set a specific flag proving they passed the OTP check
                # distinct name to avoid mixing with customer flow
                request.session['can_reset_designer_password'] = True

                # 3. Redirect to the Set New Password view
                return redirect('designer_forgot_password')

            else:
                messages.error(request, "Invalid OTP. Please try again.")

        except Designer.DoesNotExist:
            messages.error(request, "Designer not found.")
            return redirect('initiate_designer_forgot_password')

    # You can reuse the generic validate_otp.html if you want,
    # or make a specific validate_designer_otp.html
    return render(request, 'validate_designer_otp.html')


def designer_forgot_password(request):
    # 1. Security Check
    if not request.session.get('can_reset_designer_password'):
        return redirect('initiate_designer_forgot_password')

    # Get the email from the session
    email = request.session.get('temp_email')

    if request.method == "POST":
        new_password = request.POST.get('new_password')
        try:
            user = Designer.objects.get(email=email)
            # ... (your existing password logic)
            user.password = make_password(new_password)
            user.save()

            # Cleanup session
            request.session.pop('temp_email', None)
            request.session.pop('can_reset_designer_password', None)

            messages.success(request, "Password changed successfully!")
            return redirect("designer_login")
        except Exception as e:
            messages.error(request, f"Error: {e}")

    # --- FIX HERE: Pass the email variable to the template ---
    return render(request, "designer_forgot_password.html", {'email': email})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Designer


def designer_change_password(request):
    email = request.session.get('email')

    # 1. Fetch the designer object to pass to the header
    try:
        designer = Designer.objects.get(email=email)
    except Designer.DoesNotExist:
        messages.error(request, "Session error. Please login again.")
        return redirect("designer_login")

    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        try:
            # 2. Verify Old Password
            if not check_password(old_password, designer.password):
                messages.error(request, "Old password is incorrect!")
                return redirect("designer_change_password")

            # 3. Check if new password is same as old
            if check_password(new_password, designer.password):
                messages.error(request, "New password cannot be same as old password!")
                return redirect("designer_change_password")

            # 4. Hash and Save New Password
            designer.password = make_password(new_password)
            designer.save()

            messages.success(request, "Password changed successfully! Please login again.")
            return redirect("designer_login")

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    # 5. Pass 'designer' in the context dictionary
    return render(request, "designer_change_password.html", {
        "email": email,
        "designer": designer
    })


def designer_registration(request):
    try:
        if request.method == 'POST':
            form = DesignerForm(request.POST, request.FILES)

            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                if Designer.objects.filter(email=email).exists():
                    messages.error(request, '⚠️ This email is already registered.')
                    return render(request, 'designer_registration.html', {'form': form})

                designer = form.save(commit=False)
                designer.password = make_password(password)
                designer.save()

                return render(
                    request,
                    "designer_login.html",
                    {"msg": "✅ Successfully Registered! Please Login.."}
                )
            else:
                print("Form Errors:", form.errors)
                return render(request, "designer_registration.html", {"form": form, "errors": form.errors})

        else:
            form = DesignerForm()
            return render(request, 'designer_registration.html', {'form': form})

    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return render(request, 'designer_registration.html', {'form': DesignerForm()})


def designer_profile(request):
    email = request.session.get("email")
    if not email:
        return redirect("designer_login")

    designer = get_object_or_404(Designer, email=email)
    return render(request, "designer_profile.html", {
        "reg": [designer],
        "designer": designer  # ✅ pass designer to template
    })


def designer_update_profile(request, id):
    contact = get_object_or_404(Designer, id=id)

    if request.method == 'POST':
        # 1. Standard Fields
        contact.fullname = request.POST.get('fullname')
        contact.email = request.POST.get('email')
        contact.mobile_number = request.POST.get('mobile_number')
        contact.address = request.POST.get('address')
        contact.city = request.POST.get('city')
        contact.location = request.POST.get('location')
        contact.pincode = request.POST.get('pincode')
        contact.gender = request.POST.get('gender')
        contact.experience = request.POST.get('experience')
        contact.aboutme = request.POST.get('aboutme')

        # 2. Handle Specialization Checkboxes
        # request.POST.getlist returns a Python list ['men', 'women']
        specialization_list = request.POST.getlist('specialization')
        # Join them into a single string "men,women" for the database
        contact.specialization = ",".join(specialization_list)

        # 3. Handle Image
        if 'profile_image' in request.FILES:
            contact.profile_image = request.FILES['profile_image']

        contact.save()
        messages.success(request, "Profile updated successfully")
        return redirect('designer_profile')

    # GET Request: Convert the database string "men,women" back to a list ['men', 'women']
    # This allows us to check the boxes in the HTML
    current_specializations = contact.specialization.split(',') if contact.specialization else []

    return render(request, 'designer_update_profile.html', {
        'contact': contact,
        'designer': contact,
        'current_specializations': current_specializations  # Pass this list to template
    })


def delete_designer_profile(request, id):
    try:
        contact = get_object_or_404(Designer, id=id)
        contact.delete()
        messages.success(request, "Profile deleted successfully")
    except DatabaseError as e:
        messages.error(request, f"Error deleting profile: {e}")
    return redirect('designer_profile')

from .models import Designer,DesignerGallery
from .forms import DesignerGalleryForm
from django.db import DatabaseError

# Other views...

def designer_gallery_upload(request):
    email = request.session.get("email")
    if not email:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('designer_login')

    try:
        designer = Designer.objects.get(email=email)
    except Designer.DoesNotExist:
        messages.error(request, "Designer profile not found.")
        return redirect('designer_login')
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return redirect('designer_login')

    if request.method == 'POST':
        form = DesignerGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery_image = form.save(commit=False)
            gallery_image.designer = designer  # Link the image to the logged-in designer
            gallery_image.save()
            messages.success(request, 'Image uploaded successfully to your gallery!')
            return redirect('designer_gallery_upload')
        else:
            messages.error(request, 'Failed to upload image. Please check the form.')
    else:
        form = DesignerGalleryForm()

    # Retrieve all images for the current designer
    gallery_images = designer.gallery_images.all()

    return render(request, 'designer_gallery_upload.html', {
        'form': form,
        'gallery_images': gallery_images,
        'designer': designer,  # ✅ Pass designer to the template
    })


def delete_image(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(DesignerGallery, pk=image_id)  # ✅ Use your model
        image.delete()
        messages.success(request, 'Image deleted successfully.')
    return redirect('designer_gallery_upload')

from .models import Designer, DesignerService

from django.contrib import messages
from .forms import DesignerServiceForm  # Assuming your form is in .forms


def designer_add_service(request):
    email = request.session.get("email")
    if not email:
        messages.error(request, "You must be logged in to add a service.")
        return redirect('designer_login')

    designer = get_object_or_404(Designer, email=email)

    if request.method == 'POST':
        form = DesignerServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.designer = designer
            service.save()
            messages.success(request, f"Service '{service.title}' added successfully!")

            # ✅ PASS THE ID HERE
            return redirect('designer_view_services', designer_id=designer.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = DesignerServiceForm()

    context = {
        'form': form,
        'designer': designer   # ✅ added this
    }
    return render(request, "designer_add_service.html", context)

def designer_view_services(request, designer_id):
    try:
        designer = get_object_or_404(Designer, id=designer_id)
        services = designer.services.all()  # related_name="services"
        return render(request, "designer_view_services.html", {
            "designer": designer,
            "services": services
        })
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        return redirect("designer_view_services")

# In online_tailor_booking_system_app/views.py

def designer_edit_service(request, service_id):
    email = request.session.get("email")
    if not email:
        messages.error(request, "Login required.")
        return redirect("designer_login")
    designer = get_object_or_404(Designer, email=email)
    # Fetch the existing service instance
    service = get_object_or_404(DesignerService, id=service_id, designer=designer)
    if request.method == "POST":
        # Pass request.POST, request.FILES, and the existing instance
        form = DesignerServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully!")
            return redirect("designer_view_services", designer_id=designer.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Pre-fill the form with existing data
        form = DesignerServiceForm(instance=service)
    return render(request, "designer_edit_service.html", {
        "designer": designer,
        "form": form,  # We are now passing the form, not just the service object
        "service": service  # Optional: kept in case you display the current image separately
    })


# Add this to online_tailor_booking_system_app/views.py

def designer_delete_service(request, service_id):
    email = request.session.get("email")
    if not email:
        messages.error(request, "Login required.")
        return redirect("designer_login")
    try:
        # Get the designer profile
        designer = get_object_or_404(Designer, email=email)

        # Get the specific service and ensure it belongs to this designer
        service = get_object_or_404(DesignerService, id=service_id, designer=designer)

        # Delete the service
        service.delete()
        messages.success(request, "Service deleted successfully!")

        # Redirect back to the view services page
        return redirect("designer_view_services", designer_id=designer.id)
    except Exception as e:
        messages.error(request, f"Error deleting service: {e}")
        return redirect("designer_index")


from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking, Designer

from datetime import timedelta
from django.utils import timezone


def designer_order(request, designer_id):
    designer = get_object_or_404(Designer, id=designer_id)

    if request.method == "POST":
        booking_id = request.POST.get("booking_id")
        status = request.POST.get("status")
        booking = get_object_or_404(Booking, id=booking_id, designer=designer)

        # --- NEW LOGIC FOR DATES ---
        if status == 'in_progress':
            # Set the start date to today
            booking.actual_start_date = timezone.now().date()

            # Calculate end date: Today + Service Time Period (days)
            if booking.service.timeperiod:
                booking.expected_end_date = booking.actual_start_date + timedelta(days=booking.service.timeperiod)
        # ---------------------------

        booking.status = status
        booking.save()

        # Email logic (Keep your existing email logic here)
        if status.lower() == "cancelled":
            # ... your existing rejection email code ...
            pass
        elif status.lower() == "accepted":
            # ... your existing acceptance email code ...
            pass

        return redirect("designer_order", designer_id=designer.id)

    orders = Booking.objects.filter(designer=designer).select_related("customer", "service")

    return render(request, "designer_order.html", {
        "designer": designer,
        "orders": orders
    })


def designer_view_reviews(request, designer_id):
    designer = get_object_or_404(Designer, id=designer_id)
    reviews = designer.reviews.select_related('customer', 'booking').all()

    # Calculate average rating
    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 2)

    return render(request, 'designer_view_reviews.html', {
        'designer': designer,
        'reviews': reviews,
        'avg_rating': avg_rating
    })

