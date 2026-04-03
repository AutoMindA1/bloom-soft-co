import { useState } from "react";

const C = {
  sky: "#B9D7F2",
  peri: "#A0C0E4",
  ice: "#D7E8FA",
  sage: "#A5C6B2",
  gold: "#C3A564",
  blush: "#F5B9C8",
  navy: "#323F5A",
  white: "#F8FBFF",
  midnight: "#1C263E",
  sageLight: "#d4e8dc",
  blushLight: "#fce4ec",
  goldLight: "#f5ecd4",
  iceDeep: "#c5d8f0",
};

const phases = [
  {
    id: "create",
    title: "Create",
    icon: "\u2728",
    color: C.blush,
    bg: C.blushLight,
    desc: "AI-powered content generation pipeline",
    nodes: [
      {
        name: "Imagen 3",
        detail: "Generate watercolor art from text prompts",
        inputs: "Text prompt + style vars",
        outputs: "PNG artwork (300dpi)",
        status: "active",
      },
      {
        name: "Claude SEO Engine",
        detail:
          "Generate titles, descriptions, and 13 optimized tags per listing",
        inputs: "Product type + subject",
        outputs: "Complete listing copy",
        status: "active",
      },
      {
        name: "reportlab PDF Gen",
        detail:
          "Build Conference journals & activity booklets programmatically",
        inputs: "Python scripts",
        outputs: "Print-ready 8.5x11 PDFs",
        status: "active",
      },
    ],
    howTo: [
      "Open Google AI Studio (aistudio.google.com)",
      "Paste prompt from prompts/imagen3/ folder",
      "Download PNG, save to products/wall-art/",
      "Run: python scripts/generate-listing.py --type animal --subject 'your subject'",
      "Copy listing output to Etsy",
    ],
  },
  {
    id: "process",
    title: "Process",
    icon: "\u2699\uFE0F",
    color: C.sky,
    bg: C.ice,
    desc: "Automation scripts transform raw assets into upload-ready packs",
    nodes: [
      {
        name: "batch-resize.py",
        detail:
          "Takes 1 PNG, outputs 9 standard print sizes + 2 phone sizes, auto-zips",
        inputs: "Single PNG or folder",
        outputs:
          "ZIP with 4x6, 5x7, 8x10, 11x14, 16x20, A4, A3, 1080x1920, 1170x2532",
        status: "active",
      },
      {
        name: "generate-listing.py",
        detail:
          "Template-based copy generator for 6 product types \u2014 no API needed",
        inputs: "--type + --subject + --color",
        outputs:
          "Imagen prompt + Etsy title + description + 13 tags + Redbubble desc + price",
        status: "active",
      },
    ],
    howTo: [
      "Open Terminal, cd into Bloom Soft folder",
      "Run: python scripts/batch-resize.py products/wall-art/your_file.png",
      "Find ZIP in output/ folder",
      "Upload ZIP contents as Etsy digital download files",
      "For phone wallpapers: add --phone-only flag",
    ],
  },
  {
    id: "catalog",
    title: "Catalog",
    icon: "\uD83D\uDCE6",
    color: C.sage,
    bg: C.sageLight,
    desc: "53 SKUs across 6 product categories",
    nodes: [
      {
        name: "Wall Art Singles",
        detail: "14 designs \u2014 animals, botanicals, fashion x nature",
        inputs: "Imagen 3 PNGs",
        outputs: "Multi-size digital downloads",
        status: "active",
        price: "$4.99-$7.99",
      },
      {
        name: "Phone Wallpapers",
        detail: "10 designs optimized for iPhone/Android",
        inputs: "Imagen 3 PNGs",
        outputs: "1080x1920 + 1170x2532",
        status: "active",
        price: "$3.99-$4.99",
      },
      {
        name: "Art Bundles",
        detail: "6 themed 5-packs at bundle discount",
        inputs: "Curated sets",
        outputs: "ZIP with 5 designs x 9 sizes",
        status: "active",
        price: "$14.99-$19.99",
      },
      {
        name: "Revelation System",
        detail: "30-page premium adult Conference journal \u2014 HERO PRODUCT",
        inputs: "reportlab script",
        outputs: "PDF with D/I/P/W/T tags, pattern map, 30-day challenge",
        status: "hero",
        price: "$9.99",
      },
      {
        name: "Conference Passport",
        detail: "22-page kids activity passport with stamps & games",
        inputs: "reportlab script",
        outputs: "PDF with destinations, feelings explorer, trading cards",
        status: "hero",
        price: "$7.99",
      },
      {
        name: "Standard Journal",
        detail: "21-page traditional note-taking journal",
        inputs: "reportlab script",
        outputs: "PDF with speaker grids + 6-box reflection",
        status: "active",
        price: "$7.99",
      },
      {
        name: "Activity Booklet",
        detail: "18-page kids activity booklet",
        inputs: "reportlab script",
        outputs: "PDF with bingo, word search, maze, coloring",
        status: "active",
        price: "$6.99",
      },
      {
        name: "Family Bundle",
        detail: "Adult journal + Kids passport combo",
        inputs: "2 PDFs",
        outputs: "Bundled listing",
        status: "active",
        price: "$14.99",
      },
      {
        name: "Ultimate Collection",
        detail: "All 4 Conference products",
        inputs: "4 PDFs",
        outputs: "Best value bundle",
        status: "active",
        price: "$19.99",
      },
    ],
    howTo: [
      "All products live in products/ folder",
      "Wall art: products/wall-art/*.png",
      "Conference: products/conference/adult/ and products/conference/kids/",
      "Listings copy: listings/etsy/*.md \u2014 copy-paste into Etsy",
      "Bundles are virtual \u2014 create as separate Etsy listing linking same files",
    ],
  },
  {
    id: "sell",
    title: "Sell",
    icon: "\uD83D\uDED2",
    color: C.gold,
    bg: C.goldLight,
    desc: "Two-channel distribution \u2014 digital downloads + print-on-demand",
    nodes: [
      {
        name: "Etsy Shop",
        detail:
          "Primary revenue channel \u2014 digital downloads, instant delivery",
        inputs: "ZIP files + listing copy",
        outputs: "Automatic delivery to buyer",
        status: "active",
      },
      {
        name: "Redbubble",
        detail: "Print-on-demand \u2014 passive income, no inventory",
        inputs: "PNG uploads",
        outputs:
          "Mugs, tees, stickers, prints \u2014 Redbubble handles printing/shipping",
        status: "active",
      },
    ],
    howTo: [
      "Go to etsy.com/sell \u2014 create shop as 'Bloom Soft Co'",
      "For each product: New Listing \u2192 Digital \u2192 Upload files",
      "Copy title, description, tags from listings/etsy/*.md",
      "Set prices per the catalog pricing above",
      "For Redbubble: redbubble.com/portfolio \u2192 Upload \u2192 Enable all product types",
      "Set Redbubble margin to 20% until you hit 10 sales",
    ],
  },
  {
    id: "grow",
    title: "Grow",
    icon: "\uD83D\uDCC8",
    color: C.peri,
    bg: C.iceDeep,
    desc: "Multi-platform growth engine drives traffic to listings",
    nodes: [
      {
        name: "Etsy SEO",
        detail: "13 niche-first tags, optimized titles, listing quality score",
        inputs: "Keyword research",
        outputs: "Organic Etsy search traffic",
        status: "active",
      },
      {
        name: "Etsy Ads",
        detail: "$5-10/day, Conference products first, scale winners",
        inputs: "Budget",
        outputs: "Paid traffic to top listings",
        status: "pending",
      },
      {
        name: "TikTok",
        detail: "Art process videos, hook-first scripts, behind-the-scenes",
        inputs: "Screen recordings + scripts from marketing/social/",
        outputs: "Viral traffic spikes",
        status: "pending",
      },
      {
        name: "Pinterest",
        detail: "1 pin per product, boards by aesthetic, SEO-rich descriptions",
        inputs: "Product images + descriptions",
        outputs: "Long-tail evergreen traffic",
        status: "pending",
      },
      {
        name: "Instagram",
        detail: "Aesthetic grid, stories, reels of art process",
        inputs: "Product images + behind-the-scenes",
        outputs: "Brand awareness + link in bio traffic",
        status: "pending",
      },
    ],
    howTo: [
      "TikTok: Download TikTok app, create @bloomsoftco account",
      "Record screen while generating art in Imagen 3 \u2014 speed it up 4x",
      "Use hooks from marketing/social/launch-week-content.md",
      "Pinterest: Create business account, make boards: 'Soft Wall Art', 'Cottagecore Decor', 'Conference Journals'",
      "Instagram: Match TikTok content, add product links in bio",
      "Etsy Ads: Start at $5/day on Conference products, increase budget on winners after 3 days",
    ],
  },
];

