#!/usr/bin/env python3
"""
Bloom Soft Co. — Conference Passport (Kids) PDF Generator
April 2026 General Conference Edition

Generates: conference-passport-kids-april-2026.pdf
Target: ~30 pages, 8.5x11
"""

import math
import os
import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas

# ── Brand Colors ──
BLUSH_PINK = HexColor("#F5B9C8")
SAGE_GREEN = HexColor("#A5C6B2")
WARM_GOLD = HexColor("#C3A564")
SKY_BLUE = HexColor("#B9D7F2")
DEEP_NAVY = HexColor("#323F5A")
CREAM = HexColor("#FDF8F0")
ICE_BLUE = HexColor("#D7E8FA")
SOFT_LAVENDER = HexColor("#E8D5E8")
PERIWINKLE = HexColor("#A0C0E4")

WIDTH, HEIGHT = letter
MARGIN = 0.75 * inch

# ── Floral Drawing Primitives ──

def draw_small_bloom(c, x, y, color, size=6):
    c.saveState()
    c.setFillColor(color)
    c.setStrokeColor(white)
    c.setLineWidth(0.3)
    for i in range(5):
        angle = i * 72
        px = x + size * math.cos(math.radians(angle))
        py = y + size * math.sin(math.radians(angle))
        c.circle(px, py, size * 0.55, fill=1, stroke=1)
    c.setFillColor(WARM_GOLD)
    c.circle(x, y, size * 0.35, fill=1, stroke=0)
    c.restoreState()

def draw_leaf(c, x, y, angle=45, size=12):
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
    c.saveState()
    c.translate(x, y)
    if corner == 1:
        c.scale(-1, 1)
    elif corner == 2:
        c.scale(-1, -1)
    elif corner == 3:
        c.scale(1, -1)
    draw_stem(c, 0, 0, 20, 30)
    draw_stem(c, 0, 0, -10, 35)
    draw_stem(c, 0, 0, 30, 15)
    draw_small_bloom(c, 20, 30, BLUSH_PINK, 5)
    draw_small_bloom(c, -10, 35, SKY_BLUE, 4)
    draw_small_bloom(c, 30, 15, SOFT_LAVENDER, 4.5)
    draw_leaf(c, 8, 12, 60, 10)
    draw_leaf(c, 18, 8, 30, 8)
    draw_leaf(c, -5, 18, 120, 9)
    c.setFillColor(WARM_GOLD)
    c.circle(25, 25, 2, fill=1, stroke=0)
    c.circle(-3, 28, 1.5, fill=1, stroke=0)
    c.restoreState()

def draw_small_floral(c, x, y, color=BLUSH_PINK):
    """Tiny floral accent for kids pages."""
    draw_small_bloom(c, x, y, color, 4)
    draw_leaf(c, x - 5, y - 6, 45, 7)
    draw_leaf(c, x + 5, y - 6, 135, 7)

# ── Destination Theme Drawings ──

def draw_mountain_meadow(c, x, y):
    """Session 1 theme: mountain silhouette + wildflowers."""
    c.saveState()
    # Mountains
    c.setFillColor(HexColor("#9BB5A8"))
    p = c.beginPath()
    p.moveTo(x - 40, y)
    p.lineTo(x - 15, y + 30)
    p.lineTo(x + 5, y + 10)
    p.lineTo(x + 25, y + 35)
    p.lineTo(x + 45, y)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # Snow cap
    c.setFillColor(white)
    p2 = c.beginPath()
    p2.moveTo(x + 20, y + 30)
    p2.lineTo(x + 25, y + 35)
    p2.lineTo(x + 30, y + 30)
    p2.close()
    c.drawPath(p2, fill=1, stroke=0)
    # Wildflowers at base
    draw_small_bloom(c, x - 20, y + 3, BLUSH_PINK, 3)
    draw_small_bloom(c, x, y + 3, SKY_BLUE, 3)
    draw_small_bloom(c, x + 15, y + 3, SOFT_LAVENDER, 3)
    c.restoreState()

def draw_river_water(c, x, y):
    """Session 2 theme: wave lines + water lilies."""
    c.saveState()
    c.setStrokeColor(SKY_BLUE)
    c.setLineWidth(1.5)
    for i in range(3):
        wy = y + i * 10
        p = c.beginPath()
        p.moveTo(x - 35, wy)
        p.curveTo(x - 20, wy + 6, x - 10, wy - 6, x, wy)
        p.curveTo(x + 10, wy + 6, x + 20, wy - 6, x + 35, wy)
        c.drawPath(p, fill=0, stroke=1)
    # Water lily
    draw_small_bloom(c, x + 5, y + 25, BLUSH_PINK, 4)
    draw_leaf(c, x - 2, y + 18, 0, 8)
    c.restoreState()

def draw_sunset_stars(c, x, y):
    """Session 3 theme: stars + evening flowers."""
    c.saveState()
    # Stars
    c.setFillColor(WARM_GOLD)
    star_positions = [(-25, 30), (-10, 35), (5, 25), (20, 33), (30, 20)]
    for sx, sy in star_positions:
        draw_star(c, x + sx, y + sy, 3)
    # Evening flower
    draw_small_bloom(c, x, y + 5, SOFT_LAVENDER, 4)
    draw_leaf(c, x - 6, y, 45, 7)
    c.restoreState()

def draw_star(c, x, y, size):
    """Draw a simple 5-pointed star."""
    c.saveState()
    p = c.beginPath()
    for i in range(5):
        angle = math.radians(90 + i * 72)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        if i == 0:
            p.moveTo(px, py)
        else:
            p.lineTo(px, py)
        # Inner point
        inner_angle = math.radians(90 + i * 72 + 36)
        ipx = x + size * 0.4 * math.cos(inner_angle)
        ipy = y + size * 0.4 * math.sin(inner_angle)
        p.lineTo(ipx, ipy)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()

def draw_sunrise(c, x, y):
    """Session 4 theme: sun rays + morning glories."""
    c.saveState()
    # Sun
    c.setFillColor(WARM_GOLD)
    c.circle(x, y + 20, 10, fill=1, stroke=0)
    # Rays
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(1)
    for i in range(8):
        angle = math.radians(i * 45)
        rx1 = x + 13 * math.cos(angle)
        ry1 = y + 20 + 13 * math.sin(angle)
        rx2 = x + 18 * math.cos(angle)
        ry2 = y + 20 + 18 * math.sin(angle)
        c.line(rx1, ry1, rx2, ry2)
    # Morning glory
    draw_small_bloom(c, x - 15, y + 5, SKY_BLUE, 4)
    draw_small_bloom(c, x + 15, y + 5, PERIWINKLE, 3.5)
    c.restoreState()

