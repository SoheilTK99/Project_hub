from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name    = form.cleaned_data["name"]
            email   = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"پیام جدید از سایت - {name}"
            body = f"نام: {name}\nایمیل: {email}\n\nمتن پیام:\n{message}"

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,      # from
                ["soheil.ce.99@gmail.com"],        # to  ← ایمیل خودت
            )

            messages.success(request, "پیامت با موفقیت ارسال شد ")
            return redirect("contact")  # یا هر صفحه‌ای که دوست داری
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