const conferenceProducts = [
  {
    name: "Revelation System",
    audience: "Adults",
    pages: 30,
    price: "$9.99",
    hero: true,
    tagline: "Not just a journal \u2014 a revelation system",
    features: [
      {
        name: "D/I/P/W/T Tagging",
        desc: "Color-code every insight: Doctrine, Invitation, Promise, Warning, Testimony",
      },
      {
        name: "Pattern Pentagon Map",
        desc: "Visual map connecting themes across all 5 sessions",
      },
      {
        name: "Prophetic Promise Tracker",
        desc: "IF/THEN format with 30-day checkbox grid per promise",
      },
      {
        name: "Spiritual Inventory",
        desc: "Pre + Post Conference self-assessment across 8 dimensions",
      },
      {
        name: "30-Day Challenge Calendar",
        desc: "One specific action per day to apply what you learned",
      },
      {
        name: "Letter to Future Me",
        desc: "Write to your October Conference self \u2014 seal and open later",
      },
      {
        name: "Tear-Out Quote Cards",
        desc: "4 dotted-border cards for scriptures, mirror, or locker",
      },
      {
        name: "Unique Session Reflections",
        desc: "Each session has different questions that deepen across the weekend",
      },
    ],
    file: "products/conference/adult/conference-revelation-system-april-2026.pdf",
  },
  {
    name: "Conference Passport",
    audience: "Kids (ages 6-12)",
    pages: 22,
    price: "$7.99",
    hero: true,
    tagline: "Turn Conference into an adventure",
    features: [
      {
        name: "5 Destination Stamps",
        desc: "Each session is a unique destination with its own theme and stamp to color",
      },
      {
        name: "Feelings Explorer",
        desc: "Circle emotions, match colors to feelings, draw what the Spirit felt like",
      },
      {
        name: "Conference Bingo",
        desc: "5x5 card + blank card to make your own",
      },
      {
        name: "Word Search",
        desc: "15x15 grid with 15 Conference words \u2014 fully solvable",
      },
      {
        name: "Temple Maze",
        desc: "Navigate the path to the temple \u2014 solvable with 2 dead ends",
      },
      {
        name: "Speaker Trading Card",
        desc: "Fill in stats: name, topic, best quote, Spirit Level 1-10, star rating",
      },
      {
        name: "Scripture Card Designer",
        desc: "Design a keep-in-your-scriptures card with verse and personal note",
      },
      {
        name: "Promise Bracelet Craft",
        desc: "5 cut-out strips with 'I will...' promises \u2014 tape into a wearable bracelet",
      },
      {
        name: "Conference Feelings Map",
        desc: "Plot all 5 sessions on one page \u2014 see your emotional journey",
      },
      {
        name: "Souvenir Collection",
        desc: "6 cards to capture favorite quotes and why they matter",
      },
    ],
    file: "products/conference/kids/conference-passport-kids-april-2026.pdf",
  },
  {
    name: "Standard Journal",
    audience: "Adults",
    pages: 21,
    price: "$7.99",
    hero: false,
    tagline: "Classic Conference note-taking, beautifully designed",
    features: [
      {
        name: "Speaker Grid",
        desc: "Track every speaker per session",
      },
      {
        name: "6-Box Reflection",
        desc: "Stories, Scriptures, Blessings, Quotes, Christ Connections, Action Plan",
      },
      {
        name: "Action Items Page",
        desc: "Consolidate all commitments in one place",
      },
      {
        name: "Testimony Page",
        desc: "Record what you know to be true after Conference",
      },
    ],
    file: "products/conference/adult/general-conference-journal-april-2026.pdf",
  },
  {
    name: "Activity Booklet",
    audience: "Kids (ages 4-10)",
    pages: 18,
    price: "$6.99",
    hero: false,
    tagline: "Keep little hands busy and little hearts listening",
    features: [
      {
        name: "Conference Bingo",
        desc: "5x5 card with Conference-themed squares",
      },
      { name: "Word Search", desc: "15-word solvable puzzle" },
      { name: "Maze", desc: "Solvable path with dead ends" },
      {
        name: "I Spy Checklist",
        desc: "Things to watch for during Conference",
      },
      {
        name: "Draw What You Hear",
        desc: "8 boxes for sketching during talks",
      },
      {
        name: "Coloring Page",
        desc: "Conference-themed illustration",
      },
    ],
    file: "products/conference/kids/general-conference-kids-activity-booklet-april-2026.pdf",
  },
];

