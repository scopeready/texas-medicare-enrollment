"""Texas topic pages, part B: turning 65, Winter Texans, veterans, Medicaid, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_TDI, SRC_HHS_MEDICARE, SRC_SHIP_TX, SRC_YTB, SRC_STARPLUS, SRC_TFL, SRC_VA)
SRC_MN_SNOW = ("Minnesota Medicare Enrollment (sister site): Medicare for Minnesota snowbirds", "https://minnesotamedicareenrollment.com/snowbirds")
SRC_AZ = ("Medicare Enrollment Arizona (sister site with Mesa and Sun City offices)", "https://www.medicareenrollmentarizona.com")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in Texas guide", crumb="Turning 65", scene="hillcountry",
     title="Turning 65 in Texas: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Texas: your 7-month enrollment window, the Medigap open enrollment that does not repeat, still-working rules, the deadlines with lifelong penalties, and a checklist. Free help from a licensed Texas agent.",
     llm="Turning 65 in Texas: enrollment windows, the parts of Medicare, the choice between Advantage and Medigap by county, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Texas: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Texas, where the right answer in Harris County is not always the right answer in Hale County.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In Texas it does not repeat: there is no birthday rule and no annual switching window.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Texas twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
<h2>1. Your enrollment window: the 7-month Initial Enrollment Period</h2>
<p>Your Initial Enrollment Period (IEP) is seven months long: the three months <em>before</em> the month you turn 65, your birthday month, and the three months <em>after</em>. Signing up in the three months before your birthday means coverage starts the first of your birthday month. You enroll through Social Security (online at ssa.gov, by phone, or at an office); if you already draw Social Security you are enrolled in A and B automatically.</p>
<ul>
<li><strong>Part A</strong> (hospital) is premium-free for most people, so most enroll when first eligible.</li>
<li><strong>Part B</strong> (medical) carries the $202.90 standard monthly premium in [[YEAR]] &mdash; and a timing decision if you are still working (see below).</li>
</ul>
<h2>2. The parts of Medicare, briefly</h2>
<ul>
<li><strong>Part A</strong> &mdash; inpatient hospital, skilled nursing, hospice.</li>
<li><strong>Part B</strong> &mdash; doctors, outpatient care, preventive services.</li>
<li><strong>Part C (Medicare Advantage)</strong> &mdash; a private all-in-one alternative that bundles A, B and usually drug coverage, sold by county.</li>
<li><strong>Part D</strong> &mdash; prescription drug coverage.</li>
<li><strong>Medigap</strong> &mdash; a supplement that pairs with A and B and works anywhere in the country.</li>
</ul>
<h2>3. Your big decision: two paths</h2>
<table class="ctable">
<caption>The two ways most Texans put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a county-based network that changes yearly.</td></tr>
</tbody></table>
<p>Where you live tilts the answer. In Houston, Dallas, San Antonio or Austin the Advantage menu is deep and the networks include most big systems. In the Panhandle, the Permian Basin, East Texas or the brush country the menu is short and got shorter for 2026, and a Medigap policy&rsquo;s any-provider access is often the practical choice. If MD Anderson, UT Southwestern or a Mayo referral is in your future, a supplement removes the network question entirely. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>.</p>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above, and in Texas it does not repeat. Our research site sets the two side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/texas">turning 65 in Texas</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no Texas insurer can turn you down or charge more for your health. Afterward, Texas insurers can use medical underwriting, and there is no birthday rule to fall back on.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. Texas&rsquo;s big employers &mdash; the state, the universities, the school districts, the health systems, the oil majors &mdash; generally qualify; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll. Teachers with TRS-Care have their own rules; ask us.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Find out how deep the Advantage menu is in your county, and whether it changed for [[YEAR]].</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if a specific institution is your care.</li>
<li>If you travel or winter elsewhere, read the <a href="/winter-texans">Winter Texans guide</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid, see <a href="/medicaid">STAR+PLUS</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help Texans sort through it every day &mdash; clearly, patiently, and at no cost to you. Texas HICAP (800-252-9240) offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in Texas?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel, budget and county. The Advantage menu is deep in the big metros and thin in much of rural Texas. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in Texas?", "Your county decides how many Advantage plans you can choose from, and the gap between Houston and a rural county is wider than in most states. Your Medigap open enrollment does not repeat in Texas, so using it well matters. And a large share of Texans reach 65 with TRICARE For Life or VA care, which changes the calculation.")],
     sources=[SRC_CMS, SRC_TDI, SRC_HHS_MEDICARE, SRC_SHIP_TX], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Texas"),

dict(slug="winter-texans", nav_title="Medicare for Winter Texans and traveling Texans", crumb="Winter Texans", scene="gulf",
     title="Medicare for Winter Texans &amp; Traveling Texans | ECOS Medicare Solutions",
     desc="Which Medicare plans work when you split the year between the Rio Grande Valley and Minnesota, or travel from Texas to see family: Medigap travels, most Advantage HMOs cover emergencies only, and residency decides your county.",
     llm="Medicare for Winter Texans (Valley and Coastal Bend visitors from the Midwest and Canada) and Texans who travel: which plans work out of area, residency rules, Part D away from home",
     eyebrow="Guide · Two homes, one plan", h1="Medicare for Winter Texans and Texans who travel",
     sub="Whether you come to the Valley from Minnesota each November or leave Lubbock for a grandchild in Denver each summer, the rule is the same: some plans follow you and some stop at the county line.",
     keyfacts=["A Medigap policy with Original Medicare works with any provider in the U.S. that accepts Medicare, in both states, all year. It is the simplest two-home coverage there is.",
               "Most Medicare Advantage HMOs cover only emergencies and urgent care outside their service area; some PPOs cover routine care out of network at higher cost; a few plans have a travel benefit. Read the Evidence of Coverage, not the brochure.",
               "Your plan is tied to the county of your permanent residence. Wintering away for five months does not change that; moving your legal residence does, and it opens a Special Enrollment Period.",
               "Roughly 100,000 Winter Texans spend the season in the Valley and along the coast. Our Minnesota site covers the same question from the other end; our Arizona site has offices in Mesa and Sun City."],
     body="""<p>Texas is both a snowbird destination and a state whose retirees travel. The Rio Grande Valley, the Coastal Bend and the Hill Country fill each winter with retirees from Minnesota, Iowa, Michigan, Illinois and Ontario, and every summer Texans head for cooler grandchildren in Colorado and New Mexico. The Medicare rules are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>Which plans travel</h2>
