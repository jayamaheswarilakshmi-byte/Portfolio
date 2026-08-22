import json, os
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from google import genai
from .models import Profile, Skill, Experience, Service, Project, ContactMessage
from django.http import HttpResponse
from django.core.mail import send_mail

from google.genai import types  # <-- Add this line

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            # 1. Save message to Django Database
            ContactMessage.objects.create(
                name=name, 
                email=email, 
                subject=subject, 
                message=message
            )

            # 2. Prepare and Send Email Notification to Your Gmail
            email_subject = f"Portfolio Contact: {subject if subject else 'New Inquiry'}"
            full_email_body = (
                f"You received a new message from your portfolio website:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message}"
            )

            try:
                send_mail(
                    subject=email_subject,
                    message=full_email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER], # Sends directly to your email
                    fail_silently=False,
                    
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                # If email delivery fails, message is still saved in DB
                messages.warning(
                    request, 
                    "Your message was saved, but we encountered an issue sending the email notification."
                )

            return redirect('home')

    context = {
        'profile': Profile.objects.first(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'index.html', context)

@csrf_exempt
def ai_chat_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_msg = data.get("message", "")
            
            profile = Profile.objects.first()
            name = profile.name if profile else "Jayalakshmi Subramanian"
            
            system_prompt = f"You are the AI assistant for {name}'s portfolio. Answer questions briefly and professionally in 2-3 sentences max."
            
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                return JsonResponse({"reply": "API key missing in server configuration."}, status=500)

            client = genai.Client(api_key=api_key)
            
            # Updated to current active model string
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=user_msg,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                )
            )
            return JsonResponse({"reply": response.text})
            
        except Exception as e:
            # Displays exact error if the API call fails
            return JsonResponse({"reply": f"Error: {str(e)}"}, status=500)
            
    return JsonResponse({"reply": "Invalid request method."}, status=405)
def test_email_view(request):
    try:
        send_mail(
            subject="Render Live SMTP Test",
            message="This is a test email sent directly from a test URL.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return HttpResponse(f"<h1>Success! Email sent to {settings.EMAIL_HOST_USER}</h1>")
    except Exception as e:
        return HttpResponse(f"<h1>Email Failed!</h1><p><b>Error Details:</b> {e}</p>")