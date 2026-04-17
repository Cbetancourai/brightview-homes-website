"""Generate per-plan landing pages for Brightview Homes floor plans.

One HTML page per plan at /Website/<plan-slug>.html. Each page is a standalone
SEO landing page so the plan can rank for its own queries.
"""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parent.parent

PLANS = [
    {
        "slug": "cambria",
        "name": "Cambria",
        "style": "Ranch",
        "stories": 1,
        "sqft": 1665, "beds": 4, "baths": 2, "garage": 2,
        "price": 269990,
        "tagline": "A 4-bedroom single-story Ranch with an open great room, split-bedroom layout, and a rear primary suite.",
        "meta_desc": "Cambria floor plan — 4BR, 2BA, 2-car garage, 1,665 sq ft single-story Ranch new home by Brightview Homes. Build on your lot across Orlando & Central Florida from $269,990.",
        "intro": "The Cambria is one of Brightview's most popular single-story Ranch designs — four true bedrooms, two full baths, and an efficient 1,665 sq ft footprint that fits most scattered lots in Central Florida. The great room, kitchen, and dining form one continuous living zone, while the primary suite is set privately at the rear of the home and three secondary bedrooms share a well-appointed bath at the front.",
        "highlights": [
            "Open-concept great room, dining, and kitchen with a clean sight line to the rear lanai",
            "Split-bedroom layout — primary suite is separated from the three secondary bedrooms",
            "Primary bath with dual vanity, walk-in closet, and frameless shower upgrade option",
            "Two-car garage with direct interior entry via the everyday foyer",
            "Fits on typical 50–75 foot wide scattered lots across all 16 Brightview counties",
        ],
        "rooms": [
            {"name": "Great Room", "dim": "22' x 18'"},
            {"name": "Kitchen", "dim": "13' x 16'"},
            {"name": "Dining", "dim": "10' x 14'"},
            {"name": "Primary Suite", "dim": "14' x 16'"},
            {"name": "Bedrooms 2–4", "dim": "~11' x 12' each"},
            {"name": "2-Car Garage", "dim": "20' x 20'"},
        ],
        "best_for": "First-time buyers, move-up families, and investors looking for a 4-bedroom rental product. Also ideal as a scatter-lot primary residence in cities like Sanford, DeLand, and Kissimmee where 4-bedroom homes command premium rents and resale.",
        "cities": ["sanford", "deland", "kissimmee", "lakeland"],
    },
    {
        "slug": "tribeca",
        "name": "Tribeca",
        "style": "Ranch",
        "stories": 1,
        "sqft": 1665, "beds": 3, "baths": 2, "garage": 2,
        "price": 269990,
        "tagline": "A 3-bedroom single-story Ranch with a center-island kitchen and covered rear lanai.",
        "meta_desc": "Tribeca floor plan — 3BR, 2BA, 2-car garage, 1,665 sq ft single-story Ranch by Brightview Homes. Ideal for DSCR investors and first-time buyers. From $269,990.",
        "intro": "The Tribeca is the most rent-efficient floor plan in the Brightview lineup — 3 bedrooms, 2 baths, 1,665 sq ft of functional single-story living, and a spec-build cost that makes it a natural fit for DSCR investors and build-to-rent portfolios. The open kitchen with center island anchors the home, while the primary suite sits at the rear with a walk-in closet and covered lanai access.",
        "highlights": [
            "Open-concept living, dining, and kitchen with a large center island",
            "Primary suite with walk-in closet and en suite bath at the rear of the home",
            "Covered rear lanai — a Brightview standard feature for outdoor Florida living",
            "Two secondary bedrooms plus a full second bath on the opposite wing",
            "One of the most DSCR-friendly plans in the Brightview lineup",
        ],
        "rooms": [
            {"name": "Great Room", "dim": "15'2\" x 16'2\""},
            {"name": "Kitchen + Dining", "dim": "Open island kitchen + dining"},
            {"name": "Owner's Suite", "dim": "12'10\" x 15'10\""},
            {"name": "Bedroom 3", "dim": "11'5\" x 10'2\""},
            {"name": "Lanai", "dim": "10' x 10'"},
            {"name": "2-Car Garage", "dim": "20' x 20'"},
        ],
        "best_for": "First-time buyers, downsizers, and investors building for long-term rental or DSCR-financed buy-and-hold strategies. Most popular plan in Polk and Osceola counties for build-to-rent.",
        "cities": ["kissimmee", "lakeland", "winter-haven", "st-cloud"],
    },
    {
        "slug": "legacy",
        "name": "Legacy",
        "style": "Ranch",
        "stories": 1,
        "sqft": 1805, "beds": 4, "baths": 2, "garage": 2,
        "price": 299990,
        "tagline": "A 4-bedroom Ranch with split-wing privacy, a walk-in pantry, and a soaking-tub primary suite.",
        "meta_desc": "Legacy floor plan — 4BR, 2BA, 2-car garage, 1,805 sq ft Ranch by Brightview Homes. Upgraded kitchen with center island, spa primary bath. From $299,990.",
        "intro": "The Legacy steps up from the Cambria with an additional 140 sq ft of living space, an upgraded kitchen featuring a walk-in pantry and larger center island, and a spa-style primary bath. Four bedrooms across a split-wing floor plan make this a strong fit for growing families who need the extra square footage without stepping up to a two-story design.",
        "highlights": [
            "Four-bedroom split-wing layout for maximum privacy between primary and secondary bedrooms",
            "Upgraded kitchen with center island, walk-in pantry, and casual dining space",
            "Primary suite with soaking tub, separate shower, and dual-sink vanity",
            "Covered rear lanai for seamless indoor-outdoor Florida living",
            "Soaring great room ceilings and abundant natural light throughout",
        ],
        "rooms": [
            {"name": "Great Room", "dim": "~20' x 17'"},
            {"name": "Kitchen + Dining", "dim": "Center-island kitchen + nook"},
            {"name": "Primary Suite", "dim": "~14' x 16'"},
            {"name": "Bedrooms 2–4", "dim": "~11' x 12' each"},
            {"name": "Walk-in Pantry", "dim": "Adjacent to kitchen"},
            {"name": "2-Car Garage", "dim": "20' x 20'"},
        ],
        "best_for": "Move-up families wanting a larger 4-bedroom Ranch with elevated finishes. Most popular in Sanford, DeLand, and Lakeland for primary homes in the $400K range.",
        "cities": ["sanford", "deland", "lakeland", "winter-haven"],
    },
    {
        "slug": "hudson",
        "name": "Hudson",
        "style": "Two Story",
        "stories": 2,
        "sqft": 1821, "beds": 3, "baths": 2.5, "garage": 2,
        "price": 299990,
        "tagline": "A two-story plan with all three bedrooms upstairs and an open main-floor living area.",
        "meta_desc": "Hudson floor plan — 3BR, 2.5BA, 2-car garage, 1,821 sq ft two-story home by Brightview Homes. Compact footprint, private upstairs bedrooms. From $299,990.",
        "intro": "The Hudson is Brightview's most compact two-story plan — a 1,821 sq ft design that fits on narrower urban and infill lots while giving you a true two-story living experience. All three bedrooms sit privately upstairs, while the main floor opens up into a single living, dining, and kitchen space perfect for entertaining without interrupting bedroom privacy.",
        "highlights": [
            "All three bedrooms tucked privately on the second floor",
            "Open main-floor living, dining, and kitchen for entertaining",
            "Primary suite with walk-in closet and en suite bath on the second floor",
            "Main-floor powder room — no need to send guests upstairs",
            "Efficient footprint fits on narrower urban and infill lots",
        ],
        "rooms": [
            {"name": "Great Room (1st floor)", "dim": "~16' x 16'"},
            {"name": "Kitchen + Dining (1st floor)", "dim": "Open plan with island"},
            {"name": "Primary Suite (2nd floor)", "dim": "~13' x 14'"},
            {"name": "Bedrooms 2 & 3 (2nd floor)", "dim": "~11' x 11' each"},
            {"name": "Powder Room (1st floor)", "dim": "Half bath"},
            {"name": "2-Car Garage", "dim": "20' x 20'"},
        ],
        "best_for": "Buyers with narrower scattered lots, infill tear-down projects in Orlando and College Park, and young couples who want privacy between guests and bedrooms. Urban fit.",
        "cities": ["orlando", "sanford", "winter-garden", "lakeland"],
    },
    {
        "slug": "valencia",
        "name": "Valencia",
        "style": "Ranch",
        "stories": 1,
        "sqft": 1920, "beds": 4, "baths": 2.5, "garage": 2,
        "price": 309990,
        "tagline": "A 4-bedroom single-story Ranch with 2.5 baths, quartz kitchen, and a flex room.",
        "meta_desc": "Valencia floor plan — 4BR, 2.5BA, 2-car garage, 1,920 sq ft Ranch by Brightview Homes. Quartz kitchen, primary with dual walk-ins and spa bath. From $309,990.",
        "intro": "The Valencia is the versatile family plan — four bedrooms, a true 2.5 baths (rare at this price point), a gourmet kitchen with quartz countertops and a walk-in pantry, and a flex room that adapts as a home office, playroom, or gym. At 1,920 sq ft across a single story, it delivers big-home feel without the two-story complexity.",
        "highlights": [
            "Spacious Ranch layout with four bedrooms and 2.5 baths",
            "Wide-open kitchen and living area with quartz countertops and island seating",
            "Primary suite with dual walk-in closets, soaking tub, and spa-style shower",
            "Flex room adaptable as home office, playroom, or fitness space",
            "Covered rear lanai with pre-plumbed options for outdoor kitchen or pool",
        ],
        "rooms": [
            {"name": "Great Room", "dim": "~22' x 18'"},
            {"name": "Kitchen + Dining", "dim": "Quartz island + walk-in pantry"},
            {"name": "Flex Room", "dim": "~11' x 12'"},
            {"name": "Primary Suite", "dim": "~14' x 17' with dual walk-ins"},
            {"name": "Bedrooms 2–4", "dim": "~11' x 12' each"},
            {"name": "2-Car Garage", "dim": "20' x 20'"},
        ],
        "best_for": "Families wanting the biggest single-story Ranch under $320K. Strong in Winter Garden, Clermont, Orlando, and Sanford markets for primary residence buyers.",
        "cities": ["winter-garden", "clermont", "orlando", "sanford"],
    },
    {
        "slug": "brighton",
        "name": "Brighton",
        "style": "Two Story",
        "stories": 2,
        "sqft": 2069, "beds": 4, "baths": 2.5, "garage": 2,
        "price": 329990,
        "tagline": "A 4-bedroom two-story with an impressive main-floor great room and upstairs loft.",
        "meta_desc": "Brighton floor plan — 4BR, 2.5BA, 2-car garage, 2,069 sq ft two-story by Brightview Homes. Main-floor great room + upstairs loft. From $329,990.",
        "intro": "The Brighton is a beautifully proportioned two-story home with an impressive main-floor great room and four bedrooms privately located on the second floor. The open kitchen flows into a light-filled gathering space, and the upstairs adds a loft area — perfect as a reading nook, media space, or homework zone that keeps the bedrooms private.",
        "highlights": [
            "Impressive open kitchen and great room on the main floor",
            "All four bedrooms privately located on the second floor",
            "Primary suite with large walk-in closet, soaking tub, and frameless shower",
            "Upstairs loft — versatile as a reading nook, media room, or study",
            "Two-car garage with optional third-car elevation available",
        ],
        "rooms": [
            {"name": "Great Room (1st floor)", "dim": "~22' x 18'"},
            {"name": "Kitchen + Dining (1st floor)", "dim": "Island kitchen + dining area"},
            {"name": "Powder Room (1st floor)", "dim": "Half bath"},
            {"name": "Primary Suite (2nd floor)", "dim": "~14' x 16'"},
            {"name": "Bedrooms 2–4 (2nd floor)", "dim": "~11' x 12' each"},
            {"name": "Loft (2nd floor)", "dim": "~12' x 11'"},
        ],
        "best_for": "Families wanting a two-story with upstairs separation between primary and secondary bedrooms. Popular across Orlando, Winter Garden, Clermont, and Kissimmee.",
        "cities": ["orlando", "winter-garden", "clermont", "kissimmee"],
    },
    {
        "slug": "kensington",
        "name": "Kensington",
        "style": "Ranch",
        "stories": 1,
        "sqft": 2112, "beds": 4, "baths": 3, "garage": 2,
        "price": 339990,
        "tagline": "A premium single-story Ranch with a three-way split bedroom layout and chef's kitchen.",
        "meta_desc": "Kensington floor plan — 4BR, 3BA, 2-car garage, 2,112 sq ft Ranch by Brightview Homes. Three-way split layout, chef kitchen, tray-ceiling great room. From $339,990.",
        "intro": "The Kensington is Brightview's premium single-story offering — four bedrooms, three full baths, and one of the most open and dramatic great room designs in the lineup. The chef-inspired kitchen anchors the heart of the home with an oversized island, gas-range option, and butler's pantry. A three-way split bedroom layout ensures maximum privacy for every member of the household.",
        "highlights": [
            "Three-way split bedroom layout — ultimate privacy between primary, secondary, and guest bedrooms",
            "Chef-inspired kitchen with oversized island and butler's pantry",
            "Dramatic great room with tray ceiling and luxury flooring package",
            "Primary suite with dual walk-in closets, soaking tub, and frameless shower",
            "Covered outdoor lanai with optional summer kitchen rough-in",
        ],
        "rooms": [
            {"name": "Great Room", "dim": "~22' x 20' with tray ceiling"},
            {"name": "Kitchen + Butler's Pantry", "dim": "Oversized island + walk-in pantry"},
            {"name": "Primary Suite", "dim": "~15' x 17'"},
            {"name": "Bedrooms 2 & 3", "dim": "~11' x 12' each"},
            {"name": "Guest Suite", "dim": "Bedroom 4 with adjacent full bath"},
            {"name": "2-Car Garage", "dim": "20' x 20'"},
        ],
        "best_for": "Families wanting premium finishes without stepping into two-story complexity. Strong in Lake Mary, Mount Dora, Winter Garden, and New Smyrna Beach.",
        "cities": ["lake-mary", "mount-dora", "winter-garden", "new-smyrna-beach"],
    },
    {
        "slug": "belmont",
        "name": "Belmont",
        "style": "Ranch",
        "stories": 1,
        "sqft": 2307, "beds": 4, "baths": 3, "garage": 3,
        "price": 369990,
        "tagline": "A distinguished Ranch with a rare 3-car garage, coffered great room, and gourmet kitchen.",
        "meta_desc": "Belmont floor plan — 4BR, 3BA, 3-car garage, 2,307 sq ft Ranch by Brightview Homes. Coffered great room, gourmet kitchen, formal foyer. From $369,990.",
        "intro": "The Belmont is a distinguished single-story Ranch home offering four bedrooms, three full baths, a three-car garage, and over 2,300 sq ft of thoughtfully designed living space. A formal entry foyer leads into a sweeping open-concept living area with a coffered-ceiling great room, gourmet kitchen, and casual dining nook with access to the covered lanai. Brightview's most complete single-story premium design.",
        "highlights": [
            "Rare three-car garage — perfect for Florida lifestyle storage (boats, golf carts, tools)",
            "Coffered-ceiling great room with luxury flooring package",
            "Gourmet kitchen with double wall ovens and quartz island",
            "Formal entry foyer with soaring ceilings and natural light",
            "Primary suite with his-and-hers walk-in closets and spa bath",
        ],
        "rooms": [
            {"name": "Great Room", "dim": "24'8\" x 22'"},
            {"name": "Kitchen + Dining", "dim": "Gourmet with walk-in pantry"},
            {"name": "Owner's Suite", "dim": "13'4\" x 16'"},
            {"name": "Bedroom 2", "dim": "12'4\" x 12'"},
            {"name": "Bedroom 3", "dim": "10'8\" x 12'8\""},
            {"name": "Bedroom 4", "dim": "10'8\" x 11'4\""},
            {"name": "3-Car Garage", "dim": "28' x 21'"},
            {"name": "Lanai", "dim": "17' x 11'8\""},
        ],
        "best_for": "Move-up buyers and families wanting premium single-story square footage with the rare 3-car garage. Most popular in Lake Mary, Mount Dora, and New Smyrna Beach.",
        "cities": ["lake-mary", "mount-dora", "new-smyrna-beach", "winter-garden"],
    },
    {
        "slug": "astoria",
        "name": "Astoria",
        "style": "Ranch",
        "stories": 1,
        "sqft": 2551, "beds": 4, "baths": 3.5, "garage": 2,
        "price": 409990,
        "tagline": "A sprawling single-story Ranch with a private guest suite for multigenerational living.",
        "meta_desc": "Astoria floor plan — 4BR, 3.5BA, 2-car garage, 2,551 sq ft Ranch by Brightview Homes. Private guest suite, gourmet kitchen, flex room. From $409,990.",
        "intro": "The Astoria is one of Brightview's most impressive Ranch designs — a sprawling single-story home with four bedrooms, three and a half baths, and 2,551 sq ft of premium living space. A standout feature is the private guest suite with its own en suite bath, making the Astoria ideal for multigenerational families or homeowners who frequently host extended-stay guests.",
        "highlights": [
            "Private guest suite with en suite bath — ideal for multigenerational living or in-laws",
            "Gourmet kitchen with large prep island and walk-in pantry",
            "Primary suite with dual vanity, soaking tub, frameless shower, and two walk-in closets",
            "Expansive covered lanai with optional outdoor-kitchen rough-in",
            "Flex room off the foyer for home office or formal dining",
        ],
        "rooms": [
            {"name": "Great Room", "dim": "~24' x 20'"},
            {"name": "Gourmet Kitchen", "dim": "Prep island + walk-in pantry"},
            {"name": "Primary Suite", "dim": "~16' x 17' with dual closets"},
            {"name": "Guest Suite", "dim": "~12' x 13' with en suite"},
            {"name": "Bedrooms 3 & 4", "dim": "~11' x 12' each"},
            {"name": "Flex Room", "dim": "~11' x 12'"},
            {"name": "2-Car Garage", "dim": "20' x 22'"},
        ],
        "best_for": "Multigenerational families, buyers hosting extended-stay guests, and anyone wanting the largest single-story Ranch in the Brightview lineup. Popular in Lake Mary, Mount Dora, New Smyrna Beach, and Winter Garden.",
        "cities": ["lake-mary", "mount-dora", "new-smyrna-beach", "winter-garden"],
    },
    {
        "slug": "stephanie",
        "name": "Stephanie Estate",
        "style": "Two Story",
        "stories": 2,
        "sqft": 3479, "beds": 4, "baths": 3.5, "garage": 2,
        "price": 559990,
        "tagline": "Brightview's flagship two-story estate home — 3,479 sq ft with a grand foyer and second-floor loft.",
        "meta_desc": "Stephanie Estate floor plan — 4BR, 3.5BA, 2-car garage, 3,479 sq ft two-story estate by Brightview Homes. Grand foyer, gourmet kitchen, second-floor loft. From $559,990.",
        "intro": "The Stephanie Estate is Brightview's flagship floor plan — a stunning two-story home with 3,479 sq ft, four bedrooms, three and a half baths, and design features that rival luxury production builders. The main floor features a grand foyer, formal dining room, open great room with coffered ceilings, and a gourmet kitchen worthy of a professional chef. The second floor is home to a spacious loft, three secondary bedrooms, and an opulent primary suite with a covered balcony.",
        "highlights": [
            "Grand foyer and formal dining room for elegant entertaining",
            "Gourmet kitchen with quartz island, double ovens, and walk-in pantry",
            "Primary suite with sitting area, dual walk-in closets, soaking tub, and frameless shower",
            "Second-floor loft perfect as media room, game room, or home office",
            "Covered balcony off the primary suite overlooking the rear yard",
        ],
        "rooms": [
            {"name": "Grand Foyer (1st floor)", "dim": "Soaring entry"},
            {"name": "Formal Dining (1st floor)", "dim": "~12' x 14'"},
            {"name": "Great Room (1st floor)", "dim": "~24' x 20' coffered"},
            {"name": "Gourmet Kitchen (1st floor)", "dim": "Quartz island + walk-in pantry"},
            {"name": "Primary Suite (2nd floor)", "dim": "~18' x 20' w/ sitting area"},
            {"name": "Loft (2nd floor)", "dim": "~16' x 14'"},
            {"name": "Bedrooms 2–4 (2nd floor)", "dim": "~12' x 12' each"},
            {"name": "2-Car Garage", "dim": "20' x 22'"},
        ],
        "best_for": "Luxury move-up buyers and multigenerational families wanting the largest Brightview home. Most popular in Lake Mary, Mount Dora, and high-end Orlando tear-down lots.",
        "cities": ["lake-mary", "mount-dora", "orlando", "new-smyrna-beach"],
    },
]