const bundles = [
  {
    name: "Family Bundle",
    includes: ["Revelation System", "Conference Passport"],
    price: "$14.99",
    savings: "Save $2.99",
  },
  {
    name: "Ultimate Collection",
    includes: [
      "Revelation System",
      "Conference Passport",
      "Standard Journal",
      "Activity Booklet",
    ],
    price: "$19.99",
    savings: "Save $12.96",
  },
];

const revenue = {
  target: 1999,
  targetLabel: "MacBook Pro M4 Pro for Chloe",
  scenarios: [
    {
      name: "Conservative",
      total: 1300,
      wallArt: { units: 120, avg: 5.5 },
      conference: { units: 80, avg: 8.5 },
      ads: 150,
      net: 1150,
      color: C.sky,
    },
    {
      name: "Moderate",
      total: 1680,
      wallArt: { units: 150, avg: 5.75 },
      conference: { units: 120, avg: 8.75 },
      ads: 200,
      net: 1480,
      color: C.sage,
    },
    {
      name: "Aggressive",
      total: 2060,
      wallArt: { units: 180, avg: 6.0 },
      conference: { units: 160, avg: 9.0 },
      ads: 250,
      net: 1810,
      color: C.gold,
    },
  ],
  weeklyPlan: [
    {
      week: "Week 1",
      focus: "Launch Conference products + 10 wall art listings",
      revenue: "$200-400",
      actions: "Etsy setup, first listings, TikTok account, $5/day ads",
    },
    {
      week: "Week 2",
      focus: "Scale winners + add 15 more SKUs",
      revenue: "$350-550",
      actions:
        "Double ad budget on top sellers, Pinterest boards, daily TikTok",
    },
    {
      week: "Week 3",
      focus: "Bundle push + social proof",
      revenue: "$400-600",
      actions:
        "Request reviews, create bundles, Instagram launch, Redbubble upload",
    },
    {
      week: "Week 4",
      focus: "Optimize + scale what works",
      revenue: "$350-510",
      actions: "Kill underperformers, boost winners, prep May seasonal",
    },
  ],
};