def draw_garden_gate(c, x, y):
    """Session 5 theme: arch + climbing roses."""
    c.saveState()
    # Arch
    c.setStrokeColor(SAGE_GREEN)
    c.setLineWidth(1.5)
    p = c.beginPath()
    p.moveTo(x - 18, y)
    p.lineTo(x - 18, y + 25)
    p.curveTo(x - 18, y + 40, x + 18, y + 40, x + 18, y + 25)
    p.lineTo(x + 18, y)
    c.drawPath(p, fill=0, stroke=1)
    # Climbing roses
    draw_small_bloom(c, x - 18, y + 15, BLUSH_PINK, 3)
    draw_small_bloom(c, x + 18, y + 20, BLUSH_PINK, 3)
    draw_small_bloom(c, x, y + 38, BLUSH_PINK, 3.5)
    draw_leaf(c, x - 22, y + 10, 90, 6)
    draw_leaf(c, x + 20, y + 14, 90, 6)
    c.restoreState()

# ── Stamp Outlines ──

def draw_temple_outline(c, x, y, size=30):
    """Temple stamp outline to color in."""
    c.saveState()
    c.setStrokeColor(HexColor("#C0B0A0"))
    c.setLineWidth(1)
    c.setFillColor(white)
    # Base
    c.rect(x - size * 0.6, y, size * 1.2, size * 0.5, fill=1, stroke=1)
    # Top section
    c.rect(x - size * 0.4, y + size * 0.5, size * 0.8, size * 0.4, fill=1, stroke=1)
    # Spire
    p = c.beginPath()
    p.moveTo(x - size * 0.1, y + size * 0.9)
    p.lineTo(x, y + size * 1.2)
    p.lineTo(x + size * 0.1, y + size * 0.9)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    # Door
    c.rect(x - size * 0.1, y, size * 0.2, size * 0.3, fill=0, stroke=1)
    c.restoreState()

def draw_mountain_outline(c, x, y, size=30):
    c.saveState()
    c.setStrokeColor(HexColor("#C0B0A0"))
    c.setLineWidth(1)
    c.setFillColor(white)
    p = c.beginPath()
    p.moveTo(x - size, y)
    p.lineTo(x - size * 0.2, y + size)
    p.lineTo(x + size * 0.1, y + size * 0.6)
    p.lineTo(x + size * 0.4, y + size * 1.1)
    p.lineTo(x + size, y)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.restoreState()

def draw_tree_outline(c, x, y, size=30):
    c.saveState()
    c.setStrokeColor(HexColor("#C0B0A0"))
    c.setLineWidth(1)
    c.setFillColor(white)
    # Trunk
    c.rect(x - size * 0.1, y, size * 0.2, size * 0.4, fill=1, stroke=1)
    # Foliage
    c.circle(x, y + size * 0.7, size * 0.4, fill=1, stroke=1)
    c.restoreState()

def draw_sun_outline(c, x, y, size=25):
    c.saveState()
    c.setStrokeColor(HexColor("#C0B0A0"))
    c.setLineWidth(1)
    c.setFillColor(white)
    c.circle(x, y + size * 0.5, size * 0.35, fill=1, stroke=1)
    for i in range(8):
        angle = math.radians(i * 45)
        rx1 = x + size * 0.45 * math.cos(angle)
        ry1 = y + size * 0.5 + size * 0.45 * math.sin(angle)
        rx2 = x + size * 0.6 * math.cos(angle)
        ry2 = y + size * 0.5 + size * 0.6 * math.sin(angle)
        c.line(rx1, ry1, rx2, ry2)
    c.restoreState()

def draw_flower_outline(c, x, y, size=25):
    c.saveState()
    c.setStrokeColor(HexColor("#C0B0A0"))
    c.setLineWidth(1)
    c.setFillColor(white)
    for i in range(5):
        angle = math.radians(90 + i * 72)
        px = x + size * 0.3 * math.cos(angle)
        py = y + size * 0.5 + size * 0.3 * math.sin(angle)
        c.circle(px, py, size * 0.2, fill=1, stroke=1)
    c.circle(x, y + size * 0.5, size * 0.15, fill=1, stroke=1)
    # Stem
    c.line(x, y + size * 0.2, x, y)
    draw_leaf(c, x - 5, y + size * 0.1, 45, 8)
    c.restoreState()

STAMP_DRAWERS = [draw_temple_outline, draw_mountain_outline, draw_tree_outline,
                 draw_sun_outline, draw_flower_outline]
THEME_DRAWERS = [draw_mountain_meadow, draw_river_water, draw_sunset_stars,
                 draw_sunrise, draw_garden_gate]

# ── Session Data ──

SESSION_NAMES = [
    "Saturday Morning Landing",
    "Saturday Afternoon Station",
    "Saturday Evening Summit",
    "Sunday Morning Meadow",
    "Sunday Afternoon Arrival",
]

SESSION_THEMES = [
    "Mountain Meadow",
    "River & Water",
    "Sunset & Stars",
    "Sunrise",
    "Garden Gate",
]

FEELINGS = ["Happy", "Peaceful", "Thinking", "Loved", "Brave", "Amazed"]
FEELING_COLORS = [WARM_GOLD, SAGE_GREEN, SKY_BLUE, BLUSH_PINK, PERIWINKLE, SOFT_LAVENDER]

# ── Word Search ──

WORD_SEARCH_WORDS = [
    "PROPHET", "TEMPLE", "PRAYER", "FAITH", "JESUS",
    "BAPTISM", "REPENTANCE", "SPIRIT", "FAMILY", "COVENANT",
    "SERVE", "LOVE", "LISTEN", "GROW", "PEACE"
]

def generate_word_search(size=15):
    """Generate a solvable word search grid with all words placed."""
    grid = [['' for _ in range(size)] for _ in range(size)]
    placed_words = []
    directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]

    random.seed(42)  # Reproducible

    sorted_words = sorted(WORD_SEARCH_WORDS, key=len, reverse=True)

    for word in sorted_words:
        placed = False
        attempts = 0
        while not placed and attempts < 500:
            attempts += 1
            d = random.choice(directions)
            r = random.randint(0, size - 1)
            col = random.randint(0, size - 1)

            # Check if word fits
            end_r = r + d[0] * (len(word) - 1)
            end_c = col + d[1] * (len(word) - 1)
            if end_r < 0 or end_r >= size or end_c < 0 or end_c >= size:
                continue

            # Check conflicts
            ok = True
            for i, ch in enumerate(word):
                cr = r + d[0] * i
                cc = col + d[1] * i
                if grid[cr][cc] != '' and grid[cr][cc] != ch:
                    ok = False
                    break
            if not ok:
                continue

            # Place word
            for i, ch in enumerate(word):
                cr = r + d[0] * i
                cc = col + d[1] * i
                grid[cr][cc] = ch
            placed_words.append(word)
            placed = True

    # Fill empty cells with random letters
    for r in range(size):
        for col in range(size):
            if grid[r][col] == '':
                grid[r][col] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    return grid, placed_words

# ── Maze Generation ──