def city_display(slug):
    # Reverse of gen_cities.CITIES but we just title-case the slug for link text
    return slug.replace("-", " ").title().replace(" Fl", " FL")


def build_faqs(p):
    """Return list of (question, answer) tuples for this plan."""
    name = p["name"]
    sqft = f"{p['sqft']:,}"
    price = f"${p['price']:,}"
    garage = p["garage"]
    style = p["style"]
    story_word = "single-story" if p["stories"] == 1 else "two-story"
    return [
        (
            f"How much does the {name} floor plan cost?",
            f"The {name} starts at {price} for the base floor plan. That includes Brightview's standard finish package (quartz kitchen, wood-look flooring, stainless appliances, impact-rated windows where required, covered rear lanai), but does not include lot cost, site prep, impact fees, or structural options. We'll give you an itemized quote specific to your lot and selections at consultation.",
        ),
        (
            f"Can I modify the {name} floor plan?",
            f"Yes, within reason. The {name} offers structural options including extended lanais, alternate garage configurations, and in some elevations a bonus room. Larger modifications — moving load-bearing walls, changing the overall footprint, adding a second story to a Ranch plan — are possible but require a custom-plan review and usually add both cost and timeline. We'll quote honestly on any change.",
        ),
        (
            f"How big of a lot do I need to build the {name}?",
            f"The {name} is a {sqft} sq ft {style} home with a {garage}-car garage. For a standard elevation, we typically recommend a minimum lot width of 50–60 feet and a buildable depth sufficient for the home footprint plus setbacks, driveway, and a covered rear lanai. Every county and HOA has different setback requirements — send us your parcel and we'll confirm fit in a free feasibility review.",
        ),
        (
            f"What exterior styles are available for the {name}?",
            f"The {name} is available in multiple Brightview exterior styles — typically Craftsman, Florida Traditional, Modern Farmhouse, and Coastal, with Mediterranean available on larger plans. Each exterior shares the same floor plan but varies the roofline, window proportions, porch details, and siding package. You can pick the style that fits your neighborhood and HOA architectural guidelines.",
        ),
        (
            f"How long does it take to build the {name}?",
            f"A typical {name} build runs 8–12 months from signed contract to keys. Breakdown: feasibility and plan review (3–5 weeks), permit application and approval (6–12 weeks depending on county), site prep and foundation (3–4 weeks), vertical construction (4–6 months for a {story_word} home), and final inspections and CO (2–4 weeks). Polk and Volusia typically permit fastest; Orange and Seminole take longer.",
        ),
    ]


