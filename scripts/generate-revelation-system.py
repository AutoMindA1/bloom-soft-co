#!/usr/bin/env python3
"""
Bloom Soft Co. — Conference Revelation System PDF Generator
April 2026 General Conference Edition

Generates: conference-revelation-system-april-2026.pdf
Target: ~32 pages, 8.5x11
"""

import math
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

# ── Brand Colors ──
BLUSH_PINK = HexColor("#F5B9C8")
SAGE_GREEN = HexColor("#A5C6B2")
WARM_GOLD = HexColor("#C3A564")
SKY_BLUE = HexColor("#B9D7F2")
DEEP_NAVY = HexColor("#323F5A")
CREAM = HexColor("#FDF8F0")
LIGHT_CREAM = HexColor("#FFFDF7")
ICE_BLUE = HexColor("#D7E8FA")
PERIWINKLE = HexColor("#A0C0E4")
SOFT_LAVENDER = HexColor("#E8D5E8")

WIDTH, HEIGHT = letter  # 8.5 x 11 inches
MARGIN = 0.75 * inch

# ── Floral Drawing Primitives ──

def draw_small_bloom(c, x, y, color, size=6):
    """Draw a simple 5-petal flower."""
    c.saveState()
    c.setFillColor(color)
    c.setStrokeColor(white)
    c.setLineWidth(0.3)
    for i in range(5):
        angle = i * 72
        px = x + size * math.cos(math.radians(angle))
        py = y + size * math.sin(math.radians(angle))
        c.circle(px, py, size * 0.55, fill=1, stroke=1)
    # center
    c.setFillColor(WARM_GOLD)
    c.circle(x, y, size * 0.35, fill=1, stroke=0)
    c.restoreState()

def draw_leaf(c, x, y, angle=45, size=12):
    """Draw a simple leaf shape."""
    c.saveState()
    c.setFillColor(SAGE_GREEN)
    c.setStrokeColor(HexColor("#8BB09E"))
    c.setLineWidth(0.5)
    c.translate(x, y)
    c.rotate(angle)
    p = c.beginPath()
    p.moveTo(0, 0)
    p.curveTo(size * 0.4, size * 0.6, size * 0.8, size * 0.5, size, 0)
    p.curveTo(size * 0.8, -size * 0.5, size * 0.4, -size * 0.6, 0, 0)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.restoreState()

def draw_stem(c, x1, y1, x2, y2):
    """Draw a curved stem."""
    c.saveState()
    c.setStrokeColor(SAGE_GREEN)
    c.setLineWidth(1)
    mx = (x1 + x2) / 2 + 8
    my = (y1 + y2) / 2
    p = c.beginPath()
    p.moveTo(x1, y1)
    p.curveTo(mx, y1, mx, y2, x2, y2)
    c.drawPath(p, fill=0, stroke=1)
    c.restoreState()

def draw_floral_cluster(c, x, y, corner=0):
    """Draw a small wildflower cluster (~1 inch). corner: 0=TR, 1=TL, 2=BL, 3=BR"""
    c.saveState()
    c.translate(x, y)
    if corner == 1:
        c.scale(-1, 1)
    elif corner == 2:
        c.scale(-1, -1)
    elif corner == 3:
        c.scale(1, -1)

    # Stems
    draw_stem(c, 0, 0, 20, 30)
    draw_stem(c, 0, 0, -10, 35)
    draw_stem(c, 0, 0, 30, 15)

    # Blooms
    draw_small_bloom(c, 20, 30, BLUSH_PINK, 5)
    draw_small_bloom(c, -10, 35, SKY_BLUE, 4)
    draw_small_bloom(c, 30, 15, SOFT_LAVENDER, 4.5)

    # Leaves
    draw_leaf(c, 8, 12, 60, 10)
    draw_leaf(c, 18, 8, 30, 8)
    draw_leaf(c, -5, 18, 120, 9)

    # Small buds
    c.setFillColor(WARM_GOLD)
    c.circle(25, 25, 2, fill=1, stroke=0)
    c.circle(-3, 28, 1.5, fill=1, stroke=0)

    c.restoreState()

def draw_gold_corner_accent(c, x, y, size=30, corner=0):
    """Draw a small gold vine corner accent."""
    c.saveState()
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(0.8)
    c.translate(x, y)
    if corner == 1:
        c.scale(-1, 1)
    elif corner == 2:
        c.scale(-1, -1)
    elif corner == 3:
        c.scale(1, -1)
    p = c.beginPath()
    p.moveTo(0, size)
    p.lineTo(0, 0)
    p.lineTo(size, 0)
    c.drawPath(p, fill=0, stroke=1)
    # small curl
    p2 = c.beginPath()
    p2.moveTo(0, size * 0.6)
    p2.curveTo(size * 0.15, size * 0.4, size * 0.3, size * 0.15, size * 0.6, 0)
    c.drawPath(p2, fill=0, stroke=1)
    c.restoreState()

