from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ComposeEmailForm
from .models import SentEmail


@login_required
def compose_view(request):
    form = ComposeEmailForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        recipient = form.cleaned_data["recipient"]
        subject = form.cleaned_data["subject"]
        body = form.cleaned_data["body"]
        success = True
        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )
        except Exception as e:
            success = False
            messages.error(request, f"Failed to send: {e}")

        SentEmail.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            body=body,
            success=success,
        )
        if success:
            return redirect("sent")
    return render(request, "mailer/compose.html", {"form": form})


@login_required
def sent_view(request):
    emails = SentEmail.objects.filter(sender=request.user)
    return render(request, "mailer/sent.html", {"emails": emails})