<table class="ctable">
<caption>How each plan type behaves once you are outside its service area. Emergencies are covered by every plan, everywhere in the U.S.</caption>
<thead><tr><th scope="col">Plan type</th><th scope="col">Routine care in the other state</th><th scope="col">What you pay there</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + Medigap</th><td>Any provider that accepts Medicare</td><td>Same as at home &mdash; the supplement pays its share anywhere</td></tr>
<tr><th scope="row">Medicare Advantage PPO</th><td>Out-of-network providers, if the plan allows</td><td>Higher out-of-network copays or coinsurance; check the plan&rsquo;s out-of-network maximum</td></tr>
<tr><th scope="row">Medicare Advantage HMO</th><td>Emergencies and urgent care only, on most plans</td><td>Routine care generally not covered out of area</td></tr>
<tr><th scope="row">Part D (standalone or built in)</th><td>National pharmacy networks; mail order</td><td>Preferred-pharmacy pricing may differ; check that a chain near your other home is preferred</td></tr>
</tbody></table>
<div class="note-box"><p><strong>A few Advantage plans offer a &ldquo;visitor&rdquo; or &ldquo;travel&rdquo; benefit</strong> that extends in-network coverage for up to six or twelve months away from home, and some national carriers let you use their network in other states. It is plan-specific and it changes. If a travel benefit is the reason you are choosing an Advantage plan, we get it in writing from the Evidence of Coverage before you enroll.</p></div>
<h2>If you are a Winter Texan</h2>
<p>Your plan comes from your home county in Minnesota, Michigan or wherever you file your taxes. A Medigap policy covers DHR Health, Valley Baptist or Christus Spohn the same way it covers your hospital at home. An Advantage HMO from home probably does not, beyond emergencies, and a Texas doctor who is out of network can bill you in full. If you are on an Advantage plan and spend five months here every year, the honest comparison is a Medigap policy from your home state or a PPO with a documented travel benefit. Our Minnesota site covers the same question from the other end: <a href="https://minnesotamedicareenrollment.com/snowbirds">Medicare for Minnesota snowbirds</a>.</p>
<h2>If you are a Texan who travels</h2>
<p>The same rules apply in reverse. A Medigap policy from Texas works at a hospital in Denver, Albuquerque or Branson. An Advantage HMO from Lubbock covers emergencies there and little else. If you keep a second place in Ruidoso or Red River, or spend summers with family out of state, price the plan on how it behaves <em>there</em>, not on the $0 premium at home.</p>
<h2>Residency: the rule that decides everything</h2>
<p>Medicare Advantage and Part D plans are sold by county, and you must live in the plan&rsquo;s service area &mdash; meaning your <em>permanent</em> residence. Wintering away for four or five months does not change that; most plans allow up to six months, and some up to twelve, out of area before they disenroll you. What does change it is moving your legal residence: registering to vote, licensing the car, filing as a Texas resident. That triggers a Special Enrollment Period, ends your old plan, and means choosing from the plans sold in your new county. A Medigap policy is different: once issued it stays in force wherever you live, though the premium may be re-rated to the new state.</p>
<h2>Becoming a Texas resident</h2>
<p>Texas has no state income tax, which is why a lot of Winter Texans eventually make the move permanent. When you do, you choose from the plans sold in your new county &mdash; and if you had a Medigap policy at home, you can usually keep it or replace it. Our agency is licensed in Texas, Minnesota, Arizona, Colorado and eleven other states, so we can move your coverage cleanly in either direction; the state-by-state switching rules are on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p>
<h2>Part D away from home</h2>
<p>Every Part D plan has a national pharmacy network, so filling a prescription in McAllen or Minneapolis is not a problem. Pricing can be: plans have <em>preferred</em> pharmacies where copays are lowest, and the H-E-B that is preferred here may not have a preferred counterpart up north. Mail order at 90-day supplies solves most of it. We check both ZIP codes when we compare plans.</p>""",
     faqs=[("I am a Winter Texan from Minnesota. Does my Medicare Advantage plan work in the Valley?", "For emergencies and urgent care, yes &mdash; every plan covers those anywhere in the U.S. For routine care, most HMOs do not; some PPOs cover out-of-network care at higher cost, and a few plans have a travel benefit. Read the Evidence of Coverage, and if travel is why you chose the plan, get the benefit in writing."),
           ("Does a Texas Medigap policy work in other states?", "Yes. A Medigap policy pays alongside Original Medicare with any provider in the country that accepts Medicare, with no network and no service area. It is the simplest travel coverage."),
           ("How long can I be out of state without losing my Advantage plan?", "It depends on the plan; most allow up to six months out of the service area, some up to twelve. Changing your legal residence ends the plan regardless of time, and gives you a Special Enrollment Period to pick a plan where you live now."),
           ("Can you help me if I become a Texas resident?", "Yes. Our agency is licensed in Texas and sixteen other states including Minnesota, Arizona and Colorado, so we help you move your coverage cleanly, including the Medigap switching rules that differ by state.")],
     sources=[SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_MN_SNOW, SRC_AZ], cta="Two homes? Let&rsquo;s make sure your plan covers both."),

dict(slug="veterans", nav_title="Medicare for Texas veterans and military retirees", crumb="Veterans", scene="ranch",
     title="Medicare for Texas Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (Houston, Dallas, San Antonio, Temple, El Paso) work with Medicare in Texas, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision. From a retired Air Force officer.",
     llm="Medicare for Texas veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, Texas VA systems and the bases around Fort Cavazos, JBSA and Fort Bliss",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for Texas veterans and military retirees",
     sub="Texas has the second-largest veteran population in the country. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "Texas VA care runs through the DeBakey VA in Houston, VA North Texas in Dallas, the South Texas VA in San Antonio, the Central Texas VA in Temple, the El Paso VA, the West Texas VA in Big Spring, the Amarillo VA and the Valley Coastal Bend system.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Texas is home to roughly 1.5 million veterans and the retiree communities of Fort Cavazos, Joint Base San Antonio, Fort Bliss, Sheppard, Dyess, Goodfellow and the naval air stations on the coast. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
<div class="twocol">
<div class="panel panel--good"><h3>TRICARE For Life (TFL)</h3>
<ul>
<li>Requires you to have Medicare <strong>Part A and Part B</strong>.</li>
<li>Pays <strong>secondary</strong> to Medicare &mdash; it wraps around Medicare like a supplement.</li>
<li>TFL pharmacy is <strong>creditable</strong>, so a separate Part D plan is usually unnecessary.</li>
<li>TFL can pair with a Medicare Advantage plan; because drug coverage already exists, an <strong>MA-only plan</strong> (Advantage without Part D) can add dental or vision without duplicating your Rx.</li>
<li>Because TFL already fills Medicare&rsquo;s gaps, a Medigap policy is usually unnecessary too.</li>
</ul></div>
<div class="panel panel--note"><h3>VA health care</h3>
<ul>
<li>Separate from Medicare &mdash; the two <strong>do not coordinate</strong> and don&rsquo;t disrupt each other.</li>
<li>Medicare doesn&rsquo;t pay at VA facilities; the VA doesn&rsquo;t cover Medicare cost-sharing.</li>
<li>VA medical is <strong>not creditable</strong> for Part B &mdash; enroll in Part B on time to avoid a lifelong penalty.</li>
<li>VA pharmacy <strong>is creditable</strong> for Part D, so you can rely on it for drug coverage.</li>
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; MD Anderson or Baylor with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Military hospitals after 65</h2>
<p>Brooke Army Medical Center, Darnall at Fort Cavazos and William Beaumont at Fort Bliss continue to see retirees on a space-available basis under TRICARE rules. Medicare does not pay there. Most Texas military retirees pair TFL with civilian care nearby, and we have pages for the three big retiree communities: <a href="/fort-cavazos">Fort Cavazos</a>, <a href="/joint-base-san-antonio">Joint Base San Antonio</a> and <a href="/fort-bliss">Fort Bliss</a>.</p>
<h2>Which Texas plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Texas Veterans Commission, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at Brooke Army Medical Center or the Houston VA?", "No. Medicare does not pay at military or VA facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Texas Medicaid: STAR+PLUS, Medicare Savings Programs, Extra Help", crumb="Texas Medicaid &amp; STAR+PLUS", scene="alamo",
     title="Medicare &amp; Texas Medicaid: STAR+PLUS, QMB, SLMB | ECOS Medicare Solutions",
     desc="How Medicare works with Texas Medicaid: STAR+PLUS for adults 65+, Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium, Extra Help, Dual Special Needs Plans, and where to apply (YourTexasBenefits.com).",
     llm="Medicare and Texas Medicaid (dual eligible): STAR+PLUS, Medicare Savings Programs (QMB/SLMB/QI) through HHSC, Extra Help, D-SNPs, applying at YourTexasBenefits.com",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Texas Medicaid: STAR+PLUS and the Medicare Savings Programs",
     sub="If you qualify for both Medicare and Texas Medicaid &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in Texas, and where to apply.",
     keyfacts=["Texas Medicaid is administered by the Texas Health and Human Services Commission (HHSC). Adults 65 and over and people with disabilities who qualify get their Medicaid benefits through the STAR+PLUS managed-care program.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. Income limits change each year; federal resource limits apply. Apply at YourTexasBenefits.com or through HHSC.",
               "Qualifying for a Medicare Savings Program or Medicaid automatically qualifies you for Extra Help with Part D costs.",
               "Dual Special Needs Plans (D-SNPs) are Advantage plans for people with both Medicare and Medicaid; they are a large part of the menu in the Valley, San Antonio and Houston. Free counseling: Texas HICAP, 800-252-9240."],
     body="""<p>Some Texans qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Texas Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medicaid works for seniors in Texas</h2>