def render(p):
    slug = p["slug"]
    url = f"https://brightviewhomes.us/{slug}.html"
    title = f"{p['name']} Floor Plan — {p['beds']}BR {p['baths']}BA {p['sqft']:,} Sq Ft | Brightview Homes"
    meta = p["meta_desc"]

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": f"{p['name']} Floor Plan",
        "description": p["intro"],
        "category": "New Home Floor Plan",
        "url": url,
        "image": f"https://brightviewhomes.us/images/floor-plans/{slug}/floor-plan.jpg",
        "brand": {"@type": "Brand", "name": "Brightview Homes"},
        "manufacturer": {
            "@type": "HomeBuilder",
            "name": "Brightview Homes",
            "url": "https://brightviewhomes.us/",
            "telephone": "+1-321-310-2849",
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "USD",
            "price": str(p["price"]),
            "availability": "https://schema.org/InStock",
            "url": url,
        },
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "Bedrooms", "value": p["beds"]},
            {"@type": "PropertyValue", "name": "Bathrooms", "value": p["baths"]},
            {"@type": "PropertyValue", "name": "Garage", "value": f"{p['garage']}-car"},
            {"@type": "PropertyValue", "name": "Square Feet", "value": p["sqft"]},
            {"@type": "PropertyValue", "name": "Stories", "value": p["stories"]},
            {"@type": "PropertyValue", "name": "Style", "value": p["style"]},
        ],
    }

    bc_jsonld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://brightviewhomes.us/"},
            {"@type": "ListItem", "position": 2, "name": "Floor Plans", "item": "https://brightviewhomes.us/floor-plans.html"},
            {"@type": "ListItem", "position": 3, "name": f"{p['name']} Floor Plan", "item": url},
        ],
    }

    hl = "".join(f"<li>{html.escape(x)}</li>" for x in p["highlights"])
    rooms = "".join(
        f'<div class="card"><div class="card-eyebrow">Room</div><h4>{html.escape(r["name"])}</h4><p>{html.escape(r["dim"])}</p></div>'
        for r in p["rooms"]
    )
    city_cards = "".join(
        f'<div class="card"><div class="card-eyebrow">Build in</div><h4>{c.replace("-"," ").title()}, FL</h4><p>Scattered-lot new construction by Brightview.</p><a href="new-homes-{c}.html">New homes in {c.replace("-"," ").title()} →</a></div>'
        for c in p["cities"]
    )

    faqs = build_faqs(p)
    faq_html = "".join(
        f'<details style="border-top:1px solid rgba(30,58,82,.12);padding:1.1rem 0"{" open" if i == 0 else ""}><summary style="font-family:var(--serif);font-size:20px;font-weight:500;color:var(--navy);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem">{q}<span style="color:var(--gold);font-size:20px">+</span></summary><p style="font-size:15px;color:var(--navy);line-height:1.75;margin-top:.9rem">{html.escape(a)}</p></details>'
        for i, (q, a) in enumerate(faqs)
    )
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{html.escape(meta)}">
<meta name="keywords" content="{p['name']} floor plan, {p['beds']} bedroom new home Orlando, {p['name']} home plan Brightview, new home {p['sqft']} sq ft">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#1E3A52">
<meta property="og:type" content="product">
<meta property="og:site_name" content="Brightview Homes">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(meta)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://brightviewhomes.us/images/floor-plans/{slug}/floor-plan.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{html.escape(meta)}">
<meta name="twitter:image" content="https://brightviewhomes.us/images/floor-plans/{slug}/floor-plan.jpg">
<link rel="icon" type="image/png" href="/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="bv-landing.css">
<style>
  .plan-hero {{ display: grid; grid-template-columns: 1.1fr 1fr; gap: 2.5rem; align-items: center; }}
  .plan-hero-img {{ width: 100%; border-radius: 8px; box-shadow: 0 8px 32px rgba(0,0,0,.35); }}
  @media (max-width: 820px) {{ .plan-hero {{ grid-template-columns: 1fr; }} }}
  .price-pill {{ display: inline-block; background: var(--gold); color: #fff; font-weight: 500; padding: 4px 12px; border-radius: 4px; font-size: 13px; letter-spacing: .03em; }}
</style>
<script type="application/ld+json">{json.dumps(jsonld)}</script>
<script type="application/ld+json">{json.dumps(bc_jsonld)}</script>
<script type="application/ld+json">{json.dumps(faq_schema)}</script>
</head>
<body>

<nav class="bv-nav">
  <a href="index.html" class="nav-logo"><img src="logo-nav.png" alt="Brightview Homes"></a>
  <div class="nav-links">
    <a href="index.html">Home</a>
    <a href="floor-plans.html" class="active">Floor Plans</a>
    <a href="communities.html">Communities</a>
    <a href="available-lots.html">Lots</a>
    <a href="build-on-your-lot.html">Build On Your Lot</a>
  </div>
  <a href="https://brightviewhomes.us/contact/" class="nav-cta" target="_blank">Contact</a>
</nav>

<main>
  <section class="hero">
    <div class="hero-inner plan-hero">
      <div>
        <div class="eyebrow">Brightview Floor Plan</div>
        <h1>{p['name']} — {p['beds']}BR {p['baths']}BA {p['sqft']:,} Sq Ft {p['style']}</h1>
        <p class="hero-sub">{html.escape(p['tagline'])}</p>
        <div class="hero-stats">
          <div><div class="hero-stat-val">{p['sqft']:,}</div><div class="hero-stat-label">Sq Ft</div></div>
          <div><div class="hero-stat-val">{p['beds']}</div><div class="hero-stat-label">Beds</div></div>
          <div><div class="hero-stat-val">{p['baths']}</div><div class="hero-stat-label">Baths</div></div>
          <div><div class="hero-stat-val">{p['garage']}</div><div class="hero-stat-label">Car Garage</div></div>
          <div><div class="hero-stat-val">{p['stories']}</div><div class="hero-stat-label">{"Story" if p['stories']==1 else "Stories"}</div></div>
        </div>
        <div class="btn-group">
          <a class="btn btn-primary" href="plan-pdf.html?plan={slug}">View Full PDF</a>
          <a class="btn btn-outline" href="https://brightviewhomes.us/contact/?plan={p['name'].replace(' ','%20')}" target="_blank">Get a quote</a>
        </div>
        <p style="margin-top:1rem;font-size:13px;color:rgba(255,255,255,.65)">Starting from <span class="price-pill">${p['price']:,}</span></p>
      </div>
      <div>
        <img class="plan-hero-img" src="images/floor-plans/{slug}/floor-plan.jpg" alt="{p['name']} floor plan architectural drawing — {p['beds']} bed {p['baths']} bath {p['sqft']} sq ft by Brightview Homes">
      </div>
    </div>
  </section>

  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a><span class="sep">›</span>
    <a href="floor-plans.html">Floor Plans</a><span class="sep">›</span>
    <span>{p['name']}</span>
  </nav>

  <section class="section">
    <div class="section-inner">
      <div class="section-eyebrow">★ About the {p['name']}</div>
      <h2>The {p['name']} floor plan</h2>
      <p>{html.escape(p['intro'])}</p>
    </div>
  </section>

  <section class="section alt">
    <div class="section-inner">
      <div class="section-eyebrow">★ Design highlights</div>
      <h2>What makes the {p['name']} stand out</h2>
      <ul>{hl}</ul>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-eyebrow">★ Room dimensions</div>
      <h2>Rooms &amp; layout</h2>
      <p>A quick reference of the major rooms and their approximate dimensions. See the <a href="plan-pdf.html?plan={slug}">full architectural PDF</a> for exact specs, electrical layouts, and exterior options.</p>
      <div class="grid-3">{rooms}</div>
    </div>
  </section>

  <section class="section alt">
    <div class="section-inner">
      <div class="section-eyebrow">★ Best fit</div>
      <h2>Who the {p['name']} works best for</h2>
      <p>{html.escape(p['best_for'])}</p>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-eyebrow">★ Build the {p['name']} in these cities</div>
      <h2>Where Brightview builds the {p['name']}</h2>
      <p>The {p['name']} is available as a scatter-lot build across all 16 Central Florida counties Brightview serves. These cities are where it's been most popular:</p>
      <div class="grid-3">{city_cards}</div>
    </div>
  </section>

  <section class="section alt">
    <div class="section-inner">
      <div class="section-eyebrow">★ {p['name']} FAQ</div>
      <h2>Common questions about the {p['name']}</h2>
      <div style="max-width:820px">
        {faq_html}
      </div>
    </div>
  </section>

  <section class="cta-band">
    <h2>Ready to build the {p['name']}?</h2>
    <p>Get a realistic, itemized quote — no obligation. We'll walk through lot, exterior, and finish options.</p>
    <div class="btn-group" style="justify-content:center">
      <a class="btn btn-primary" href="plan-pdf.html?plan={slug}">Download the PDF</a>
      <a class="btn btn-outline" href="tel:+13213102849">Call (321) 310-2849</a>
    </div>
  </section>
</main>

<footer>
  © Brightview Homes · <a href="index.html">Home</a> · <a href="floor-plans.html">Floor Plans</a> · <a href="communities.html">Communities</a> · <a href="https://brightviewhomes.us/contact/">Contact</a>
</footer>

</body>
</html>
"""


def main():
    for p in PLANS:
        out = ROOT / f"{p['slug']}.html"
        out.write_text(render(p))
        print(f"  wrote {out.name}")
    print(f"Generated {len(PLANS)} plan pages.")


if __name__ == "__main__":
    main()
