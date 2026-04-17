"""Generate city landing pages for Brightview Homes.

Writes one HTML per city into Website/ root. Run from Website/ dir:
    python3 _scripts/gen_cities.py
"""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parent.parent

CITIES = [
    # --- SEMINOLE ---
    {
        "slug": "sanford",
        "name": "Sanford",
        "county": "Seminole",
        "zip_sample": "32773",
        "lat": 28.8028, "lng": -81.2731,
        "tagline": "Historic downtown charm, lakefront waterfront, and brand-new construction on scattered lots.",
        "meta_desc": "New homes in Sanford, FL. Brightview Homes builds custom & scattered-lot new construction in Seminole County — historic downtown, lakefront, SunRail access. From $269K.",
        "hero_sub": "Sanford blends historic downtown character with modern lakefront living — and Brightview is actively building scattered-lot new construction homes across the city. Bring us your lot, or ask about available lots we already have under contract.",
        "intro": "Sanford is one of Seminole County's most underrated cities — affordable compared to Lake Mary and Winter Park, with direct SunRail access to downtown Orlando, a walkable historic downtown, and a working waterfront on Lake Monroe. Brightview Homes currently has two active builds in Sanford with lot acquisition prices between $50K–$70K and finished home values in the low $400Ks.",
        "why_points": [
            "SunRail commuter line connects Sanford directly to downtown Orlando and Poinciana — no I-4 traffic.",
            "Lake Monroe riverfront, RiverWalk trail, and a restored historic downtown with 20+ restaurants and bars.",
            "Scattered lot availability in established neighborhoods — rare inventory you won't find in master-planned communities.",
            "Top-rated Seminole County Public Schools — one of Florida's highest-rated districts.",
            "Easy access to SR-417 and I-4 for commutes to Orlando, Lake Mary, and the beaches.",
        ],
        "neighborhoods": [
            {"name": "Historic Downtown Sanford", "desc": "Brick streets, Victorian-era architecture, and walkable blocks near 1st Street and Magnolia Avenue."},
            {"name": "Lake Mary Boulevard Corridor", "desc": "Newer subdivisions, upgraded commercial, and quick access to SunRail Sanford Station."},
            {"name": "Markham Woods / Markham Meadows", "desc": "Large-lot estate living on the western edge of Sanford, minutes to I-4 and Heathrow."},
            {"name": "Riverwalk / Monroe Harbor", "desc": "Lake Monroe waterfront, marina access, and Sanford's most scenic setting."},
        ],
        "commute": "Sanford sits at the junction of SR-417, SR-46, and I-4. Downtown Orlando is ~30 minutes by car or ~50 minutes stress-free on SunRail. Daytona Beach is ~45 minutes east via I-4, and the Sanford Orlando International Airport (SFB) handles low-cost Allegiant flights to 50+ destinations.",
        "schools": "Seminole County Public Schools consistently rank in Florida's top 5. Notable Sanford-area schools include Seminole High School, Crystal Lake Elementary, and the K-8 Sanford School of the Arts.",
        "featured_plans": ["cambria", "tribeca", "legacy", "valencia"],
    },
    {
        "slug": "lake-mary",
        "name": "Lake Mary",
        "county": "Seminole",
        "zip_sample": "32746",
        "lat": 28.7589, "lng": -81.3176,
        "tagline": "Florida's corporate hub with top-rated schools and upscale master-planned living.",
        "meta_desc": "New homes in Lake Mary, FL. Brightview Homes builds custom new construction in Seminole County's most prestigious address — top schools, corporate hub, SunRail access.",
        "hero_sub": "Lake Mary is Florida's corporate headquarters hub — home to offices for AAA, Mitsubishi, and Verizon Wireless — and consistently ranked among the best places to live in the US. Brightview builds on scattered lots across the city.",
        "intro": "Lake Mary sits at the heart of Seminole County's economic engine, anchored by Heathrow's corporate campus and the Colonial TownPark lifestyle district. The schools are among Florida's highest-rated, the median household income is one of the state's highest, and resale prices have climbed steadily for two decades. Brightview builds new construction homes here when lots come available — typically mid-$400Ks to $700K depending on lot position.",
        "why_points": [
            "Consistently ranked in 'Best Places to Live in America' by Money magazine and Niche.com.",
            "Lake Mary High School is a Florida A-rated school with a strong IB/AP program.",
            "Heathrow corporate campus minutes away — office headquarters for AAA, CHEP, Mitsubishi Power.",
            "SunRail Lake Mary Station for car-free commutes into downtown Orlando.",
            "SR-417 and I-4 interchange for fast access to everywhere in Central Florida.",
        ],
        "neighborhoods": [
            {"name": "Heathrow", "desc": "Gated master-planned community with golf, country club, and Seminole County's highest-rated schools."},
            {"name": "Markham Woods Road Corridor", "desc": "Estate-sized lots, mature oaks, and a rural feel minutes from I-4."},
            {"name": "Colonial TownPark Area", "desc": "Walkable mixed-use district with restaurants, shopping, and newer townhomes and villas."},
            {"name": "Crystal Lake Area", "desc": "Established neighborhoods on chain of lakes, southern Lake Mary."},
        ],
        "commute": "Lake Mary's SR-46A and I-4 interchange puts you 25 minutes from downtown Orlando, 20 minutes from Orlando International Airport via SR-417, and 45 minutes from New Smyrna Beach. SunRail's Lake Mary Station is a 35-minute one-seat ride to downtown Orlando.",
        "schools": "Lake Mary sits within Seminole County's highest-performing school zones. Lake Mary High School, Heathrow Elementary, and Markham Woods Middle consistently earn A ratings from the Florida Department of Education.",
        "featured_plans": ["kensington", "belmont", "astoria", "stephanie"],
    },
    # --- ORANGE ---
    {
        "slug": "orlando",
        "name": "Orlando",
        "county": "Orange",
        "zip_sample": "32801",
        "lat": 28.5383, "lng": -81.3792,
        "tagline": "The heart of Central Florida — build a brand-new home on a scattered lot in any Orlando neighborhood.",
        "meta_desc": "New homes in Orlando, FL from Brightview Homes. Custom new construction on scattered lots across every Orlando neighborhood — East Orlando, Audubon Park, College Park, and more. From $269K.",
        "hero_sub": "Orlando isn't a single market — it's 30+ neighborhoods each with their own character. Brightview builds on scattered lots across the city so you get new construction in the neighborhood you actually want to live in, not a distant master-planned subdivision.",
        "intro": "Most new-construction buyers in Orlando are steered toward master-planned communities 30+ minutes from downtown. Brightview does it differently — we build new homes on individual scattered lots across Orlando's established neighborhoods, including East Orlando, Baldwin Park area, College Park, Audubon Park, Conway, and SoDo. We currently have an active build in East Orlando on a $65K lot with a home value of $450K–$480K — a combination you simply can't find in a new-community build.",
        "why_points": [
            "Scattered-lot construction lets you choose the Orlando neighborhood that fits your lifestyle, not settle for a distant subdivision.",
            "Orlando is the 20th-largest metro in the US and one of the fastest-growing — resale appreciation remains strong.",
            "Home to Orlando International Airport (MCO), Orlando Health, AdventHealth, UCF, and Lockheed Martin.",
            "World-class theme parks, professional sports (Magic, City SC, Pride), and Florida's best restaurants within 20 minutes of most Orlando homes.",
            "Florida has no state income tax — Orlando combines big-city amenities with homestead-exempt tax benefits.",
        ],
        "neighborhoods": [
            {"name": "East Orlando", "desc": "Near UCF, Waterford Lakes, and Lee Vista. Affordable scattered lots with strong rental demand and new builds in the low $400Ks."},
            {"name": "College Park", "desc": "Historic bungalow neighborhood just north of downtown. Tear-down lots exist and new-construction infill is in high demand."},
            {"name": "Audubon Park", "desc": "The Garden District — hip, walkable, with a strong food-and-drink scene. Limited infill lots but premium prices when available."},
            {"name": "Baldwin Park / Winter Park Border", "desc": "High-end, planned streetscape with lake access. Scattered-lot tear-downs available at a premium."},
            {"name": "SoDo / Delaney Park", "desc": "South of downtown. Mature oaks, brick streets, and direct access to Orlando Health / SODO district."},
            {"name": "Conway / Belle Isle", "desc": "South Orlando chain-of-lakes area with boating access and A-rated elementary schools."},
        ],
        "commute": "Orlando's central position means nothing is more than 30 minutes away — downtown, MCO airport, theme parks, UCF, or the Space Coast. I-4, SR-408 (East-West), SR-417, and SR-528 (Beachline) form a grid around the city. Most Brightview lots put you under 20 minutes from downtown Orlando or MCO.",
        "schools": "Orange County Public Schools is Florida's fourth-largest district. A-rated schools exist in specific zones — Audubon Park K-8, Lake Highland Prep, Baldwin Park Elementary, Boone High School (Delaney Park/SoDo), and Winter Park High School's overlap zones. We can help match lot selection to school-zone preference.",
        "featured_plans": ["cambria", "valencia", "legacy", "kensington"],
    },
    {
        "slug": "winter-garden",
        "name": "Winter Garden",
        "county": "Orange",
        "zip_sample": "34787",
        "lat": 28.5653, "lng": -81.5861,
        "tagline": "One of America's fastest-growing cities, with a downtown named 'Main Street of America.'",
        "meta_desc": "New homes in Winter Garden, FL. Brightview Homes builds custom new construction on scattered lots in west Orange County — top-rated schools, historic downtown, West Orange Trail access.",
        "hero_sub": "Winter Garden has transformed from a citrus town into one of the most in-demand new-home markets in Orange County. Brightview builds on scattered lots in Winter Garden and neighboring Horizon West, Oakland, and Tildenville.",
        "intro": "Winter Garden's historic downtown on Plant Street has been named one of the top small-town downtowns in America. Couple that with A-rated schools, direct access to the West Orange Trail, and proximity to Disney and the Turnpike, and it's no surprise the city tops every 'fastest growing' list in Florida. Lot prices here are competitive but resale is strong — new-construction Brightview homes in the area typically sit in the mid-$400Ks to $600Ks.",
        "why_points": [
            "Historic Plant Street downtown — farmer's market every Saturday, craft breweries, restaurants, and the Garden Theatre.",
            "West Orange Trail — 22 miles of paved bike/walk trail connecting Winter Garden to Apopka and Killarney.",
            "A-rated Orange County schools including Whispering Oak Elementary and West Orange High School.",
            "Under 15 minutes to Disney, 20 minutes to downtown Orlando, and direct Turnpike access.",
            "Horizon West — one of the top-selling master-planned areas in the US — borders Winter Garden.",
        ],
        "neighborhoods": [
            {"name": "Historic Downtown Winter Garden", "desc": "Brick streets, craftsman bungalows, and Plant Street's walkable district."},
            {"name": "Oakland", "desc": "Small town adjoining Winter Garden — lakefront lots on Lake Apopka, historic character."},
            {"name": "Tildenville", "desc": "Established, tree-lined neighborhood with scattered tear-down lot availability."},
            {"name": "Horizon West / Hamlin", "desc": "Newer master-planned area to the south with access to Walt Disney World."},
        ],
        "commute": "Winter Garden's position on the Turnpike (exit 272) makes north-south travel fast. Downtown Orlando is ~20 minutes via SR-408, Disney is 15 minutes south, and Orlando International Airport is 30 minutes via SR-417.",
        "schools": "Orange County's west zone schools consistently earn A ratings. Whispering Oak Elementary, Sunridge Middle, and West Orange High School anchor the district.",
        "featured_plans": ["valencia", "kensington", "belmont", "astoria"],
    },
    # --- VOLUSIA ---
    {
        "slug": "deland",
        "name": "DeLand",
        "county": "Volusia",
        "zip_sample": "32724",
        "lat": 29.0283, "lng": -81.3031,
        "tagline": "Athens of Florida — a historic college town with brick streets and new-home scattered lots.",
        "meta_desc": "New homes in DeLand, FL. Brightview Homes builds custom new construction on scattered lots in Volusia County — Stetson University, historic downtown, easy I-4 access.",
        "hero_sub": "DeLand is home to Stetson University, one of the best-preserved historic downtowns in Florida, and some of the most reasonable scattered-lot pricing in Central Florida. Brightview has multiple active builds across the city.",
        "intro": "DeLand consistently wins 'America's Best Main Street' awards, and for good reason — the downtown is walkable, the historic architecture is largely intact, and the Stetson University campus anchors a cultural scene you won't find in most Volusia cities. Brightview Homes has been active in DeLand since 2023, with lots in the $40K–$70K range and finished homes priced in the $380K–$450K range.",
        "why_points": [
            "Stetson University drives a vibrant downtown with restaurants, galleries, and a craft-brewery scene.",
            "Historic downtown DeLand — 8 consecutive 'Great American Main Street' awards.",
            "Lot pricing among the lowest in Central Florida, with homes appreciating steadily.",
            "I-4 access — 30 minutes to downtown Orlando, 20 minutes to Daytona Beach.",
            "Outdoor recreation — Blue Spring State Park, St. Johns River, and the Spring-to-Spring Trail.",
        ],
        "neighborhoods": [
            {"name": "Historic DeLand / Downtown", "desc": "Brick streets, Victorian architecture, and walking distance to Stetson, restaurants, and shops."},
            {"name": "Glenwood", "desc": "Rural-feel western DeLand with large lots and mature oaks, near Hontoon Island State Park."},
            {"name": "DeLand Country Club", "desc": "Golf-course community on the east side with established homes and available scattered lots."},
            {"name": "Beresford / Lake Beresford", "desc": "Waterfront living on the St. Johns River with boat-access lots."},
        ],
        "commute": "DeLand sits directly on I-4, making the 30-mile trip to downtown Orlando around 35 minutes. Daytona Beach is 20 minutes east via SR-44, and the Sanford SunRail station is 25 minutes south for car-free Orlando commutes.",
        "schools": "Volusia County Public Schools — notable DeLand-area schools include Citrus Grove Elementary, DeLand High School, and Freedom Elementary. Stetson University also runs a highly regarded K-12 private option at the Stetson Baptist Christian School.",
        "featured_plans": ["cambria", "tribeca", "legacy", "hudson"],
    },
    {
        "slug": "new-smyrna-beach",
        "name": "New Smyrna Beach",
        "county": "Volusia",
        "zip_sample": "32168",
        "lat": 29.0258, "lng": -80.9270,
        "tagline": "Florida's best surf town, with Atlantic beaches, Intracoastal Waterway, and limited scattered lots.",
        "meta_desc": "New homes in New Smyrna Beach, FL. Brightview Homes builds custom coastal new construction on scattered lots — Atlantic beachfront, Intracoastal Waterway, historic Canal Street.",
        "hero_sub": "New Smyrna Beach is Volusia's premier coastal city — famous for surfing, Canal Street restaurants, and the undeveloped Canaveral National Seashore. Scattered lots are limited, so opportunities go fast.",
        "intro": "If Daytona is for spring break, New Smyrna is for locals. The surfing is some of the best on the East Coast, the historic Canal Street has a restaurant scene that rivals downtown Orlando, and the south end of the city borders the 58,000-acre Canaveral National Seashore. Brightview Homes builds scattered-lot coastal homes here when lot inventory is available — typically in the $500K–$900K range given the premium waterfront values.",
        "why_points": [
            "Voted 'Best Surf Town in Florida' by Surfer Magazine and Surfline.",
            "Canal Street historic district with 30+ restaurants, craft breweries, art galleries, and live music.",
            "Canaveral National Seashore — 24 miles of undeveloped Atlantic beach on the city's southern border.",
            "Growing artist community and the New Smyrna Beach Museum of Art.",
            "Daytona International Airport 20 minutes north, Orlando International 75 minutes west.",
        ],
        "neighborhoods": [
            {"name": "Historic Downtown / Canal Street", "desc": "Walkable downtown with Victorian-era homes on tree-lined streets."},
            {"name": "Beachside / South Atlantic Avenue", "desc": "Ocean-side or ocean-view lots on the barrier island — the most sought-after New Smyrna address."},
            {"name": "Indian River Shores", "desc": "Intracoastal Waterway and deepwater boat-access lots on the mainland side."},
            {"name": "Venetian Bay", "desc": "Newer planned community on the mainland with golf course and resort amenities."},
        ],
        "commute": "US-1 and I-95 connect New Smyrna to Daytona Beach (20 min north), Orlando (75 min west via I-4), Kennedy Space Center (40 min south), and Melbourne (90 min south). The Daytona International Airport is 20 minutes north.",
        "schools": "Volusia County Public Schools — New Smyrna Beach High School, Read-Pattillo Elementary, and Indian River Elementary are the primary neighborhood options.",
        "featured_plans": ["kensington", "belmont", "astoria", "stephanie"],
    },
    # --- LAKE ---
    {
        "slug": "clermont",
        "name": "Clermont",
        "county": "Lake",
        "zip_sample": "34711",
        "lat": 28.5494, "lng": -81.7728,
        "tagline": "Rolling hills, 1,000+ lakes, and one of the fastest-growing cities in Central Florida.",
        "meta_desc": "New homes in Clermont, FL. Brightview Homes builds custom new construction on scattered lots in Lake County — chain of lakes, 20 min to Disney, minutes from Orlando via Turnpike.",
        "hero_sub": "Clermont has become one of Central Florida's hottest markets — the hills are real, the chain of lakes is 14 lakes deep, and the Turnpike puts you 20 minutes from Disney. Brightview builds on scattered lots citywide.",
        "intro": "Clermont sits on the highest terrain in peninsular Florida — actual rolling hills, with the iconic Citrus Tower at one of the highest points. The city has grown from 9,000 residents in 2000 to over 45,000 today, driven by proximity to the Orlando theme parks, a booming restaurant scene, and the Clermont Chain of Lakes. Scattered-lot opportunities exist across the city, with Brightview homes typically landing in the $400K–$600K range.",
        "why_points": [
            "Clermont Chain of Lakes — 14 connected lakes for boating, bass fishing, and waterfront living.",
            "Rolling hills, citrus history, and Florida's legitimate 'hill country' topography.",
            "20 minutes to Walt Disney World via US-27 and SR-429.",
            "National Training Center — Olympic-caliber fitness center that put Clermont on the triathlon map.",
            "Growing downtown, new Publix-anchored centers, and Waterfront Park on Lake Minneola.",
        ],
        "neighborhoods": [
            {"name": "Downtown Clermont / Lake Minneola", "desc": "Walkable downtown on Lake Minneola with Waterfront Park and the South Lake Trail."},
            {"name": "Minneola", "desc": "Adjoining Clermont to the north — newer construction and larger lot availability."},
            {"name": "Kings Ridge / Legends", "desc": "Established golf-community neighborhoods with resale and scattered infill opportunities."},
            {"name": "Montverde", "desc": "Upscale rural enclave west of Clermont with estate-sized lots and Montverde Academy."},
        ],
        "commute": "Clermont sits at the intersection of the Florida Turnpike and US-27. Walt Disney World is 20 minutes south via SR-429, Orlando International Airport is 45 minutes via the Turnpike, and downtown Orlando is 35 minutes via SR-50.",
        "schools": "Lake County Schools — Cypress Ridge Elementary, East Ridge Middle, and East Ridge High School serve most Clermont residents. Montverde Academy is a nationally ranked private school option in the area.",
        "featured_plans": ["valencia", "kensington", "belmont", "astoria"],
    },
    {
        "slug": "mount-dora",
        "name": "Mount Dora",
        "county": "Lake",
        "zip_sample": "32757",
        "lat": 28.8028, "lng": -81.6444,
        "tagline": "'New England of Central Florida' — lakefront charm, antique district, and historic downtown.",
        "meta_desc": "New homes in Mount Dora, FL. Brightview Homes builds custom new construction on scattered lots in Lake County — lakefront, historic downtown, famous art and antique festivals.",
        "hero_sub": "Mount Dora earned its 'New England of Florida' nickname — hills, oaks, a working lighthouse, and a downtown that feels like Kennebunkport. Brightview builds scattered-lot homes in Mount Dora and neighboring Tavares and Eustis.",
        "intro": "Mount Dora is one of Central Florida's most distinctive towns — built on hills around Lake Dora, with a charming lighthouse, a historic downtown anchored by the Lakeside Inn (Florida's oldest continuously-operating hotel), and a calendar packed with arts, crafts, and antique festivals. The city has seen steady growth without losing its character. Scattered lot inventory is limited but available, and Brightview homes here typically run $450K–$700K.",
        "why_points": [
            "Historic downtown with the Donnelly House, Lakeside Inn, and 150+ shops and restaurants along Donnelly and 4th Avenue.",
            "Mount Dora Arts Festival, Antique Extravaganza, and Craft Fair bring 250,000+ visitors annually.",
            "Lake Dora, the Dora Canal, and the Harris Chain of Lakes — some of Florida's best bass fishing.",
            "The 'New England of Florida' — oaks, hills, and a seasonal climate that feels like the Carolinas.",
            "45 minutes to Orlando, 20 minutes to Leesburg, and direct SR-429 access to the Turnpike.",
        ],
        "neighborhoods": [
            {"name": "Historic Downtown Mount Dora", "desc": "Victorian and craftsman homes within walking distance of downtown and Lake Dora."},
            {"name": "Country Club of Mount Dora", "desc": "Golf-community living with lakefront options and newer construction."},
            {"name": "Loch Leven", "desc": "Gated lakefront community on Lake Dora — one of the most prestigious addresses in Lake County."},
            {"name": "Sullivan Ranch", "desc": "Master-planned community to the north with amenity center and community pool."},
        ],
        "commute": "SR-429 and the Turnpike make Mount Dora commutes into Orlando (45 min) and Leesburg (20 min) straightforward. Orlando International Airport is 55 minutes south.",
        "schools": "Lake County Schools — Round Lake Charter Elementary, Mount Dora Middle, and Mount Dora High School are the core neighborhood options.",
        "featured_plans": ["kensington", "belmont", "astoria", "stephanie"],
    },
    # --- OSCEOLA ---
    {
        "slug": "kissimmee",
        "name": "Kissimmee",
        "county": "Osceola",
        "zip_sample": "34741",
        "lat": 28.2920, "lng": -81.4076,
        "tagline": "Gateway to Disney, Celebration, and the fastest-growing metro in Central Florida.",
        "meta_desc": "New homes in Kissimmee, FL. Brightview Homes builds custom new construction on scattered lots in Osceola County — Disney corridor, short-term rental potential, booming growth.",
        "hero_sub": "Kissimmee is one of the fastest-growing cities in Florida — minutes from Disney, with strong short-term rental demand and substantial new-home appetite. Brightview builds scattered-lot primary and investment homes here.",
        "intro": "Kissimmee has evolved from a cattle town into Central Florida's tourism and bedroom-community epicenter. The Disney corridor on US-192 drives short-term rental demand, while the Poinciana and St. Cloud directions attract primary-home buyers. Brightview Homes builds scattered-lot homes for both primary residence and investor buyers here — DSCR financing through Springwell Capital makes it a natural fit for rental-property investors.",
        "why_points": [
            "Minutes from Walt Disney World, Disney Springs, Sea World, and the main Orlando tourist corridor.",
            "Strong short-term rental demand and some of Central Florida's most permissive STR zoning.",
            "Florida's Turnpike and I-4 provide 20-minute access to Orlando International Airport.",
            "Lake Tohopekaliga ('Lake Toho') — 18,810 acres of bass fishing and boating access.",
            "Fast-growing Osceola County schools and major employers including Advent Health and NeoCity tech corridor.",
        ],
        "neighborhoods": [
            {"name": "Celebration", "desc": "Disney's original master-planned town — planned streetscape, town center, and a premium address."},
            {"name": "Lake Nona Border", "desc": "Medical City and the USTA campus sit just north; Kissimmee residents get Lake Nona proximity without Lake Nona pricing."},
            {"name": "Poinciana", "desc": "Large growing community straddling Osceola/Polk county line — scattered lot inventory and primary-home focus."},
            {"name": "Shingle Creek / Lake Toho", "desc": "Lakefront and near-lake lots on Kissimmee's east side with boating access."},
        ],
        "commute": "Kissimmee's Florida Turnpike access and proximity to I-4 make Orlando commutes straightforward — downtown Orlando 25 minutes, Orlando International Airport 20 minutes, Disney 10 minutes. SunRail's Kissimmee Station connects to downtown Orlando by train.",
        "schools": "The School District of Osceola County — notable schools include Celebration High School, Liberty High School, and Kissimmee Elementary. School quality varies by neighborhood zone, so lot selection matters.",
        "featured_plans": ["cambria", "tribeca", "valencia", "legacy"],
    },
    {
        "slug": "st-cloud",
        "name": "St. Cloud",
        "county": "Osceola",
        "zip_sample": "34769",
        "lat": 28.2489, "lng": -81.2812,
        "tagline": "Small-town feel, big-lot availability, and 30 minutes from Lake Nona Medical City.",
        "meta_desc": "New homes in St. Cloud, FL. Brightview Homes builds custom new construction on scattered lots in Osceola County — larger lots, small-town feel, proximity to Lake Nona and Orlando.",
        "hero_sub": "St. Cloud gives you the small-town feel of old Florida with scattered-lot availability you won't find closer to the theme parks — plus quick access to Lake Nona Medical City, the Orlando airport, and the Space Coast.",
        "intro": "St. Cloud has become one of the most popular markets for buyers who want more land and a quieter setting without leaving metro Orlando. Lot inventory on larger parcels is still available, Canoe Creek and Narcoossee corridors are seeing heavy growth, and Lake Nona Medical City is a 20-minute commute. Brightview Homes builds scattered-lot primary residences here for families trading urban density for space.",
        "why_points": [
            "Scattered-lot and larger-lot inventory — 1/4 acre and up still available across much of the city.",
            "Lake Nona Medical City 20 minutes north — one of the fastest-growing job markets in Florida.",
            "Historic downtown St. Cloud on Lake Toho's southern shore.",
            "US-192 and Florida's Turnpike provide direct access to Orlando, Disney, and the Space Coast.",
            "Strong Osceola County school zoning in Canoe Creek and Narcoossee areas.",
        ],
        "neighborhoods": [
            {"name": "Narcoossee Corridor", "desc": "Rapidly growing area along Narcoossee Road with scattered lot and new-community options, adjoining Lake Nona."},
            {"name": "Canoe Creek", "desc": "Larger-lot rural-feel area south of St. Cloud with growing residential development."},
            {"name": "Historic Downtown St. Cloud", "desc": "Walkable lakefront downtown on Lake Toho with craftsman-era homes."},
            {"name": "Harmony", "desc": "Conservation-based master-planned community east of St. Cloud with top-rated schools."},
        ],
        "commute": "St. Cloud's Turnpike and US-192 position puts Orlando International Airport 25 minutes away, Lake Nona 20 minutes, Disney 25 minutes, and downtown Orlando 35 minutes.",
        "schools": "The School District of Osceola County — Harmony High School (in the Harmony community) is A-rated; St. Cloud High School, Neptune Middle, and Canoe Creek K-8 also serve the city.",
        "featured_plans": ["cambria", "valencia", "legacy", "kensington"],
    },
    # --- POLK ---
    {
        "slug": "lakeland",
        "name": "Lakeland",
        "county": "Polk",
        "zip_sample": "33801",
        "lat": 28.0395, "lng": -81.9498,
        "tagline": "Midway between Orlando and Tampa — affordable new construction in a growing I-4 corridor city.",
        "meta_desc": "New homes in Lakeland, FL. Brightview Homes builds custom new construction on scattered lots in Polk County — midway between Orlando and Tampa, Publix headquarters, lower cost of living.",
        "hero_sub": "Lakeland is the economic engine of the I-4 corridor between Orlando and Tampa — home to Publix Super Markets, Florida Polytechnic University, and some of the most affordable new-construction opportunities in Central Florida.",
        "intro": "Lakeland sits at the exact geographic midpoint between Orlando and Tampa on I-4, and it's reaping the benefits — Amazon fulfillment, Publix's global headquarters, and a tech-and-manufacturing boom driven by Florida Polytechnic University. Lakeland new-construction pricing is typically 15–25% below comparable Orange/Seminole County homes, which has made it one of the strongest appreciation markets in the state. Brightview Homes builds scattered-lot homes here in the $350K–$550K range.",
        "why_points": [
            "Midway between Orlando (50 min) and Tampa (40 min) on I-4 — perfect for dual-market commuters.",
            "Publix Super Markets global HQ, Amazon fulfillment, and major logistics employment.",
            "Florida Polytechnic University — the state's STEM-focused public university.",
            "38 named lakes within city limits — boating, fishing, and waterfront living options at lower price points.",
            "Historic downtown Lakeland has been undergoing a restaurant and culture renaissance.",
        ],
        "neighborhoods": [
            {"name": "Historic Dixieland / South Lake Morton", "desc": "Tree-lined streets of craftsman and Spanish-revival homes near downtown."},
            {"name": "Lakeland Highlands", "desc": "Established unincorporated area south of Lakeland with larger lots and top Polk schools."},
            {"name": "Bartow Road Corridor", "desc": "Growing residential development along US-98 south toward Bartow."},
            {"name": "North Lakeland / I-4 Corridor", "desc": "Newer development with quick I-4 access to Orlando and Tampa."},
        ],
        "commute": "Lakeland's I-4 position means downtown Tampa is 40 minutes west and downtown Orlando is 50 minutes east. Tampa International Airport is 45 minutes, Orlando International is 55 minutes, and Disney is 35 minutes northeast.",
        "schools": "Polk County Public Schools — George Jenkins High School, Lakeland High School, and Lakeland Highlands Middle consistently rank among Polk's strongest. A-rated elementary options include Scott Lake Elementary and Highlands Grove Elementary.",
        "featured_plans": ["cambria", "tribeca", "legacy", "valencia"],
    },
    {
        "slug": "oviedo",
        "name": "Oviedo",
        "county": "Seminole",
        "zip_sample": "32765",
        "lat": 28.6700, "lng": -81.2081,
        "tagline": "Family-oriented, A-rated schools, and one of Central Florida's best-balanced lifestyles.",
        "meta_desc": "New homes in Oviedo, FL. Brightview Homes builds custom new construction on scattered lots in Seminole County — A-rated schools, UCF corridor, Oviedo on the Park.",
        "hero_sub": "Oviedo consistently ranks in the top tier of Florida's best cities to raise a family — A-rated schools, low crime, and a walkable new downtown at Oviedo on the Park. Brightview builds scattered-lot homes throughout the city.",
        "intro": "Oviedo sits at the eastern edge of Seminole County, bordering the University of Central Florida and the fast-growing Lake Mary / Heathrow corridor. The city has been transformed in the past decade by the Oviedo on the Park mixed-use development — a walkable downtown with restaurants, a splash pad, amphitheater, and the Oviedo City Hall. A-rated schools, the Oviedo High School 'Lions' football tradition, and some of Seminole's best-priced scatter lots make it a consistent relocation target.",
        "why_points": [
            "Oviedo High School, Hagerty High School, and top-rated Seminole County elementary and middle schools.",
            "Oviedo on the Park — the city's new walkable downtown with 15+ restaurants, amphitheater, and farmers market.",
            "UCF main campus 10 minutes south — strong rental demand if investing.",
            "SR-417 and SR-408 connect Oviedo to downtown Orlando in 25 minutes and MCO in 30.",
            "Legendary chicken statues and community character — Oviedo takes its identity seriously.",
        ],
        "neighborhoods": [
            {"name": "Oviedo on the Park", "desc": "Walkable downtown core with newer townhomes, restaurants, and the amphitheater."},
            {"name": "Alafaya Woods", "desc": "Established family neighborhood with larger lots and mature oaks near UCF."},
            {"name": "Twin Rivers", "desc": "Gated community on the Econlockhatchee River with nature trails."},
            {"name": "Kingsbridge / Stoneybrook", "desc": "Golf-community neighborhoods on the city's southern edge."},
        ],
        "commute": "SR-417 (Greeneway) and SR-408 (East-West) give Oviedo fast access to downtown Orlando (25 min) and Orlando International Airport (30 min). UCF is 10 minutes south, and Lake Mary is 15 minutes west via Red Bug Lake Road.",
        "schools": "Oviedo is in Seminole County Public Schools — Florida's highest-rated district. Notable schools include Oviedo High School, Hagerty High School, Jackson Heights Middle, and Carillon Elementary.",
        "featured_plans": ["cambria", "valencia", "kensington", "belmont"],
    },
    {
        "slug": "winter-park",
        "name": "Winter Park",
        "county": "Orange",
        "zip_sample": "32789",
        "lat": 28.5999, "lng": -81.3392,
        "tagline": "The most prestigious address in Orange County — historic lakeside living minutes from downtown Orlando.",
        "meta_desc": "New homes in Winter Park, FL. Brightview Homes — headquartered in Winter Park — builds custom new construction on scattered lots in the county's most prestigious market.",
        "hero_sub": "Winter Park is where Brightview Homes is headquartered. It's also one of the most prestigious addresses in Orange County — home of Rollins College, the Morse Museum of American Art, and the iconic Park Avenue shopping district.",
        "intro": "Winter Park was founded as a winter resort for wealthy Northerners in the 1880s and has retained its character better than almost any city in Florida. The tree-canopied streets, chain of lakes, and walkable Park Avenue anchor a real estate market where scatter-lot tear-downs are the most common path to new construction. Brightview Homes is headquartered at 480 N Orlando Ave in Winter Park — meaning we build in our home market with all the local knowledge that comes with it.",
        "why_points": [
            "Rollins College — America's oldest college in Florida, with a liberal-arts campus on Lake Virginia.",
            "Park Avenue — one of the most famous walkable shopping districts in the South.",
            "Winter Park Chain of Lakes — six connected lakes with the historic Scenic Boat Tour since 1938.",
            "A-rated Winter Park schools and top private options including Trinity Prep and Winter Park Christian.",
            "Brightview is headquartered in Winter Park — we know this market intimately.",
        ],
        "neighborhoods": [
            {"name": "Park Avenue / Central Park", "desc": "Historic pedestrian district with brick streets, boutique shopping, and Central Park concerts."},
            {"name": "Olde Winter Park / Interlachen", "desc": "Tree-canopied streets with craftsman and Spanish-revival homes on the chain of lakes."},
            {"name": "College Park Border", "desc": "Bungalow neighborhoods overlapping with Orlando's College Park — strong tear-down lot market."},
            {"name": "Maitland / Audubon Border", "desc": "Transition areas with slightly larger lots and Lake Maitland access."},
            {"name": "Aloma Corridor", "desc": "Eastern Winter Park with a mix of mid-century ranches and newer infill."},
        ],
        "commute": "Winter Park is 10 minutes from downtown Orlando via I-4, 15 minutes from MCO via SR-417, and 5 minutes from the Winter Park / Park Avenue SunRail station for car-free downtown commutes.",
        "schools": "Orange County Public Schools — Winter Park High School, Glenridge Middle, Brookshire Elementary, and Audubon Park K-8 are the primary neighborhood schools. Private options include Trinity Prep, Winter Park Christian, and Rollins-area schools.",
        "featured_plans": ["kensington", "belmont", "astoria", "stephanie"],
    },
    {
        "slug": "port-orange",
        "name": "Port Orange",
        "county": "Volusia",
        "zip_sample": "32129",
        "lat": 29.1383, "lng": -80.9956,
        "tagline": "Daytona's family-friendly southern neighbor, with top schools and Spruce Creek Fly-In country.",
        "meta_desc": "New homes in Port Orange, FL. Brightview Homes builds custom new construction on scattered lots in Volusia County — top schools, Daytona Beach access, Spruce Creek Fly-In.",
        "hero_sub": "Port Orange has quietly become one of Volusia County's most sought-after relocation markets — Atlantic beach access, highly rated schools, and the world-famous Spruce Creek Fly-In community for aviation enthusiasts.",
        "intro": "Port Orange sits directly south of Daytona Beach on US-1 and I-95, but feels like a completely different city — quieter, more family-oriented, and anchored by top-rated schools. The Spruce Creek Fly-In is a 1,300-acre residential airpark — the largest in the world — and gives Port Orange a unique aviation culture. Brightview builds scattered-lot new construction throughout the city for buyers who want coastal Florida lifestyle without Daytona's spring-break energy.",
        "why_points": [
            "A-rated Volusia County schools — Spruce Creek High School consistently ranks among Florida's best.",
            "Spruce Creek Fly-In — the world's largest residential airpark with private taxiways to hangars.",
            "Atlantic beaches 10 minutes east (Wilbur-by-the-Sea and Dunlawton Avenue beach approach).",
            "I-95, US-1, and Dunlawton Avenue provide fast access to Daytona, New Smyrna, and Orlando.",
            "Port Orange is larger than most coastal Florida cities — 60,000+ residents with real commercial infrastructure.",
        ],
        "neighborhoods": [
            {"name": "Spruce Creek Fly-In", "desc": "Residential airpark with private hangars and taxiways — one of the most unique addresses in the country."},
            {"name": "Waters Edge / Summer Trees", "desc": "Family neighborhoods near Spruce Creek Park and the Spruce Creek preserve."},
            {"name": "Port Orange Plantation", "desc": "Established golf-adjacent community with larger lot availability."},
            {"name": "Beachside / Wilbur-by-the-Sea", "desc": "Small unincorporated beachside area east of Port Orange with ocean-view lots."},
        ],
        "commute": "I-95 and US-1 give Port Orange direct access to Daytona Beach (10 min north), New Smyrna Beach (15 min south), Orlando (75 min west via I-4), and Jacksonville (90 min north). Daytona International Airport is 15 minutes, Orlando International is 80 minutes.",
        "schools": "Volusia County Public Schools — Spruce Creek High School (A-rated), Creekside Middle, Cypress Creek Elementary, and Horizon Elementary. Private options include Calvary Christian Academy.",
        "featured_plans": ["valencia", "kensington", "belmont", "astoria"],
    },
    {
        "slug": "groveland",
        "name": "Groveland",
        "county": "Lake",
        "zip_sample": "34736",
        "lat": 28.5586, "lng": -81.8509,
        "tagline": "One of America's fastest-growing cities — rolling hills, affordable scatter lots, and Turnpike access.",
        "meta_desc": "New homes in Groveland, FL. Brightview Homes builds custom new construction on scattered lots in Lake County — one of America's fastest-growing cities, near Disney and Clermont.",
        "hero_sub": "Groveland has topped national 'fastest-growing cities' lists for several years running — and with rolling hills, Florida Turnpike access, and some of the best-priced scatter lots in the region, it's easy to see why.",
        "intro": "Groveland is the current growth leader in Lake County — smaller than Clermont but growing faster, with scatter-lot pricing that still offers solid value for buyers and builders. The city's position between Clermont and the Turnpike makes commutes to Orlando (45 min) and Walt Disney World (25 min) manageable, and the Lake David corridor is seeing significant residential and retail development. Brightview Homes builds scatter-lot homes across Groveland in the $350K–$500K range.",
        "why_points": [
            "Consistently named one of America's fastest-growing cities (US Census Bureau).",
            "Rolling hills and Lake County's chain of lakes topography — legitimate elevation in peninsular Florida.",
            "Florida Turnpike access — Walt Disney World is 25 minutes and downtown Orlando 45 minutes.",
            "Scatter-lot pricing 20–30% lower than comparable Orange County or Seminole lots.",
            "Growing school infrastructure and new Lake County elementary/middle schools in the area.",
        ],
        "neighborhoods": [
            {"name": "Lake David Corridor", "desc": "New commercial and residential development along Lake David, the city's cultural center."},
            {"name": "Cherry Lake", "desc": "Established waterfront community on Cherry Lake with larger lots."},
            {"name": "Clermont Border / Waterside Pointe", "desc": "Rolling-hills communities bordering Clermont with newer construction and resale."},
            {"name": "Villa City / Bay Lake Road", "desc": "Rural-feel areas with larger buildable parcels."},
        ],
        "commute": "Groveland's Florida Turnpike (exit 267) position puts Walt Disney World 25 minutes south via SR-429, downtown Orlando 45 minutes east, and Orlando International Airport 55 minutes via the Turnpike.",
        "schools": "Lake County Schools — Groveland Elementary, Gray Middle, and South Lake High School serve most of the city. Lake County is investing heavily in new school construction in the growth corridor.",
        "featured_plans": ["cambria", "tribeca", "valencia", "legacy"],
    },
    {
        "slug": "celebration",
        "name": "Celebration",
        "county": "Osceola",
        "zip_sample": "34747",
        "lat": 28.3169, "lng": -81.5347,
        "tagline": "The original Disney-designed master-planned town — walkable downtown, premium schools, and a cohesive aesthetic.",
        "meta_desc": "New homes in Celebration, FL. Brightview Homes builds custom new construction on scattered lots in the original Disney-designed community — walkable downtown, A-rated schools.",
        "hero_sub": "Celebration is Disney's original master-planned town — a walkable, highly designed community with a town center, lakes, and a scripted aesthetic. Scattered lots exist but go fast; Brightview builds when opportunities arise.",
        "intro": "Celebration was built by The Walt Disney Company in the 1990s as a model new-urbanist town, drawing design influence from Seaside and classic Southern pedestrian cities. The town center sits on Lake Rianhard with restaurants, a boutique hotel, and year-round events. Schools are A-rated, the streetscape is immaculate, and the premium is real — but buyers pay for a cohesive aesthetic and a walkable community that's nearly impossible to find anywhere else in Central Florida.",
        "why_points": [
            "Walkable town center on Lake Rianhard — restaurants, boutique shopping, and community events year-round.",
            "Celebration K-8 School and Celebration High School — consistently A-rated Osceola County schools.",
            "Original Disney town planning — cohesive architecture, tree-lined streets, and pedestrian-first design.",
            "Direct access to Walt Disney World (5 min) and the entire tourism corridor via US-192.",
            "Professional service and medical hub with AdventHealth Celebration as a major employer.",
        ],
        "neighborhoods": [
            {"name": "Celebration Village / Downtown", "desc": "Walkable core with front-porch homes, town center, and Lake Rianhard access."},
            {"name": "Artisan Park", "desc": "Newer Celebration neighborhood with townhomes and modern architecture."},
            {"name": "West Village", "desc": "Family-oriented Celebration neighborhood with parks and pools."},
            {"name": "North Village", "desc": "Larger-lot Celebration neighborhood bordering the conservation areas."},
        ],
        "commute": "Celebration's US-192 and I-4 access puts Walt Disney World 5 minutes west, Orlando International Airport 20 minutes north, downtown Orlando 30 minutes, and Disney Springs 15 minutes.",
        "schools": "Celebration K-8 School (on-site in the community) and Celebration High School are both A-rated. The School District of Osceola County also offers Neptune Middle and other Osceola options nearby.",
        "featured_plans": ["kensington", "belmont", "astoria", "stephanie"],
    },
    {
        "slug": "davenport",
        "name": "Davenport",
        "county": "Polk",
        "zip_sample": "33837",
        "lat": 28.1614, "lng": -81.6020,
        "tagline": "The Disney corridor's new-home hotspot — STR-friendly zoning, Polk pricing, and I-4 access.",
        "meta_desc": "New homes in Davenport, FL. Brightview Homes builds custom new construction on scattered lots in Polk County — Disney corridor, STR-friendly, affordable new homes near Orlando attractions.",
        "hero_sub": "Davenport is at the epicenter of the Disney short-term rental corridor — minutes from the theme parks, with some of the most permissive STR zoning in Central Florida. For primary homeowners, it's an I-4 corridor value play.",
        "intro": "Davenport has transformed from a quiet Polk County town into one of Central Florida's biggest growth markets — driven largely by its position 15 minutes from Walt Disney World and its STR-friendly zoning. Posner Park and Champions Gate have brought major retail and restaurants, I-4 gives you direct Orlando or Tampa access, and Polk County pricing makes new-construction math work for both primary homeowners and investors. Brightview builds scatter-lot new homes here in the $350K–$500K range.",
        "why_points": [
            "Short-term rental friendly — one of the strongest STR markets in Central Florida outside of Kissimmee.",
            "Walt Disney World is 15 minutes via I-4 and US-192; Disney Springs is 12 minutes.",
            "Posner Park and Champions Gate bring 100+ retailers and restaurants to the immediate area.",
            "I-4 corridor midway between Orlando (35 min) and Tampa (55 min).",
            "Polk County pricing — new construction 20–25% less than comparable Osceola or Orange County scatter lots.",
        ],
        "neighborhoods": [
            {"name": "Posner Park / Champions Gate Border", "desc": "The growth hub of Davenport with major retail, restaurants, and newer master-planned communities."},
            {"name": "Historic Downtown Davenport", "desc": "Smaller walkable historic area with craftsman-era homes."},
            {"name": "Legacy Park", "desc": "Master-planned community with amenities popular with STR investors."},
            {"name": "Ridgewood Lakes / Solivita Border", "desc": "55+ and family communities on the northern Davenport edge."},
        ],
        "commute": "Davenport's I-4 (exit 55) position puts Walt Disney World 15 minutes east via US-192, Orlando International Airport 35 minutes via I-4, downtown Orlando 40 minutes, and Tampa International Airport 55 minutes.",
        "schools": "Polk County Public Schools — Davenport Elementary, Shelley S. Boone Middle, and Ridge Community High School serve most Davenport residents. Newer Polk schools are being added in the growth corridor.",
        "featured_plans": ["tribeca", "cambria", "valencia", "legacy"],
    },
    {
        "slug": "winter-haven",
        "name": "Winter Haven",
        "county": "Polk",
        "zip_sample": "33881",
        "lat": 28.0222, "lng": -81.7329,
        "tagline": "Chain of Lakes city, home of LEGOLAND and some of Central Florida's most affordable new homes.",
        "meta_desc": "New homes in Winter Haven, FL. Brightview Homes builds custom new construction on scattered lots in Polk County — Chain of Lakes, LEGOLAND, affordable pricing, growing I-4 corridor.",
        "hero_sub": "Winter Haven's Chain of Lakes gives it some of the best waterfront living in Central Florida at a fraction of Orange County prices — plus LEGOLAND, a working downtown, and major I-4 corridor growth.",
        "intro": "Winter Haven is anchored by the 25-lake Chain of Lakes and downtown's Central Park, a lakefront centerpiece that's driven the city's downtown revitalization. LEGOLAND Florida brings 2+ million visitors annually, feeding the service economy, and AdventHealth's growing Winter Haven campus has made healthcare a major employer. Brightview Homes builds scattered-lot homes here in the $350K–$500K range — some of the most competitive new-construction pricing in Central Florida.",
        "why_points": [
            "Chain of Lakes — 25 connected lakes with boating, waterfront living, and world-class bass fishing.",
            "LEGOLAND Florida resort — Winter Haven's biggest tourist and service-economy driver.",
            "AdventHealth Winter Haven — a growing regional medical center and top employer.",
            "Downtown Winter Haven on Lake Silver — new restaurants, craft breweries, and the historic Ritz Theater.",
            "Polk County's second-largest city, with strong commercial and residential growth momentum.",
        ],
        "neighborhoods": [
            {"name": "Downtown Winter Haven / Lake Silver", "desc": "Walkable downtown on Lake Silver with restaurants, breweries, and craftsman-era homes."},
            {"name": "Lake Eloise / LEGOLAND Area", "desc": "Established lakefront neighborhood adjacent to LEGOLAND and Cypress Gardens Adventure Park."},
            {"name": "Cypress Gardens", "desc": "Historic community around the original Cypress Gardens theme park — mature oaks and lake access."},
            {"name": "Lake Alfred / US-17", "desc": "Growing residential corridor north of Winter Haven along US-17."},
        ],
        "commute": "Winter Haven sits just south of I-4, giving 50-minute access to downtown Orlando and 45 minutes to Tampa. Disney is 40 minutes north, Orlando International Airport is 55 minutes northeast, and Tampa International Airport is 60 minutes west.",
        "schools": "Polk County Public Schools — Winter Haven High School, Lake Region High School, and Winter Haven Senior Ninth Grade Center serve the city. Chain of Lakes Collegiate High School is a popular dual-enrollment option.",
        "featured_plans": ["cambria", "tribeca", "legacy", "valencia"],
    },
]