const sprintChecklist = [
  {
    task: "Generate cover art in Imagen 3 (4 covers)",
    category: "Art",
    time: "1 hr",
    done: false,
  },
  {
    task: "Overlay text on covers in Canva",
    category: "Design",
    time: "30 min",
    done: false,
  },
  {
    task: "Create Etsy seller account",
    category: "Setup",
    time: "20 min",
    done: false,
  },
  {
    task: "Upload 4 Conference products to Etsy",
    category: "Launch",
    time: "1 hr",
    done: false,
  },
  {
    task: "Upload 10 wall art listings to Etsy",
    category: "Launch",
    time: "2 hrs",
    done: false,
  },
  {
    task: "Create TikTok @bloomsoftco account",
    category: "Social",
    time: "10 min",
    done: false,
  },
  {
    task: "Record first TikTok (art generation process)",
    category: "Social",
    time: "30 min",
    done: false,
  },
  {
    task: "Create Pinterest business account + 3 boards",
    category: "Social",
    time: "20 min",
    done: false,
  },
  {
    task: "Pin all products to Pinterest",
    category: "Social",
    time: "30 min",
    done: false,
  },
  {
    task: "Turn on Etsy Ads ($5/day on Conference products)",
    category: "Ads",
    time: "10 min",
    done: false,
  },
  {
    task: "Upload top 10 designs to Redbubble",
    category: "Launch",
    time: "1 hr",
    done: false,
  },
  {
    task: "Share shop link with family/friends for first reviews",
    category: "Growth",
    time: "15 min",
    done: false,
  },
];

function StatusDot({ status }) {
  const colors = { active: "#22c55e", hero: C.gold, pending: "#94a3b8" };
  return (
    <span
      style={{
        display: "inline-block",
        width: 8,
        height: 8,
        borderRadius: "50%",
        background: colors[status] || colors.pending,
        marginRight: 6,
      }}
    />
  );
}

function PhaseNav({ phases, active, setActive }) {
  return (
    <div
      style={{
        display: "flex",
        gap: 4,
        overflowX: "auto",
        padding: "0 0 12px",
      }}
    >
      {phases.map((p, i) => (
        <button
          key={p.id}
          onClick={() => setActive(i)}
          style={{
            flex: "1 1 0",
            minWidth: 100,
            padding: "12px 8px",
            border: "none",
            cursor: "pointer",
            background: active === i ? p.color : C.white,
            borderBottom:
              active === i ? `3px solid ${C.navy}` : `3px solid transparent`,
            borderRadius: "8px 8px 0 0",
            transition: "all 0.2s",
          }}
        >
          <div style={{ fontSize: 20 }}>{p.icon}</div>
          <div
            style={{
              fontSize: 12,
              fontWeight: 700,
              color: C.navy,
              marginTop: 2,
            }}
          >
            {p.title}
          </div>
        </button>
      ))}
    </div>
  );
}

