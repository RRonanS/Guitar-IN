import uinput

MOUSE_SENSE = 10

teclas = {
    'E3': uinput.KEY_O,
    'F3': uinput.KEY_I,
    'F#3/Gb3': uinput.KEY_SPACE
        }
mouse = {
    'A3': (uinput.REL_X, 1),
    'G3': (uinput.REL_X, -1),
    'G#4/Ab4': (uinput.REL_Y, 1),
    'C#5/Db5': (uinput.REL_Y, -1),
    'C5': (uinput.BTN_LEFT, 1), 
    'D4': (uinput.BTN_RIGHT, 1)
    }

events = [uinput.REL_X, uinput.REL_Y, uinput.KEY_I, uinput.KEY_O, 
          uinput.BTN_RIGHT, uinput.BTN_LEFT, uinput.KEY_SPACE]
dispositivo = uinput.Device(events)

def mapear(disp, entrada):
    """Dado o dispositivo e uma entrada, mapeia a entrada para um evento"""
    if entrada in mouse:
        if mouse[entrada][0] in (uinput.BTN_RIGHT, uinput.BTN_LEFT):
            disp.emit(mouse[entrada][0], mouse[entrada][1])
            disp.emit(mouse[entrada][0], 0)
        else:
            disp.emit(mouse[entrada][0], mouse[entrada][1]*MOUSE_SENSE)
    elif entrada in teclas:
        disp.emit_click(teclas[entrada])