# ── Page Templates ──

def page_background(c):
    """Cream background."""
    c.setFillColor(CREAM)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)

def draw_header_line(c, y):
    """Thin gold decorative line."""
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(0.5)
    c.line(MARGIN, y, WIDTH - MARGIN, y)

def draw_writing_lines(c, start_y, count, spacing=22, left=MARGIN, right=None):
    """Draw lined writing area."""
    if right is None:
        right = WIDTH - MARGIN
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(0.3)
    y = start_y
    for _ in range(count):
        c.line(left, y, right, y)
        y -= spacing
    return y

def draw_dotted_line(c, x1, y1, x2, y2):
    """Draw a dotted line."""
    c.saveState()
    c.setStrokeColor(HexColor("#B0A090"))
    c.setLineWidth(0.5)
    c.setDash(3, 3)
    c.line(x1, y1, x2, y2)
    c.restoreState()

# ── Content Data ──

SESSION_NAMES = [
    "Saturday Morning",
    "Saturday Afternoon",
    "Saturday Evening",
    "Sunday Morning",
    "Sunday Afternoon",
]

SESSION_SUBTITLES = [
    "Session 1",
    "Session 2",
    "Session 3 — Priesthood / General",
    "Session 4",
    "Session 5",
]

REFLECT_PROMPTS = [
    # Session 1 — Saturday Morning
    [
        ("First Impressions", "What surprised you? What wasn't what you expected?"),
        ("Strongest Feeling", "What moment hit you the hardest?"),
        ("One Quote", "Write the single sentence you most want to remember."),
        ("Christ Connection", "Where did you see the Savior in this session?"),
        ("Immediate Action", "One thing you'll do TODAY based on this session."),
    ],
    # Session 2 — Saturday Afternoon
    [
        ("Patterns Emerging", "Did anything from Session 1 come up again?"),
        ("Doctrine vs. Invitation", "Was this session more about teaching or asking you to act?"),
        ("Speaker Spotlight", "Which speaker felt like they were talking directly to you?"),
        ("Scripture Thread", "What scripture kept coming to mind?"),
        ("Immediate Action", "One thing you'll do TODAY."),
    ],
    # Session 3 — Saturday Evening
    [
        ("Midpoint Check", "What's the theme God keeps repeating to YOU?"),
        ("Prophetic Weight", "What did the prophet emphasize? Why does it matter NOW?"),
        ("Personal Warning", "Was there a warning you needed to hear?"),
        ("Promise Claimed", "What blessing was offered and what's the condition?"),
        ("Immediate Action", "One thing you'll do TODAY."),
    ],
    # Session 4 — Sunday Morning
    [
        ("Deepening", "How has your understanding shifted since Saturday?"),
        ("The Repeated Message", "God has now said this [X] times \u2014 what is it?"),
        ("Testimony Moment", "When did you KNOW something was true?"),
        ("Connection to Your Life", "What specific situation does this apply to?"),
        ("Immediate Action", "One thing you'll do TODAY."),
    ],
    # Session 5 — Sunday Afternoon
    [
        ("Final Impression", "If you could only keep ONE thing from this entire Conference, what is it?"),
        ("The Pattern of Your Revelation", "Look back at all 5 sessions. What type of revelation came most? (D/I/P/W/T)"),
        ("Letter to Future Me", "Write 3\u20134 sentences to yourself at October Conference about what you felt and what you promised."),
        ("Gratitude", "What are you most thankful for after this weekend?"),
        ("Covenant", "What will you DO differently starting tomorrow?"),
    ],
]

DIPT_TYPES = [
    ("D", "Doctrine", "A truth was clarified or confirmed"),
    ("I", "Invitation", "You felt prompted to act"),
    ("P", "Promise", "A blessing was offered with a condition"),
    ("W", "Warning", "A caution or correction was given"),
    ("T", "Testimony", "Your witness of truth was strengthened"),
]