PLAN_DISPLAY = {
    "cambria":    "Cambria — 4BR/2BA/1,665 sf",
    "tribeca":    "Tribeca — 3BR/2BA/1,665 sf",
    "legacy":     "Legacy — 4BR/2BA/1,805 sf",
    "hudson":     "Hudson — 3BR/2.5BA/1,821 sf",
    "valencia":   "Valencia — 4BR/2.5BA/1,920 sf",
    "brighton":   "Brighton — 4BR/2.5BA/2,069 sf",
    "kensington": "Kensington — 4BR/3BA/2,112 sf",
    "belmont":    "Belmont — 4BR/3BA/2,307 sf",
    "astoria":    "Astoria — 4BR/3.5BA/2,551 sf",
    "stephanie":  "Stephanie Estate — 4BR/3.5BA/3,479 sf",
}


def build_faqs(city):
    """Return list of (question, answer) tuples for this city."""
    name = city["name"]
    county = city["county"]
    return [
        (
            f"Does Brightview Homes build new homes in {name}, FL?",
            f"Yes. Brightview builds scatter-lot new construction homes in {name} and throughout {county} County. Whether you already own a lot or want us to find one, we build one of our 10 floor plans on an individual parcel rather than inside a master-planned subdivision — which is how you get new construction in established {name} neighborhoods.",
        ),
        (
            f"How much does it cost to build a new home in {name}?",
            f"Brightview base pricing starts at $269,990 for our Cambria and Tribeca plans (1,665 sq ft) and goes to $559,990 for the 3,479 sq ft Stephanie Estate — all before lot cost and selections. {name} lot pricing and {county} County impact fees affect the all-in price. We'll give you an itemized, transparent quote specific to the lot and plan at consultation.",
        ),
        (
            f"Does Brightview have available lots in {name} right now?",
            f"Lot availability in {name} changes weekly. Some lots we've acquired are under contract and available for a Brightview build; others are listed through our brokerage (LPT Realty). If you don't see active inventory, we also help you find and evaluate open-market lots in {name} and throughout {county} County. Call (321) 310-2849 or email through the contact form for current availability.",
        ),
        (
            f"How long does permitting take in {county} County?",
            f"Permitting in {county} County typically takes 6–12 weeks from application submission to issued permit, depending on complexity (standard infill vs. wetlands, flood zone, or HOA architectural review). Brightview handles the full permit process — including impact fees, tap fees, and inspections — so you don't navigate the county on your own.",
        ),
        (
            f"Which Brightview floor plans work best in {name}?",
            f"Any of our 10 floor plans can be built on a {name} scatter lot, but the most popular choices for {county} County buyers are: " + ", ".join(PLAN_DISPLAY[pid].split(" — ")[0] for pid in city["featured_plans"]) + f". You can browse all 10 on our <a href='floor-plans.html'>floor plans page</a> or view the full architectural PDF for any plan.",
        ),
    ]


