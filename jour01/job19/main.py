def draw_rectangle(width,height):
    str_width = ''
    for i in range(height):
            if(i == 0 or i == height - 1):
                for j in range(width):
                    str_width += '-'
            else:
                for j in range(width):
                    str_width += ' '
            print('|' + str_width + '|')
            str_width = ''


draw_rectangle(10, 3)