THIRTY_DAY_ITEMS = [
    "Re-read your Session 1 notes. What still resonates?",
    "Act on one \"Immediate Action\" you wrote down.",
    "Share one insight from Conference with a family member.",
    "Read a scripture referenced in Conference.",
    "Pray about the theme God repeated to you.",
    "Write in your journal about how Conference changed your week.",
    "Listen to one Conference talk again (churchofjesuschrist.org).",
    "Act on your Session 2 \"Immediate Action.\"",
    "Identify one habit to start based on Conference counsel.",
    "Teach someone what you learned about the Savior.",
    "Re-read your \"Letter to Future Me.\" Still feel it?",
    "Fast with a Conference-inspired purpose.",
    "Act on your Session 3 \"Immediate Action.\"",
    "Review your DIPT tags. Which type dominated? Why?",
    "Memorize one quote from your notes.",
    "Share your Conference experience in a Church class or conversation.",
    "Act on your Session 4 \"Immediate Action.\"",
    "Read a General Conference talk you missed.",
    "Write about how you've changed since Conference weekend.",
    "Identify a promise you claimed. Are you keeping the condition?",
    "Act on your Session 5 \"Immediate Action.\"",
    "Study the scriptures referenced in the talk that moved you most.",
    "Express gratitude to someone God brought to mind during Conference.",
    "Review all your \"Immediate Actions.\" How many did you do?",
    "Set a personal goal for the next 6 months based on Conference.",
    "Write a testimony statement shaped by Conference revelation.",
    "Listen to the prophet's talk one more time.",
    "Evaluate: What covenant are you keeping better now?",
    "Plan how you'll prepare differently for October Conference.",
    "Seal your growth. Write: \"Because of April Conference, I now...\""
]


