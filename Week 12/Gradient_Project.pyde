# create an animated gradient for four different moods

# store current mood
mode = None
# establish the timevariable for animation
t = 0
# store typed variables before pressing enter
buffer = ""

# setup the canvas
def setup():
    
    # size the canvas to the fill the entirety of a 13 inch screen
    size(1500, 900)
    
    # no line
    noStroke()
    
    # align the text to the center of the canvas
    textAlign(CENTER, CENTER)
    
    # size the text to 20 pixels
    textSize(20)
    
    # make the background black
    fill(180)
    
    # upon setup, display prompt
    display_prompt()

def draw():
    
    # if no mood is selected, show prompt
    if mode is None:
        display_prompt()
        return
    
    # update the time variable for animation
    global t
    t += 0.01
    
    # otherwise, draw the animated gradient and effects
    draw_background()
    draw_gradient()
    draw_overlay()
    draw_vignette()
    draw_border()

def display_prompt():
    background(0)
    fill(180)
    text("Type: happy, sad, angry, or calm", width / 2, height / 2)

    

    # Instead of loadPixels(), we now draw coloured rectangles each frame.
    # This ensures the entire screen refreshes and colour motion is visible.
    step = 10  # controls softness of gradient (smaller = smoother but slower)
    for y in range(0, height, step):
        for x in range(0, width, step):
            nx = float(x) / width
            ny = float(y) / height


            # Subtle moving pattern using layered sine waves
            v = 0.5 + 0.5 * sin((nx * 3 + t) + sin(ny * 4 - t))
            v2 = 0.5 + 0.5 * sin((nx + ny) * 2 + t * 1.5)
            blend = constrain((v + v2) / 2.0, 0, 1)


            # Pick colour palette by mood
            if mode == "happy":
                c1 = color(255, 140, 80)
                c2 = color(255, 105, 180)
                c3 = color(255, 235, 120)
            elif mode == "sad":
                c1 = color(10, 20, 60)
                c2 = color(25, 50, 120)
                c3 = color(0, 0, 0)
            elif mode == "calm":
                c1 = color(240, 235, 220)
                c2 = color(255, 255, 245)
                c3 = color(230, 225, 210)


            # Dynamic oscillation between palette colours
            pulse = (sin(t * 0.8) + 1) / 2.0
            base = lerpColor(c1, c2, pulse)
            final_col = lerpColor(base, c3, blend)


            fill(final_col)
            rect(x, y, step, step)  # draw block of colour


def keyTyped():
    global buffer, mode
    if key == ENTER or key == RETURN:
        word = buffer.strip().lower()
        if word in ["happy", "sad", "calm"]:
            mode = word
        buffer = ""
    elif key.isalpha():
        buffer += key
