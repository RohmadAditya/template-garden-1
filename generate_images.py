import os

os.makedirs('assets/images', exist_ok=True)

# Helper for SVG generation
def save_svg(filename, content):
    path = os.path.join('assets/images', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Created {path}")

# 1. Hero Garden
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
  <defs>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#bae6fd"/>
      <stop offset="60%" stop-color="#e0f2fe"/>
      <stop offset="100%" stop-color="#fef3c7"/>
    </linearGradient>
    <linearGradient id="grassGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="40%" stop-color="#22c55e"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
    <linearGradient id="wallGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="woodGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="stoneGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Sky & Sun -->
  <rect width="1200" height="800" fill="url(#skyGrad)"/>
  <circle cx="950" cy="180" r="85" fill="#fef08a" opacity="0.85"/>
  <circle cx="950" cy="180" r="110" fill="#fef08a" opacity="0.3"/>

  <!-- Modern House Background -->
  <rect x="0" y="160" width="850" height="420" fill="url(#wallGrad)"/>
  <!-- Glass Window Panels -->
  <rect x="80" y="220" width="280" height="340" fill="#0284c7" opacity="0.35"/>
  <rect x="85" y="225" width="130" height="330" fill="#38bdf8" opacity="0.4"/>
  <line x1="220" y1="220" x2="220" y2="560" stroke="#0f172a" stroke-width="4"/>
  <!-- Wood Accent Wall Panel -->
  <rect x="420" y="200" width="380" height="360" fill="url(#woodGrad)"/>
  <line x1="420" y1="260" x2="800" y2="260" stroke="#451a03" stroke-width="2"/>
  <line x1="420" y1="320" x2="800" y2="320" stroke="#451a03" stroke-width="2"/>
  <line x1="420" y1="380" x2="800" y2="380" stroke="#451a03" stroke-width="2"/>
  <line x1="420" y1="440" x2="800" y2="440" stroke="#451a03" stroke-width="2"/>
  <line x1="420" y1="500" x2="800" y2="500" stroke="#451a03" stroke-width="2"/>

  <!-- Lush Green Lawn Foreground -->
  <path d="M0,520 Q450,500 800,530 T1200,510 L1200,800 L0,800 Z" fill="url(#grassGrad)"/>

  <!-- Stepping Stones (Andesite Path) -->
  <g filter="url(#shadow)">
    <ellipse cx="260" cy="620" rx="90" ry="28" fill="url(#stoneGrad)"/>
    <ellipse cx="440" cy="660" rx="100" ry="32" fill="url(#stoneGrad)"/>
    <ellipse cx="640" cy="640" rx="95" ry="30" fill="url(#stoneGrad)"/>
    <ellipse cx="840" cy="670" rx="105" ry="34" fill="url(#stoneGrad)"/>
    <ellipse cx="1040" cy="650" rx="90" ry="28" fill="url(#stoneGrad)"/>
  </g>

  <!-- White Coral Stones Border -->
  <g fill="#f8fafc" opacity="0.95">
    <ellipse cx="140" cy="550" rx="12" ry="7"/>
    <ellipse cx="170" cy="555" rx="15" ry="8"/>
    <ellipse cx="200" cy="552" rx="11" ry="6"/>
    <ellipse cx="230" cy="558" rx="14" ry="7"/>
    <ellipse cx="320" cy="580" rx="16" ry="9"/>
    <ellipse cx="350" cy="585" rx="13" ry="7"/>
    <ellipse cx="560" cy="590" rx="18" ry="9"/>
    <ellipse cx="590" cy="595" rx="14" ry="7"/>
    <ellipse cx="740" cy="590" rx="15" ry="8"/>
    <ellipse cx="770" cy="585" rx="12" ry="6"/>
  </g>

  <!-- Big Ornamental Frangipani / Kamboja Fosil Tree (Right) -->
  <g filter="url(#shadow)">
    <!-- Tree Trunk -->
    <path d="M960,680 Q930,550 900,450 Q960,380 940,280 Q990,320 1020,400 Q1060,530 1040,680 Z" fill="#78350f"/>
    <path d="M900,450 Q820,380 780,320 Q830,350 880,420 Z" fill="#78350f"/>
    <path d="M940,360 Q960,260 990,200 Q980,280 950,350 Z" fill="#78350f"/>

    <!-- Foliage / Green Clusters -->
    <ellipse cx="780" cy="300" rx="75" ry="50" fill="#15803d"/>
    <ellipse cx="760" cy="280" rx="65" ry="45" fill="#22c55e"/>
    <ellipse cx="980" cy="190" rx="90" ry="60" fill="#15803d"/>
    <ellipse cx="970" cy="170" rx="75" ry="50" fill="#4ade80"/>
    <ellipse cx="910" cy="260" rx="80" ry="55" fill="#166534"/>
    <ellipse cx="920" cy="240" rx="70" ry="45" fill="#22c55e"/>

    <!-- White Plumeria Flowers with Yellow Centers -->
    <g transform="translate(760,280)">
      <circle cx="0" cy="0" r="16" fill="#ffffff"/>
      <circle cx="0" cy="0" r="6" fill="#facc15"/>
    </g>
    <g transform="translate(940,210)">
      <circle cx="0" cy="0" r="18" fill="#ffffff"/>
      <circle cx="0" cy="0" r="7" fill="#facc15"/>
    </g>
    <g transform="translate(1010,230)">
      <circle cx="0" cy="0" r="15" fill="#ffffff"/>
      <circle cx="0" cy="0" r="5" fill="#facc15"/>
    </g>
  </g>

  <!-- Left Side Cycas & Tropical Shrubs -->
  <g>
    <path d="M40,640 Q80,560 140,540 Q100,580 80,660 Z" fill="#166534"/>
    <path d="M60,650 Q110,580 180,570 Q130,610 90,670 Z" fill="#22c55e"/>
    <path d="M20,660 Q60,590 120,590 Q80,630 50,680 Z" fill="#15803d"/>
    <path d="M90,670 Q140,600 210,610 Q160,640 120,690 Z" fill="#4ade80"/>
  </g>

  <!-- Garden Spotlights with Warm Light Glow -->
  <g>
    <path d="M720,680 L760,540 L840,570 Z" fill="#fef08a" opacity="0.35"/>
    <rect x="715" y="675" width="16" height="24" rx="4" fill="#0f172a"/>
    <circle cx="723" cy="680" r="6" fill="#facc15"/>
  </g>

  <!-- Tag / Watermark -->
  <rect x="40" y="40" width="220" height="48" rx="24" fill="#0f172a" opacity="0.85"/>
  <text x="150" y="70" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="16" fill="#ffffff" text-anchor="middle">NusaGarden Landscape</text>
</svg>'''
save_svg('hero-garden.svg', hero_svg)

# 2. Service Minimalis
service_min_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="minBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="100%" stop-color="#d1fae5"/>
    </linearGradient>
    <linearGradient id="grass1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#22c55e"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#minBg)"/>
  <!-- Minimalist Clean Wall -->
  <rect x="0" y="80" width="800" height="300" fill="#f8fafc"/>
  <rect x="100" y="130" width="220" height="200" fill="#0284c7" opacity="0.25" rx="8"/>
  <rect x="360" y="110" width="400" height="240" fill="#e2e8f0" rx="8"/>

  <!-- Grass Ground -->
  <rect x="0" y="380" width="800" height="220" fill="url(#grass1)"/>
  
  <!-- Stepping Stones -->
  <rect x="240" y="440" width="140" height="50" rx="8" fill="#64748b"/>
  <rect x="420" y="480" width="150" height="55" rx="8" fill="#475569"/>
  <rect x="180" y="520" width="160" height="50" rx="8" fill="#64748b"/>

  <!-- White Coral Stones Border -->
  <g fill="#ffffff" opacity="0.9">
    <ellipse cx="80" cy="400" rx="20" ry="10"/>
    <ellipse cx="120" cy="405" rx="18" ry="9"/>
    <ellipse cx="160" cy="402" rx="22" ry="11"/>
    <ellipse cx="640" cy="410" rx="24" ry="12"/>
    <ellipse cx="680" cy="408" rx="20" ry="10"/>
    <ellipse cx="720" cy="412" rx="22" ry="11"/>
  </g>

  <!-- Architectural Plants (Sikas & Snake Plants) -->
  <path d="M120,480 Q100,320 60,260 Q120,320 140,480 Z" fill="#166534"/>
  <path d="M140,480 Q140,280 130,220 Q160,290 150,480 Z" fill="#22c55e"/>
  <path d="M150,480 Q180,310 220,250 Q170,330 160,480 Z" fill="#15803d"/>

  <path d="M680,480 Q660,340 630,280 Q680,330 690,480 Z" fill="#166534"/>
  <path d="M690,480 Q710,310 740,240 Q710,320 700,480 Z" fill="#22c55e"/>

  <rect x="30" y="30" width="220" height="40" rx="20" fill="#1b4332"/>
  <text x="140" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" text-anchor="middle">Taman Minimalis Modern</text>
</svg>'''
save_svg('service-minimalis.svg', service_min_svg)

# 3. Service Kering / Zen
service_kering_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="zenSand" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
  </defs>
  <!-- Background Wall (Japanese Wood Slat Style) -->
  <rect width="800" height="600" fill="#f1f5f9"/>
  <rect x="0" y="0" width="800" height="320" fill="#334155"/>
  <g stroke="#1e293b" stroke-width="4">
    <line x1="80" y1="0" x2="80" y2="320"/>
    <line x1="160" y1="0" x2="160" y2="320"/>
    <line x1="240" y1="0" x2="240" y2="320"/>
    <line x1="320" y1="0" x2="320" y2="320"/>
    <line x1="400" y1="0" x2="400" y2="320"/>
    <line x1="480" y1="0" x2="480" y2="320"/>
    <line x1="560" y1="0" x2="560" y2="320"/>
    <line x1="640" y1="0" x2="640" y2="320"/>
    <line x1="720" y1="0" x2="720" y2="320"/>
  </g>

  <!-- Zen Raked Sand Floor -->
  <rect x="0" y="320" width="800" height="280" fill="url(#zenSand)"/>
  <!-- Concentric Raked Sand Ripples -->
  <g stroke="#cbd5e1" stroke-width="3" fill="none">
    <ellipse cx="480" cy="460" rx="140" ry="40"/>
    <ellipse cx="480" cy="460" rx="180" ry="55"/>
    <ellipse cx="480" cy="460" rx="220" ry="70"/>
    <ellipse cx="480" cy="460" rx="260" ry="85"/>
  </g>

  <!-- Large Zen Rocks / Andesite Boulder -->
  <ellipse cx="480" cy="455" rx="70" ry="45" fill="#475569"/>
  <ellipse cx="440" cy="445" rx="45" ry="35" fill="#64748b"/>
  <ellipse cx="525" cy="460" rx="35" ry="25" fill="#334155"/>

  <!-- Japanese Stone Lantern (Kasuga Toro) on Left -->
  <g transform="translate(180, 260)">
    <rect x="-15" y="100" width="30" height="80" fill="#64748b"/>
    <polygon points="-30,100 30,100 20,80 -20,80" fill="#475569"/>
    <!-- Light Box -->
    <rect x="-18" y="55" width="36" height="25" fill="#fef08a"/>
    <!-- Roof -->
    <polygon points="-45,55 45,55 0,30" fill="#334155"/>
    <circle cx="0" cy="22" r="8" fill="#475569"/>
  </g>

  <!-- Bonsai Tree -->
  <g transform="translate(560, 260)">
    <path d="M0,120 Q-20,70 10,40 Q-30,20 -20,-10 Q10,10 20,50 Q40,90 20,120 Z" fill="#78350f"/>
    <ellipse cx="-20" cy="-10" rx="45" ry="25" fill="#15803d"/>
    <ellipse cx="-25" cy="-20" rx="35" ry="20" fill="#22c55e"/>
    <ellipse cx="25" cy="15" rx="40" ry="22" fill="#15803d"/>
    <ellipse cx="20" cy="5" rx="32" ry="18" fill="#4ade80"/>
  </g>

  <rect x="30" y="30" width="220" height="40" rx="20" fill="#1b4332"/>
  <text x="140" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" text-anchor="middle">Taman Kering (Zen)</text>
</svg>'''
save_svg('service-kering.svg', service_kering_svg)

# 4. Service Vertical Garden
service_vertical_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="wallBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#wallBg)"/>
  
  <!-- Vertical Grid Wall Structure -->
  <rect x="80" y="60" width="640" height="480" fill="#334155" rx="12"/>
  
  <!-- Rows of Dense Lush Green Foliage -->
  <!-- Layer 1: Dark Green Base -->
  <g fill="#166534">
    <ellipse cx="160" cy="120" rx="60" ry="40"/>
    <ellipse cx="280" cy="130" rx="70" ry="45"/>
    <ellipse cx="400" cy="115" rx="65" ry="40"/>
    <ellipse cx="520" cy="125" rx="75" ry="45"/>
    <ellipse cx="640" cy="120" rx="60" ry="40"/>

    <ellipse cx="140" cy="220" rx="65" ry="45"/>
    <ellipse cx="260" cy="230" rx="75" ry="45"/>
    <ellipse cx="380" cy="215" rx="70" ry="40"/>
    <ellipse cx="500" cy="225" rx="80" ry="50"/>
    <ellipse cx="620" cy="220" rx="65" ry="45"/>

    <ellipse cx="160" cy="330" rx="70" ry="45"/>
    <ellipse cx="280" cy="340" rx="80" ry="50"/>
    <ellipse cx="400" cy="325" rx="75" ry="45"/>
    <ellipse cx="520" cy="335" rx="85" ry="50"/>
    <ellipse cx="640" cy="330" rx="70" ry="45"/>

    <ellipse cx="150" cy="440" rx="75" ry="50"/>
    <ellipse cx="270" cy="450" rx="85" ry="55"/>
    <ellipse cx="390" cy="435" rx="80" ry="50"/>
    <ellipse cx="510" cy="445" rx="90" ry="55"/>
    <ellipse cx="630" cy="440" rx="75" ry="50"/>
  </g>

  <!-- Layer 2: Vibrant Bright Leaves (Lime & Emerald) -->
  <g fill="#22c55e">
    <ellipse cx="200" cy="140" rx="50" ry="35"/>
    <ellipse cx="340" cy="135" rx="55" ry="35"/>
    <ellipse cx="460" cy="145" rx="60" ry="40"/>
    <ellipse cx="580" cy="130" rx="50" ry="35"/>

    <ellipse cx="190" cy="245" rx="55" ry="38"/>
    <ellipse cx="320" cy="240" rx="60" ry="40"/>
    <ellipse cx="440" cy="250" rx="65" ry="42"/>
    <ellipse cx="570" cy="235" rx="55" ry="38"/>

    <ellipse cx="210" cy="355" rx="60" ry="40"/>
    <ellipse cx="340" cy="350" rx="65" ry="42"/>
    <ellipse cx="460" cy="360" rx="70" ry="45"/>
    <ellipse cx="590" cy="345" rx="60" ry="40"/>

    <ellipse cx="200" cy="465" rx="65" ry="45"/>
    <ellipse cx="330" cy="460" rx="70" ry="45"/>
    <ellipse cx="450" cy="470" rx="75" ry="48"/>
    <ellipse cx="580" cy="455" rx="65" ry="45"/>
  </g>

  <!-- Layer 3: Highlight Accents (Red & Variegated) -->
  <g fill="#f87171" opacity="0.85">
    <circle cx="270" cy="210" r="14"/>
    <circle cx="490" cy="190" r="16"/>
    <circle cx="360" cy="310" r="18"/>
    <circle cx="550" cy="410" r="16"/>
  </g>

  <!-- Irrigation Pipe Line -->
  <line x1="80" y1="530" x2="720" y2="530" stroke="#0ea5e9" stroke-width="4"/>

  <rect x="30" y="30" width="220" height="40" rx="20" fill="#1b4332"/>
  <text x="140" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" text-anchor="middle">Vertical Living Wall</text>
</svg>'''
save_svg('service-vertical.svg', service_vertical_svg)

# 5. Service Kolam Koi
service_kolam_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="pondWater" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="stoneWall" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <!-- Background Yard -->
  <rect width="800" height="600" fill="#22c55e"/>
  
  <!-- Andesite Waterfall Wall Behind -->
  <rect x="140" y="40" width="520" height="220" fill="url(#stoneWall)" rx="8"/>
  <!-- Waterfall Spout & Flow -->
  <rect x="340" y="140" width="120" height="15" fill="#0f172a"/>
  <path d="M340,155 L320,260 L480,260 L460,155 Z" fill="#bae6fd" opacity="0.8"/>
  <ellipse cx="400" cy="260" rx="80" ry="15" fill="#ffffff" opacity="0.6"/>

  <!-- Pond Body -->
  <rect x="100" y="240" width="600" height="320" rx="24" fill="#334155"/>
  <rect x="120" y="260" width="560" height="280" rx="16" fill="url(#pondWater)"/>

  <!-- Glass Front Rim Accent -->
  <rect x="120" y="520" width="560" height="20" fill="#7dd3fc" opacity="0.5"/>

  <!-- Swimming Koi Fish (Kohaku White & Red) -->
  <!-- Koi 1 -->
  <g transform="translate(300, 360) rotate(-25)">
    <path d="M0,0 Q35,-15 70,0 Q35,15 0,0 Z" fill="#ffffff"/>
    <circle cx="35" cy="-2" r="10" fill="#ef4444"/>
    <circle cx="50" cy="2" r="8" fill="#ef4444"/>
    <polygon points="70,0 95,-12 90,0 95,12" fill="#ffffff" opacity="0.8"/>
    <circle cx="12" cy="-4" r="2" fill="#0f172a"/>
  </g>
  <!-- Koi 2 -->
  <g transform="translate(480, 430) rotate(140)">
    <path d="M0,0 Q35,-15 70,0 Q35,15 0,0 Z" fill="#f97316"/>
    <circle cx="28" cy="2" r="10" fill="#000000"/>
    <polygon points="70,0 95,-12 90,0 95,12" fill="#fed7aa" opacity="0.8"/>
    <circle cx="12" cy="-4" r="2" fill="#ffffff"/>
  </g>
  <!-- Koi 3 -->
  <g transform="translate(240, 450) rotate(35)">
    <path d="M0,0 Q30,-12 60,0 Q30,12 0,0 Z" fill="#ffffff"/>
    <circle cx="24" cy="-2" r="9" fill="#ef4444"/>
    <polygon points="60,0 80,-10 75,0 80,10" fill="#ffffff" opacity="0.8"/>
  </g>

  <!-- Water Lily Leaves -->
  <ellipse cx="580" cy="320" rx="35" ry="18" fill="#15803d"/>
  <path d="M580,320 L610,315 L595,335 Z" fill="url(#pondWater)"/>
  <circle cx="585" cy="315" r="8" fill="#f472b6"/>

  <rect x="30" y="30" width="220" height="40" rx="20" fill="#1b4332"/>
  <text x="140" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" text-anchor="middle">Kolam Koi & Waterfall</text>
</svg>'''
save_svg('service-kolam.svg', service_kolam_svg)

# 6. Service Tropis
service_tropis_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="tropSky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#fef3c7"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#tropSky)"/>
  <rect x="0" y="420" width="800" height="180" fill="#15803d"/>

  <!-- Balinese Stone Relief Wall -->
  <rect x="180" y="240" width="440" height="200" fill="#78350f" opacity="0.3" rx="8"/>

  <!-- Palm Tree & Heliconia (Banana Leaves) -->
  <g>
    <!-- Trunk -->
    <path d="M120,520 Q140,300 200,160" stroke="#78350f" stroke-width="24" fill="none"/>
    <!-- Palm Fronds -->
    <path d="M200,160 Q100,120 40,160" stroke="#16a34a" stroke-width="10" fill="none"/>
    <path d="M200,160 Q140,80 80,80" stroke="#22c55e" stroke-width="10" fill="none"/>
    <path d="M200,160 Q220,60 260,80" stroke="#15803d" stroke-width="10" fill="none"/>
    <path d="M200,160 Q280,100 340,140" stroke="#22c55e" stroke-width="10" fill="none"/>
    <path d="M200,160 Q260,180 320,220" stroke="#16a34a" stroke-width="10" fill="none"/>
  </g>

  <!-- Big Heliconia Leaves (Center & Right) -->
  <g fill="#166534">
    <ellipse cx="440" cy="380" rx="40" ry="120" transform="rotate(-25 440 380)"/>
    <ellipse cx="520" cy="370" rx="45" ry="130" transform="rotate(15 520 370)"/>
    <ellipse cx="600" cy="400" rx="35" ry="110" transform="rotate(35 600 400)"/>
  </g>
  <g fill="#22c55e">
    <ellipse cx="410" cy="400" rx="35" ry="100" transform="rotate(-35 410 400)"/>
    <ellipse cx="480" cy="390" rx="40" ry="110" transform="rotate(5 480 390)"/>
    <ellipse cx="560" cy="410" rx="35" ry="100" transform="rotate(25 560 410)"/>
  </g>

  <!-- Red Tropical Bird of Paradise Flower -->
  <g transform="translate(480, 310)">
    <path d="M0,0 Q20,-30 40,-40 Q30,-20 0,0 Z" fill="#ef4444"/>
    <path d="M0,0 Q10,-35 25,-55 Q15,-25 0,0 Z" fill="#f97316"/>
    <path d="M0,0 Q0,-40 5,-65 Q-5,-30 0,0 Z" fill="#eab308"/>
  </g>

  <rect x="30" y="30" width="220" height="40" rx="20" fill="#1b4332"/>
  <text x="140" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" text-anchor="middle">Taman Tropis Nuansa Bali</text>
</svg>'''
save_svg('service-tropis.svg', service_tropis_svg)

# 7. Service Perawatan
service_rawat_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="careBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f0fdf4"/>
      <stop offset="100%" stop-color="#bbf7d0"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#careBg)"/>
  
  <!-- Fresh Cut Lawn -->
  <rect x="0" y="440" width="800" height="160" fill="#16a34a"/>
  <!-- Alternating Lawn Stripes -->
  <rect x="100" y="440" width="100" height="160" fill="#15803d"/>
  <rect x="300" y="440" width="100" height="160" fill="#15803d"/>
  <rect x="500" y="440" width="100" height="160" fill="#15803d"/>
  <rect x="700" y="440" width="100" height="160" fill="#15803d"/>

  <!-- Gardening Tools (Shears & Watering Can) -->
  <!-- Watering Can -->
  <g transform="translate(480, 260)">
    <rect x="0" y="40" width="140" height="120" rx="16" fill="#0284c7"/>
    <!-- Handle -->
    <path d="M-20,50 Q-60,100 0,140" stroke="#0284c7" stroke-width="14" fill="none"/>
    <!-- Spout -->
    <path d="M130,120 L220,50" stroke="#0284c7" stroke-width="16" fill="none"/>
    <ellipse cx="230" cy="45" rx="15" ry="25" fill="#38bdf8"/>
    <!-- Water Drops -->
    <g fill="#38bdf8" opacity="0.8">
      <circle cx="260" cy="70" r="6"/>
      <circle cx="280" cy="100" r="5"/>
      <circle cx="270" cy="130" r="7"/>
      <circle cx="295" cy="150" r="6"/>
      <circle cx="285" cy="180" r="8"/>
    </g>
  </g>

  <!-- Potted Healthy Plant being pruned -->
  <g transform="translate(240, 220)">
    <ellipse cx="80" cy="220" rx="70" ry="25" fill="#b45309"/>
    <polygon points="20,220 40,320 120,320 140,220" fill="#d97706"/>
    <!-- Leaves -->
    <ellipse cx="80" cy="160" rx="55" ry="30" fill="#15803d"/>
    <ellipse cx="50" cy="120" rx="45" ry="25" fill="#22c55e"/>
    <ellipse cx="110" cy="110" rx="45" ry="25" fill="#16a34a"/>
    <ellipse cx="80" cy="70" rx="35" ry="20" fill="#4ade80"/>
  </g>

  <rect x="30" y="30" width="220" height="40" rx="20" fill="#1b4332"/>
  <text x="140" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" text-anchor="middle">Perawatan & Pemangkasan</text>
</svg>'''
save_svg('service-perawatan.svg', service_rawat_svg)

# 8. Before Garden (Messy, muddy, weeds)
before_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
  <rect width="1200" height="800" fill="#e2e8f0"/>
  <!-- Dull Grey Sky -->
  <rect width="1200" height="400" fill="#cbd5e1"/>
  <!-- Old Unfinished Brick Wall -->
  <rect x="0" y="240" width="1200" height="260" fill="#b45309" opacity="0.6"/>
  <!-- Broken ground / muddy dirt -->
  <rect x="0" y="460" width="1200" height="340" fill="#78350f"/>
  
  <!-- Mud puddles & gravel debris -->
  <ellipse cx="400" cy="620" rx="220" ry="60" fill="#451a03"/>
  <ellipse cx="850" cy="670" rx="180" ry="50" fill="#451a03"/>
  <!-- Scattered Rocks & Broken Bricks -->
  <rect x="220" y="540" width="60" height="30" fill="#991b1b" rx="4" transform="rotate(15 220 540)"/>
  <rect x="310" y="580" width="50" height="28" fill="#991b1b" rx="4" transform="rotate(-20 310 580)"/>
  <rect x="680" y="590" width="70" height="35" fill="#991b1b" rx="4" transform="rotate(8 680 590)"/>
  <rect x="760" y="550" width="55" height="30" fill="#94a3b8" rx="6"/>

  <!-- Wild Overgrown Yellowed Weeds -->
  <g stroke="#a16207" stroke-width="4">
    <line x1="120" y1="580" x2="100" y2="480"/>
    <line x1="130" y1="580" x2="140" y2="460"/>
    <line x1="140" y1="580" x2="160" y2="490"/>

    <line x1="550" y1="570" x2="530" y2="470"/>
    <line x1="560" y1="570" x2="570" y2="450"/>
    <line x1="570" y1="570" x2="600" y2="480"/>

    <line x1="1020" y1="600" x2="990" y2="500"/>
    <line x1="1030" y1="600" x2="1040" y2="470"/>
  </g>

  <!-- Stamp Badge -->
  <rect x="40" y="40" width="240" height="50" rx="8" fill="#991b1b"/>
  <text x="160" y="72" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="18" text-anchor="middle">KONDISI AWAL (SEBELUM)</text>
</svg>'''
save_svg('before-garden.svg', before_svg)

# 9. After Garden (Beautiful, lush, landscaped)
after_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
  <defs>
    <linearGradient id="afterSky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="60%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#fef08a"/>
    </linearGradient>
    <linearGradient id="afterGrass" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#afterSky)"/>
  <circle cx="1000" cy="150" r="70" fill="#fef08a" opacity="0.9"/>

  <!-- Modern White Clean Wall with Lighting -->
  <rect x="0" y="220" width="1200" height="260" fill="#f8fafc"/>
  <line x1="0" y1="220" x2="1200" y2="220" stroke="#0f172a" stroke-width="8"/>

  <!-- Spotlights on Wall -->
  <polygon points="300,220 220,380 380,380" fill="#fef08a" opacity="0.4"/>
  <polygon points="700,220 620,380 780,380" fill="#fef08a" opacity="0.4"/>
  <polygon points="1000,220 920,380 1080,380" fill="#fef08a" opacity="0.4"/>

  <!-- Manicured Grass Lawn -->
  <rect x="0" y="440" width="1200" height="360" fill="url(#afterGrass)"/>

  <!-- Stepping Stones Path -->
  <g fill="#475569">
    <ellipse cx="280" cy="540" rx="80" ry="25"/>
    <ellipse cx="440" cy="580" rx="90" ry="28"/>
    <ellipse cx="620" cy="550" rx="85" ry="26"/>
    <ellipse cx="800" cy="600" rx="95" ry="30"/>
    <ellipse cx="980" cy="570" rx="85" ry="26"/>
  </g>

  <!-- Big Ornamental Kamboja & Palms -->
  <g>
    <ellipse cx="180" cy="360" rx="90" ry="55" fill="#15803d"/>
    <ellipse cx="170" cy="340" rx="75" ry="45" fill="#22c55e"/>
    <!-- Flowers -->
    <circle cx="150" cy="330" r="12" fill="#ffffff"/>
    <circle cx="150" cy="330" r="4" fill="#facc15"/>
    <circle cx="210" cy="350" r="14" fill="#ffffff"/>
    <circle cx="210" cy="350" r="5" fill="#facc15"/>

    <ellipse cx="880" cy="340" rx="100" ry="60" fill="#15803d"/>
    <ellipse cx="870" cy="320" rx="85" ry="50" fill="#4ade80"/>
    <circle cx="850" cy="310" r="14" fill="#ffffff"/>
    <circle cx="850" cy="310" r="5" fill="#facc15"/>
  </g>

  <!-- White Coral Border -->
  <g fill="#ffffff">
    <ellipse cx="100" cy="460" rx="16" ry="8"/>
    <ellipse cx="140" cy="462" rx="18" ry="9"/>
    <ellipse cx="180" cy="458" rx="15" ry="7"/>
    <ellipse cx="220" cy="465" rx="19" ry="9"/>
    <ellipse cx="780" cy="460" rx="18" ry="8"/>
    <ellipse cx="820" cy="463" rx="16" ry="8"/>
    <ellipse cx="860" cy="458" rx="20" ry="9"/>
  </g>

  <!-- Stamp Badge -->
  <rect x="40" y="40" width="260" height="50" rx="8" fill="#15803d"/>
  <text x="170" y="72" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="18" text-anchor="middle">SELESAI (NUSAGARDEN)</text>
</svg>'''
save_svg('after-garden.svg', after_svg)

# Projects 1 to 6
save_svg('project-pondokindah.svg', hero_svg.replace('NusaGarden Landscape', 'Villa Pondok Indah'))
save_svg('project-bsd.svg', service_kering_svg.replace('Taman Kering (Zen)', 'Zen Garden BSD'))
save_svg('project-senopati.svg', service_vertical_svg.replace('Vertical Living Wall', 'Living Wall Senopati'))
save_svg('project-sentul.svg', service_kolam_svg.replace('Kolam Koi & Waterfall', 'Kolam Koi Sentul City'))
save_svg('project-bandung.svg', service_tropis_svg.replace('Taman Tropis Nuansa Bali', 'Resort Cafe Dago'))
save_svg('project-bekasi.svg', service_min_svg.replace('Taman Minimalis Modern', 'Backyard Summarecon'))

# Team Avatars (Vector Portraits)
def make_avatar(name, title, color_bg, shirt_color, is_female=False):
    hair = '<path d="M70,80 Q100,20 130,80 Q140,120 135,140 Q130,120 120,90 Q100,50 80,90 Q70,120 65,140 Z" fill="#1e293b"/>' if is_female else '<path d="M70,85 Q100,30 130,85 Q125,60 100,55 Q75,60 70,85 Z" fill="#0f172a"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <rect width="400" height="400" fill="{color_bg}"/>
  <circle cx="200" cy="150" r="70" fill="#fed7aa"/>
  {hair.replace('70,', '140,').replace('100,', '200,').replace('130,', '260,').replace('140', '270').replace('120', '240').replace('135', '265').replace('80', '160').replace('90', '180').replace('50', '100').replace('65', '135').replace('85', '170').replace('30', '60').replace('125', '250').replace('60', '120').replace('55', '110').replace('75', '150')}
  <!-- Eyes & Smile -->
  <circle cx="175" cy="150" r="6" fill="#0f172a"/>
  <circle cx="225" cy="150" r="6" fill="#0f172a"/>
  <path d="M185,180 Q200,195 215,180" stroke="#9a3412" stroke-width="4" fill="none" stroke-linecap="round"/>
  <!-- Body / Shoulders -->
  <path d="M100,380 Q100,260 200,260 Q300,260 300,380 Z" fill="{shirt_color}"/>
  <!-- Name badge -->
  <rect x="50" y="320" width="300" height="50" rx="25" fill="#0f172a" opacity="0.85"/>
  <text x="200" y="352" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="16" text-anchor="middle">{name}</text>
</svg>'''

save_svg('team-riana.svg', make_avatar('Riana Prasetya', 'Landscape Architect', '#dcfce7', '#1b4332', is_female=True))
save_svg('team-bambang.svg', make_avatar('Bambang Sujarwo', 'Horticulturist', '#fef3c7', '#854d0e', is_female=False))
save_svg('team-ahmad.svg', make_avatar('Ahmad Fauzan', 'Contractor', '#e0f2fe', '#0369a1', is_female=False))
save_svg('team-dewi.svg', make_avatar('Dewi Lestari', 'Quality Assurance', '#fce7f3', '#9d174d', is_female=True))

# Testimonial Client Avatars
save_svg('avatar-nadya.svg', make_avatar('Ibu Nadya', 'Klien BSD', '#fed7aa', '#c2410c', is_female=True))
save_svg('avatar-hendra.svg', make_avatar('Bpk. Hendra', 'Klien Bandung', '#dbeafe', '#1d4ed8', is_female=False))
save_svg('avatar-aditya.svg', make_avatar('Bpk. Aditya', 'Klien Jakarta', '#d1fae5', '#047857', is_female=False))

# Nursery & Greenhouse
nursery_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
  <defs>
    <linearGradient id="nurSky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#ecfdf5"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#nurSky)"/>
  
  <!-- Greenhouse Architecture (Glass Structure) -->
  <polygon points="200,350 400,180 800,180 1000,350" fill="#38bdf8" opacity="0.3"/>
  <rect x="200" y="350" width="800" height="250" fill="#0284c7" opacity="0.2"/>
  <g stroke="#ffffff" stroke-width="4">
    <line x1="400" y1="180" x2="400" y2="600"/>
    <line x1="600" y1="180" x2="600" y2="600"/>
    <line x1="800" y1="180" x2="800" y2="600"/>
    <line x1="200" y1="350" x2="1000" y2="350"/>
    <line x1="200" y1="480" x2="1000" y2="480"/>
  </g>

  <!-- Green Ground & Hundreds of Nursery Pots -->
  <rect x="0" y="520" width="1200" height="280" fill="#15803d"/>
  
  <!-- Rows of Potted Plants in Nursery -->
  <g fill="#22c55e">
    <!-- Row 1 -->
    <ellipse cx="100" cy="580" rx="35" ry="25"/>
    <ellipse cx="180" cy="580" rx="35" ry="25"/>
    <ellipse cx="260" cy="580" rx="35" ry="25"/>
    <ellipse cx="340" cy="580" rx="35" ry="25"/>
    <ellipse cx="420" cy="580" rx="35" ry="25"/>
    <ellipse cx="500" cy="580" rx="35" ry="25"/>
    <ellipse cx="580" cy="580" rx="35" ry="25"/>
    <ellipse cx="660" cy="580" rx="35" ry="25"/>
    <ellipse cx="740" cy="580" rx="35" ry="25"/>
    <ellipse cx="820" cy="580" rx="35" ry="25"/>
    <ellipse cx="900" cy="580" rx="35" ry="25"/>
    <ellipse cx="980" cy="580" rx="35" ry="25"/>
    <ellipse cx="1060" cy="580" rx="35" ry="25"/>
    <!-- Row 2 -->
    <ellipse cx="140" cy="660" rx="45" ry="30"/>
    <ellipse cx="240" cy="660" rx="45" ry="30"/>
    <ellipse cx="340" cy="660" rx="45" ry="30"/>
    <ellipse cx="440" cy="660" rx="45" ry="30"/>
    <ellipse cx="540" cy="660" rx="45" ry="30"/>
    <ellipse cx="640" cy="660" rx="45" ry="30"/>
    <ellipse cx="740" cy="660" rx="45" ry="30"/>
    <ellipse cx="840" cy="660" rx="45" ry="30"/>
    <ellipse cx="940" cy="660" rx="45" ry="30"/>
    <ellipse cx="1040" cy="660" rx="45" ry="30"/>
  </g>
  <g fill="#4ade80">
    <ellipse cx="100" cy="570" rx="25" ry="18"/>
    <ellipse cx="180" cy="570" rx="25" ry="18"/>
    <ellipse cx="260" cy="570" rx="25" ry="18"/>
    <ellipse cx="340" cy="570" rx="25" ry="18"/>
    <ellipse cx="420" cy="570" rx="25" ry="18"/>
    <ellipse cx="500" cy="570" rx="25" ry="18"/>
    <ellipse cx="580" cy="570" rx="25" ry="18"/>
    <ellipse cx="660" cy="570" rx="25" ry="18"/>
    <ellipse cx="740" cy="570" rx="25" ry="18"/>
    <ellipse cx="820" cy="570" rx="25" ry="18"/>
    <ellipse cx="900" cy="570" rx="25" ry="18"/>
    <ellipse cx="980" cy="570" rx="25" ry="18"/>
    <ellipse cx="1060" cy="570" rx="25" ry="18"/>
  </g>

  <!-- Title Badge -->
  <rect x="40" y="40" width="300" height="50" rx="25" fill="#1b4332" opacity="0.9"/>
  <text x="190" y="72" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="16" text-anchor="middle">Kebun Nursery & Greenhouse</text>
</svg>'''
save_svg('nursery-greenhouse.svg', nursery_svg)

print("All SVG assets generated successfully!")

