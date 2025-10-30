# define the axis
Y_AXIS = 1
X_AXIS = 2
axis = None

# define c1 and c2
c1 = None
c2 = None

# store the current mood
mode = None
# store the text input
typed = ""


#set up the canvas
def setup():
    # size the canvas to 500 pixels x 500 pixels
    size(500, 500) 
    # disable strokes for shapes 
    noStroke()
    # ensure the text is center aligned
    textAlign(CENTER, CENTER)
    
    
# define a function that draws a gradient between c1 and c2 over a rectangular area
def setGradient(x, y, w, h, c1, c2, axis):
   
    # vertical gradient
    if axis == Y_AXIS:
        # loop through each horizontal line from y to y+h
        for i in range(y, y + int(h)):
            # map the current line position i to a value between 0 and 1 
            inter = map(i, y, y + h, 0, 1)
            # blend c1 and c2 based on previously established inter
            c = lerpColor(c1, c2, inter)
            # set the stroke colour to the blended colour
            stroke(c)
            # draw a horizontal line across the rectangle at position i
            line(x, i, x + w, i)
            
    # horizontal gradient
    elif axis == X_AXIS:
        # loop through each vertical line from x to x+w
        for i in range(x, x + int(w)):
            # map the current line position i to a value between 0 and 1
            inter = map(i, x, x + w, 0, 1)
             # blend c1 and c2 based on previously established inter
            c = lerpColor(c1, c2, inter)
            # set the stroke colour to the blended colour
            stroke(c)
            line(i, y, i, y + h)


# begin the draw function
def draw():
    # define c1 and c2 as variables that exist outside the current function
    global c1, c2
    # set the background to black
    background(0)
    

    # when no mood has been selected, prompt users to select a chosen mood
    if mode is None:
        # opening screen
        fill(200)
        textSize(20)
        text("Type: happy, sad, angry, afraid or calm", width / 2, height / 2)
        
        # show typed input live
        fill(255)
        textSize(18)
        text(typed, width / 2, height - 60)
        
        
    else:
    # Choose colors based on mood
    # establish the colour palette for when 'happy' has been selected
        if mode == "happy":
            c1 = color(237, 129, 223)  
            c2 = color(255, 250, 90) 
            axis = Y_AXIS
            
    # establish the colour palette for when 'sad' has been selected
        elif mode == "sad":
            c1 = color(31, 42, 152)    
            c2 = color(147, 148, 152)
            axis = X_AXIS
            
    # establish the colour palette for when 'angry' has been selected   
        elif mode == "angry":
           c1 = color(252, 32, 20)
           c2 = color(21, 6, 2)
           axis = Y_AXIS
           
    # establish the colour palette for when 'afraid' has been selected   
        elif mode == "afraid":
           c1 = color(199, 164, 219)
           c2 = color(112,12, 152)
           axis = X_AXIS
           
    # establish the colour palette for when 'calm' has been selected
        elif mode == "calm":
           c1 = color(122, 209, 178)  
           c2 = color(167, 206, 206) 
           axis = X_AXIS
    
        # establish the foregound gradient
        setGradient(0, 0, width, height, c1, c2, axis)

        # show which letters have been typed by the user
        fill(255)
        textSize(18)
        text(typed, width / 2, height - 60)

        # draw instruction text at the bottom only after the mood is selected
        textSize(14)
        text("Type: happy, sad, angry, afraid, or calm", width / 2, height - 20)


# define a function that will automatically run whenever a key is typed
def keyTyped():
   
    # refer to variables previosuly defined
    global typed, mode
    
    
    # enable the use of backspace to account for any mistakes in typing
    if key == BACKSPACE:
        # remove the last letter typed
        typed = typed[:-1]  


    # Add the typed letter to the buffer
    if key.isalpha():
        typed += key.lower()

    # Check for the mood typed 
    if typed == "happy":
        mode = "happy"
        typed = ""
        
    elif typed == "sad":
        mode = "sad"
        typed = ""
        
    elif typed == "angry":
        mode = "angry"
        typed = ""
        
    elif typed == "afraid":
        mode = "afraid"
        typed = ""
        
    elif typed == "calm":
        mode = "calm"
        typed = ""