def build_pdf():
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "products", "conference", "adult")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "conference-revelation-system-april-2026.pdf")

    c = canvas.Canvas(output_path, pagesize=letter)
    c.setTitle("Conference Revelation System — April 2026")
    c.setAuthor("Bloom Soft Co.")

    page_num = [0]

    def new_page():
        if page_num[0] > 0:
            c.showPage()
        page_num[0] += 1
        page_background(c)

    def footer(c):
        c.setFont("Helvetica", 7)
        c.setFillColor(HexColor("#A09080"))
        c.drawCentredString(WIDTH / 2, 0.4 * inch, f"Bloom Soft Co.  \u00b7  Conference Revelation System  \u00b7  April 2026")
        c.drawRightString(WIDTH - MARGIN, 0.4 * inch, f"{page_num[0]}")

    # ═══════════════════════════════════════
    # PAGE 1: Cover
    # ═══════════════════════════════════════
    new_page()

    # Floral accents on cover corners
    draw_floral_cluster(c, MARGIN + 10, HEIGHT - MARGIN - 10, corner=2)
    draw_floral_cluster(c, WIDTH - MARGIN - 10, HEIGHT - MARGIN - 10, corner=3)
    draw_floral_cluster(c, MARGIN + 10, MARGIN + 50, corner=0)
    draw_floral_cluster(c, WIDTH - MARGIN - 10, MARGIN + 50, corner=1)

    # Gold corner accents
    draw_gold_corner_accent(c, MARGIN + 5, HEIGHT - MARGIN - 5, 40, corner=2)
    draw_gold_corner_accent(c, WIDTH - MARGIN - 5, HEIGHT - MARGIN - 5, 40, corner=3)
    draw_gold_corner_accent(c, MARGIN + 5, MARGIN + 5, 40, corner=0)
    draw_gold_corner_accent(c, WIDTH - MARGIN - 5, MARGIN + 5, 40, corner=1)

    # Title
    c.setFont("Times-BoldItalic", 32)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 80, "Conference")
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 40, "Revelation System")

    c.setFont("Times-Italic", 16)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2, "April 2026 General Conference")

    c.setFont("Helvetica", 11)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 40, "The Church of Jesus Christ of Latter-day Saints")

    # Brand
    c.setFont("Times-Italic", 10)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, MARGIN + 20, "Bloom Soft Co.")

    # ═══════════════════════════════════════
    # PAGE 2: How to Use This System
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "How to Use This System")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    y = HEIGHT - MARGIN - 75
    instructions = [
        ("Before Each Session", [
            "Find a quiet, comfortable place to write.",
            "Pray briefly that the Spirit will teach you personally.",
            "Have this journal and a pen ready before the session begins."
        ]),
        ("During Each Session", [
            "Use the note-taking page to capture speakers, quotes, and impressions.",
            "Don't try to write everything \u2014 capture what the Spirit highlights for YOU.",
            "Mark moments that feel personal with a star \u2605 in the margin."
        ]),
        ("After Each Session", [
            "Turn to the Reflect & Apply page for that session.",
            "Answer each prompt honestly and specifically.",
            "Tag your revelations using the DIPT system (explained on the next page).",
            "Write your Immediate Action \u2014 something you'll do TODAY."
        ]),
        ("After Conference Weekend", [
            "Complete the 30-Day Challenge to keep your revelations alive.",
            "Write your Letter to My October Self and seal it.",
            "Cut out the Quote Cards and keep them where you'll see them."
        ]),
    ]

    c.setFont("Helvetica", 10)
    for section_title, items in instructions:
        c.setFont("Times-BoldItalic", 13)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, section_title)
        y -= 18
        c.setFont("Helvetica", 10)
        c.setFillColor(HexColor("#4A4A4A"))
        for item in items:
            c.drawString(MARGIN + 15, y, f"\u2022  {item}")
            y -= 15
        y -= 10

    # ═══════════════════════════════════════
    # PAGE 3: DIPT Revelation Tagging System
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "The DIPT Revelation Tagging System")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 11)
    c.setFillColor(HexColor("#4A4A4A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 65,
                        "As you listen, tag each revelation with a letter. Over time, patterns emerge.")

    y = HEIGHT - MARGIN - 100
    tag_colors = [BLUSH_PINK, SKY_BLUE, WARM_GOLD, HexColor("#E8A0A0"), SAGE_GREEN]

    for i, (letter_tag, name, desc) in enumerate(DIPT_TYPES):
        # Tag circle
        c.setFillColor(tag_colors[i])
        c.circle(MARGIN + 25, y + 5, 15, fill=1, stroke=0)
        c.setFont("Times-Bold", 16)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 25, y, letter_tag)

        # Label
        c.setFont("Times-Bold", 13)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN + 50, y + 5, name)

        c.setFont("Helvetica", 10)
        c.setFillColor(HexColor("#4A4A4A"))
        c.drawString(MARGIN + 50, y - 10, desc)

        y -= 50

    # Example box
    y -= 10
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(0.5)
    c.setFillColor(HexColor("#FFF8EC"))
    c.roundRect(MARGIN, y - 80, WIDTH - 2 * MARGIN, 80, 5, fill=1, stroke=1)

    c.setFont("Times-BoldItalic", 11)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN + 15, y - 15, "Example:")
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#4A4A4A"))
    c.drawString(MARGIN + 15, y - 32,
                 "\"If ye love me, keep my commandments\" \u2014 Elder Smith")
    c.drawString(MARGIN + 15, y - 47,
                 "Tags:  I  (invitation to act)  +  P  (promise of the Spirit)")
    c.drawString(MARGIN + 15, y - 62,
                 "By Session 5, you'll see which types God used most to speak to you.")

    # Floral accent
    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

    # ═══════════════════════════════════════
    # PAGES 4-13: Session Pages (5 sessions x 2 pages each)
    # ═══════════════════════════════════════

    for session_idx in range(5):
        # ── Session Note-Taking Page ──
        new_page()
        footer(c)

        # Floral accent — alternate corners per session
        corners_pos = [
            (WIDTH - MARGIN - 15, HEIGHT - MARGIN - 15, 1),  # top-right
            (MARGIN + 15, HEIGHT - MARGIN - 15, 0),           # top-left
            (WIDTH - MARGIN - 15, MARGIN + 40, 3),            # bottom-right
            (MARGIN + 15, MARGIN + 40, 2),                    # bottom-left
            (WIDTH - MARGIN - 15, HEIGHT - MARGIN - 15, 1),  # top-right
        ]
        cx, cy, cc = corners_pos[session_idx]
        draw_floral_cluster(c, cx, cy, corner=cc)

        # Session header
        c.setFont("Times-BoldItalic", 20)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, HEIGHT - MARGIN - 30, SESSION_NAMES[session_idx])

        c.setFont("Times-Italic", 11)
        c.setFillColor(WARM_GOLD)
        c.drawString(MARGIN, HEIGHT - MARGIN - 48, SESSION_SUBTITLES[session_idx])

        draw_header_line(c, HEIGHT - MARGIN - 55)

        # Speaker tracking boxes
        y = HEIGHT - MARGIN - 80
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "Speakers & Topics")
        y -= 5

        for _ in range(4):
            y -= 18
            c.setFont("Helvetica", 8)
            c.setFillColor(HexColor("#808080"))
            c.drawString(MARGIN + 5, y + 3, "Speaker:")
            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(0.3)
            c.line(MARGIN + 55, y, MARGIN + 200, y)
            c.drawString(MARGIN + 210, y + 3, "Topic:")
            c.line(MARGIN + 245, y, WIDTH - MARGIN - 60, y)
            c.drawString(WIDTH - MARGIN - 55, y + 3, "Tag:")
            c.line(WIDTH - MARGIN - 30, y, WIDTH - MARGIN, y)

        # Notes area
        y -= 25
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "Notes, Quotes & Impressions")
        y -= 8
        draw_writing_lines(c, y, 18, spacing=20)

        # ── Reflect & Apply Page ──
        new_page()
        footer(c)

        c.setFont("Times-BoldItalic", 18)
        c.setFillColor(DEEP_NAVY)
        c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                            f"Reflect & Apply \u2014 {SESSION_NAMES[session_idx]}")

        draw_header_line(c, HEIGHT - MARGIN - 45)

        # Floral accent on opposite corner from notes page
        opp_corners = [
            (MARGIN + 15, MARGIN + 40, 0),
            (WIDTH - MARGIN - 15, MARGIN + 40, 1),
            (MARGIN + 15, HEIGHT - MARGIN - 15, 2),
            (WIDTH - MARGIN - 15, HEIGHT - MARGIN - 15, 3),
            (MARGIN + 15, MARGIN + 40, 0),
        ]
        ox, oy, oc = opp_corners[session_idx]
        draw_floral_cluster(c, ox, oy, corner=oc)

        y = HEIGHT - MARGIN - 70
        prompts = REFLECT_PROMPTS[session_idx]

        for prompt_title, prompt_question in prompts:
            # Prompt title with gold accent
            c.setFillColor(WARM_GOLD)
            c.circle(MARGIN + 5, y + 4, 3, fill=1, stroke=0)

            c.setFont("Times-Bold", 12)
            c.setFillColor(DEEP_NAVY)
            c.drawString(MARGIN + 15, y, prompt_title)

            y -= 16
            c.setFont("Times-Italic", 10)
            c.setFillColor(HexColor("#5A5A5A"))
            c.drawString(MARGIN + 15, y, prompt_question)

            y -= 10
            y = draw_writing_lines(c, y, 3, spacing=18, left=MARGIN + 15)
            y -= 12

        # ── Scripture Study & Additional Notes Page ──
        new_page()
        footer(c)

        c.setFont("Times-BoldItalic", 18)
        c.setFillColor(DEEP_NAVY)
        c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                            f"Scripture Study \u2014 {SESSION_NAMES[session_idx]}")

        draw_header_line(c, HEIGHT - MARGIN - 45)

        # Floral accent
        draw_floral_cluster(c, WIDTH - MARGIN - 15, HEIGHT - MARGIN - 15, corner=1)

        y = HEIGHT - MARGIN - 70
        c.setFont("Times-Bold", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "Scriptures Referenced in This Session:")
        y -= 8

        for _ in range(4):
            y -= 20
            c.setFont("Helvetica", 8)
            c.setFillColor(HexColor("#808080"))
            c.drawString(MARGIN + 5, y + 3, "Reference:")
            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(0.3)
            c.line(MARGIN + 65, y, MARGIN + 220, y)
            c.drawString(MARGIN + 230, y + 3, "Context:")
            c.line(MARGIN + 270, y, WIDTH - MARGIN, y)

        y -= 30
        c.setFont("Times-Bold", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "One Scripture I Want to Study Deeper:")
        y -= 5
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.line(MARGIN, y, WIDTH - MARGIN, y)

        y -= 25
        c.setFont("Times-Bold", 12)
        c.drawString(MARGIN, y, "What the Spirit Taught Me Through This Scripture:")
        y -= 8
        draw_writing_lines(c, y, 6, spacing=20)

        y -= 135
        c.setFont("Times-Bold", 12)
        c.drawString(MARGIN, y, "Additional Notes & Impressions:")
        y -= 8
        draw_writing_lines(c, y, 6, spacing=20)

        draw_floral_cluster(c, MARGIN + 15, MARGIN + 40, corner=0)

    # ═══════════════════════════════════════
    # Conference Overview & Schedule Page
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 20)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Conference Overview")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    y = HEIGHT - MARGIN - 70
    c.setFont("Times-Bold", 13)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN, y, "April 2026 General Conference Schedule")

    y -= 25
    schedule = [
        ("Saturday Morning", "Session 1", "10:00 AM MT"),
        ("Saturday Afternoon", "Session 2", "2:00 PM MT"),
        ("Saturday Evening", "Session 3 \u2014 Priesthood/General", "6:00 PM MT"),
        ("Sunday Morning", "Session 4", "10:00 AM MT"),
        ("Sunday Afternoon", "Session 5", "2:00 PM MT"),
    ]

    for name, label, time in schedule:
        c.setFillColor(WARM_GOLD)
        c.circle(MARGIN + 8, y + 4, 5, fill=1, stroke=0)

        c.setFont("Times-Bold", 11)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN + 20, y, name)

        c.setFont("Helvetica", 10)
        c.setFillColor(HexColor("#5A5A5A"))
        c.drawString(MARGIN + 180, y, label)
        c.drawRightString(WIDTH - MARGIN, y, time)
        y -= 22

    y -= 15
    c.setFont("Times-Bold", 13)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN, y, "My Conference Goals")
    y -= 5

    goals = [
        "What do I most want to learn from this Conference?",
        "What question am I bringing to the Lord?",
        "What am I willing to change?",
    ]
    for goal in goals:
        y -= 18
        c.setFont("Times-Italic", 10)
        c.setFillColor(HexColor("#5A5A5A"))
        c.drawString(MARGIN + 10, y, goal)
        y -= 8
        draw_writing_lines(c, y, 3, spacing=18, left=MARGIN + 10)
        y -= 60

    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

    # ═══════════════════════════════════════
    # Personal Covenant Page
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "My Conference Covenant")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 11)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 65,
                        "After 5 sessions of revelation, what will you covenant to do?")

    y = HEIGHT - MARGIN - 100

    covenant_prompts = [
        ("I Will Start...", "A new practice, habit, or study I will begin."),
        ("I Will Stop...", "Something I will leave behind."),
        ("I Will Continue...", "Something I\u2019m already doing that was confirmed."),
        ("I Will Strengthen...", "A relationship or covenant I will deepen."),
        ("I Will Serve...", "Someone specific I will reach out to."),
    ]

    for title, desc in covenant_prompts:
        c.setFillColor(WARM_GOLD)
        c.circle(MARGIN + 5, y + 4, 3, fill=1, stroke=0)

        c.setFont("Times-Bold", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN + 15, y, title)

        y -= 15
        c.setFont("Times-Italic", 9)
        c.setFillColor(HexColor("#5A5A5A"))
        c.drawString(MARGIN + 15, y, desc)

        y -= 8
        y = draw_writing_lines(c, y, 3, spacing=18, left=MARGIN + 15)
        y -= 10

    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)
    draw_floral_cluster(c, MARGIN + 15, MARGIN + 40, corner=0)

    # ═══════════════════════════════════════
    # Testimony & Gratitude Page
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "My Testimony After Conference")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 11)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 65,
                        "Write your testimony as it stands after this weekend of revelation.")

    y = HEIGHT - MARGIN - 90
    draw_writing_lines(c, y, 12, spacing=22)

    y -= 12 * 22 + 20
    c.setFont("Times-Bold", 13)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN, y, "I Am Grateful For:")
    y -= 8
    draw_writing_lines(c, y, 8, spacing=22)

    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

    # ═══════════════════════════════════════
    # Speaker Index Page
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Speaker Index")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "Track every speaker across all 5 sessions for quick reference.")

    y = HEIGHT - MARGIN - 85

    # Table header
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN + 5, y, "#")
    c.drawString(MARGIN + 25, y, "Speaker Name")
    c.drawString(MARGIN + 180, y, "Session")
    c.drawString(MARGIN + 240, y, "Topic")
    c.drawString(WIDTH - MARGIN - 40, y, "Tag")
    y -= 3
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(0.5)
    c.line(MARGIN, y, WIDTH - MARGIN, y)

    # 25 rows
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(0.3)
    for i in range(25):
        y -= 20
        c.setFont("Helvetica", 8)
        c.setFillColor(HexColor("#B0A090"))
        c.drawString(MARGIN + 5, y + 3, str(i + 1))
        c.line(MARGIN + 25, y, MARGIN + 170, y)
        c.line(MARGIN + 180, y, MARGIN + 230, y)
        c.line(MARGIN + 240, y, WIDTH - MARGIN - 50, y)
        c.line(WIDTH - MARGIN - 40, y, WIDTH - MARGIN, y)

    draw_floral_cluster(c, MARGIN + 15, MARGIN + 40, corner=0)

    # ═══════════════════════════════════════
    # Additional Notes Pages (4 pages)
    # ═══════════════════════════════════════
    for notes_page in range(4):
        new_page()
        footer(c)

        c.setFont("Times-BoldItalic", 20)
        c.setFillColor(DEEP_NAVY)
        c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Notes")

        draw_header_line(c, HEIGHT - MARGIN - 45)

        draw_writing_lines(c, HEIGHT - MARGIN - 65, 30, spacing=22)

        if notes_page == 0:
            draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)
        else:
            draw_floral_cluster(c, MARGIN + 15, MARGIN + 40, corner=0)

    # ═══════════════════════════════════════
    # Revelation Summary
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 20)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "My Revelation Summary")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 11)
    c.setFillColor(HexColor("#4A4A4A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 65,
                        "Look across all 5 sessions. What patterns do you see?")

    y = HEIGHT - MARGIN - 95

    # DIPT tally
    c.setFont("Times-Bold", 13)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN, y, "Revelation Type Tally")
    y -= 25

    for i, (letter_tag, name, _) in enumerate(DIPT_TYPES):
        c.setFillColor(tag_colors[i])
        c.circle(MARGIN + 15, y + 4, 10, fill=1, stroke=0)
        c.setFont("Times-Bold", 12)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 15, y, letter_tag)

        c.setFont("Helvetica", 10)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN + 35, y, f"{name}:")

        # Tally boxes
        for j in range(10):
            bx = MARGIN + 120 + j * 25
            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(0.5)
            c.rect(bx, y - 5, 18, 18, fill=0, stroke=1)

        y -= 30

    # Dominant type
    y -= 10
    c.setFont("Times-Bold", 12)
    c.setFillColor(DEEP_NAVY)
    c.drawString(MARGIN, y, "My dominant revelation type this Conference:")
    y -= 5
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.line(MARGIN, y, WIDTH - MARGIN, y)

    y -= 30
    c.setFont("Times-Bold", 12)
    c.drawString(MARGIN, y, "What this tells me about how God speaks to me:")
    y -= 8
    draw_writing_lines(c, y, 5, spacing=20)

    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

    # ═══════════════════════════════════════
    # PAGE 15: 30-Day Challenge (page 1 of 2)
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 20)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "30-Day Post-Conference Challenge")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "One small action each day to keep your Conference revelations alive.")

    y = HEIGHT - MARGIN - 85

    for i in range(15):
        day_num = i + 1
        # Day circle
        c.setFillColor(tag_colors[i % 5])
        c.circle(MARGIN + 12, y + 3, 9, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 12, y, str(day_num))

        # Challenge text
        c.setFont("Helvetica", 9)
        c.setFillColor(HexColor("#4A4A4A"))
        c.drawString(MARGIN + 28, y, THIRTY_DAY_ITEMS[i])

        # Checkbox
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.setLineWidth(0.5)
        c.rect(WIDTH - MARGIN - 15, y - 3, 12, 12, fill=0, stroke=1)

        y -= 22

    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

    # ═══════════════════════════════════════
    # PAGE 16: 30-Day Challenge (page 2 of 2)
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 20)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "30-Day Challenge (continued)")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    y = HEIGHT - MARGIN - 70

    for i in range(15, 30):
        day_num = i + 1
        c.setFillColor(tag_colors[i % 5])
        c.circle(MARGIN + 12, y + 3, 9, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 12, y, str(day_num))

        c.setFont("Helvetica", 9)
        c.setFillColor(HexColor("#4A4A4A"))
        c.drawString(MARGIN + 28, y, THIRTY_DAY_ITEMS[i])

        c.setStrokeColor(HexColor("#D4C5B0"))
        c.setLineWidth(0.5)
        c.rect(WIDTH - MARGIN - 15, y - 3, 12, 12, fill=0, stroke=1)

        y -= 22

    draw_floral_cluster(c, MARGIN + 15, MARGIN + 40, corner=0)

    # ═══════════════════════════════════════
    # PAGE 17: Letter to My October Self
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    # Dotted border around entire page
    c.saveState()
    c.setStrokeColor(HexColor("#B0A090"))
    c.setLineWidth(0.8)
    c.setDash(4, 3)
    inset = 0.5 * inch
    c.rect(inset, inset, WIDTH - 2 * inset, HEIGHT - 2 * inset, fill=0, stroke=1)
    c.restoreState()

    # Scissors icon (simple representation)
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#A09080"))
    c.drawString(inset - 5, HEIGHT - inset - 15, "\u2702")

    # Fold & seal tab
    tab_y = inset + 20
    c.saveState()
    c.setStrokeColor(HexColor("#B0A090"))
    c.setLineWidth(0.5)
    c.setDash(2, 2)
    tab_w = 1.5 * inch
    tab_x = WIDTH / 2 - tab_w / 2
    c.rect(tab_x, tab_y - 10, tab_w, 20, fill=0, stroke=1)
    c.restoreState()

    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor("#A09080"))
    c.drawCentredString(WIDTH / 2, tab_y - 5, "\u2702  fold & seal  \u2702")

    # Title
    c.setFont("Times-BoldItalic", 24)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 40, "Letter to My October Self")

    c.setFont("Times-Italic", 12)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "Seal this page. Open it at October Conference.")

    draw_header_line(c, HEIGHT - MARGIN - 75)

    # Writing area
    y = HEIGHT - MARGIN - 100
    draw_writing_lines(c, y, 22, spacing=22, left=MARGIN + 10, right=WIDTH - MARGIN - 10)

    # Quote at bottom
    c.setFont("Times-Italic", 9)
    c.setFillColor(HexColor("#A09080"))
    c.drawCentredString(WIDTH / 2, inset + 45,
                        "\u201cRemember the feelings you had. They were real.\u201d")

    # Floral accents in corners inside the dotted border
    draw_floral_cluster(c, inset + 20, HEIGHT - inset - 10, corner=2)
    draw_floral_cluster(c, WIDTH - inset - 20, HEIGHT - inset - 10, corner=3)

    # ═══════════════════════════════════════
    # PAGE 18: Tear-Out Quote Cards
    # ═══════════════════════════════════════
    new_page()
    footer(c)

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Tear-Out Quote Cards")

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 48,
                        "Cut along the dotted lines. Keep these where you\u2019ll see them.")

    # 2x2 grid of cards
    card_w = (WIDTH - 2 * MARGIN - 0.3 * inch) / 2
    card_h = (HEIGHT - MARGIN - 1.2 * inch - MARGIN - 0.5 * inch) / 2
    card_top = HEIGHT - MARGIN - 70

    card_accents = [BLUSH_PINK, SKY_BLUE, SOFT_LAVENDER, SAGE_GREEN]
    card_corners = [0, 1, 2, 3]

    for row in range(2):
        for col in range(2):
            idx = row * 2 + col
            cx = MARGIN + col * (card_w + 0.3 * inch)
            cy = card_top - row * (card_h + 0.3 * inch)

            # Dotted border
            c.saveState()
            c.setStrokeColor(HexColor("#B0A090"))
            c.setLineWidth(0.6)
            c.setDash(4, 3)
            c.rect(cx, cy - card_h, card_w, card_h, fill=0, stroke=1)
            c.restoreState()

            # Scissors icon
            c.setFont("Helvetica", 10)
            c.setFillColor(HexColor("#A09080"))
            c.drawString(cx - 2, cy - 8, "\u2702")

            # Floral accent in corner
            accent_positions = [
                (cx + card_w - 15, cy - 15, 1),
                (cx + 15, cy - 15, 0),
                (cx + card_w - 15, cy - card_h + 15, 3),
                (cx + 15, cy - card_h + 15, 2),
            ]
            ax, ay, ac = accent_positions[idx]
            draw_floral_cluster(c, ax, ay, corner=ac)

            # Card content
            inner_x = cx + 15
            inner_y = cy - 30

            c.setFont("Times-Italic", 9)
            c.setFillColor(HexColor("#808080"))
            c.drawString(inner_x, inner_y, "My favorite quote from Conference:")

            inner_y -= 15
            draw_writing_lines(c, inner_y, 3, spacing=20,
                               left=inner_x, right=cx + card_w - 15)

            # Watermark
            c.setFont("Times-Italic", 7)
            c.setFillColor(HexColor("#D4C5B0"))
            c.drawCentredString(cx + card_w / 2, cy - card_h + 12, "Bloom Soft Co.")

    # ═══════════════════════════════════════
    # PAGE 19: Back Cover
    # ═══════════════════════════════════════
    new_page()

    # Floral clusters
    draw_floral_cluster(c, WIDTH / 2 - 30, HEIGHT / 2 + 40, corner=0)
    draw_floral_cluster(c, WIDTH / 2 + 30, HEIGHT / 2 + 40, corner=1)
    draw_floral_cluster(c, WIDTH / 2, HEIGHT / 2 - 20, corner=2)

    c.setFont("Times-BoldItalic", 18)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 80, "Bloom Soft Co.")

    c.setFont("Times-Italic", 11)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 60, "soft \u00b7 intentional \u00b7 beautiful")

    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#A09080"))
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 60,
                        "For personal and family use.")
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 75,
                        "Not an official publication of The Church of Jesus Christ of Latter-day Saints.")

    c.save()
    return output_path, page_num[0]


if __name__ == "__main__":
    path, pages = build_pdf()
    print(f"Generated: {path}")
    print(f"Total pages: {pages}")