function PhaseDetail({ phase }) {
  const [expanded, setExpanded] = useState(null);
  return (
    <div
      style={{
        background: phase.bg,
        borderRadius: 12,
        padding: 20,
        marginTop: 8,
      }}
    >
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 10,
          marginBottom: 4,
        }}
      >
        <span style={{ fontSize: 28 }}>{phase.icon}</span>
        <div>
          <h3
            style={{
              margin: 0,
              color: C.navy,
              fontFamily: "Georgia, serif",
              fontSize: 20,
            }}
          >
            {phase.title}
          </h3>
          <p
            style={{
              margin: 0,
              fontSize: 12,
              color: C.navy,
              opacity: 0.65,
            }}
          >
            {phase.desc}
          </p>
        </div>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr",
          gap: 8,
          marginTop: 16,
        }}
      >
        {phase.nodes.map((node, i) => (
          <div
            key={i}
            onClick={() => setExpanded(expanded === i ? null : i)}
            style={{
              background: C.white,
              borderRadius: 10,
              padding: "14px 16px",
              cursor: "pointer",
              border:
                node.status === "hero"
                  ? `2px solid ${C.gold}`
                  : `1px solid ${phase.color}`,
              transition: "all 0.2s",
              boxShadow:
                expanded === i ? `0 4px 16px ${phase.color}44` : "none",
            }}
          >
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
              }}
            >
              <div style={{ display: "flex", alignItems: "center" }}>
                <StatusDot status={node.status} />
                <span
                  style={{
                    fontWeight: 700,
                    color: C.navy,
                    fontSize: 14,
                  }}
                >
                  {node.name}
                </span>
                {node.price && (
                  <span
                    style={{
                      marginLeft: 8,
                      background: C.gold,
                      color: C.white,
                      borderRadius: 4,
                      padding: "1px 8px",
                      fontSize: 11,
                      fontWeight: 700,
                    }}
                  >
                    {node.price}
                  </span>
                )}
              </div>
              <span style={{ color: C.navy, opacity: 0.4, fontSize: 18 }}>
                {expanded === i ? "\u25B2" : "\u25BC"}
              </span>
            </div>
            <p
              style={{
                margin: "4px 0 0",
                fontSize: 12,
                color: C.navy,
                opacity: 0.7,
              }}
            >
              {node.detail}
            </p>
            {expanded === i && (
              <div
                style={{
                  marginTop: 12,
                  padding: "10px 12px",
                  background: phase.bg,
                  borderRadius: 8,
                  fontSize: 12,
                }}
              >
                <div style={{ marginBottom: 6 }}>
                  <strong style={{ color: C.navy }}>Input:</strong>{" "}
                  <span style={{ color: C.navy, opacity: 0.8 }}>
                    {node.inputs}
                  </span>
                </div>
                <div>
                  <strong style={{ color: C.navy }}>Output:</strong>{" "}
                  <span style={{ color: C.navy, opacity: 0.8 }}>
                    {node.outputs}
                  </span>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 20,
          background: C.white,
          borderRadius: 10,
          padding: 16,
        }}
      >
        <h4
          style={{
            margin: "0 0 10px",
            color: C.navy,
            fontSize: 13,
            textTransform: "uppercase",
            letterSpacing: 1,
          }}
        >
          How Chloe Does This
        </h4>
        {phase.howTo.map((step, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              gap: 8,
              marginBottom: 8,
              fontSize: 13,
              color: C.navy,
            }}
          >
            <span
              style={{
                fontWeight: 700,
                color: C.gold,
                minWidth: 20,
              }}
            >
              {i + 1}.
            </span>
            <span>{step}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function ConferenceView() {
  const [selected, setSelected] = useState(0);
  const product = conferenceProducts[selected];
  return (
    <div>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 8,
          marginBottom: 16,
        }}
      >
        {conferenceProducts.map((p, i) => (
          <button
            key={i}
            onClick={() => setSelected(i)}
            style={{
              padding: "12px 8px",
              border: "none",
              cursor: "pointer",
              borderRadius: 10,
              background: selected === i ? (p.hero ? C.gold : C.navy) : C.white,
              color: selected === i ? C.white : C.navy,
              boxShadow:
                selected === i
                  ? `0 4px 12px ${C.navy}33`
                  : `0 1px 4px ${C.navy}11`,
              transition: "all 0.2s",
            }}
          >
            <div style={{ fontSize: 13, fontWeight: 700 }}>{p.name}</div>
            <div
              style={{
                fontSize: 11,
                opacity: 0.75,
                marginTop: 2,
              }}
            >
              {p.audience}
            </div>
            <div
              style={{
                fontSize: 16,
                fontWeight: 800,
                marginTop: 4,
              }}
            >
              {p.price}
            </div>
          </button>
        ))}
      </div>

      <div
        style={{
          background: product.hero
            ? `linear-gradient(135deg, ${C.goldLight}, ${C.blushLight})`
            : C.white,
          borderRadius: 14,
          padding: 24,
          border: product.hero ? `2px solid ${C.gold}` : `1px solid ${C.ice}`,
        }}
      >
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "flex-start",
          }}
        >
          <div>
            <h3
              style={{
                margin: 0,
                color: C.navy,
                fontFamily: "Georgia, serif",
                fontSize: 22,
              }}
            >
              {product.name}
            </h3>
            <p
              style={{
                margin: "4px 0 0",
                fontSize: 13,
                color: C.navy,
                opacity: 0.65,
                fontStyle: "italic",
              }}
            >
              {product.tagline}
            </p>
          </div>
          <div style={{ textAlign: "right" }}>
            <div
              style={{
                fontSize: 28,
                fontWeight: 800,
                color: C.gold,
              }}
            >
              {product.price}
            </div>
            <div
              style={{
                fontSize: 11,
                color: C.navy,
                opacity: 0.5,
              }}
            >
              {product.pages} pages | {product.audience}
            </div>
          </div>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 8,
            marginTop: 20,
          }}
        >
          {product.features.map((f, i) => (
            <div
              key={i}
              style={{
                background: `${C.white}cc`,
                borderRadius: 8,
                padding: "10px 12px",
                border: `1px solid ${C.ice}`,
              }}
            >
              <div
                style={{
                  fontWeight: 700,
                  color: C.navy,
                  fontSize: 12,
                  marginBottom: 2,
                }}
              >
                {f.name}
              </div>
              <div
                style={{
                  fontSize: 11,
                  color: C.navy,
                  opacity: 0.7,
                  lineHeight: 1.4,
                }}
              >
                {f.desc}
              </div>
            </div>
          ))}
        </div>

        <div
          style={{
            marginTop: 16,
            padding: "10px 14px",
            background: C.ice,
            borderRadius: 8,
            fontSize: 12,
            color: C.navy,
          }}
        >
          <strong>File:</strong> {product.file}
        </div>
      </div>

      <div style={{ marginTop: 20 }}>
        <h4
          style={{
            margin: "0 0 10px",
            color: C.navy,
            fontSize: 14,
          }}
        >
          Bundle Deals
        </h4>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 10,
          }}
        >
          {bundles.map((b, i) => (
            <div
              key={i}
              style={{
                background: C.goldLight,
                borderRadius: 10,
                padding: 14,
                border: `1px solid ${C.gold}`,
              }}
            >
              <div
                style={{
                  fontWeight: 700,
                  color: C.navy,
                  fontSize: 14,
                }}
              >
                {b.name}
              </div>
              <div
                style={{
                  fontSize: 11,
                  color: C.navy,
                  opacity: 0.7,
                  margin: "4px 0",
                }}
              >
                {b.includes.join(" + ")}
              </div>
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  marginTop: 8,
                }}
              >
                <span
                  style={{
                    fontSize: 20,
                    fontWeight: 800,
                    color: C.gold,
                  }}
                >
                  {b.price}
                </span>
                <span
                  style={{
                    background: C.sage,
                    color: C.white,
                    borderRadius: 4,
                    padding: "2px 8px",
                    fontSize: 11,
                    fontWeight: 700,
                  }}
                >
                  {b.savings}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function RevenueView() {
  const [selectedScenario, setSelectedScenario] = useState(1);
  const s = revenue.scenarios[selectedScenario];
  const pct = Math.min(100, Math.round((s.total / revenue.target) * 100));

  return (
    <div>
      <div
        style={{
          background: `linear-gradient(135deg, ${C.navy}, ${C.midnight})`,
          borderRadius: 14,
          padding: 24,
          marginBottom: 20,
        }}
      >
        <div style={{ textAlign: "center", marginBottom: 16 }}>
          <div
            style={{
              fontSize: 13,
              color: C.gold,
              fontWeight: 600,
              textTransform: "uppercase",
              letterSpacing: 2,
            }}
          >
            Revenue Target
          </div>
          <div
            style={{
              fontSize: 42,
              fontWeight: 800,
              color: C.white,
              fontFamily: "Georgia, serif",
            }}
          >
            ${revenue.target.toLocaleString()}
          </div>
          <div style={{ fontSize: 12, color: C.peri }}>
            {revenue.targetLabel}
          </div>
        </div>

        <div
          style={{
            background: `${C.white}15`,
            borderRadius: 8,
            height: 24,
            overflow: "hidden",
            marginBottom: 8,
          }}
        >
          <div
            style={{
              height: "100%",
              borderRadius: 8,
              transition: "width 0.5s ease",
              width: `${pct}%`,
              background:
                pct >= 100
                  ? `linear-gradient(90deg, ${C.sage}, ${C.gold})`
                  : `linear-gradient(90deg, ${s.color}, ${C.gold})`,
            }}
          />
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            fontSize: 11,
            color: C.peri,
          }}
        >
          <span>${s.total.toLocaleString()} projected</span>
          <span>{pct}% of goal</span>
        </div>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, 1fr)",
          gap: 8,
          marginBottom: 20,
        }}
      >
        {revenue.scenarios.map((sc, i) => (
          <button
            key={i}
            onClick={() => setSelectedScenario(i)}
            style={{
              padding: 16,
              border: "none",
              cursor: "pointer",
              borderRadius: 10,
              background: selectedScenario === i ? sc.color : C.white,
              color: selectedScenario === i ? C.white : C.navy,
              boxShadow:
                selectedScenario === i
                  ? `0 4px 12px ${sc.color}44`
                  : "0 1px 4px rgba(0,0,0,0.06)",
              transition: "all 0.2s",
            }}
          >
            <div style={{ fontSize: 12, fontWeight: 600 }}>{sc.name}</div>
            <div
              style={{
                fontSize: 24,
                fontWeight: 800,
                marginTop: 4,
              }}
            >
              ${sc.total.toLocaleString()}
            </div>
            <div
              style={{
                fontSize: 10,
                opacity: 0.75,
                marginTop: 2,
              }}
            >
              Net: ${sc.net.toLocaleString()}
            </div>
          </button>
        ))}
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: 12,
          marginBottom: 20,
        }}
      >
        <div
          style={{
            background: C.white,
            borderRadius: 10,
            padding: 16,
            border: `1px solid ${C.ice}`,
          }}
        >
          <div
            style={{
              fontSize: 11,
              fontWeight: 700,
              color: C.navy,
              textTransform: "uppercase",
              letterSpacing: 1,
              marginBottom: 10,
            }}
          >
            Wall Art Revenue
          </div>
          <div
            style={{
              fontSize: 28,
              fontWeight: 800,
              color: C.navy,
            }}
          >
            {s.wallArt.units}
          </div>
          <div
            style={{
              fontSize: 11,
              color: C.navy,
              opacity: 0.6,
            }}
          >
            units x ${s.wallArt.avg.toFixed(2)} avg
          </div>
          <div
            style={{
              fontSize: 16,
              fontWeight: 700,
              color: C.sage,
              marginTop: 4,
            }}
          >
            ${(s.wallArt.units * s.wallArt.avg).toFixed(0)}
          </div>
        </div>
        <div
          style={{
            background: C.white,
            borderRadius: 10,
            padding: 16,
            border: `1px solid ${C.ice}`,
          }}
        >
          <div
            style={{
              fontSize: 11,
              fontWeight: 700,
              color: C.navy,
              textTransform: "uppercase",
              letterSpacing: 1,
              marginBottom: 10,
            }}
          >
            Conference Revenue
          </div>
          <div
            style={{
              fontSize: 28,
              fontWeight: 800,
              color: C.navy,
            }}
          >
            {s.conference.units}
          </div>
          <div
            style={{
              fontSize: 11,
              color: C.navy,
              opacity: 0.6,
            }}
          >
            units x ${s.conference.avg.toFixed(2)} avg
          </div>
          <div
            style={{
              fontSize: 16,
              fontWeight: 700,
              color: C.gold,
              marginTop: 4,
            }}
          >
            ${(s.conference.units * s.conference.avg).toFixed(0)}
          </div>
        </div>
      </div>

      <div
        style={{
          background: C.white,
          borderRadius: 10,
          padding: 16,
          border: `1px solid ${C.ice}`,
        }}
      >
        <h4
          style={{
            margin: "0 0 12px",
            color: C.navy,
            fontSize: 14,
          }}
        >
          4-Week Revenue Plan
        </h4>
        {revenue.weeklyPlan.map((w, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              gap: 12,
              padding: "10px 0",
              borderBottom: i < 3 ? `1px solid ${C.ice}` : "none",
            }}
          >
            <div
              style={{
                minWidth: 60,
                fontWeight: 700,
                color: C.gold,
                fontSize: 13,
              }}
            >
              {w.week}
            </div>
            <div style={{ flex: 1 }}>
              <div
                style={{
                  fontWeight: 600,
                  color: C.navy,
                  fontSize: 13,
                }}
              >
                {w.focus}
              </div>
              <div
                style={{
                  fontSize: 11,
                  color: C.navy,
                  opacity: 0.6,
                  marginTop: 2,
                }}
              >
                {w.actions}
              </div>
            </div>
            <div
              style={{
                minWidth: 70,
                textAlign: "right",
                fontWeight: 700,
                color: C.sage,
                fontSize: 13,
              }}
            >
              {w.revenue}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function SprintView() {
  const [checks, setChecks] = useState(sprintChecklist.map((s) => s.done));
  const toggle = (i) => {
    const n = [...checks];
    n[i] = !n[i];
    setChecks(n);
  };
  const done = checks.filter(Boolean).length;
  const total = checks.length;
  const categories = [...new Set(sprintChecklist.map((s) => s.category))];

  return (
    <div>
      <div
        style={{
          background: `linear-gradient(135deg, ${C.sage}, ${C.navy})`,
          borderRadius: 14,
          padding: 20,
          marginBottom: 20,
          color: C.white,
        }}
      >
        <div
          style={{
            fontSize: 13,
            fontWeight: 600,
            textTransform: "uppercase",
            letterSpacing: 2,
          }}
        >
          Launch Sprint Progress
        </div>
        <div
          style={{
            fontSize: 36,
            fontWeight: 800,
            fontFamily: "Georgia, serif",
            margin: "4px 0",
          }}
        >
          {done}/{total}
        </div>
        <div
          style={{
            background: `${C.white}25`,
            borderRadius: 6,
            height: 12,
            overflow: "hidden",
            marginTop: 8,
          }}
        >
          <div
            style={{
              height: "100%",
              borderRadius: 6,
              background: C.gold,
              width: `${(done / total) * 100}%`,
              transition: "width 0.3s",
            }}
          />
        </div>
        <div style={{ fontSize: 11, marginTop: 6, opacity: 0.8 }}>
          {done === total
            ? "Ready to launch!"
            : `${total - done} tasks remaining \u2014 estimated ${sprintChecklist
                .filter((s, i) => !checks[i])
                .reduce((a, s) => {
                  const m = parseInt(s.time);
                  return a + (s.time.includes("hr") ? m * 60 : m);
                }, 0)} min`}
        </div>
      </div>

      {categories.map((cat) => (
        <div key={cat} style={{ marginBottom: 16 }}>
          <div
            style={{
              fontSize: 11,
              fontWeight: 700,
              color: C.navy,
              textTransform: "uppercase",
              letterSpacing: 1,
              marginBottom: 8,
              paddingLeft: 4,
            }}
          >
            {cat}
          </div>
          {sprintChecklist.map(
            (item, i) =>
              item.category === cat && (
                <div
                  key={i}
                  onClick={() => toggle(i)}
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 10,
                    padding: "10px 12px",
                    background: checks[i] ? `${C.sage}15` : C.white,
                    borderRadius: 8,
                    marginBottom: 4,
                    cursor: "pointer",
                    border: `1px solid ${checks[i] ? C.sage : C.ice}`,
                    transition: "all 0.15s",
                  }}
                >
                  <div
                    style={{
                      width: 20,
                      height: 20,
                      borderRadius: 4,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      background: checks[i] ? C.sage : "transparent",
                      border: `2px solid ${checks[i] ? C.sage : C.peri}`,
                      color: C.white,
                      fontSize: 12,
                      fontWeight: 700,
                    }}
                  >
                    {checks[i] && "\u2713"}
                  </div>
                  <span
                    style={{
                      flex: 1,
                      fontSize: 13,
                      color: C.navy,
                      textDecoration: checks[i] ? "line-through" : "none",
                      opacity: checks[i] ? 0.5 : 1,
                    }}
                  >
                    {item.task}
                  </span>
                  <span
                    style={{
                      fontSize: 11,
                      color: C.navy,
                      opacity: 0.4,
                    }}
                  >
                    {item.time}
                  </span>
                </div>
              ),
          )}
        </div>
      ))}
    </div>
  );
}