def render(city):
    slug = city["slug"]
    url = f"https://brightviewhomes.us/new-homes-{slug}.html"
    title = f"New Homes in {city['name']}, FL | Brightview Homes"
    meta = city["meta_desc"]

    jsonld = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "url": url,
        "name": title,
        "description": meta,
        "isPartOf": {"@type": "WebSite", "name": "Brightview Homes", "url": "https://brightviewhomes.us/"},
        "about": {
            "@type": "Place",
            "name": f"{city['name']}, Florida",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": city["name"],
                "addressRegion": "FL",
                "postalCode": city["zip_sample"],
                "addressCountry": "US",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": city["lat"], "longitude": city["lng"]},
        },
        "provider": {
            "@type": "HomeBuilder",
            "name": "Brightview Homes",
            "url": "https://brightviewhomes.us/",
            "telephone": "+1-321-310-2849",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "480 N Orlando Ave, Suite 236",
                "addressLocality": "Winter Park",
                "addressRegion": "FL",
                "postalCode": "32789",
                "addressCountry": "US",
            },
        },
    }

    bc_jsonld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://brightviewhomes.us/"},
            {"@type": "ListItem", "position": 2, "name": "Communities", "item": "https://brightviewhomes.us/communities.html"},
            {"@type": "ListItem", "position": 3, "name": f"New Homes in {city['name']}, FL", "item": url},
        ],
    }

    hl_items = "".join(f"<li>{html.escape(p)}</li>" for p in city["why_points"])
    nb_cards = "".join(
        f'<div class="card"><div class="card-eyebrow">Neighborhood</div><h4>{html.escape(n["name"])}</h4><p>{html.escape(n["desc"])}</p></div>'
        for n in city["neighborhoods"]
    )
    plan_cards = "".join(
        f'<div class="card"><div class="card-eyebrow">Floor plan</div><h4>{PLAN_DISPLAY[pid].split(" — ")[0]}</h4><p>{PLAN_DISPLAY[pid].split(" — ")[1]}</p><a href="{pid}.html">See the {PLAN_DISPLAY[pid].split(" — ")[0]} →</a></div>'
        for pid in city["featured_plans"]
    )

    faqs = build_faqs(city)
    faq_html = "".join(
        f'<details style="border-top:1px solid rgba(30,58,82,.12);padding:1.1rem 0"{" open" if i == 0 else ""}><summary style="font-family:var(--serif);font-size:20px;font-weight:500;color:var(--navy);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem">{q}<span style="color:var(--gold);font-size:20px">+</span></summary><p style="font-size:15px;color:var(--navy);line-height:1.75;margin-top:.9rem">{a}</p></details>'
        for i, (q, a) in enumerate(faqs)
    )
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a.replace("<a href='floor-plans.html'>", "").replace("</a>", ""))},
            }
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
<meta name="keywords" content="new homes {city['name']} FL, new home builder {city['name']}, custom home builder {city['name']}, new construction {city['name']}, {city['county']} County builder">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#1E3A52">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Brightview Homes">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(meta)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://brightviewhomes.us/logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{html.escape(meta)}">
<meta name="twitter:image" content="https://brightviewhomes.us/logo.png">
<link rel="icon" type="image/png" href="/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="bv-landing.css">
<script type="application/ld+json">{json.dumps(jsonld)}</script>
<script type="application/ld+json">{json.dumps(bc_jsonld)}</script>
<script type="application/ld+json">{json.dumps(faq_schema)}</script>
</head>
<body>

