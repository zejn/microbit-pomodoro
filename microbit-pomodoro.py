from microbit import display, button_a, button_b, Image, sleep

count = 0
minute = 0
counting = False

image_none = Image("00000:00000:00000:00000:00000")
image_all = Image("55555:55555:55555:55555:55555")

image_off = Image("00005:00050:00500:05000:50000")
display.show(image_off)

# loop
while True:
    sleep(1000)
    a_pressed = button_a.was_pressed()
    b_pressed = button_b.was_pressed()
    if not counting and a_pressed:
        # start timer
        counting = True
        count = 0
        minute = 0
        display.show(image_all)
        display.set_pixel(0, 0, 8)

    if counting:
        if b_pressed:
            # stop timer
            counting = False
            display.show(image_off)
        elif minute < 25:
            # process timer
            count += 1
            if count >= 60:
                count = 0
                x = minute % 5
                y = int(minute / 5)
                display.set_pixel(x, y, 0)
                minute += 1
                if minute < 25:
                    x = minute % 5
                    y = int(minute / 5)
                    display.set_pixel(x, y, 8)
        elif minute >= 25:
            count += 1
            # flash for end
            if count % 2 == 1:
                display.show(image_all)
            else:
                display.show(image_none)