export default function BloomSoftCommandCenter() {
  const [view, setView] = useState("pipeline");
  const [activePhase, setActivePhase] = useState(0);

  const views = [
    { id: "pipeline", label: "Pipeline", icon: "\u26A1" },
    { id: "conference", label: "Conference", icon: "\uD83D\uDCD6" },
    { id: "revenue", label: "Revenue", icon: "\uD83D\uDCB0" },
    { id: "sprint", label: "Sprint", icon: "\uD83D\uDE80" },
  ];

  return (
    <div
      style={{
        background: "#f4f4f4",
        minHeight: "100vh",
        fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      }}
    >
      <div
        style={{
          maxWidth: 780,
          margin: "0 auto",
          padding: "16px 16px 40px",
        }}
      >
        <div style={{ textAlign: "center", padding: "20px 0 16px" }}>
          <h1
            style={{
              margin: 0,
              color: C.navy,
              fontFamily: "Georgia, serif",
              fontSize: 26,
              letterSpacing: -0.5,
            }}
          >
            Bloom Soft Co.
          </h1>
          <p
            style={{
              margin: "2px 0 0",
              color: C.gold,
              fontSize: 12,
              fontStyle: "italic",
            }}
          >
            Command Center
          </p>
        </div>

        <div
          style={{
            display: "flex",
            gap: 4,
            marginBottom: 16,
            background: C.white,
            borderRadius: 10,
            padding: 4,
          }}
        >
          {views.map((v) => (
            <button
              key={v.id}
              onClick={() => setView(v.id)}
              style={{
                flex: 1,
                padding: "10px 6px",
                border: "none",
                cursor: "pointer",
                borderRadius: 8,
                background: view === v.id ? C.navy : "transparent",
                color: view === v.id ? C.white : C.navy,
                fontSize: 12,
                fontWeight: 600,
                transition: "all 0.2s",
              }}
            >
              <span style={{ marginRight: 4 }}>{v.icon}</span>
              {v.label}
            </button>
          ))}
        </div>

        {view === "pipeline" && (
          <>
            <PhaseNav
              phases={phases}
              active={activePhase}
              setActive={setActivePhase}
            />
            <PhaseDetail phase={phases[activePhase]} />
          </>
        )}
        {view === "conference" && <ConferenceView />}
        {view === "revenue" && <RevenueView />}
        {view === "sprint" && <SprintView />}

        <div
          style={{
            textAlign: "center",
            marginTop: 32,
            fontSize: 11,
            color: C.navy,
            opacity: 0.3,
          }}
        >
          Bloom Soft Co. | Owner: Chloe Swainston (13) | Operator: Caleb
          Swainston | Target: $1,999
        </div>
      </div>
    </div>
  );
}