<p>Texas Medicaid is administered by the <strong>Texas Health and Human Services Commission (HHSC)</strong>. Texas did not expand Medicaid, so for adults 65 and over eligibility is based on income and resources under the state&rsquo;s aged-and-disabled rules, and it is determined by HHSC &mdash; not by an insurance agency. You apply at <strong>YourTexasBenefits.com</strong>, by phone at 2-1-1, or at a local HHSC office. Once eligible, most seniors receive their Medicaid benefits through <strong>STAR+PLUS</strong>, a managed-care program in which a health plan coordinates Medicaid services, including long-term services and supports, while Medicare continues to pay first for medical care.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. Texas&rsquo;s income limits change each year and Texas uses the federal resource limits. You apply through HHSC, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Medicaid benefits intact. In Texas many D-SNPs are offered by the same companies that run STAR+PLUS plans, so the two sides can be aligned.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from Texas HICAP &mdash; the Health Information, Counseling and Advocacy Program, Texas&rsquo;s State Health Insurance Assistance Program &mdash; at 800-252-9240. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Medicaid benefits working alongside Medicare. Eligibility decisions rest with HHSC and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Texas Medicaid, the Texas Health and Human Services Commission, or the federal Medicare program.</p>""",
     faqs=[("What is STAR+PLUS?", "Texas&rsquo;s Medicaid managed-care program for adults 65 and over and people with disabilities. A health plan coordinates your Medicaid services, including long-term services and supports, while Medicare keeps paying first for your medical care. Many STAR+PLUS carriers also offer Dual Special Needs Plans on the Medicare side."),
           ("Who counts as dual eligible in Texas?", "People who qualify for both Medicare and Texas Medicaid. There are full and partial categories; eligibility is determined by HHSC and CMS, based on income and resources."),
           ("Can Texas Medicaid pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply at YourTexasBenefits.com; Texas HICAP (800-252-9240) can help."),
           ("Where do I apply for Medicaid if I am over 65?", "At YourTexasBenefits.com, by calling 2-1-1, or at a local HHSC benefits office. Texas did not expand Medicaid, so eligibility for seniors follows the aged-and-disabled rules.")],
     sources=[SRC_STARPLUS, SRC_YTB, SRC_HHS_MEDICARE, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Texas Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Texas", crumb="Chronic SNPs", scene="pines",
     title="Chronic SNPs (C-SNP) in Texas | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Texas: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Texas for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Texas",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by Texas county and is concentrated in the metros; a regular Advantage plan or a Medigap policy may still serve you better.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. Texas, with its high rates of diabetes and heart disease, has more C-SNPs than most states, mostly in the big metros.</p>
<h2>Conditions that can qualify</h2>
<p>Medicare defines the chronic conditions a C-SNP can serve. Common examples include:</p>
<ul>
<li>Diabetes mellitus</li>
<li>Chronic heart failure and certain cardiovascular disorders</li>
<li>Chronic lung disorders such as COPD</li>
<li>End-stage renal disease (ESRD) requiring dialysis</li>
<li>Certain other qualifying chronic conditions</li>
</ul>
<p>You generally need a provider to verify that you have the qualifying condition in order to enroll, and a diagnosis gives you a Special Enrollment Period to join one outside the normal windows.</p>
<h2>What a C-SNP usually offers</h2>
<ul>
<li><strong>Care coordination</strong> tailored to your condition, often including a care team or coordinator.</li>
<li><strong>A drug formulary</strong> built with your condition&rsquo;s medications in mind, plus included Part D coverage.</li>
<li><strong>Extra benefits</strong> that vary by plan, and frequently a $0 or low plan premium.</li>
</ul>
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your endocrinologist or cardiologist is in it applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Texas Medicaid.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Texas?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Texas", crumb="Institutional SNPs", scene="hillcountry",
     title="Institutional SNPs (I-SNP) in Texas | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Texas for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Texas Medicaid and STAR+PLUS.",
     llm="Institutional Special Needs Plans (I-SNP) in Texas for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Texas",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In Texas, many people in long-term care also qualify for Medicaid through STAR+PLUS; a D-SNP aligned with the STAR+PLUS plan may then be the better fit, and we compare the two."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul>
<li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li>
<li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment.</li>
</ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP aligned with STAR+PLUS</a> if Medicaid is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Texas Medicaid &amp; STAR+PLUS</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Texas county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with STAR+PLUS.")],
     sources=[SRC_MA_GOV, SRC_STARPLUS], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="hillcountry",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Texas agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Texas agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling land, a year of royalties, or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, how much of it is taxed, and the rules for teachers and other Texans outside Social Security.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Texas, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Texas. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Texas?", "The book covers Medicare and retirement decisions nationally. For Texas specifics &mdash; county-by-county Advantage menus, STAR+PLUS, TRICARE communities &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