def generate_maze(rows=11, cols=11):
    """Generate a solvable maze using recursive backtracking.
    Returns a 2D grid where True = wall, False = path.
    Guaranteed solvable with 2 dead ends."""
    maze = [[True] * cols for _ in range(rows)]
    random.seed(42)

    def carve(r, col):
        maze[r][col] = False
        dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc]:
                maze[r + dr // 2][col + dc // 2] = False
                carve(nr, nc)

    carve(1, 1)
    # Ensure start and end are open
    maze[0][1] = False  # Start
    maze[rows - 1][cols - 2] = False  # End

    return maze

# ── Bingo Data ──

BINGO_WORDS = [
    "Someone says\n\"Jesus Christ\"", "A hymn\nis sung", "Temples are\nmentioned",
    "A prophet\nspeaks", "Someone\ncries", "Scripture is\nquoted",
    "Missionary\nwork", "A story\nis told", "Prayer is\nmentioned",
    "Family is\nmentioned", "Repentance", "Holy Ghost\nmentioned",
    "FREE\nSPACE", "Service to\nothers", "Baptism\nmentioned",
    "A child\nis mentioned", "Scriptures\nquoted", "Love is\nmentioned",
    "Faith", "Gratitude\nexpressed", "Covenant\nmentioned",
    "Peace\nmentioned", "A promise\nis made", "Prophets of\nold mentioned",
    "Forgiveness\nmentioned",
]

# ── Page Helpers ──

def page_background(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)

def draw_header_line(c, y):
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(0.5)
    c.line(MARGIN, y, WIDTH - MARGIN, y)

def draw_writing_lines(c, start_y, count, spacing=22, left=MARGIN, right=None):
    if right is None:
        right = WIDTH - MARGIN
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(0.3)
    y = start_y
    for _ in range(count):
        c.line(left, y, right, y)
        y -= spacing
    return y

def footer(c, page_num):
    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor("#A09080"))
    c.drawCentredString(WIDTH / 2, 0.4 * inch,
                        "Bloom Soft Co.  \u00b7  Conference Passport  \u00b7  April 2026")
    c.drawRightString(WIDTH - MARGIN, 0.4 * inch, str(page_num))


