# Galaxy Voyage — Part 1: Concept, planning, perspective math
# Classwork 17 — Armando Karin Molina Marrufo

import pygame

# ============================================================
# INPUT - Load all settings from config.txt
# ============================================================
config = {}
with open('config.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line or '=' not in line:
            continue
        parameter, value = line.split('=')
        if ',' in value:
            config[parameter] = tuple(int(c.strip()) for c in value.split(','))
        elif '.' in value:
            config[parameter] = float(value)
        else:
            config[parameter] = int(value)

# ============================================================
# PROCESS - Helper functions
# ============================================================

def calculate_x_positions(surface, vertical_lines, space):
    # PROCESS - Build a list of equally-spaced x positions centered on screen
    x_positions = []
    width        = surface.get_width()
    spacing      = space * width
    central_line = width / 2
    offset       = -int(vertical_lines / 2)
    for _ in range(vertical_lines):
        x_positions.append(central_line + offset * spacing)
        offset += 1
    return x_positions

def calculate_y_positions(surface, horizontal_lines, vanishing_point, scroll_offset, power=2.0):
    # PROCESS - Apply power transform so lines bunch near horizon, spread near bottom
    # t = 0 at horizon, t = 1 at bottom of screen
    height           = surface.get_height()
    vy               = vanishing_point[1]
    available_height = height - vy
    y_positions      = []
    for i in range(horizontal_lines):
        t = ((i + 1) / horizontal_lines + scroll_offset) % 1.0
        t_curved = t ** power          # non-linear spacing = depth illusion
        y = vy + t_curved * available_height
        if vy < y < height:
            y_positions.append(int(y))
    return y_positions

def draw_vertical_lines(surface, x_positions, vanishing_point, color, line_width=2):
    # OUTPUT - Draw each vertical line from its bottom x toward the vanishing point
    height = surface.get_height()
    vx, vy = vanishing_point
    for x in x_positions:
        pygame.draw.line(surface, color, (int(x), height), (int(vx), int(vy)), line_width)

def draw_horizontal_lines(surface, y_positions, x_positions, vanishing_point, color, line_width=1):
    # OUTPUT - Draw horizontal lines; left/right endpoints shrink toward vanishing point
    screen_height = surface.get_height()
    vx, vy        = vanishing_point
    left_x  = x_positions[0]
    right_x = x_positions[-1]
    for y in y_positions:
        # PROCESS - Interpolate endpoints along the outermost perspective lines
        denom = vy - screen_height
        t  = (y - screen_height) / denom if denom != 0 else 0
        xl = left_x  + t * (vx - left_x)
        xr = right_x + t * (vx - right_x)
        pygame.draw.line(surface, color, (int(xl), y), (int(xr), y), line_width)

# ============================================================
# INITIALIZATION
# ============================================================
pygame.init()
screen = pygame.display.set_mode((config['width'], config['height']))
pygame.display.set_caption('Galaxy Voyage — Part 1')
clock = pygame.time.Clock()

# PROCESS - Compute vertical line positions once (they don't change)
x_positions = calculate_x_positions(
    surface        = screen,
    vertical_lines = config['vertical_lines'],
    space          = config['space']
)
print(f"x_positions (sanity check): {[round(x) for x in x_positions]}")

# PROCESS - Vanishing point: top-center of the screen
vanishing_point = (config['width'] * 0.5, config['height'] * 0.25)

# PROCESS - Scroll state
scroll_offset = 0.0

# ============================================================
# MAIN LOOP
# ============================================================
running = True
while running:

    # INPUT - Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # PROCESS - Advance scroll offset each frame
    scroll_offset = (scroll_offset + config['scroll_speed']) % 1.0

    # PROCESS - Recalculate horizontal line positions with current scroll
    y_positions = calculate_y_positions(
        surface          = screen,
        horizontal_lines = config['horizontal_lines'],
        vanishing_point  = vanishing_point,
        scroll_offset    = scroll_offset,
        power            = config['perspective_power']
    )

    # OUTPUT - Clear screen and draw grid
    screen.fill(config['bg_color'])
    draw_vertical_lines(screen, x_positions, vanishing_point, config['line_color'])
    draw_horizontal_lines(screen, y_positions, x_positions, vanishing_point, config['line_color'])

    # OUTPUT - Draw vanishing point marker
    pygame.draw.circle(screen, (255, 200, 50),
                       (int(vanishing_point[0]), int(vanishing_point[1])), 4)

    pygame.display.flip()
    clock.tick(config['fps'])

pygame.quit()
