from vpython import *
#GlowScript 2.9 VPython
# Create a simple scrolling text object
scene.width = scene.height = 250
scene.title = 'This is a test'
B = box(pos=vec(0.1,0.2,0))

# Create a textarea element on the web page, below the box object.
# $ stands for jQuery, an important web page addition to JavaScript.
# The string \n represents a carriage return.
T = $('<textarea/>').val('Click above.\n').appendTo(scene.caption_anchor).css('width', '250px').css('height', '90px').css('font-family', 'sans-serif').css('font-size', '14px')

scene.waitfor('click')
# T.val() represents the current contents of the textarea; add to it:
T.val(T.val()+'B.pos = '+B.pos.toString()+'\n')
T.val(T.val()+'Type more text here and a scroll bar will appear.\n')

def getinput(ev):
    win.delete()
    scene.append_to_caption('\nHello, '+ev.text+'!')
    
win = winput(prompt="\n\nWhat is your name?", type='string', bind=getinput)