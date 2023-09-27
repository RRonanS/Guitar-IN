import uinput
import time

events = (
    uinput.KEY_E,
    uinput.KEY_H,
    uinput.KEY_L,
    uinput.KEY_O,
    )

with uinput.Device(events) as device:
    time.sleep(1)
    device.emit_click(uinput.KEY_H)
    device.emit_click(uinput.KEY_E)
    device.emit_click(uinput.KEY_L)
    device.emit_click(uinput.KEY_L)
    device.emit_click(uinput.KEY_O)
