from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def equipment(request):
    return render(request, "pages/equipment.html")

def pricing(request):
    return render(request, "pages/pricing.html")

def solutions(request):
    return render(request, "pages/solutions.html")

def portal(request):
    return render(request, "pages/portal.html")

def dashboard(request):
    return render(request, "pages/dashboard.html")

def settings_page(request):
    return render(request, "pages/settings.html")

def carrier_login(request):
    if request.method == "POST":
        messages.success(request, "Login functionality coming soon. Contact dispatch for access.")
        return redirect("portal")
    return render(request, "pages/carrier_login.html")

def carrier_logout(request):
    messages.success(request, "You have been logged out.")
    return redirect("home")

def blog(request):
    return render(request, "pages/blog.html")

def carrier_packet(request):
    return render(request, "pages/carrier_packet.html")

def schedule_call(request):
    return render(request, "pages/schedule_call.html")

def help_page(request):
    return render(request, "pages/help.html")

def search(request):
    query = request.GET.get("q", "").strip()
    results = []
    pages = [
        {"title": "Home", "url": "/", "keywords": "home dispatch freight loads booking rates"},
        {"title": "About Us", "url": "/about/", "keywords": "about company team mission vision values"},
        {"title": "Services", "url": "/services/", "keywords": "services dispatch load booking broker credit checks invoicing factoring route planning"},
        {"title": "Solutions", "url": "/solutions/", "keywords": "solutions billing invoicing document management compliance after hours driver statements"},
        {"title": "Fleet & Equipment", "url": "/equipment/", "keywords": "equipment fleet dry van reefer flatbed step deck box truck power only"},
        {"title": "Rates & Pricing", "url": "/pricing/", "keywords": "pricing rates usd per mile percentage weekly calculator lane"},
        {"title": "Carrier Onboarding", "url": "/onboarding/carrier/", "keywords": "onboarding carrier application mc dot w9 coi authority compliance"},
        {"title": "Contact Us", "url": "/contact/", "keywords": "contact phone text email address"},
        {"title": "Help & Guide", "url": "/help/", "keywords": "help guide faq getting started glossary terms"},
        {"title": "Blog", "url": "/blog/", "keywords": "blog news articles tips lane updates"},
        {"title": "Carrier Packet", "url": "/carrier-packet/", "keywords": "packet documents compliance w9 coi authority banking"},
        {"title": "Schedule a Call", "url": "/schedule-call/", "keywords": "schedule call book consultation specialist"},
    ]
    if query:
        q = Q()
        for word in query.lower().split():
            q |= Q(title__icontains=word) | Q(keywords__icontains=word)
        results = [p for p in pages if query.lower() in p["title"].lower() or query.lower() in p["keywords"].lower()]
    return render(request, "pages/search.html", {"query": query, "results": results})
