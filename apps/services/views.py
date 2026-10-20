from django.shortcuts import render
from django.http import JsonResponse

CORRIDOR_RATES = {
    "jhb-durban": {"superlink": [18, 25], "triaxle": [16, 22], "rigid10": [10, 14], "flatbed8": [9, 12], "reefer": [22, 30]},
    "durban-jhb": {"superlink": [18, 25], "triaxle": [16, 22], "rigid10": [10, 14], "flatbed8": [9, 12], "reefer": [22, 30]},
    "jhb-cpt": {"superlink": [15, 22], "triaxle": [14, 20], "rigid10": [9, 13], "flatbed8": [8, 11], "reefer": [20, 28]},
    "cpt-jhb": {"superlink": [15, 22], "triaxle": [14, 20], "rigid10": [9, 13], "flatbed8": [8, 11], "reefer": [20, 28]},
    "jhb-plk": {"superlink": [12, 18], "triaxle": [11, 16], "rigid10": [8, 11], "flatbed8": [7, 10], "reefer": [16, 22]},
    "plk-jhb": {"superlink": [12, 18], "triaxle": [11, 16], "rigid10": [8, 11], "flatbed8": [7, 10], "reefer": [16, 22]},
    "jhb-nel": {"superlink": [14, 20], "triaxle": [12, 18], "rigid10": [8, 12], "flatbed8": [7, 10], "reefer": [18, 24]},
    "nel-jhb": {"superlink": [14, 20], "triaxle": [12, 18], "rigid10": [8, 12], "flatbed8": [7, 10], "reefer": [18, 24]},
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
    rates = CORRIDOR_RATES.get(key)

    if not rates or vehicle not in rates:
        return JsonResponse({"error": "Corridor not found"}, status=404)

    min_r, max_r = rates[vehicle]
    return JsonResponse({
        "origin": origin,
        "destination": destination,
        "vehicle": vehicle,
        "distance_km": distance,
        "rate_per_km": {"min": min_r, "max": max_r},
        "total_estimate": {"min": round(min_r * distance, 2), "max": round(max_r * distance, 2)},
        "dispatch_fee_percent": {"min": 5, "max": 8},
    })
