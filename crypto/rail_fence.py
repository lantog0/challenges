def go(txt, k):
    start = k * 2 - 2
    l = len(txt)

    loop = [x if x != 0 else start for x in range(start, -1, -2)]
    pos = 0
    msg = [' ' for x in range(l)]
    dist = 0
    counter = 0

    for d in loop:
        current = pos
        mov = 0
        status = False


        while current < l:
            msg[current] = txt[counter]

            if status is True and dist != 0:
                mov = dist
            else:
                mov = d

            current += mov
            status = not status
            counter += 1

        pos += 1
        dist += 2

    return ''.join(msg)

msg = """Wnb.r.ietoeh Fo"lKutrts"znl cc hi ee ekOtggsnkidy hini cna neea civo lh"""

print go(msg, 8)
