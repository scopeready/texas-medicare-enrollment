"""Texas site identity, home page, navigation. Tokens [[PHONE]] etc. are filled by generate.py."""
from datetime import date

TODAY = date(2026, 9, 4)
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#14365c"/>'
        '<polygon points="21,7 24.6,17.4 35.6,17.4 26.7,23.9 30.1,34.3 21,27.9 11.9,34.3 15.3,23.9 6.4,17.4 17.4,17.4" fill="#e7c486"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#14365c"/>'
           '<polygon points="21,7 24.6,17.4 35.6,17.4 26.7,23.9 30.1,34.3 21,27.9 11.9,34.3 15.3,23.9 6.4,17.4 17.4,17.4" fill="#e7c486"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://texasmedicareenrollment.com", domain="texasmedicareenrollment.com", name="Texas Medicare Enrollment",
    org="ECOS Medicare Solutions", state="Texas", abbr="TX", demonym="Texans",
    # TODO(Darin): swap for a Texas (512 / 713 / 214 / 210) number. The agency's main line keeps the site from launching with a dead phone.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # Texas requires... the producer licence number is shown beside Darin's name site-wide via the engine.
    state_license="2514981", state_license_label="TX License",
    web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer",
    plan_year=2026, iso=TODAY.isoformat(), reviewed=TODAY.strftime("%B %-d, %Y"),
    fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000"),
    network=[("Medicare Enrollment Arizona", "https://www.medicareenrollmentarizona.com"), ("Georgia Medicare Enrollment", "https://georgiamedicareenrollment.com"),
             ("Minnesota Medicare Enrollment", "https://minnesotamedicareenrollment.com"), ("Medicare Enrollment Nevada", "https://medicareenrollmentnevada.com"),
             ("Colorado Medicare Enrollment", "https://coloradomedicareenrollment.com"), ("Tennessee Medicare Quotes", "https://www.tennesseemedicarequotes.com"),
             ("Medicare Enrollment Utah", "https://medicareenrollmentutah.com"), ("Medicare Enrollment Florida", "https://medicareenrollmentflorida.com"), ("California Medicare Enrollment", "https://www.californiamedicareenrollment.com"),
             ("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"), ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")],
    sameas_org_extra=["https://howdoiapplyformedicare.com", "https://medicareadvantageanswers.com", "https://dentalinsurancetomorrow.com"],
    sameas_darin=["https://www.myecos360.com/darin-weidauer", "https://www.linkedin.com/in/darin-weidauer-3165a816b/", "https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ",
                  "https://www.medicareenrollmentarizona.com/about", "https://minnesotamedicareenrollment.com/about", "https://georgiamedicareenrollment.com/", "https://medicareenrollmentutah.com/about", "https://medicareenrollmentflorida.com/about", "https://www.californiamedicareenrollment.com/about", "https://www.mymedigaprate.com/about"],
    tpmo=("We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. "
          "Please contact Medicare.gov, 1-800-MEDICARE, or the Texas Health Information, Counseling and Advocacy Program (HICAP, Texas&rsquo;s State Health "
          "Insurance Assistance Program, 800-252-9240) to get information on all of your options."),
    not_affiliated="the State of Texas, the Texas Health and Human Services Commission, Texas Medicaid, or the Texas Department of Insurance",
    ship_name="Texas HICAP", ship_phone="800-252-9240",
    brand_tag="Plain-English Medicare help in Texas", theme_color="#14365c",
    footer_tagline="Plain-English Medicare guidance for Texas retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping Texas retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Houston and Dallas to El Paso and the Rio Grande Valley.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and Texas Medicaid dual eligibility",
                 "STAR+PLUS", "Medicare for military retirees", "Winter Texans"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "My plan left my county", "Medicare Advantage", "Medicare Supplement (Medigap)",
                      "Part D drug plan", "I'm a Winter Texan / I travel", "I have VA / TRICARE", "I have Medicaid too"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. A plan leaving your county opens a Special Enrollment Period.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across Texas',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/winter-texans">Winter Texans &amp; travel</a>', '<a href="/medicaid">Texas Medicaid, STAR+PLUS and Medicare Savings Programs</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="hillcountry", h1="Texas Medicare questions, answered plainly",
                  sub="The questions we hear most from Texans &mdash; about plans leaving rural counties, Medigap underwriting, MD Anderson and Mayo referrals, Winter Texans, TRICARE, and what any of this costs. Short answers, with links to the longer ones.",
                  title="Texas Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions Texans ask most: Advantage plans leaving counties, Medigap rules, under-65 Plan A, STAR+PLUS, Winter Texans, TRICARE and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for Texas retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from Houston, Dallas–Fort Worth, San Antonio and Austin to El Paso, the Panhandle and the Rio Grande Valley.",
    llm_facts=["Darin Weidauer holds Texas insurance license #2514981 (NPN 18580338).",
               "Texas uses the federal Medigap plan letters (A–N) and has no state birthday or anniversary rule; the Texas Department of Insurance regulates Medigap. Texas requires insurers to offer at least Plan A to people under 65 who are on Medicare because of a disability.",
               "About 2.3 million Texans, roughly half of the state's Medicare beneficiaries, are in Medicare Advantage for 2026. UnitedHealthcare and Humana withdrew plans from a number of rural Texas counties for the 2026 plan year, and Humana has announced further reductions for 2027.",
               "Texas's SHIP is the Health Information, Counseling and Advocacy Program (HICAP), run by Texas Health and Human Services with the Area Agencies on Aging: 800-252-9240.",
               "Texas Medicaid is administered by the Texas Health and Human Services Commission (HHSC); adults 65+ and people with disabilities who qualify are served through the STAR+PLUS managed-care program. Apply at YourTexasBenefits.com. Medicare Savings Programs (QMB, SLMB, QI) are also handled by HHSC and automatically qualify the enrollee for Part D Extra Help.",
               "Texas has the second-largest veteran population in the country, with major Medicare-age military communities around Fort Cavazos (Killeen), Joint Base San Antonio and Fort Bliss (El Paso).",
               "The Rio Grande Valley and Coastal Bend host roughly 100,000 Winter Texans each year; a Medigap policy works in both states, most Advantage HMOs cover only emergencies out of area."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/winter-texans", "Winter Texans"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in Texas</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/winter-texans">Winter Texans &amp; travel</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">Texas Medicaid &amp; STAR+PLUS</a>',
                   '<a href="/faq">Questions Texans ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://www.hhs.texas.gov/services/health/medicare" rel="noopener">Texas HICAP (SHIP)</a>, 800-252-9240',
                                    '<a href="https://www.tdi.texas.gov" rel="noopener">Texas Department of Insurance</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a local network &mdash; so your providers, your county and your prescriptions matter.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider nationwide that accepts Medicare &mdash; MD Anderson, Mayo, or a clinic in the Valley.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Texas Medicaid.", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="hillcountry", title="Medicare Help in Texas [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for Texans: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, from Houston to El Paso.",
    eyebrow="Medicare made clear · Statewide in Texas",
    h1="Medicare in Texas, explained by someone who actually teaches it.",
    sub="Turning 65, retiring, or re-shopping because your plan pulled out of your county? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in Texas &middot; TX License #2514981 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="Texas is different", different_h2="Three things about Medicare in Texas that the national websites gloss over",
    different_lede="Texas has 254 counties, half its Medicare population in Advantage plans, and some of the widest gaps in the country between what is sold in Houston and what is sold in Hereford. Start with what is actually for sale where you live.",
    different_cards=[
        ("Your county decides your menu", "Harris County has dozens of Advantage plans; a Panhandle or Big Bend county may have two, and for 2026 UnitedHealthcare and Humana pulled out of a number of rural counties. A plan leaving your county opens a Special Enrollment Period and, often, a guaranteed-issue right to Medigap.", "/medicare-advantage", "What a non-renewal notice gives you"),
        ("The big names contract selectively", "MD Anderson, Mayo referrals, UT Southwestern, Texas Children&rsquo;s adult programs &mdash; each takes Original Medicare and contracts with some Advantage plans, not all. If a specific institution is your care, that decides the plan type before price does.", "/medicare-supplement", "When a supplement is the safer path"),
        ("Two million military families", "Texas is home to Fort Cavazos, Joint Base San Antonio and Fort Bliss. TRICARE For Life and VA care each work with Medicare differently, and the Part B timing mistake is expensive and permanent.", "/veterans", "Veterans &amp; Medicare"),
    ],
    options_h2="Four ways Texans get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your travel. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you spend the year. These are the situations Texans ask us about most.",
    situations=[
        ("Winter Texans &amp; travelers", "Which plans work when you split the year between the Valley and Minnesota, or drive to a grandchild in Denver.", "/winter-texans", "Medicare for Winter Texans"),
        ("My plan left my county", "The 2026 carrier exits hit rural Texas hardest. What a discontinuation notice gives you, and the deadline that comes with it.", "/medicare-advantage", "What to do next"),
        ("Veterans &amp; military retirees", "TRICARE For Life, VA care &mdash; Houston, Dallas, San Antonio, Temple, El Paso &mdash; and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Texas Medicaid", "STAR+PLUS, the Medicare Savings Programs that pay your Part B premium, and Dual Special Needs Plans that coordinate both.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the Texas-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer (TX License #2514981) is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Texas retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with Texans by phone and video across all 254 counties. Find Medicare guidance for your city:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("My Medicare Advantage plan is leaving my Texas county. What do I do?", "You are not alone: for the 2026 plan year UnitedHealthcare and Humana withdrew from a number of rural Texas counties, and Humana has announced more reductions for 2027. A non-renewal notice gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending. Call before the deadline on the notice."),
        ("When can I enroll in or change my Medicare plan in Texas?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving counties, losing a plan, or qualifying for Medicaid opens a Special Enrollment Period."),
        ("Does MD Anderson take Medicare Advantage?", "MD Anderson accepts Original Medicare, and therefore any Medigap policy. It contracts with some Medicare Advantage plans and not others, and the list changes each year. If MD Anderson &mdash; or UT Southwestern, Houston Methodist, or a Mayo referral &mdash; is your care, we confirm the plan&rsquo;s status in writing before you enroll."),
        ("I have VA or TRICARE benefits. Do I still need Medicare?", "Often, yes. VA health care and Medicare do not coordinate with each other, and TRICARE For Life requires you to have Medicare Parts A and B. Enrolling in Part B on time matters even with VA care, because VA medical coverage is not creditable for Part B and the late penalty lasts for life. Our Veterans page explains how these benefits fit together."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in Texas, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and Texas HICAP (800-252-9240) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your travel together.",
)

OG = dict(line1="Medicare help in", line2="Texas", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="texasmedicareenrollment.com", mark="star5",
          palette=dict(primary=(20, 54, 92), dark=(13, 37, 64), gold=(231, 196, 134), paper=(245, 241, 232), sky=(223, 230, 238),
                       far=(207, 216, 211), mid=(157, 176, 138), green=(79, 107, 58)))