def build_pdf():
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              "products", "conference", "kids")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "conference-passport-kids-april-2026.pdf")

    c = canvas.Canvas(output_path, pagesize=letter)
    c.setTitle("Conference Passport \u2014 Kids \u2014 April 2026")
    c.setAuthor("Bloom Soft Co.")

    page_num = [0]

    def new_page():
        if page_num[0] > 0:
            c.showPage()
        page_num[0] += 1
        page_background(c)

    # ═══════════════════════════════════════
    # PAGE 1: Cover
    # ═══════════════════════════════════════
    new_page()

    draw_floral_cluster(c, MARGIN + 10, HEIGHT - MARGIN - 10, corner=2)
    draw_floral_cluster(c, WIDTH - MARGIN - 10, HEIGHT - MARGIN - 10, corner=3)
    draw_floral_cluster(c, MARGIN + 10, MARGIN + 50, corner=0)
    draw_floral_cluster(c, WIDTH - MARGIN - 10, MARGIN + 50, corner=1)

    # Scattered small blooms for playful feel
    draw_small_bloom(c, WIDTH / 2 - 80, HEIGHT / 2 + 120, SKY_BLUE, 4)
    draw_small_bloom(c, WIDTH / 2 + 90, HEIGHT / 2 + 100, BLUSH_PINK, 3.5)
    draw_small_bloom(c, WIDTH / 2 - 60, HEIGHT / 2 - 80, SOFT_LAVENDER, 3)
    draw_small_bloom(c, WIDTH / 2 + 70, HEIGHT / 2 - 60, WARM_GOLD, 3.5)

    c.setFont("Times-BoldItalic", 30)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 70, "Conference")
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 32, "Passport")

    c.setFont("Times-Italic", 14)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 5, "April 2026 General Conference")

    c.setFont("Helvetica", 11)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 30,
                        "The Church of Jesus Christ of Latter-day Saints")

    # Name field
    c.setFont("Times-Italic", 12)
    c.setFillColor(HexColor("#808080"))
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 70, "Traveler's Name:")
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(0.5)
    c.line(WIDTH / 2 - 100, HEIGHT / 2 - 85, WIDTH / 2 + 100, HEIGHT / 2 - 85)

    c.setFont("Times-Italic", 10)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, MARGIN + 20, "Bloom Soft Co.")

    # ═══════════════════════════════════════
    # PAGE 2: How Your Passport Works
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "How Your Passport Works")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    y = HEIGHT - MARGIN - 75
    steps = [
        ("\u2708 Pack Your Bags!", "You're about to go on a 5-session journey through General Conference!"),
        ("\u270f Write It Down", "Each session is a new destination. Listen carefully and write what you hear and feel."),
        ("\ud83d\ude0a How Did It Feel?", "After each session, color in the face that matches your feelings."),
        ("\ud83c\udfa8 Do the Activity!", "After each session, there's a fun activity waiting for you!"),
        ("\ud83c\udfb2 Play Bingo!", "Use your Bingo card during sessions. Can you get BINGO?"),
        ("\ud83c\udf1f Collect Your Stamps!", "Color in a stamp at each destination to complete your journey."),
        ("\ud83d\udcaa Make Your Bracelet!", "At the end, cut out your promise strips and make a bracelet!"),
    ]

    for emoji, text in steps:
        c.setFont("Times-Bold", 13)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN + 5, y, emoji)
        c.drawString(MARGIN + 25, y, text.split(",")[0] if "," in text else text)
        y -= 15
        if "," in text:
            c.setFont("Helvetica", 10)
            c.setFillColor(HexColor("#5A5A5A"))
            c.drawString(MARGIN + 25, y, text.split(",", 1)[1].strip())
            y -= 10
        y -= 12

    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

    # ═══════════════════════════════════════
    # PAGE 3: Journey Map
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "My Conference Journey")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    # Draw a winding path with 5 destination stops
    path_y_positions = [HEIGHT - MARGIN - 110, HEIGHT - MARGIN - 210,
                        HEIGHT - MARGIN - 310, HEIGHT - MARGIN - 410,
                        HEIGHT - MARGIN - 510]
    path_x_positions = [MARGIN + 80, WIDTH - MARGIN - 80, MARGIN + 80,
                        WIDTH - MARGIN - 80, WIDTH / 2]

    # Draw connecting path
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(2)
    c.setDash(6, 4)
    for i in range(4):
        c.line(path_x_positions[i], path_y_positions[i],
               path_x_positions[i + 1], path_y_positions[i + 1])
    c.setDash()

    # Draw destination circles with theme icons
    for i in range(5):
        px, py = path_x_positions[i], path_y_positions[i]

        # Destination circle
        c.setFillColor(white)
        c.setStrokeColor(WARM_GOLD)
        c.setLineWidth(1.5)
        c.circle(px, py, 25, fill=1, stroke=1)

        # Session number
        c.setFont("Times-Bold", 16)
        c.setFillColor(DEEP_NAVY)
        c.drawCentredString(px, py - 5, str(i + 1))

        # Session name
        c.setFont("Helvetica", 8)
        c.setFillColor(HexColor("#5A5A5A"))
        name_x = px + 35 if i % 2 == 0 else px - 35
        align = "left" if i % 2 == 0 else "right"
        if i == 4:
            c.drawCentredString(px, py - 35, SESSION_NAMES[i])
        elif align == "left":
            c.drawString(px + 30, py - 3, SESSION_NAMES[i])
        else:
            c.drawRightString(px - 30, py - 3, SESSION_NAMES[i])

        # Theme icon near destination
        theme_offset_x = 45 if i % 2 == 0 else -45
        if i == 4:
            theme_offset_x = 0

    # Start and end labels
    c.setFont("Times-BoldItalic", 11)
    c.setFillColor(SAGE_GREEN)
    c.drawCentredString(path_x_positions[0], path_y_positions[0] + 35, "START!")

    c.setFont("Times-BoldItalic", 11)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(path_x_positions[4], path_y_positions[4] - 40, "FINISHED!")

    draw_floral_cluster(c, MARGIN + 10, MARGIN + 40, corner=0)

    # ═══════════════════════════════════════
    # PAGES 4+: Session Destination Pages + Feelings + Activities
    # ═══════════════════════════════════════

    for session_idx in range(5):
        # ── Destination Page ──
        new_page()
        footer(c, page_num[0])

        # Theme art
        theme_drawer = THEME_DRAWERS[session_idx]
        theme_drawer(c, WIDTH - MARGIN - 40, HEIGHT - MARGIN - 35)

        c.setFont("Times-BoldItalic", 20)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, HEIGHT - MARGIN - 30, SESSION_NAMES[session_idx])

        c.setFont("Times-Italic", 11)
        c.setFillColor(WARM_GOLD)
        c.drawString(MARGIN, HEIGHT - MARGIN - 48, f"Session {session_idx + 1} \u2014 {SESSION_THEMES[session_idx]}")

        draw_header_line(c, HEIGHT - MARGIN - 55)

        # Stamp box with unique outline
        stamp_x = WIDTH - MARGIN - 70
        stamp_y = HEIGHT - MARGIN - 160
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.setLineWidth(1)
        c.setDash(3, 2)
        c.rect(stamp_x, stamp_y, 60, 60, fill=0, stroke=1)
        c.setDash()
        c.setFont("Helvetica", 6)
        c.setFillColor(HexColor("#A09080"))
        c.drawCentredString(stamp_x + 30, stamp_y - 10, "Color me in!")

        # Unique stamp outline inside box
        STAMP_DRAWERS[session_idx](c, stamp_x + 30, stamp_y + 8, 18)

        # What I heard
        y = HEIGHT - MARGIN - 80
        c.setFont("Times-Bold", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "What I Heard:")
        y -= 8
        draw_writing_lines(c, y, 4, spacing=20, right=stamp_x - 15)

        y -= 90
        c.setFont("Times-Bold", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "My Favorite Speaker:")
        y -= 5
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.line(MARGIN + 120, y, WIDTH - MARGIN, y)

        y -= 25
        c.setFont("Times-Bold", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "Something I Want to Remember:")
        y -= 8
        draw_writing_lines(c, y, 4, spacing=20)

        y -= 95
        c.setFont("Times-Bold", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, "A Question I Have:")
        y -= 8
        draw_writing_lines(c, y, 2, spacing=20)

        # Small floral accent
        draw_small_floral(c, MARGIN + 15, MARGIN + 50)

        # ── How Did This Session Feel? Page ──
        new_page()
        footer(c, page_num[0])

        c.setFont("Times-BoldItalic", 20)
        c.setFillColor(DEEP_NAVY)
        c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                            "How Did This Session Feel?")

        draw_header_line(c, HEIGHT - MARGIN - 45)

        c.setFont("Times-Italic", 11)
        c.setFillColor(HexColor("#5A5A5A"))
        c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                            f"Session {session_idx + 1}: {SESSION_NAMES[session_idx]}")

        # Feeling faces — 3x2 grid
        y = HEIGHT - MARGIN - 100
        face_size = 25
        face_labels = FEELINGS
        cols = 3
        col_width = (WIDTH - 2 * MARGIN) / cols

        for i, (feeling, fcolor) in enumerate(zip(face_labels, FEELING_COLORS)):
            row = i // cols
            col = i % cols
            fx = MARGIN + col * col_width + col_width / 2
            fy = y - row * 90

            # Circle for face
            c.setStrokeColor(fcolor)
            c.setLineWidth(2)
            c.setFillColor(white)
            c.circle(fx, fy, face_size, fill=1, stroke=1)

            # Label below
            c.setFont("Times-Bold", 10)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(fx, fy - face_size - 12, feeling)

            # Instruction
            c.setFont("Helvetica", 7)
            c.setFillColor(HexColor("#A09080"))
            c.drawCentredString(fx, fy - face_size - 24, "circle me!")

        # Draw/write section
        draw_y = y - 220
        c.setFont("Times-Bold", 13)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, draw_y, "Draw or write about how you feel:")

        draw_y -= 10
        # Drawing box
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.setLineWidth(0.5)
        box_height = draw_y - MARGIN - 30
        c.rect(MARGIN, MARGIN + 30, WIDTH - 2 * MARGIN, box_height, fill=0, stroke=1)

        draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

        # ── Activity Page (unique per session) ──
        new_page()
        footer(c, page_num[0])

        if session_idx == 0:
            # WORD SEARCH
            c.setFont("Times-BoldItalic", 20)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Conference Word Search")

            draw_header_line(c, HEIGHT - MARGIN - 45)

            c.setFont("Times-Italic", 10)
            c.setFillColor(HexColor("#5A5A5A"))
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 60,
                                "Find all 15 Conference words hidden in the grid!")

            grid, placed = generate_word_search(15)

            # Draw grid
            cell_size = 22
            grid_w = 15 * cell_size
            grid_x = (WIDTH - grid_w) / 2
            grid_y = HEIGHT - MARGIN - 85

            for r in range(15):
                for col_idx in range(15):
                    cx = grid_x + col_idx * cell_size
                    cy = grid_y - r * cell_size

                    c.setStrokeColor(HexColor("#D4C5B0"))
                    c.setLineWidth(0.3)
                    c.rect(cx, cy - cell_size, cell_size, cell_size, fill=0, stroke=1)

                    c.setFont("Courier-Bold", 11)
                    c.setFillColor(DEEP_NAVY)
                    c.drawCentredString(cx + cell_size / 2, cy - cell_size + 6,
                                        grid[r][col_idx])

            # Word list below grid
            list_y = grid_y - 15 * cell_size - 20
            c.setFont("Times-Bold", 10)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(WIDTH / 2, list_y, "Words to Find:")

            list_y -= 15
            # 3 columns of words
            words_per_col = 5
            col_w = (WIDTH - 2 * MARGIN) / 3
            c.setFont("Helvetica", 9)
            c.setFillColor(HexColor("#5A5A5A"))
            for i, word in enumerate(WORD_SEARCH_WORDS):
                col = i // words_per_col
                row = i % words_per_col
                wx = MARGIN + col * col_w + 10
                wy = list_y - row * 14
                c.drawString(wx, wy, f"\u25a1 {word}")

            draw_small_floral(c, WIDTH - MARGIN - 20, MARGIN + 50, SKY_BLUE)

        elif session_idx == 1:
            # TEMPLE MAZE
            c.setFont("Times-BoldItalic", 20)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Temple Maze")

            draw_header_line(c, HEIGHT - MARGIN - 45)

            c.setFont("Times-Italic", 10)
            c.setFillColor(HexColor("#5A5A5A"))
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 60,
                                "Find your way to the temple!")

            maze = generate_maze(21, 21)
            cell_size = 20
            maze_rows = len(maze)
            maze_cols = len(maze[0])
            maze_w = maze_cols * cell_size
            maze_h = maze_rows * cell_size
            maze_x = (WIDTH - maze_w) / 2
            maze_y = HEIGHT - MARGIN - 85

            # Draw maze
            for r in range(maze_rows):
                for col_idx in range(maze_cols):
                    cx = maze_x + col_idx * cell_size
                    cy = maze_y - r * cell_size

                    if maze[r][col_idx]:  # Wall
                        c.setFillColor(SAGE_GREEN)
                        c.rect(cx, cy - cell_size, cell_size, cell_size, fill=1, stroke=0)
                    else:
                        c.setFillColor(white)
                        c.rect(cx, cy - cell_size, cell_size, cell_size, fill=1, stroke=0)

            # Start label
            c.setFont("Times-Bold", 10)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(maze_x + cell_size, maze_y + 10, "Start")

            # Temple at end
            end_x = maze_x + (maze_cols - 2) * cell_size + cell_size / 2
            end_y = maze_y - maze_rows * cell_size - 5
            draw_temple_outline(c, end_x, end_y, 12)
            c.setFont("Helvetica", 7)
            c.setFillColor(HexColor("#A09080"))
            c.drawCentredString(end_x, end_y - 10, "Temple!")

            draw_small_floral(c, MARGIN + 20, MARGIN + 50, BLUSH_PINK)

        elif session_idx == 2:
            # SCRIPTURE CARD
            c.setFont("Times-BoldItalic", 20)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                                "Design Your Scripture Card")

            draw_header_line(c, HEIGHT - MARGIN - 45)

            c.setFont("Times-Italic", 10)
            c.setFillColor(HexColor("#5A5A5A"))
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                                "Design a card you can keep in your scriptures!")

            # Card template — large centered card
            card_w = WIDTH - 2.5 * inch
            card_h = 5 * inch
            card_x = (WIDTH - card_w) / 2
            card_y = (HEIGHT - card_h) / 2 - 0.3 * inch

            # Decorative border
            c.setStrokeColor(WARM_GOLD)
            c.setLineWidth(1.5)
            c.rect(card_x, card_y, card_w, card_h, fill=0, stroke=1)

            # Inner border
            inner = 8
            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(0.5)
            c.rect(card_x + inner, card_y + inner,
                   card_w - 2 * inner, card_h - 2 * inner, fill=0, stroke=1)

            # Floral corners on card
            draw_small_floral(c, card_x + 20, card_y + card_h - 20, BLUSH_PINK)
            draw_small_floral(c, card_x + card_w - 20, card_y + card_h - 20, SKY_BLUE)
            draw_small_floral(c, card_x + 20, card_y + 20, SOFT_LAVENDER)
            draw_small_floral(c, card_x + card_w - 20, card_y + 20, SAGE_GREEN)

            # Scripture reference
            y = card_y + card_h - 50
            c.setFont("Times-Bold", 12)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(WIDTH / 2, y, "Scripture Reference:")
            y -= 5
            c.setStrokeColor(HexColor("#D4C5B0"))
            c.line(card_x + 30, y, card_x + card_w - 30, y)

            # Verse text
            y -= 30
            c.setFont("Times-Bold", 12)
            c.drawCentredString(WIDTH / 2, y, "The Verse:")
            y -= 8
            draw_writing_lines(c, y, 5, spacing=22,
                               left=card_x + 25, right=card_x + card_w - 25)

            # Why this matters
            y -= 130
            c.setFont("Times-Bold", 12)
            c.drawCentredString(WIDTH / 2, y, "Why This Matters to Me:")
            y -= 8
            draw_writing_lines(c, y, 3, spacing=22,
                               left=card_x + 25, right=card_x + card_w - 25)

        elif session_idx == 3:
            # TRADING CARD
            c.setFont("Times-BoldItalic", 20)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                                "My Favorite Speaker Trading Card")

            draw_header_line(c, HEIGHT - MARGIN - 45)

            # Card
            card_w = 4.5 * inch
            card_h = 6.5 * inch
            card_x = (WIDTH - card_w) / 2
            card_y = (HEIGHT - card_h) / 2 - 0.4 * inch

            c.setStrokeColor(WARM_GOLD)
            c.setLineWidth(2)
            c.setFillColor(HexColor("#FFFDF7"))
            c.roundRect(card_x, card_y, card_w, card_h, 10, fill=1, stroke=1)

            y = card_y + card_h - 30

            # Portrait box
            portrait_size = 1.5 * inch
            portrait_x = card_x + card_w / 2 - portrait_size / 2
            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(1)
            c.rect(portrait_x, y - portrait_size, portrait_size, portrait_size,
                   fill=0, stroke=1)
            c.setFont("Helvetica", 8)
            c.setFillColor(HexColor("#A09080"))
            c.drawCentredString(card_x + card_w / 2, y - portrait_size / 2 - 3,
                                "Draw their portrait!")

            y -= portrait_size + 25

            # Fields
            fields = [
                ("Name:", 1),
                ("Calling:", 1),
                ("Topic:", 1),
                ("Best Quote:", 2),
            ]

            for label, lines in fields:
                c.setFont("Times-Bold", 11)
                c.setFillColor(DEEP_NAVY)
                c.drawString(card_x + 20, y, label)
                y -= 5
                draw_writing_lines(c, y, lines, spacing=18,
                                   left=card_x + 20, right=card_x + card_w - 20)
                y -= lines * 18 + 8

            # Spirit Level (1-10)
            c.setFont("Times-Bold", 11)
            c.setFillColor(DEEP_NAVY)
            c.drawString(card_x + 20, y, "Spirit Level:")
            y -= 3
            for i in range(10):
                cx = card_x + 25 + i * 28
                c.setStrokeColor(WARM_GOLD)
                c.setLineWidth(1)
                c.circle(cx, y - 8, 8, fill=0, stroke=1)
                c.setFont("Helvetica", 7)
                c.setFillColor(HexColor("#A09080"))
                c.drawCentredString(cx, y - 11, str(i + 1))
            y -= 28

            # Would Listen Again (star rating)
            c.setFont("Times-Bold", 11)
            c.setFillColor(DEEP_NAVY)
            c.drawString(card_x + 20, y, "Would Listen Again:")
            for i in range(5):
                sx = card_x + 150 + i * 25
                c.setStrokeColor(WARM_GOLD)
                c.setLineWidth(1)
                draw_star_outline(c, sx, y + 3, 8)

            draw_small_floral(c, card_x + card_w - 25, card_y + 20, BLUSH_PINK)

        elif session_idx == 4:
            # FEELINGS MAP
            c.setFont("Times-BoldItalic", 20)
            c.setFillColor(DEEP_NAVY)
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                                "My Conference Feelings Map")

            draw_header_line(c, HEIGHT - MARGIN - 45)

            c.setFont("Times-Italic", 10)
            c.setFillColor(HexColor("#5A5A5A"))
            c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                                "Circle your feeling for each session to see your journey!")

            # Grid: 6 feelings x 5 sessions
            grid_top = HEIGHT - MARGIN - 95
            row_height = 55
            num_sessions = 5
            label_width = 1.2 * inch
            grid_left = MARGIN + label_width
            col_width = (WIDTH - MARGIN - grid_left) / num_sessions

            # Session headers
            for i in range(num_sessions):
                cx = grid_left + i * col_width + col_width / 2
                c.setFont("Helvetica-Bold", 8)
                c.setFillColor(DEEP_NAVY)
                c.drawCentredString(cx, grid_top + 15, f"Session")
                c.drawCentredString(cx, grid_top + 3, f"{i + 1}")

            # Feeling rows
            for fi, (feeling, fcolor) in enumerate(zip(FEELINGS, FEELING_COLORS)):
                ry = grid_top - fi * row_height - 20

                # Row background (alternating)
                if fi % 2 == 0:
                    c.setFillColor(HexColor("#FFF8EC"))
                    c.rect(MARGIN, ry - 15, WIDTH - 2 * MARGIN, row_height - 5,
                           fill=1, stroke=0)

                # Feeling label
                c.setFont("Times-Bold", 11)
                c.setFillColor(DEEP_NAVY)
                c.drawString(MARGIN + 10, ry, feeling)

                # Circles to mark
                for si in range(num_sessions):
                    cx = grid_left + si * col_width + col_width / 2
                    c.setStrokeColor(fcolor)
                    c.setLineWidth(1.5)
                    c.setFillColor(white)
                    c.circle(cx, ry + 3, 14, fill=1, stroke=1)

            # Grid lines
            c.setStrokeColor(HexColor("#E0D5C5"))
            c.setLineWidth(0.3)
            for i in range(num_sessions + 1):
                gx = grid_left + i * col_width
                c.line(gx, grid_top + 25, gx, grid_top - 6 * row_height + 30)

            draw_small_floral(c, WIDTH - MARGIN - 20, MARGIN + 50, WARM_GOLD)

    # ═══════════════════════════════════════
    # ALL ABOUT ME — Traveler Profile
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "All About Me!")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62, "Every traveler needs a passport photo!")

    y = HEIGHT - MARGIN - 90

    # Self-portrait box
    portrait_size = 2 * inch
    portrait_x = WIDTH / 2 - portrait_size / 2
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(1)
    c.rect(portrait_x, y - portrait_size, portrait_size, portrait_size, fill=0, stroke=1)
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#A09080"))
    c.drawCentredString(WIDTH / 2, y - portrait_size / 2 - 3, "Draw yourself here!")

    y -= portrait_size + 25

    about_fields = [
        "My Name:",
        "My Age:",
        "My Ward / Branch:",
        "My Favorite Scripture:",
        "My Favorite Hymn:",
        "What I Love About Conference:",
        "When I Grow Up, I Want To:",
    ]

    for field in about_fields:
        c.setFont("Times-Bold", 11)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, field)
        y -= 5
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.setLineWidth(0.3)
        c.line(MARGIN + 10, y, WIDTH - MARGIN, y)
        y -= 22

    draw_small_floral(c, WIDTH - MARGIN - 20, MARGIN + 50, BLUSH_PINK)
    draw_small_floral(c, MARGIN + 20, MARGIN + 50, SKY_BLUE)

    # ═══════════════════════════════════════
    # MY CONFERENCE PRAYERS
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "My Conference Prayers")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "What do you want to ask Heavenly Father about this Conference?")

    y = HEIGHT - MARGIN - 90

    prayer_prompts = [
        ("Before Conference:", "What question do you want answered?"),
        ("During Conference:", "What are you feeling thankful for?"),
        ("After Conference:", "What did Heavenly Father teach you?"),
    ]

    for title, prompt in prayer_prompts:
        c.setFont("Times-Bold", 13)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, title)
        y -= 15
        c.setFont("Times-Italic", 10)
        c.setFillColor(HexColor("#5A5A5A"))
        c.drawString(MARGIN + 10, y, prompt)
        y -= 8
        draw_writing_lines(c, y, 5, spacing=20, left=MARGIN + 10)
        y -= 115

    draw_floral_cluster(c, WIDTH - MARGIN - 15, MARGIN + 40, corner=1)

    # ═══════════════════════════════════════
    # CONFERENCE COLORING PAGE
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Color This Garden!")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "Color these flowers while you listen to Conference!")

    # Draw large colorable floral scene using outlines only
    c.setStrokeColor(HexColor("#C0B0A0"))
    c.setLineWidth(1)

    # Ground line
    ground_y = MARGIN + 1.5 * inch
    c.line(MARGIN + 20, ground_y, WIDTH - MARGIN - 20, ground_y)

    # Large flowers to color (outlines)
    flower_positions = [
        (MARGIN + 1.5 * inch, ground_y, 2 * inch),
        (WIDTH / 2, ground_y, 2.5 * inch),
        (WIDTH - MARGIN - 1.5 * inch, ground_y, 1.8 * inch),
        (MARGIN + 2.8 * inch, ground_y, 1.5 * inch),
        (WIDTH - MARGIN - 2.8 * inch, ground_y, 2.2 * inch),
    ]

    for fx, fy, fh in flower_positions:
        # Stem
        c.line(fx, fy, fx, fy + fh)
        # Leaves on stem
        draw_leaf(c, fx - 8, fy + fh * 0.3, 45, 15)
        draw_leaf(c, fx + 8, fy + fh * 0.6, 135, 15)
        # Flower head (outline only, for coloring)
        c.setFillColor(white)
        for i in range(6):
            angle = math.radians(i * 60)
            px = fx + 15 * math.cos(angle)
            py = fy + fh + 15 * math.sin(angle)
            c.circle(px, py, 10, fill=1, stroke=1)
        c.circle(fx, fy + fh, 7, fill=1, stroke=1)

    # Butterflies
    for bx, by in [(MARGIN + 1 * inch, ground_y + 3 * inch),
                    (WIDTH - MARGIN - 1.2 * inch, ground_y + 2.5 * inch)]:
        # Simple butterfly outline
        c.circle(bx - 8, by + 5, 7, fill=0, stroke=1)
        c.circle(bx + 8, by + 5, 7, fill=0, stroke=1)
        c.circle(bx - 6, by - 5, 5, fill=0, stroke=1)
        c.circle(bx + 6, by - 5, 5, fill=0, stroke=1)
        c.line(bx, by + 10, bx, by - 8)

    # Sun in corner
    sun_x = WIDTH - MARGIN - 1 * inch
    sun_y = HEIGHT - MARGIN - 1.2 * inch
    c.circle(sun_x, sun_y, 20, fill=0, stroke=1)
    for i in range(12):
        angle = math.radians(i * 30)
        c.line(sun_x + 23 * math.cos(angle), sun_y + 23 * math.sin(angle),
               sun_x + 30 * math.cos(angle), sun_y + 30 * math.sin(angle))

    # ═══════════════════════════════════════
    # MY CONFERENCE DOODLE PAGE
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Draw What You Heard!")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "Draw a picture of your favorite Conference moment!")

    # Large empty drawing box
    box_top = HEIGHT - MARGIN - 80
    box_bottom = MARGIN + 50
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(0.5)
    c.rect(MARGIN + 10, box_bottom, WIDTH - 2 * MARGIN - 20, box_top - box_bottom,
           fill=0, stroke=1)

    # Small floral accents in corners of box
    draw_small_floral(c, MARGIN + 25, box_top - 15, BLUSH_PINK)
    draw_small_floral(c, WIDTH - MARGIN - 25, box_top - 15, SKY_BLUE)
    draw_small_floral(c, MARGIN + 25, box_bottom + 15, SAGE_GREEN)
    draw_small_floral(c, WIDTH - MARGIN - 25, box_bottom + 15, SOFT_LAVENDER)

    # ═══════════════════════════════════════
    # BINGO CARD (filled)
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Conference Bingo!")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 60,
                        "Listen during each session. Mark the square when you hear it!")

    # BINGO header letters
    bingo_letters = "BINGO"
    cell_size = 1.2 * inch
    grid_w = 5 * cell_size
    grid_x = (WIDTH - grid_w) / 2
    grid_top = HEIGHT - MARGIN - 85

    header_colors = [BLUSH_PINK, SKY_BLUE, WARM_GOLD, SAGE_GREEN, SOFT_LAVENDER]

    for i, letter_ch in enumerate(bingo_letters):
        cx = grid_x + i * cell_size + cell_size / 2
        c.setFillColor(header_colors[i])
        c.rect(grid_x + i * cell_size, grid_top - 25, cell_size, 25, fill=1, stroke=0)
        c.setFont("Times-Bold", 18)
        c.setFillColor(white)
        c.drawCentredString(cx, grid_top - 20, letter_ch)

    # Grid cells
    for row in range(5):
        for col in range(5):
            idx = row * 5 + col
            cx = grid_x + col * cell_size
            cy = grid_top - 25 - row * cell_size

            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(0.5)
            c.setFillColor(white)
            c.rect(cx, cy - cell_size, cell_size, cell_size, fill=1, stroke=1)

            # Cell text
            text = BINGO_WORDS[idx]
            if idx == 12:  # Free space
                c.setFillColor(WARM_GOLD)
                c.circle(cx + cell_size / 2, cy - cell_size / 2, cell_size * 0.35,
                         fill=1, stroke=0)
                c.setFont("Times-Bold", 9)
                c.setFillColor(white)
            else:
                c.setFont("Helvetica", 7)
                c.setFillColor(DEEP_NAVY)

            lines = text.split("\n")
            text_y = cy - cell_size / 2 + (len(lines) - 1) * 5
            for line in lines:
                c.drawCentredString(cx + cell_size / 2, text_y, line)
                text_y -= 10

    draw_small_floral(c, grid_x - 15, grid_top - 25 - 5 * cell_size + 10, BLUSH_PINK)
    draw_small_floral(c, grid_x + grid_w + 15, grid_top - 25 - 5 * cell_size + 10, SKY_BLUE)

    # ═══════════════════════════════════════
    # BLANK BINGO CARD
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                        "Make Your Own Conference Bingo!")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "Fill in your own squares before the next session!")

    # BINGO header
    for i, letter_ch in enumerate(bingo_letters):
        cx = grid_x + i * cell_size + cell_size / 2
        c.setFillColor(header_colors[i])
        c.rect(grid_x + i * cell_size, grid_top - 25, cell_size, 25, fill=1, stroke=0)
        c.setFont("Times-Bold", 18)
        c.setFillColor(white)
        c.drawCentredString(cx, grid_top - 20, letter_ch)

    # Empty grid
    for row in range(5):
        for col in range(5):
            idx = row * 5 + col
            cx = grid_x + col * cell_size
            cy = grid_top - 25 - row * cell_size

            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(0.5)
            c.setFillColor(white)
            c.rect(cx, cy - cell_size, cell_size, cell_size, fill=1, stroke=1)

            if idx == 12:  # Free space
                c.setFillColor(WARM_GOLD)
                c.circle(cx + cell_size / 2, cy - cell_size / 2, cell_size * 0.35,
                         fill=1, stroke=0)
                c.setFont("Times-Bold", 9)
                c.setFillColor(white)
                c.drawCentredString(cx + cell_size / 2, cy - cell_size / 2 + 3, "FREE")
                c.drawCentredString(cx + cell_size / 2, cy - cell_size / 2 - 7, "SPACE")

    draw_small_floral(c, grid_x - 15, grid_top - 25 - 5 * cell_size + 10, SAGE_GREEN)

    # ═══════════════════════════════════════
    # PROMISE BRACELET
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                        "My Conference Promise Bracelet")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    y = HEIGHT - MARGIN - 62
    c.drawCentredString(WIDTH / 2, y,
                        "Write a promise on each strip. Cut them out.")
    y -= 14
    c.drawCentredString(WIDTH / 2, y,
                        "Tape or glue into loops and connect them into a bracelet chain.")
    y -= 14
    c.drawCentredString(WIDTH / 2, y,
                        "Wear it to church next Sunday!")

    # 5 strips
    strip_top = y - 30
    strip_h = 0.9 * inch
    strip_gap = 15
    strip_colors = [BLUSH_PINK, SKY_BLUE, SAGE_GREEN, WARM_GOLD, SOFT_LAVENDER]

    for i in range(5):
        sy = strip_top - i * (strip_h + strip_gap)

        # Dotted cut-line border
        c.saveState()
        c.setStrokeColor(HexColor("#B0A090"))
        c.setLineWidth(0.6)
        c.setDash(4, 3)
        c.rect(MARGIN, sy - strip_h, WIDTH - 2 * MARGIN, strip_h, fill=0, stroke=1)
        c.restoreState()

        # Scissors
        c.setFont("Helvetica", 10)
        c.setFillColor(HexColor("#A09080"))
        c.drawString(MARGIN - 5, sy - 8, "\u2702")

        # "I will..." prompt
        c.setFont("Times-BoldItalic", 12)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN + 15, sy - 20, f"Session {i + 1}: I will...")

        # Writing line
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.setLineWidth(0.3)
        c.line(MARGIN + 15, sy - strip_h + 20, WIDTH - MARGIN - 40, sy - strip_h + 20)

        # Floral end-cap
        draw_small_floral(c, WIDTH - MARGIN - 20, sy - strip_h / 2, strip_colors[i])

    # ═══════════════════════════════════════
    # MY CONFERENCE HEROES
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "My Conference Heroes")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    c.setFont("Times-Italic", 10)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 62,
                        "Who were your favorite speakers? Draw or write about them!")

    y = HEIGHT - MARGIN - 90

    for i in range(3):
        # Hero card
        card_h = 1.8 * inch
        card_y = y - card_h

        c.setStrokeColor(WARM_GOLD)
        c.setLineWidth(1)
        c.setFillColor(HexColor("#FFFDF7"))
        c.roundRect(MARGIN, card_y, WIDTH - 2 * MARGIN, card_h, 8, fill=1, stroke=1)

        # Portrait box
        portrait_s = 1.2 * inch
        c.setStrokeColor(HexColor("#D4C5B0"))
        c.setLineWidth(0.5)
        c.rect(MARGIN + 15, card_y + (card_h - portrait_s) / 2,
               portrait_s, portrait_s, fill=0, stroke=1)

        c.setFont("Helvetica", 7)
        c.setFillColor(HexColor("#A09080"))
        c.drawCentredString(MARGIN + 15 + portrait_s / 2,
                            card_y + (card_h - portrait_s) / 2 + portrait_s / 2 - 3,
                            "Draw them!")

        # Fields
        fx = MARGIN + 15 + portrait_s + 15
        fy = card_y + card_h - 25

        fields = ["Name:", "What they talked about:", "What I liked best:"]
        for field in fields:
            c.setFont("Times-Bold", 9)
            c.setFillColor(DEEP_NAVY)
            c.drawString(fx, fy, field)
            fy -= 5
            c.setStrokeColor(HexColor("#D4C5B0"))
            c.setLineWidth(0.3)
            c.line(fx, fy, WIDTH - MARGIN - 15, fy)
            fy -= 18

        y = card_y - 15

    draw_small_floral(c, WIDTH - MARGIN - 20, MARGIN + 50, BLUSH_PINK)

    # ═══════════════════════════════════════
    # MY FAVORITE THINGS FROM CONFERENCE
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30,
                        "My Favorite Things!")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    y = HEIGHT - MARGIN - 75

    favorites = [
        ("My favorite talk was about:", 2),
        ("My favorite song was:", 1),
        ("The funniest moment was:", 2),
        ("Something that made me feel the Spirit:", 2),
        ("Something I want to tell my friends about:", 2),
        ("A goal I'm setting for myself:", 2),
    ]

    for prompt, lines in favorites:
        c.setFont("Times-Bold", 11)
        c.setFillColor(DEEP_NAVY)
        c.drawString(MARGIN, y, prompt)
        y -= 8
        y = draw_writing_lines(c, y, lines, spacing=18, left=MARGIN + 10)
        y -= 12

    draw_small_floral(c, WIDTH - MARGIN - 20, MARGIN + 50, SAGE_GREEN)
    draw_small_floral(c, MARGIN + 20, MARGIN + 50, SKY_BLUE)

    # ═══════════════════════════════════════
    # NOTES PAGE
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    c.setFont("Times-BoldItalic", 22)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 30, "Extra Notes & Doodles")

    draw_header_line(c, HEIGHT - MARGIN - 45)

    draw_writing_lines(c, HEIGHT - MARGIN - 65, 28, spacing=22)

    draw_small_floral(c, WIDTH - MARGIN - 20, MARGIN + 50, WARM_GOLD)

    # ═══════════════════════════════════════
    # CERTIFICATE OF COMPLETION
    # ═══════════════════════════════════════
    new_page()
    footer(c, page_num[0])

    # Gold border
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(2)
    c.rect(MARGIN - 10, MARGIN + 20, WIDTH - 2 * MARGIN + 20,
           HEIGHT - 2 * MARGIN - 10, fill=0, stroke=1)

    # Inner border
    c.setStrokeColor(HexColor("#D4C5B0"))
    c.setLineWidth(0.5)
    c.rect(MARGIN, MARGIN + 30, WIDTH - 2 * MARGIN,
           HEIGHT - 2 * MARGIN - 30, fill=0, stroke=1)

    # Floral corners
    draw_floral_cluster(c, MARGIN + 20, HEIGHT - MARGIN - 20, corner=2)
    draw_floral_cluster(c, WIDTH - MARGIN - 20, HEIGHT - MARGIN - 20, corner=3)
    draw_floral_cluster(c, MARGIN + 20, MARGIN + 60, corner=0)
    draw_floral_cluster(c, WIDTH - MARGIN - 20, MARGIN + 60, corner=1)

    c.setFont("Times-BoldItalic", 28)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 80, "Certificate")
    c.setFont("Times-BoldItalic", 20)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 110, "of Completion")

    c.setFont("Times-Italic", 12)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, HEIGHT - MARGIN - 145, "This certifies that")

    # Name line
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(0.8)
    c.line(MARGIN + 80, HEIGHT / 2 + 40, WIDTH - MARGIN - 80, HEIGHT / 2 + 40)
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#A09080"))
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 28, "(write your name)")

    c.setFont("Times-Italic", 12)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2,
                        "has completed the Conference Passport")
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 18,
                        "for the April 2026 General Conference of")
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 36,
                        "The Church of Jesus Christ of Latter-day Saints")

    c.setFont("Times-BoldItalic", 14)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 70,
                        "5 Sessions \u00b7 5 Adventures \u00b7 Journey Complete!")

    # Date line
    c.setFont("Times-Italic", 10)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, MARGIN + 100, "Date: ________________")

    c.setFont("Times-Italic", 9)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, MARGIN + 70, "Bloom Soft Co.")

    # ═══════════════════════════════════════
    # BACK COVER
    # ═══════════════════════════════════════
    new_page()

    draw_floral_cluster(c, WIDTH / 2 - 30, HEIGHT / 2 + 40, corner=0)
    draw_floral_cluster(c, WIDTH / 2 + 30, HEIGHT / 2 + 40, corner=1)
    draw_floral_cluster(c, WIDTH / 2, HEIGHT / 2 - 20, corner=2)

    # Scattered small blooms
    draw_small_bloom(c, WIDTH / 2 - 80, HEIGHT / 2 + 80, SKY_BLUE, 3)
    draw_small_bloom(c, WIDTH / 2 + 80, HEIGHT / 2 + 70, BLUSH_PINK, 3)
    draw_small_bloom(c, WIDTH / 2 - 60, HEIGHT / 2 - 50, WARM_GOLD, 2.5)

    c.setFont("Times-BoldItalic", 18)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 80, "Bloom Soft Co.")

    c.setFont("Times-Italic", 11)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 60, "soft \u00b7 intentional \u00b7 beautiful")

    c.setFont("Times-BoldItalic", 14)
    c.setFillColor(DEEP_NAVY)
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 + 20, "You did it, explorer!")
    c.setFont("Times-Italic", 11)
    c.setFillColor(HexColor("#5A5A5A"))
    c.drawCentredString(WIDTH / 2, HEIGHT / 2, "5 sessions. 5 adventures. All yours.")

    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#A09080"))
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 60,
                        "For personal and family use.")
    c.drawCentredString(WIDTH / 2, HEIGHT / 2 - 75,
                        "Not an official publication of The Church of Jesus Christ of Latter-day Saints.")

    c.save()
    return output_path, page_num[0]


def draw_star_outline(c, x, y, size):
    """Draw a star outline (not filled)."""
    c.saveState()
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(1)
    p = c.beginPath()
    for i in range(5):
        angle = math.radians(90 + i * 72)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        if i == 0:
            p.moveTo(px, py)
        else:
            p.lineTo(px, py)
        inner_angle = math.radians(90 + i * 72 + 36)
        ipx = x + size * 0.4 * math.cos(inner_angle)
        ipy = y + size * 0.4 * math.sin(inner_angle)
        p.lineTo(ipx, ipy)
    p.close()
    c.drawPath(p, fill=0, stroke=1)
    c.restoreState()


if __name__ == "__main__":
    path, pages = build_pdf()
    print(f"Generated: {path}")
    print(f"Total pages: {pages}")
