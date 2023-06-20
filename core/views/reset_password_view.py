from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from core.forms import PasswordResetForm, ResetPasswordForm
from core.utils import generate_token
from core.models import PasswordResetToken
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site

User = get_user_model()


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            # Generate token and expiration time
            token = generate_token()
            expires_at = timezone.now() + timezone.timedelta(hours=1)

            # Save the token and expiration time
            password_reset_token = PasswordResetToken.objects.create(
                user=user, token=token, expires_at=expires_at
            )
            baseURL = get_current_site(request).domain
            # Send password reset email
            email_from = settings.EMAIL_HOST_USER

            reset_link = f"http://{baseURL}/reset-password/confirm/?token={token}"

            html_message = render_to_string(
                'mail_templates/forget-password.html', {'user': user, 'url': reset_link})
            plain_message = strip_tags(html_message)
            subject = f'Reset Password'
            email = EmailMultiAlternatives(
                subject, plain_message, email_from, [email])
            email.attach_alternative(html_message, "text/html")
            email.send()

            return render(request, 'password_reset/request_sent.html')
    else:
        form = PasswordResetForm()

    return render(request, 'password_reset/request.html', {'form': form, 'is_auth_page': True})


def password_reset_confirm(request):
    token = request.GET.get('token')
    print(token)
    try:
        password_reset_token = PasswordResetToken.objects.get(token=token)
        if password_reset_token.is_expired():
            return render(request, 'password_reset/invalid_token.html')
    except PasswordResetToken.DoesNotExist:
        return render(request, 'password_reset/invalid_token.html')

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = password_reset_token.user
            new_password = form.cleaned_data['password']
            user.set_password(new_password)
            user.save()

            # Delete the token after successful password reset
            password_reset_token.delete()

            return render(request, 'password_reset/reset_complete.html')
        else:
            errors = form.errors
    else:
        form = ResetPasswordForm()

    return render(request, 'password_reset/reset_confirm.html', {'form': form, 'is_auth_page': True})
