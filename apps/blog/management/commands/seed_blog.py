from django.core.management.base import BaseCommand
from apps.blog.models import BlogPost

POSTS = [
    {
        "title": "Top 5 SA Freight Corridors for 2026",
        "category": "industry-news",
        "excerpt": "Which routes are paying best this year and how to position your truck for maximum earnings.",
        "content": "The South African freight landscape shifts every year as infrastructure, demand, and fuel costs evolve. In 2026, the N3 Durban-Johannesburg corridor remains the backbone of general freight, while the N1 Cape Town-Johannesburg route continues to reward reefer operators.\n\nPosokwan, the N4 Johannesburg-eMalahleni corridor is seeing renewed mining and tipper demand. Understanding where the demand is allows carriers to plan return loads and minimize deadhead.",
        "featured": True,
        "reading_time": 6,
    },
    {
        "title": "How to Negotiate Better Rates with Brokers",
        "category": "dispatch-tips",
        "excerpt": "Tips from our dispatch team on getting the best per-km rates across SA corridors.",
        "content": "Rate negotiation is an art. The best dispatchers know that preparation beats pressure. Always know your cost per kilometre, your minimum acceptable rate, and the current market average for the lane.\n\nPresent your case with data: your on-time record, your equipment type, and the current demand on the corridor. A broker is more likely to negotiate when you demonstrate professionalism and reliability.",
        "featured": False,
        "reading_time": 5,
    },
    {
        "title": "Understanding GIT Insurance for Carriers",
        "category": "compliance",
        "excerpt": "What Goods In Transit insurance covers, why it matters, and how to choose the right level.",
        "content": "Goods In Transit (GIT) insurance protects your cargo against loss or damage while it is being transported. For SA carriers, GIT is not optional; it is a requirement for most broker and shipper relationships.\n\nTypical cover levels range from R350,000 for smaller loads to R1,000,000 for high-value freight. Choosing the right level depends on your typical load value and the requirements of the brokers you work with.",
        "featured": False,
        "reading_time": 4,
    },
    {
        "title": "New Carrier Survival Guide: First 90 Days",
        "category": "new-carriers",
        "excerpt": "Everything you need to know to start earning quickly and build a sustainable carrier business.",
        "content": "The first 90 days as a new carrier are critical. Most new carriers struggle with broker relationships, paperwork, and finding consistent loads.\n\nStart by getting your CIPC registration, tax clearance, and GIT insurance in place. Then build relationships with a few reliable brokers rather than chasing every load board. Consistency beats volume in the early days.",
        "featured": False,
        "reading_time": 7,
    },
    {
        "title": "Minimizing Deadhead: Route Planning 101",
        "category": "route-planning",
        "excerpt": "How smart route planning can add thousands of rands to your monthly earnings.",
        "content": "Deadhead miles are the silent killer of carrier profitability. Every kilometre driven without a paying load is money lost.\n\nSmart route planning means positioning yourself where the demand is, planning return loads before you deliver, and building relationships with shippers who can offer consistent backhaul opportunities.",
        "featured": False,
        "reading_time": 5,
    },
]


class Command(BaseCommand):
    help = "Seed the blog with sample posts"

    def handle(self, *args, **options):
        created = 0
        for data in POSTS:
            obj, was_created = BlogPost.objects.get_or_create(
                title=data["title"],
                defaults=data,
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Created {created} blog posts."))
