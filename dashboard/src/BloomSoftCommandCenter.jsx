import { useState, useEffect, useRef } from "react";

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

/* ── Animated wrapper ── */
function AnimateIn({ children, delay = 0, style = {} }) {
  return (
    <div
      style={{
        animation: `slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) ${delay}s both`,
        ...style,
      }}
    >
      {children}
    </div>
  );
}

/* ── Touch-scale button wrapper ── */
function Pressable({ children, onClick, style = {}, activeScale = 0.97 }) {
  const [pressed, setPressed] = useState(false);
  return (
    <div
      onClick={onClick}
      onTouchStart={() => setPressed(true)}
      onTouchEnd={() => setPressed(false)}
      onTouchCancel={() => setPressed(false)}
      onMouseDown={() => setPressed(true)}
      onMouseUp={() => setPressed(false)}
      onMouseLeave={() => setPressed(false)}
      style={{
        transform: pressed ? `scale(${activeScale})` : "scale(1)",
        transition: "transform 0.15s cubic-bezier(0.16, 1, 0.3, 1)",
        cursor: "pointer",
        ...style,
      }}
    >
      {children}
    </div>
  );
}

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
        outputs: "Print-ready 8.5\u00d711 PDFs",
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
        outputs: "ZIP with 4\u00d76 through A3 + phone sizes",
        status: "active",
      },
      {
        name: "generate-listing.py",
        detail: "Template-based copy generator for 6 product types",
        inputs: "--type + --subject + --color",
        outputs: "Full listing copy + prompt + price",
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
        detail: "14 designs \u2014 animals, botanicals, fashion \u00d7 nature",
        inputs: "Imagen 3 PNGs",
        outputs: "Multi-size digital downloads",
        status: "active",
        price: "$4.99\u2013$7.99",
      },
      {
        name: "Phone Wallpapers",
        detail: "10 designs optimized for iPhone/Android",
        inputs: "Imagen 3 PNGs",
        outputs: "1080\u00d71920 + 1170\u00d72532",
        status: "active",
        price: "$3.99\u2013$4.99",
      },
      {
        name: "Art Bundles",
        detail: "6 themed 5-packs at bundle discount",
        inputs: "Curated sets",
        outputs: "ZIP with 5 designs \u00d7 9 sizes",
        status: "active",
        price: "$14.99\u2013$19.99",
      },
      {
        name: "Revelation System",
        detail: "30-page premium adult Conference journal \u2014 HERO",
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
      "Conference: products/conference/adult/ and kids/",
      "Listings copy: listings/etsy/*.md",
      "Bundles are virtual \u2014 create as separate Etsy listing",
    ],
  },
  {
    id: "sell",
    title: "Sell",
    icon: "\uD83D\uDED2",
    color: C.gold,
    bg: C.goldLight,
    desc: "Two-channel distribution \u2014 digital + print-on-demand",
    nodes: [
      {
        name: "Etsy Shop",
        detail: "Primary revenue \u2014 digital downloads, instant delivery",
        inputs: "ZIP files + listing copy",
        outputs: "Automatic delivery to buyer",
        status: "active",
      },
      {
        name: "Redbubble",
        detail: "Print-on-demand \u2014 passive income, no inventory",
        inputs: "PNG uploads",
        outputs: "Mugs, tees, stickers, prints",
        status: "active",
      },
    ],
    howTo: [
      "Go to etsy.com/sell \u2014 create shop as 'Bloom Soft Co'",
      "For each product: New Listing \u2192 Digital \u2192 Upload files",
      "Copy title, description, tags from listings/etsy/*.md",
      "Set prices per the catalog pricing above",
      "For Redbubble: redbubble.com/portfolio \u2192 Upload",
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
        detail: "13 niche-first tags, optimized titles",
        inputs: "Keyword research",
        outputs: "Organic Etsy search traffic",
        status: "active",
      },
      {
        name: "Etsy Ads",
        detail: "$5\u201310/day, Conference products first",
        inputs: "Budget",
        outputs: "Paid traffic to top listings",
        status: "pending",
      },
      {
        name: "TikTok",
        detail: "Art process videos, hook-first scripts",
        inputs: "Screen recordings + scripts",
        outputs: "Viral traffic spikes",
        status: "pending",
      },
      {
        name: "Pinterest",
        detail: "1 pin per product, boards by aesthetic",
        inputs: "Product images + descriptions",
        outputs: "Long-tail evergreen traffic",
        status: "pending",
      },
      {
        name: "Instagram",
        detail: "Aesthetic grid, stories, reels",
        inputs: "Product images + BTS",
        outputs: "Brand awareness + bio traffic",
        status: "pending",
      },
    ],
    howTo: [
      "TikTok: Create @bloomsoftco account",
      "Record screen while generating art \u2014 speed up 4\u00d7",
      "Use hooks from marketing/social/launch-week-content.md",
      "Pinterest: Create business account + boards",
      "Instagram: Match TikTok content, product links in bio",
      "Etsy Ads: Start $5/day, increase on winners after 3 days",
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
        desc: "Write to your October Conference self",
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
    audience: "Kids 6\u201312",
    pages: 22,
    price: "$7.99",
    hero: true,
    tagline: "Turn Conference into an adventure",
    features: [
      {
        name: "5 Destination Stamps",
        desc: "Each session is a unique destination with stamp to color",
      },
      {
        name: "Feelings Explorer",
        desc: "Circle emotions, match colors to feelings",
      },
      {
        name: "Conference Bingo",
        desc: "5\u00d75 card + blank card to make your own",
      },
      { name: "Word Search", desc: "15\u00d715 grid with 15 Conference words" },
      { name: "Temple Maze", desc: "Navigate the path to the temple" },
      {
        name: "Speaker Trading Card",
        desc: "Fill in stats: name, topic, best quote, Spirit Level",
      },
      {
        name: "Scripture Card Designer",
        desc: "Design a keep-in-your-scriptures card",
      },
      {
        name: "Promise Bracelet Craft",
        desc: "5 cut-out strips \u2014 tape into a wearable bracelet",
      },
      {
        name: "Feelings Map",
        desc: "Plot all 5 sessions \u2014 see your emotional journey",
      },
      {
        name: "Souvenir Collection",
        desc: "6 cards to capture favorite quotes",
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
      { name: "Speaker Grid", desc: "Track every speaker per session" },
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
    audience: "Kids 4\u201310",
    pages: 18,
    price: "$6.99",
    hero: false,
    tagline: "Keep little hands busy and little hearts listening",
    features: [
      {
        name: "Conference Bingo",
        desc: "5\u00d75 card with Conference-themed squares",
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
      { name: "Coloring Page", desc: "Conference-themed illustration" },
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
      week: "Wk 1",
      focus: "Launch Conference + 10 wall art",
      revenue: "$200\u2013400",
      actions: "Etsy setup, first listings, TikTok, $5/day ads",
    },
    {
      week: "Wk 2",
      focus: "Scale winners + 15 more SKUs",
      revenue: "$350\u2013550",
      actions: "Double ads on top sellers, Pinterest, daily TikTok",
    },
    {
      week: "Wk 3",
      focus: "Bundle push + social proof",
      revenue: "$400\u2013600",
      actions: "Request reviews, bundles, Instagram, Redbubble",
    },
    {
      week: "Wk 4",
      focus: "Optimize + scale winners",
      revenue: "$350\u2013510",
      actions: "Kill underperformers, boost winners, prep May",
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

/* ── Status Dot with pulse animation for hero items ── */
function StatusDot({ status }) {
  const colors = { active: "#22c55e", hero: C.gold, pending: "#94a3b8" };
  return (
    <span
      style={{
        display: "inline-block",
        width: 10,
        height: 10,
        borderRadius: "50%",
        background: colors[status] || colors.pending,
        marginRight: 8,
        boxShadow:
          status === "hero"
            ? `0 0 8px ${C.gold}88`
            : status === "active"
              ? `0 0 6px #22c55e66`
              : "none",
        animation: status === "hero" ? "pulse 2s ease-in-out infinite" : "none",
      }}
    />
  );
}

/* ── Phase Navigation (horizontal scroll, pill style) ── */
function PhaseNav({ phases, active, setActive }) {
  const scrollRef = useRef(null);

  useEffect(() => {
    const el = scrollRef.current?.children[active];
    if (el)
      el.scrollIntoView({
        behavior: "smooth",
        inline: "center",
        block: "nearest",
      });
  }, [active]);

  return (
    <div
      ref={scrollRef}
      style={{
        display: "flex",
        gap: 8,
        overflowX: "auto",
        padding: "4px 0 16px",
        scrollbarWidth: "none",
        msOverflowStyle: "none",
        WebkitOverflowScrolling: "touch",
      }}
    >
      {phases.map((p, i) => (
        <Pressable key={p.id} onClick={() => setActive(i)} activeScale={0.93}>
          <div
            style={{
              minWidth: 72,
              padding: "10px 14px",
              background: active === i ? p.color : C.white,
              borderRadius: 16,
              textAlign: "center",
              boxShadow:
                active === i
                  ? `0 4px 16px ${p.color}55`
                  : `0 1px 4px ${C.navy}10`,
              transition: "all 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
            }}
          >
            <div style={{ fontSize: 22, lineHeight: 1 }}>{p.icon}</div>
            <div
              style={{
                fontSize: 11,
                fontWeight: 700,
                color: active === i ? C.navy : `${C.navy}99`,
                marginTop: 4,
                letterSpacing: 0.5,
              }}
            >
              {p.title}
            </div>
          </div>
        </Pressable>
      ))}
    </div>
  );
}

/* ── Phase Detail Card ── */
function PhaseDetail({ phase }) {
  const [expanded, setExpanded] = useState(null);
  const [showHowTo, setShowHowTo] = useState(false);

  return (
    <AnimateIn>
      <div
        style={{
          background: phase.bg,
          borderRadius: 20,
          padding: "20px 16px",
          marginTop: 4,
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 12,
            marginBottom: 16,
          }}
        >
          <span style={{ fontSize: 32 }}>{phase.icon}</span>
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
                margin: "2px 0 0",
                fontSize: 12,
                color: C.navy,
                opacity: 0.6,
              }}
            >
              {phase.desc}
            </p>
          </div>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          {phase.nodes.map((node, i) => (
            <AnimateIn key={i} delay={i * 0.06}>
              <Pressable
                onClick={() => setExpanded(expanded === i ? null : i)}
                activeScale={0.98}
              >
                <div
                  style={{
                    background: C.white,
                    borderRadius: 14,
                    padding: "14px 16px",
                    border:
                      node.status === "hero"
                        ? `2px solid ${C.gold}`
                        : `1px solid ${phase.color}44`,
                    boxShadow:
                      expanded === i
                        ? `0 6px 24px ${phase.color}33`
                        : `0 2px 8px ${C.navy}08`,
                    transition: "all 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                    }}
                  >
                    <div
                      style={{
                        display: "flex",
                        alignItems: "center",
                        flex: 1,
                        minWidth: 0,
                      }}
                    >
                      <StatusDot status={node.status} />
                      <span
                        style={{
                          fontWeight: 700,
                          color: C.navy,
                          fontSize: 14,
                          whiteSpace: "nowrap",
                          overflow: "hidden",
                          textOverflow: "ellipsis",
                        }}
                      >
                        {node.name}
                      </span>
                      {node.price && (
                        <span
                          style={{
                            marginLeft: 8,
                            background: `linear-gradient(135deg, ${C.gold}, ${C.gold}dd)`,
                            color: C.white,
                            borderRadius: 6,
                            padding: "2px 8px",
                            fontSize: 11,
                            fontWeight: 700,
                            flexShrink: 0,
                          }}
                        >
                          {node.price}
                        </span>
                      )}
                    </div>
                    <span
                      style={{
                        color: C.navy,
                        opacity: 0.3,
                        fontSize: 12,
                        marginLeft: 8,
                        transform:
                          expanded === i ? "rotate(180deg)" : "rotate(0deg)",
                        transition:
                          "transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                      }}
                    >
                      \u25BC
                    </span>
                  </div>
                  <p
                    style={{
                      margin: "6px 0 0",
                      fontSize: 12,
                      color: C.navy,
                      opacity: 0.65,
                      lineHeight: 1.4,
                    }}
                  >
                    {node.detail}
                  </p>

                  <div
                    style={{
                      maxHeight: expanded === i ? 200 : 0,
                      overflow: "hidden",
                      transition:
                        "max-height 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease",
                      opacity: expanded === i ? 1 : 0,
                    }}
                  >
                    <div
                      style={{
                        marginTop: 12,
                        padding: "12px 14px",
                        background: phase.bg,
                        borderRadius: 10,
                        fontSize: 12,
                      }}
                    >
                      <div style={{ marginBottom: 6 }}>
                        <span style={{ fontWeight: 700, color: C.navy }}>
                          In:{" "}
                        </span>
                        <span style={{ color: C.navy, opacity: 0.75 }}>
                          {node.inputs}
                        </span>
                      </div>
                      <div>
                        <span style={{ fontWeight: 700, color: C.navy }}>
                          Out:{" "}
                        </span>
                        <span style={{ color: C.navy, opacity: 0.75 }}>
                          {node.outputs}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </Pressable>
            </AnimateIn>
          ))}
        </div>

        <AnimateIn delay={0.2}>
          <Pressable
            onClick={() => setShowHowTo(!showHowTo)}
            activeScale={0.98}
            style={{ marginTop: 16 }}
          >
            <div
              style={{
                background: C.white,
                borderRadius: 14,
                padding: 16,
                boxShadow: `0 2px 8px ${C.navy}08`,
              }}
            >
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                }}
              >
                <h4
                  style={{
                    margin: 0,
                    color: C.navy,
                    fontSize: 13,
                    textTransform: "uppercase",
                    letterSpacing: 1,
                  }}
                >
                  How Chloe Does This
                </h4>
                <span
                  style={{
                    fontSize: 12,
                    color: C.navy,
                    opacity: 0.3,
                    transform: showHowTo ? "rotate(180deg)" : "rotate(0deg)",
                    transition: "transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                  }}
                >
                  \u25BC
                </span>
              </div>
              <div
                style={{
                  maxHeight: showHowTo ? 400 : 0,
                  overflow: "hidden",
                  transition:
                    "max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease",
                  opacity: showHowTo ? 1 : 0,
                }}
              >
                <div style={{ paddingTop: 12 }}>
                  {phase.howTo.map((step, i) => (
                    <div
                      key={i}
                      style={{
                        display: "flex",
                        gap: 10,
                        marginBottom: 10,
                        fontSize: 13,
                        color: C.navy,
                      }}
                    >
                      <span
                        style={{
                          fontWeight: 800,
                          color: C.white,
                          background: C.gold,
                          borderRadius: 8,
                          width: 24,
                          height: 24,
                          display: "flex",
                          alignItems: "center",
                          justifyContent: "center",
                          fontSize: 11,
                          flexShrink: 0,
                        }}
                      >
                        {i + 1}
                      </span>
                      <span style={{ lineHeight: 1.5, paddingTop: 2 }}>
                        {step}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </Pressable>
        </AnimateIn>
      </div>
    </AnimateIn>
  );
}

/* ── Conference Products View ── */
function ConferenceView() {
  const [selected, setSelected] = useState(0);
  const product = conferenceProducts[selected];

  return (
    <div>
      <div
        style={{
          display: "flex",
          gap: 8,
          overflowX: "auto",
          padding: "0 0 16px",
          scrollbarWidth: "none",
          WebkitOverflowScrolling: "touch",
        }}
      >
        {conferenceProducts.map((p, i) => (
          <Pressable key={i} onClick={() => setSelected(i)} activeScale={0.93}>
            <div
              style={{
                minWidth: 80,
                padding: "12px 10px",
                borderRadius: 14,
                textAlign: "center",
                background:
                  selected === i
                    ? p.hero
                      ? `linear-gradient(135deg, ${C.gold}, ${C.gold}cc)`
                      : C.navy
                    : C.white,
                color: selected === i ? C.white : C.navy,
                boxShadow:
                  selected === i
                    ? `0 6px 20px ${p.hero ? C.gold : C.navy}44`
                    : `0 2px 8px ${C.navy}10`,
                transition: "all 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
              }}
            >
              <div style={{ fontSize: 12, fontWeight: 700 }}>{p.name}</div>
              <div style={{ fontSize: 10, opacity: 0.7, marginTop: 2 }}>
                {p.audience}
              </div>
              <div style={{ fontSize: 18, fontWeight: 800, marginTop: 4 }}>
                {p.price}
              </div>
            </div>
          </Pressable>
        ))}
      </div>

      <AnimateIn key={selected}>
        <div
          style={{
            background: product.hero
              ? `linear-gradient(135deg, ${C.goldLight}, ${C.blushLight})`
              : C.white,
            borderRadius: 20,
            padding: "20px 16px",
            border: product.hero ? `2px solid ${C.gold}` : `1px solid ${C.ice}`,
            boxShadow: product.hero
              ? `0 8px 32px ${C.gold}22`
              : `0 2px 12px ${C.navy}08`,
          }}
        >
          <div style={{ marginBottom: 16 }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "flex-start",
              }}
            >
              <div style={{ flex: 1 }}>
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
                    opacity: 0.6,
                    fontStyle: "italic",
                  }}
                >
                  {product.tagline}
                </p>
              </div>
              <div
                style={{ textAlign: "right", flexShrink: 0, marginLeft: 12 }}
              >
                <div style={{ fontSize: 28, fontWeight: 800, color: C.gold }}>
                  {product.price}
                </div>
                <div style={{ fontSize: 10, color: C.navy, opacity: 0.5 }}>
                  {product.pages}p \u00b7 {product.audience}
                </div>
              </div>
            </div>
          </div>

          <div
            style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}
          >
            {product.features.map((f, i) => (
              <AnimateIn key={i} delay={i * 0.04}>
                <div
                  style={{
                    background: `${C.white}dd`,
                    borderRadius: 12,
                    padding: "10px 12px",
                    border: `1px solid ${C.ice}`,
                    height: "100%",
                  }}
                >
                  <div
                    style={{
                      fontWeight: 700,
                      color: C.navy,
                      fontSize: 11,
                      marginBottom: 3,
                    }}
                  >
                    {f.name}
                  </div>
                  <div
                    style={{
                      fontSize: 10,
                      color: C.navy,
                      opacity: 0.65,
                      lineHeight: 1.4,
                    }}
                  >
                    {f.desc}
                  </div>
                </div>
              </AnimateIn>
            ))}
          </div>
        </div>
      </AnimateIn>

      <AnimateIn delay={0.15} style={{ marginTop: 16 }}>
        <h4
          style={{
            margin: "0 0 10px 4px",
            color: C.navy,
            fontSize: 14,
            fontFamily: "Georgia, serif",
          }}
        >
          Bundle Deals
        </h4>
        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          {bundles.map((b, i) => (
            <Pressable key={i} activeScale={0.98}>
              <div
                style={{
                  background: `linear-gradient(135deg, ${C.goldLight}, ${C.white})`,
                  borderRadius: 14,
                  padding: 16,
                  border: `1px solid ${C.gold}44`,
                  boxShadow: `0 2px 12px ${C.gold}15`,
                }}
              >
                <div
                  style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                  }}
                >
                  <div>
                    <div
                      style={{ fontWeight: 700, color: C.navy, fontSize: 15 }}
                    >
                      {b.name}
                    </div>
                    <div
                      style={{
                        fontSize: 11,
                        color: C.navy,
                        opacity: 0.6,
                        marginTop: 2,
                      }}
                    >
                      {b.includes.join(" + ")}
                    </div>
                  </div>
                  <div style={{ textAlign: "right" }}>
                    <div
                      style={{ fontSize: 22, fontWeight: 800, color: C.gold }}
                    >
                      {b.price}
                    </div>
                    <span
                      style={{
                        background: C.sage,
                        color: C.white,
                        borderRadius: 6,
                        padding: "2px 8px",
                        fontSize: 10,
                        fontWeight: 700,
                      }}
                    >
                      {b.savings}
                    </span>
                  </div>
                </div>
              </div>
            </Pressable>
          ))}
        </div>
      </AnimateIn>
    </div>
  );
}

/* ── Revenue View ── */
function RevenueView() {
  const [selectedScenario, setSelectedScenario] = useState(1);
  const s = revenue.scenarios[selectedScenario];
  const pct = Math.min(100, Math.round((s.total / revenue.target) * 100));
  const [animPct, setAnimPct] = useState(0);

  useEffect(() => {
    const t = setTimeout(() => setAnimPct(pct), 100);
    return () => clearTimeout(t);
  }, [pct]);

  return (
    <div>
      <AnimateIn>
        <div
          style={{
            background: `linear-gradient(145deg, ${C.navy}, ${C.midnight})`,
            borderRadius: 24,
            padding: "24px 20px",
            marginBottom: 16,
            boxShadow: `0 8px 32px ${C.midnight}66`,
          }}
        >
          <div style={{ textAlign: "center", marginBottom: 20 }}>
            <div
              style={{
                fontSize: 11,
                color: C.gold,
                fontWeight: 700,
                textTransform: "uppercase",
                letterSpacing: 3,
              }}
            >
              Revenue Target
            </div>
            <div
              style={{
                fontSize: 48,
                fontWeight: 800,
                color: C.white,
                fontFamily: "Georgia, serif",
                lineHeight: 1.1,
                margin: "4px 0",
                background: `linear-gradient(135deg, ${C.white}, ${C.gold})`,
                WebkitBackgroundClip: "text",
                WebkitTextFillColor: "transparent",
              }}
            >
              ${revenue.target.toLocaleString()}
            </div>
            <div style={{ fontSize: 12, color: C.peri, opacity: 0.8 }}>
              {revenue.targetLabel}
            </div>
          </div>

          <div
            style={{
              background: `${C.white}18`,
              borderRadius: 12,
              height: 28,
              overflow: "hidden",
              marginBottom: 8,
              padding: 3,
            }}
          >
            <div
              style={{
                height: "100%",
                borderRadius: 10,
                width: `${animPct}%`,
                background:
                  animPct >= 100
                    ? `linear-gradient(90deg, ${C.sage}, ${C.gold})`
                    : `linear-gradient(90deg, ${s.color}, ${C.gold})`,
                transition: "width 0.8s cubic-bezier(0.16, 1, 0.3, 1)",
                boxShadow: `0 0 16px ${C.gold}44`,
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
            <span style={{ fontWeight: 700, color: C.gold }}>{pct}%</span>
          </div>
        </div>
      </AnimateIn>

      <AnimateIn delay={0.1}>
        <div style={{ display: "flex", gap: 8, marginBottom: 16 }}>
          {revenue.scenarios.map((sc, i) => (
            <Pressable
              key={i}
              onClick={() => setSelectedScenario(i)}
              activeScale={0.93}
              style={{ flex: 1 }}
            >
              <div
                style={{
                  padding: "14px 8px",
                  borderRadius: 14,
                  textAlign: "center",
                  background: selectedScenario === i ? sc.color : C.white,
                  color: selectedScenario === i ? C.white : C.navy,
                  boxShadow:
                    selectedScenario === i
                      ? `0 6px 20px ${sc.color}44`
                      : `0 2px 8px ${C.navy}08`,
                  transition: "all 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                }}
              >
                <div style={{ fontSize: 11, fontWeight: 600 }}>{sc.name}</div>
                <div style={{ fontSize: 22, fontWeight: 800, marginTop: 2 }}>
                  ${sc.total.toLocaleString()}
                </div>
                <div style={{ fontSize: 10, opacity: 0.7 }}>
                  Net ${sc.net.toLocaleString()}
                </div>
              </div>
            </Pressable>
          ))}
        </div>
      </AnimateIn>

      <AnimateIn delay={0.15}>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 10,
            marginBottom: 16,
          }}
        >
          <div
            style={{
              background: C.white,
              borderRadius: 16,
              padding: 16,
              border: `1px solid ${C.ice}`,
              boxShadow: `0 2px 8px ${C.navy}06`,
            }}
          >
            <div
              style={{
                fontSize: 10,
                fontWeight: 700,
                color: C.sage,
                textTransform: "uppercase",
                letterSpacing: 1.5,
                marginBottom: 8,
              }}
            >
              Wall Art
            </div>
            <div style={{ fontSize: 28, fontWeight: 800, color: C.navy }}>
              {s.wallArt.units}
            </div>
            <div style={{ fontSize: 10, color: C.navy, opacity: 0.5 }}>
              units \u00d7 ${s.wallArt.avg.toFixed(2)}
            </div>
            <div
              style={{
                fontSize: 18,
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
              borderRadius: 16,
              padding: 16,
              border: `1px solid ${C.ice}`,
              boxShadow: `0 2px 8px ${C.navy}06`,
            }}
          >
            <div
              style={{
                fontSize: 10,
                fontWeight: 700,
                color: C.gold,
                textTransform: "uppercase",
                letterSpacing: 1.5,
                marginBottom: 8,
              }}
            >
              Conference
            </div>
            <div style={{ fontSize: 28, fontWeight: 800, color: C.navy }}>
              {s.conference.units}
            </div>
            <div style={{ fontSize: 10, color: C.navy, opacity: 0.5 }}>
              units \u00d7 ${s.conference.avg.toFixed(2)}
            </div>
            <div
              style={{
                fontSize: 18,
                fontWeight: 700,
                color: C.gold,
                marginTop: 4,
              }}
            >
              ${(s.conference.units * s.conference.avg).toFixed(0)}
            </div>
          </div>
        </div>
      </AnimateIn>

      <AnimateIn delay={0.2}>
        <div
          style={{
            background: C.white,
            borderRadius: 16,
            padding: 16,
            border: `1px solid ${C.ice}`,
            boxShadow: `0 2px 8px ${C.navy}06`,
          }}
        >
          <h4
            style={{
              margin: "0 0 12px",
              color: C.navy,
              fontSize: 14,
              fontFamily: "Georgia, serif",
            }}
          >
            4-Week Plan
          </h4>
          {revenue.weeklyPlan.map((w, i) => (
            <div
              key={i}
              style={{
                display: "flex",
                gap: 10,
                padding: "12px 0",
                borderBottom: i < 3 ? `1px solid ${C.ice}` : "none",
              }}
            >
              <div
                style={{
                  minWidth: 40,
                  fontWeight: 800,
                  color: C.white,
                  background: C.gold,
                  borderRadius: 8,
                  padding: "4px 8px",
                  fontSize: 11,
                  textAlign: "center",
                  alignSelf: "flex-start",
                }}
              >
                {w.week}
              </div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontWeight: 600, color: C.navy, fontSize: 13 }}>
                  {w.focus}
                </div>
                <div
                  style={{
                    fontSize: 11,
                    color: C.navy,
                    opacity: 0.5,
                    marginTop: 2,
                  }}
                >
                  {w.actions}
                </div>
              </div>
              <div
                style={{
                  fontWeight: 700,
                  color: C.sage,
                  fontSize: 12,
                  flexShrink: 0,
                  alignSelf: "flex-start",
                }}
              >
                {w.revenue}
              </div>
            </div>
          ))}
        </div>
      </AnimateIn>
    </div>
  );
}

/* ── Sprint Checklist View ── */
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
  const pct = Math.round((done / total) * 100);

  return (
    <div>
      <AnimateIn>
        <div
          style={{
            background: `linear-gradient(145deg, ${C.sage}, ${C.navy})`,
            borderRadius: 24,
            padding: "24px 20px",
            marginBottom: 20,
            color: C.white,
            boxShadow: `0 8px 32px ${C.navy}44`,
          }}
        >
          <div
            style={{
              fontSize: 11,
              fontWeight: 700,
              textTransform: "uppercase",
              letterSpacing: 3,
              opacity: 0.8,
            }}
          >
            Launch Sprint
          </div>
          <div
            style={{
              display: "flex",
              alignItems: "baseline",
              gap: 8,
              margin: "4px 0 12px",
            }}
          >
            <span
              style={{
                fontSize: 44,
                fontWeight: 800,
                fontFamily: "Georgia, serif",
              }}
            >
              {done}
            </span>
            <span style={{ fontSize: 20, opacity: 0.5 }}>/ {total}</span>
          </div>
          <div
            style={{
              background: `${C.white}20`,
              borderRadius: 10,
              height: 16,
              overflow: "hidden",
              padding: 2,
            }}
          >
            <div
              style={{
                height: "100%",
                borderRadius: 8,
                background: C.gold,
                width: `${pct}%`,
                transition: "width 0.4s cubic-bezier(0.16, 1, 0.3, 1)",
                boxShadow: `0 0 12px ${C.gold}66`,
              }}
            />
          </div>
          <div style={{ fontSize: 11, marginTop: 8, opacity: 0.7 }}>
            {done === total
              ? "\u2728 Ready to launch!"
              : `${total - done} tasks remaining`}
          </div>
        </div>
      </AnimateIn>

      {categories.map((cat, catIdx) => (
        <AnimateIn key={cat} delay={catIdx * 0.08}>
          <div style={{ marginBottom: 20 }}>
            <div
              style={{
                fontSize: 11,
                fontWeight: 700,
                color: C.navy,
                textTransform: "uppercase",
                letterSpacing: 1.5,
                marginBottom: 8,
                paddingLeft: 4,
              }}
            >
              {cat}
            </div>
            {sprintChecklist.map((item, i) =>
              item.category === cat ? (
                <Pressable key={i} onClick={() => toggle(i)} activeScale={0.97}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: 12,
                      padding: "12px 14px",
                      background: checks[i] ? `${C.sage}12` : C.white,
                      borderRadius: 12,
                      marginBottom: 6,
                      border: `1px solid ${checks[i] ? `${C.sage}44` : C.ice}`,
                      boxShadow: `0 1px 4px ${C.navy}06`,
                      transition: "all 0.25s cubic-bezier(0.16, 1, 0.3, 1)",
                    }}
                  >
                    <div
                      style={{
                        width: 24,
                        height: 24,
                        borderRadius: 7,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        background: checks[i] ? C.sage : "transparent",
                        border: `2px solid ${checks[i] ? C.sage : C.peri}`,
                        transition: "all 0.25s cubic-bezier(0.16, 1, 0.3, 1)",
                        transform: checks[i] ? "scale(1.05)" : "scale(1)",
                      }}
                    >
                      <span
                        style={{
                          color: C.white,
                          fontSize: 14,
                          fontWeight: 700,
                          opacity: checks[i] ? 1 : 0,
                          transform: checks[i] ? "scale(1)" : "scale(0.5)",
                          transition: "all 0.2s cubic-bezier(0.16, 1, 0.3, 1)",
                        }}
                      >
                        \u2713
                      </span>
                    </div>
                    <span
                      style={{
                        flex: 1,
                        fontSize: 13,
                        color: C.navy,
                        lineHeight: 1.4,
                        textDecoration: checks[i] ? "line-through" : "none",
                        opacity: checks[i] ? 0.4 : 1,
                        transition: "all 0.25s ease",
                      }}
                    >
                      {item.task}
                    </span>
                    <span
                      style={{
                        fontSize: 11,
                        color: C.navy,
                        opacity: 0.3,
                        flexShrink: 0,
                      }}
                    >
                      {item.time}
                    </span>
                  </div>
                </Pressable>
              ) : null,
            )}
          </div>
        </AnimateIn>
      ))}
    </div>
  );
}

/* ── Main App Shell ── */
export default function BloomSoftCommandCenter() {
  const [view, setView] = useState("pipeline");
  const [activePhase, setActivePhase] = useState(0);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    setReady(true);
  }, []);

  const views = [
    { id: "pipeline", label: "Pipeline", icon: "\u26A1" },
    { id: "conference", label: "Conference", icon: "\uD83D\uDCD6" },
    { id: "revenue", label: "Revenue", icon: "\uD83D\uDCB0" },
    { id: "sprint", label: "Sprint", icon: "\uD83D\uDE80" },
  ];

  return (
    <div
      style={{
        background: `linear-gradient(180deg, ${C.ice}88 0%, #f0f2f5 30%, #f0f2f5 100%)`,
        minHeight: "100vh",
        fontFamily:
          "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif",
        opacity: ready ? 1 : 0,
        transition: "opacity 0.4s ease",
      }}
    >
      <div style={{ maxWidth: 480, margin: "0 auto", padding: "0 16px 100px" }}>
        {/* Header */}
        <AnimateIn>
          <div style={{ textAlign: "center", padding: "24px 0 8px" }}>
            <h1
              style={{
                margin: 0,
                color: C.navy,
                fontFamily: "Georgia, serif",
                fontSize: 28,
                letterSpacing: -0.5,
                lineHeight: 1.1,
              }}
            >
              Bloom Soft Co.
            </h1>
            <p
              style={{
                margin: "4px 0 0",
                fontSize: 12,
                fontStyle: "italic",
                background: `linear-gradient(90deg, ${C.gold}, ${C.blush})`,
                WebkitBackgroundClip: "text",
                WebkitTextFillColor: "transparent",
                fontWeight: 600,
              }}
            >
              Command Center
            </p>
          </div>
        </AnimateIn>

        {/* Tab Bar */}
        <AnimateIn delay={0.1}>
          <div
            style={{
              display: "flex",
              gap: 4,
              marginBottom: 16,
              background: C.white,
              borderRadius: 16,
              padding: 4,
              boxShadow: `0 2px 12px ${C.navy}10`,
            }}
          >
            {views.map((v) => (
              <Pressable
                key={v.id}
                onClick={() => setView(v.id)}
                activeScale={0.95}
                style={{ flex: 1 }}
              >
                <div
                  style={{
                    padding: "10px 4px",
                    borderRadius: 12,
                    textAlign: "center",
                    background: view === v.id ? C.navy : "transparent",
                    color: view === v.id ? C.white : `${C.navy}88`,
                    transition: "all 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                    boxShadow:
                      view === v.id ? `0 4px 12px ${C.navy}33` : "none",
                  }}
                >
                  <div style={{ fontSize: 16, lineHeight: 1 }}>{v.icon}</div>
                  <div style={{ fontSize: 10, fontWeight: 600, marginTop: 2 }}>
                    {v.label}
                  </div>
                </div>
              </Pressable>
            ))}
          </div>
        </AnimateIn>

        {/* Content */}
        <div
          key={view}
          style={{
            animation: "fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) both",
          }}
        >
          {view === "pipeline" && (
            <>
              <PhaseNav
                phases={phases}
                active={activePhase}
                setActive={setActivePhase}
              />
              <PhaseDetail key={activePhase} phase={phases[activePhase]} />
            </>
          )}
          {view === "conference" && <ConferenceView />}
          {view === "revenue" && <RevenueView />}
          {view === "sprint" && <SprintView />}
        </div>

        {/* Footer */}
        <div
          style={{
            textAlign: "center",
            marginTop: 32,
            fontSize: 10,
            color: C.navy,
            opacity: 0.25,
            lineHeight: 1.5,
          }}
        >
          Bloom Soft Co.
          <br />
          Owner: Chloe Swainston (13) \u00b7 Operator: Caleb Swainston
          <br />
          Target: $1,999
        </div>
      </div>
    </div>
  );
}
