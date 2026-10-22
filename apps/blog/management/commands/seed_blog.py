from django.core.management.base import BaseCommand
from apps.blog.models import BlogPost

POSTS = [
    {
        "title": "Top 5 US Freight Lanes for 2026",
        "category": "industry-news",
        "excerpt": "Which lanes are paying best this year and how to position your truck for maximum earnings.",
        "content": "The US freight market shifts every year as demand, diesel prices, and capacity evolve. In 2026, the I-80 Chicago-Omaha corridor remains the backbone of general freight, while the I-20 Dallas-Atlanta route continues to reward reefer operators.\n\nMeanwhile, the I-10 Los Angeles-Phoenix lane is seeing renewed produce and cold-chain demand. Understanding where the demand is allows carriers to plan return loads and minimize deadhead.",
        "featured": True,
        "reading_time": 6,
    },
    {
        "title": "How to Negotiate Better Rates with Brokers",
        "category": "dispatch-tips",
        "excerpt": "Tips from our dispatch team on getting the best per-mile rates across US lanes.",
        "content": "Rate negotiation is an art. The best dispatchers know that preparation beats pressure. Always know your cost per mile, your minimum acceptable rate, and the current market average for the lane.\n\nPresent your case with data: your on-time record, your equipment type, and the current demand on the lane. A broker is more likely to negotiate when you demonstrate professionalism and reliability.",
        "featured": False,
        "reading_time": 5,
    },
    {
        "title": "Understanding Cargo Insurance and Your COI",
        "category": "compliance",
        "excerpt": "What your Certificate of Insurance covers, why it matters, and how to choose the right level.",
        "content": "Cargo insurance protects the freight you haul against loss or damage while it is in transit. For US carriers, a Certificate of Insurance (COI) is not optional; it is a requirement for nearly every broker and shipper relationship.\n\nTypical coverage levels range from $100,000 for standard dry van freight to $250,000 or more for high-value and reefer loads. Brokers will also want to be listed as a certificate holder. Choosing the right level depends on your typical load value and the requirements of the brokers you work with.",
        "featured": False,
        "reading_time": 4,
    },
    {
        "title": "New Authority Survival Guide: First 90 Days",
        "category": "new-carriers",
        "excerpt": "Everything you need to know to start earning quickly and build a sustainable carrier business.",
        "content": "The first 90 days with a new MC authority are critical. Most new carriers struggle with broker relationships, paperwork, and finding consistent loads.\n\nStart by getting your W-9, Certificate of Insurance, and MC authority letter in order. Then build relationships with a few reliable brokers rather than chasing every load board. Consistency beats volume in the early days.",
        "featured": False,
        "reading_time": 7,
    },
    {
        "title": "Minimizing Deadhead: Route Planning 101",
        "category": "route-planning",
        "excerpt": "How smart route planning can add thousands of dollars to your monthly earnings.",
        "content": "Deadhead miles are the silent killer of carrier profitability. Every mile driven without a paying load is money lost.\n\nSmart route planning means positioning yourself where the demand is, planning return loads before you deliver, and building relationships with shippers who can offer consistent backhaul opportunities.",
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