<nav class="bv-nav">
  <a href="index.html" class="nav-logo"><img src="logo-nav.png" alt="Brightview Homes"></a>
  <div class="nav-links">
    <a href="index.html">Home</a>
    <a href="floor-plans.html">Floor Plans</a>
    <a href="communities.html" class="active">Communities</a>
    <a href="available-lots.html">Lots</a>
    <a href="build-on-your-lot.html">Build On Your Lot</a>
  </div>
  <a href="https://brightviewhomes.us/contact/" class="nav-cta" target="_blank">Contact</a>
</nav>

<main>
  <section class="hero">
    <div class="hero-inner">
      <div class="eyebrow">New Homes in {city['name']}, Florida</div>
      <h1>Build a new home in {city['name']}, FL</h1>
      <p class="hero-sub">{html.escape(city['tagline'])} {html.escape(city['hero_sub'])}</p>
      <div class="hero-stats">
        <div><div class="hero-stat-val">10</div><div class="hero-stat-label">Floor Plans</div></div>
        <div><div class="hero-stat-val">$269K+</div><div class="hero-stat-label">Starting From</div></div>
        <div><div class="hero-stat-val">16</div><div class="hero-stat-label">FL Counties</div></div>
        <div><div class="hero-stat-val">{city['county']}</div><div class="hero-stat-label">County</div></div>
      </div>
    </div>
  </section>

  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a><span class="sep">›</span>
    <a href="communities.html">Communities</a><span class="sep">›</span>
    <span>New Homes in {city['name']}</span>
  </nav>

  <section class="section">
    <div class="section-inner">
      <div class="section-eyebrow">★ {city['name']}, FL overview</div>
      <h2>About building new in {city['name']}</h2>
      <p>{html.escape(city['intro'])}</p>
      <div class="btn-group">
        <a class="btn btn-primary" href="https://brightviewhomes.us/contact/?city={city['slug']}" target="_blank">Get a {city['name']} quote</a>
        <a class="btn btn-outline" href="floor-plans.html">Browse floor plans</a>
      </div>
    </div>
  </section>

  <section class="section alt">
    <div class="section-inner">
      <div class="section-eyebrow">★ Why build here</div>
      <h2>Why buyers are choosing {city['name']}</h2>
      <ul>{hl_items}</ul>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-eyebrow">★ Neighborhoods</div>
      <h2>{city['name']} neighborhoods we build in</h2>
      <p>Brightview builds on individual scattered lots across {city['name']}. If you already own land anywhere in {city['county']} County, we can build on it. If not, we regularly acquire lots in these neighborhoods:</p>
      <div class="grid-3">{nb_cards}</div>
    </div>
  </section>

  <section class="section alt">
    <div class="section-inner">
      <div class="section-eyebrow">★ Location &amp; commute</div>
      <h2>Getting around from {city['name']}</h2>
      <p>{html.escape(city['commute'])}</p>
      <h3>Schools</h3>
      <p>{html.escape(city['schools'])}</p>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-eyebrow">★ Recommended floor plans</div>
      <h2>Brightview plans that work well in {city['name']}</h2>
      <p>Every Brightview floor plan is available as a scatter-lot build in {city['name']}. These are the most popular plans our {city['county']} County buyers choose — but you can filter and compare all 10 plans on our <a href="floor-plans.html">floor plans page</a>.</p>
      <div class="grid-3">{plan_cards}</div>
    </div>
  </section>

  <section class="section alt">
    <div class="section-inner">
      <div class="section-eyebrow">★ {city['name']} FAQ</div>
      <h2>{city['name']} new-home questions</h2>
      <div style="max-width:820px">
        {faq_html}
      </div>
    </div>
  </section>

  <section class="cta-band">
    <h2>Ready to build in {city['name']}?</h2>
    <p>Scheduling a consultation takes 15 minutes. We'll walk through floor plans, lot options, and a realistic budget — no pressure.</p>
    <div class="btn-group" style="justify-content:center">
      <a class="btn btn-primary" href="https://brightviewhomes.us/contact/?city={city['slug']}" target="_blank">Schedule a consultation</a>
      <a class="btn btn-outline" href="tel:+13213102849">Call (321) 310-2849</a>
    </div>
  </section>
</main>

<footer>
  © Brightview Homes · <a href="index.html">Home</a> · <a href="floor-plans.html">Floor Plans</a> · <a href="communities.html">Communities</a> · <a href="available-lots.html">Lots</a> · <a href="https://brightviewhomes.us/contact/">Contact</a>
</footer>

</body>
</html>
"""


def main():
    for city in CITIES:
        out = ROOT / f"new-homes-{city['slug']}.html"
        out.write_text(render(city))
        print(f"  wrote {out.name}")
    print(f"Generated {len(CITIES)} city pages.")


if __name__ == "__main__":
    main()
