"""Hero scenes for the Texas site — layered-silhouette SVG, brand palette."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f5f1e8"/><stop offset="1" stop-color="#dfe6ee"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c="#e7c486"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".6"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def liveoak(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-6" y="-30" width="12" height="34" fill="#4a3728"/>'
            '<path d="M-60-30c-20-30 10-70 50-60 20-30 70-20 70 10 30 0 40 40 10 50-10 20-50 20-70 6-20 14-60 10-60-6z" fill="#4f6b3a"/></g>')
def bluebonnets(xs, y):
    return '<g>' + ''.join(f'<rect x="{x}" y="{y-14}" width="2" height="14" fill="#4f6b3a"/><ellipse cx="{x+1}" cy="{y-16}" rx="4" ry="7" fill="#3b4f9a"/>' for x in xs) + '</g>'
def star(cx, cy, r, fill="#e7c486"):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'

def hillcountry():
    return wrap(sun(1180, 116, 62)
        + '<path d="M0 250C200 220 380 250 560 232 760 214 940 246 1440 224V360H0Z" fill="#cfd8d3"/>'
        + '<path d="M0 290C260 262 520 296 780 276 1040 258 1240 292 1440 270V360H0Z" fill="#9db08a"/>'
        + ground(316, "#6f8f5a") + liveoak(300, 316, 1.1) + liveoak(1120, 314, .9)
        + bluebonnets(range(60, 1440, 22), 336))
def houston():
    b = '<g fill="#2b4b62">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
        [(420,180,40),(470,140,34),(514,100,50),(574,150,34),(616,80,44),(670,160,36),(716,120,58),(784,176,30),(824,128,40),(874,150,52),(936,190,36),(982,164,30)]) + '</g>'
    b += '<path d="M616 80l22-26 22 26z" fill="#2b4b62"/>'
    w = '<g fill="#e7c486" opacity=".7">' + ''.join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(526,120),(538,140),(628,110),(640,140),(728,140),(750,160),(836,150),(890,170),(552,180)]) + '</g>'
    return wrap(sun(1200, 100, 52) + '<path d="M0 262L1440 236V360H0Z" fill="#cfd8d3"/>' + b + w + ground(316, "#1d4f6e", ".95")
                + '<path d="M300 328c120-6 240 4 360-2 120-6 240 6 360 0" stroke="#e9f1f5" stroke-width="2" fill="none" opacity=".5"/>')
def dallas():
    b = '<g fill="#2b4b62">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
        [(480,170,40),(530,120,44),(584,150,34),(628,96,50),(690,166,36),(736,130,58),(804,176,30),(844,140,40),(894,160,52)]) + '</g>'
    b += '<rect x="410" y="150" width="8" height="210" fill="#2b4b62"/><circle cx="414" cy="140" r="26" fill="#2b4b62"/><circle cx="414" cy="140" r="18" fill="#e7c486" opacity=".55"/>'
    w = '<g fill="#e7c486" opacity=".7">' + ''.join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(540,140),(552,160),(640,120),(652,150),(748,150),(770,170),(856,160),(906,180)]) + '</g>'
    return wrap(sun(1190, 106, 54) + '<path d="M0 262L1440 236V360H0Z" fill="#cfd8d3"/>' + b + w + ground(318, "#6f8f5a") + liveoak(1200, 318, .9))
def alamo():
    a = ('<g fill="#c9b28a"><path d="M560 360V220h60v-40l40-30 40 30v40h60v140z"/><rect x="480" y="250" width="80" height="110"/><rect x="780" y="250" width="80" height="110"/></g>'
         '<g fill="#7a6142"><rect x="640" y="270" width="40" height="90" rx="20"/><rect x="600" y="240" width="18" height="26" rx="9"/><rect x="742" y="240" width="18" height="26" rx="9"/><rect x="654" y="200" width="12" height="18" rx="6"/></g>'
         '<path d="M620 180l40-30 40 30" stroke="#a89474" stroke-width="4" fill="none"/>')
    return wrap(sun(1180, 116, 60) + '<path d="M0 262L1440 240V360H0Z" fill="#cfd8d3"/>' + a + ground(340, "#9db08a") + liveoak(300, 340, 1.0) + liveoak(1120, 338, .8))
def capitol():
    dome = ('<g fill="#b98a7a"><rect x="560" y="230" width="320" height="130"/><rect x="640" y="176" width="160" height="60"/><path d="M640 180a80 80 0 0 1 160 0z"/>'
            '<rect x="714" y="126" width="12" height="50"/><rect x="470" y="264" width="90" height="96"/><rect x="880" y="264" width="90" height="96"/></g>'
            + star(720, 118, 12) + '<g fill="#e7c486" opacity=".5">' + ''.join(f'<rect x="{x}" y="256" width="10" height="26"/>' for x in range(584, 870, 30)) + '</g>')
    return wrap(sun(200, 110, 50) + '<path d="M0 270C300 250 600 268 1440 246V360H0Z" fill="#cfd8d3"/>' + dome + liveoak(320, 340, 1.0) + ground(330, "#6f8f5a"))
def gulf():
    pier = '<rect x="900" y="286" width="300" height="8" fill="#8a6a48"/>' + ''.join(f'<rect x="{x}" y="294" width="6" height="30" fill="#6a4e34"/>' for x in range(920, 1200, 50))
    pelican = '<g fill="#1c2630" transform="translate(600 150)"><path d="M0 0c20-14 60-14 80 0-10 6-70 6-80 0z"/><path d="M60-4c4-14 20-20 36-12l-10 6 4 8z"/></g>'
    return wrap(sun(1160, 112, 64) + '<path d="M0 262L1440 250V360H0Z" fill="#c9d6d9"/>' + ground(296, "#1d5f7e") + ground(312, "#2b7a9a", ".8")
                + '<path d="M0 330C300 322 600 340 900 330 1200 322 1350 336 1440 330V360H0Z" fill="#e8dcc0"/>' + pier + pelican)
def desert():
    yucca = lambda x, y: (f'<g transform="translate({x} {y})"><rect x="-3" y="-60" width="6" height="60" fill="#4f6b3a"/>'
                          '<path d="M0-30l-30-40M0-30l30-40M0-30l-40-18M0-30l40-18M0-30l-14-48M0-30l14-48" stroke="#4f6b3a" stroke-width="3"/><ellipse cx="0" cy="-82" rx="6" ry="16" fill="#e9e2d4"/></g>')
    return wrap(sun(1170, 110, 62, "#e7b07a") + '<path d="M0 250l200-90 160 60 220-110 200 80 180-60 200 70 280-40V360H0Z" fill="#a98b7a"/>'
                + '<path d="M0 300l260-60 220 30 240-50 300 40 420-30V360H0Z" fill="#7d6753"/>' + ground(330, "#c9a97a") + yucca(200, 330) + yucca(1180, 328))
def panhandle():
    wm = ('<g transform="translate(1100 330)" stroke="#5a4a3c" stroke-width="4" fill="none"><path d="M-20 0L0-120L20 0M-14-40h28"/>'
          '<g transform="translate(0 -128)"><circle r="22" fill="none"/><path d="M0-22V22M-22 0H22M-16-16L16 16M16-16L-16 16"/></g></g>')
    elev = '<g fill="#8a7a6a"><rect x="240" y="200" width="70" height="140"/><path d="M240 200h70l-35-30z"/><rect x="320" y="240" width="90" height="100"/></g>'
    return wrap(sun(700, 120, 66) + '<path d="M0 310L1440 300V360H0Z" fill="#c9a97a"/>' + ground(334, "#b8a76c") + wm + elev)
def pines():
    def pine(x, y, h, w, f="#2f5d4a"):
        step = h / 4; parts = ''.join(f"M{x} {y-h+i*step:.0f}l{w*(0.45+0.28*i):.0f} {step*1.35:.0f}h{-2*w*(0.45+0.28*i):.0f}z" for i in range(3))
        return f'<path d="{parts}" fill="{f}"/><rect x="{x-3}" y="{y-8}" width="6" height="12" fill="#3b2a1e"/>'
    return wrap(sun(1160, 120, 58) + '<path d="M0 262C300 240 700 270 1440 240V360H0Z" fill="#cfd8d3"/>'
                + ''.join(pine(x, 320, h, w) for x, h, w in [(120,110,30),(180,80,22),(420,100,28),(900,120,32),(960,84,24),(1280,104,28),(1340,70,20)])
                + ground(322, "#4f6b3a"))
def ranch():
    fence = ''.join(f'<rect x="{x}" y="296" width="6" height="40" fill="#5a4a3c"/>' for x in range(40, 1440, 90)) + '<rect x="0" y="306" width="1440" height="4" fill="#5a4a3c"/><rect x="0" y="322" width="1440" height="4" fill="#5a4a3c"/>'
    return wrap(sun(1170, 116, 60) + star(260, 110, 40, "#e7c486") + '<path d="M0 270C300 250 600 270 1440 250V360H0Z" fill="#9db08a"/>' + ground(330, "#6f8f5a") + fence + liveoak(760, 300, 1.0))

SCENES = {"hillcountry": hillcountry(), "houston": houston(), "dallas": dallas(), "alamo": alamo(), "capitol": capitol(),
          "gulf": gulf(), "desert": desert(), "panhandle": panhandle(), "pines": pines(), "ranch": ranch()}
