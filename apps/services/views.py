from django.shortcuts import render
from django.http import JsonResponse

LANE_RATES = {
    "chi-omaha": {"dryvan": [1.75, 2.35], "reefer": [2.05, 2.75], "boxtruck": [1.45, 1.95], "flatbed": [2.0, 2.6], "stepdeck": [2.1, 2.8]},
    "omaha-chi": {"dryvan": [1.75, 2.35], "reefer": [2.05, 2.75], "boxtruck": [1.45, 1.95], "flatbed": [2.0, 2.6], "stepdeck": [2.1, 2.8]},
    "dallas-atl": {"dryvan": [1.7, 2.3], "reefer": [2.1, 2.85], "boxtruck": [1.4, 1.9], "flatbed": [1.95, 2.55], "stepdeck": [2.05, 2.75]},
    "atl-dallas": {"dryvan": [1.7, 2.3], "reefer": [2.1, 2.85], "boxtruck": [1.4, 1.9], "flatbed": [1.95, 2.55], "stepdeck": [2.05, 2.75]},
    "la-phx": {"dryvan": [1.9, 2.5], "reefer": [2.2, 3.0], "boxtruck": [1.5, 2.0], "flatbed": [2.1, 2.7], "stepdeck": [2.2, 2.9]},
    "phx-la": {"dryvan": [1.9, 2.5], "reefer": [2.2, 3.0], "boxtruck": [1.5, 2.0], "flatbed": [2.1, 2.7], "stepdeck": [2.2, 2.9]},
    "chi-dallas": {"dryvan": [1.8, 2.4], "reefer": [2.15, 2.9], "boxtruck": [1.45, 1.95], "flatbed": [2.05, 2.65], "stepdeck": [2.15, 2.85]},
    "dallas-chi": {"dryvan": [1.8, 2.4], "reefer": [2.15, 2.9], "boxtruck": [1.45, 1.95], "flatbed": [2.05, 2.65], "stepdeck": [2.15, 2.85]},
}

def services_list(request):
    return render(request, "pages/services.html")

def api_corridor_rate(request):
    origin = request.GET.get("origin", "")
    destination = request.GET.get("destination", "")
    vehicle = request.GET.get("vehicle", "")
    distance = request.GET.get("distance", "")

    if not all([origin, destination, vehicle, distance]):
        return JsonResponse({"error": "Missing parameters"}, status=400)

    try:
        distance = float(distance)
    except ValueError:
        return JsonResponse({"error": "Invalid distance"}, status=400)

    key = f"{origin}-{destination}"
    rates = LANE_RATES.get(key)

    if not rates or vehicle not in rates:
        return JsonResponse({"error": "Lane not found"}, status=404)

    min_rate, max_rate = rates[vehicle]
    return JsonResponse({
        "origin": origin,
        "destination": destination,
        "vehicle": vehicle,
        "distance_mi": distance,
        "rate_per_mile": {"min": min_rate, "max": max_rate},
        "total_estimate": {"min": round(min_rate * distance, 2), "max": round(max_rate * distance, 2)},
        "dispatch_fee_percent": {"min": 8, "max": 10},
    })
