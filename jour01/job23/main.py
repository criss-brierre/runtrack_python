def draw_triangle(height):
    final_string = "  "
    for i in range(height):
        if(i == height - 1):
            final_string ="_"*2
        print(" "*(height-i-1) + "/" + final_string * i + "\\")


draw_triangle(5)