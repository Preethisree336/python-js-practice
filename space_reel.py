import tkinter as tk
import math

# --- WINDOW SETUP (9:16 Instagram Reel Format) ---
WIDTH, HEIGHT = 540, 960
root = tk.Tk()
root.title("Space Door Animation")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1E1928", highlightthickness=0)
canvas.pack()

# Door position and sizes
door_w, door_h = 160, 320
door_x = (WIDTH - door_w) // 2
door_y = HEIGHT // 2 - 100

frame_counter = 0

def draw_scene():
    global frame_counter
    canvas.delete("all")  # Refresh frame

    # --- ANIMATION TIMELINE MATH ---
    door_open_ratio = 0.0
    space_object = None
    zoom_progress = 0.0
    is_shocked = False

    # 0 to 60 frames: Door closed
    # 60 to 120 frames: Open door 1
    if 60 <= frame_counter < 120:
        progress = (frame_counter - 60) / 60.0
        door_open_ratio = math.sin(progress * math.pi / 2)
    # 120 to 270 frames: Earth Zoom + Boy Shocked
    elif 120 <= frame_counter < 270:
        door_open_ratio = 1.0
        space_object = "EARTH"
        zoom_progress = (frame_counter - 120) / 150.0
        is_shocked = True
    # 270 to 330 frames: Close door 1
    elif 270 <= frame_counter < 330:
        progress = (frame_counter - 270) / 60.0
        door_open_ratio = 1.0 - math.sin(progress * math.pi / 2)
    # 330 to 390 frames: Open door 2
    elif 330 <= frame_counter < 390:
        progress = (frame_counter - 330) / 60.0
        door_open_ratio = math.sin(progress * math.pi / 2)
    # 390 to 540 frames: Sun Zoom + Boy Shocked
    elif 390 <= frame_counter < 540:
        door_open_ratio = 1.0
        space_object = "SUN"
        zoom_progress = (frame_counter - 390) / 150.0
        is_shocked = True
    # 540 to 600 frames: Close door 2
    elif 540 <= frame_counter < 600:
        progress = (frame_counter - 540) / 60.0
        door_open_ratio = 1.0 - math.sin(progress * math.pi / 2)

    # --- 1. WALL & FLOOR ---
    canvas.create_rectangle(0, door_y + door_h, WIDTH, HEIGHT, fill="#120F19", outline="")
    canvas.create_line(0, door_y + door_h, WIDTH, door_y + door_h, fill="#32283C", width=3)

    # --- 2. SPACE BACKGROUND BEHIND DOOR ---
    canvas.create_rectangle(door_x, door_y, door_x + door_w, door_y + door_h, fill="#05050C", outline="")
    for i in range(25):
        sx = door_x + ((i * 37) % door_w)
        sy = door_y + ((i * 73) % door_h)
        canvas.create_oval(sx, sy, sx + 2, sy + 2, fill="white", outline="")

    # --- 3. PLANETS (EARTH / SUN ZOOM) ---
    cx, cy = door_x + door_w // 2, door_y + door_h // 2
    
    if space_object == "EARTH":
        r = int(15 + math.pow(zoom_progress, 2.5) * 200)
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="#1E6DC8", outline="#64C8FF", width=max(1, int(r*0.05)))
        if r > 5:
            canvas.create_oval(cx - r*0.6, cy - r*0.6, cx + r*0.2, cy + r*0.2, fill="#3CB450", outline="")
            canvas.create_oval(cx - r*0.1, cy + r*0.1, cx + r*0.7, cy + r*0.7, fill="#3CB450", outline="")

    elif space_object == "SUN":
        r = int(20 + math.pow(zoom_progress, 2.2) * 250)
        for i in range(3, 0, -1):
            gr = int(r * (1 + i * 0.15))
            canvas.create_oval(cx - gr, cy - gr, cx + gr, cy + gr, fill="#FF5000", outline="")
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="#FFB400", outline="")
        canvas.create_oval(cx - r*0.6, cy - r*0.6, cx + r*0.6, cy + r*0.6, fill="#FFF0B4", outline="")

    # MASK WALLS (Keeps space only inside the doorway frame)
    canvas.create_rectangle(0, 0, door_x, HEIGHT, fill="#1E1928", outline="")
    canvas.create_rectangle(door_x + door_w, 0, WIDTH, HEIGHT, fill="#1E1928", outline="")
    canvas.create_rectangle(0, 0, WIDTH, door_y, fill="#1E1928", outline="")
    canvas.create_rectangle(0, door_y + door_h, WIDTH, HEIGHT, fill="#120F19", outline="")
    canvas.create_line(0, door_y + door_h, WIDTH, door_y + door_h, fill="#32283C", width=3)

    # --- 4. DOOR LEAF ANIMATION ---
    visible_w = int(door_w * (1.0 - door_open_ratio))
    if visible_w > 0:
        canvas.create_rectangle(door_x, door_y, door_x + visible_w, door_y + door_h, fill="#8C552D", outline="")
        if visible_w > 20:
            hx = door_x + visible_w - 15
            hy = door_y + door_h // 2
            canvas.create_oval(hx - 5, hy - 5, hx + 5, hy + 5, fill="#DCB43C", outline="")

    # --- 5. DOOR FRAME ---
    canvas.create_rectangle(door_x - 10, door_y - 10, door_x + door_w + 10, door_y + door_h, outline="#463228", width=10)

    # --- 6. BOY CHARACTER ---
    bx, by = WIDTH // 2 - 120, door_y + door_h - 20
    # Legs & Body
    canvas.create_rectangle(bx - 12, by + 40, bx - 2, by + 80, fill="#283246", outline="")
    canvas.create_rectangle(bx + 2, by + 40, bx + 12, by + 80, fill="#283246", outline="")
    canvas.create_rectangle(bx - 18, by, bx + 18, by + 45, fill="#4682F0", outline="")
    # Head & Hair
    canvas.create_oval(bx - 18, by - 38, bx + 18, by - 2, fill="#F5C8A0", outline="")
    canvas.create_oval(bx - 20, by - 42, bx + 20, by - 18, fill="#321E14", outline="")

    # Reactions
    if is_shocked:
        canvas.create_line(bx - 16, by + 10, bx - 30, by - 10, fill="#F5C8A0", width=6)
        canvas.create_line(bx + 16, by + 10, bx + 30, by - 10, fill="#F5C8A0", width=6)
        canvas.create_oval(bx - 9, by - 25, bx - 3, by - 19, fill="white", outline="")
        canvas.create_oval(bx + 3, by - 25, bx + 9, by - 19, fill="white", outline="")
        canvas.create_oval(bx - 7, by - 23, bx - 5, by - 21, fill="black", outline="")
        canvas.create_oval(bx + 5, by - 23, bx + 7, by - 21, fill="black", outline="")
        canvas.create_oval(bx - 5, by - 14, bx + 5, by - 4, fill="#781414", outline="")
    else:
        canvas.create_line(bx - 16, by + 10, bx - 22, by + 35, fill="#F5C8A0", width=6)
        canvas.create_line(bx + 16, by + 10, bx + 22, by + 35, fill="#F5C8A0", width=6)
        canvas.create_oval(bx - 7, by - 23, bx - 5, by - 21, fill="black", outline="")
        canvas.create_oval(bx + 5, by - 23, bx + 7, by - 21, fill="black", outline="")

    # --- 7. REEL TOP & BOTTOM BARS ---
    canvas.create_rectangle(0, 0, WIDTH, 40, fill="black", outline="")
    canvas.create_rectangle(0, HEIGHT - 40, WIDTH, HEIGHT, fill="black", outline="")

    # Loop Timer (16ms = ~60FPS)
    frame_counter = (frame_counter + 1) % 600
    root.after(16, draw_scene)

# Start App 

draw_scene()
root.mainloop()