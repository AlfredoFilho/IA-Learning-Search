from PIL import Image, ImageDraw, ImageFont

def fill_dot(a_list, color, images):
              
    im = Image.open("Gifs/ImagemTemp.png").convert("RGBA")
    draw = ImageDraw.Draw(im)
        
    shift = a_list[0] % 2 * 25
    init_x = shift + a_list[1]*50 + a_list[1]*5
    end_x  = shift + (a_list[1]+1)*50 + a_list[1]*5
    init_y = a_list[0]*49
    end_y  = (a_list[0]+1)*49
    draw.ellipse([init_x, init_y, end_x, end_y],
                 fill = color
    )    
    
    im.save("Gifs/ImagemTemp.png", 'PNG')
    
    del draw
    return im

def fill(a_list, color, images):

    im = Image.open("Gifs/ImagemTemp2.png").convert("RGBA")
    draw = ImageDraw.Draw(im)
 
    if color == "purple":
        font_path = "font.ttf"
        font = ImageFont.truetype(font_path, 16)
        
        shift = a_list[0] % 2 * 25
        init_x = shift + a_list[1]*50 + a_list[1]*5
        init_y = a_list[0]*49
        draw.text((init_x + 21, init_y + 16), "B", fill = "black", font = font)
    
    else:
        shift = a_list[0] % 2 * 25
        init_x = shift + a_list[1]*50 + a_list[1]*5
        end_x  = shift + (a_list[1]+1)*50 + a_list[1]*5
        init_y = a_list[0]*49
        end_y  = (a_list[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = color
        )
      
    im.save("Gifs/ImagemTemp.png", 'PNG')
    im.save("Gifs/ImagemTemp2.png", 'PNG')
    
    del draw
    return im

def compute_initial_image(cat, bloqueados, saida, images) :
    
    im = Image.open("Gifs/ImagemTabuleiro.png").convert("RGBA")
    draw = ImageDraw.Draw(im)
        
    shift = saida[0] % 2 * 25
    init_x = shift + saida[1]*50 + saida[1]*5
    end_x  = shift + (saida[1]+1)*50 + saida[1]*5
    init_y = saida[0]*49
    end_y  = (saida[0]+1)*49
    draw.ellipse([init_x, init_y, end_x, end_y],
                 fill = "#456fb2")
        
    for el in bloqueados :
        shift = el[0] % 2 * 25                                            
        init_x = shift + el[1]*50 + el[1]*5                    
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.line([init_x+12, init_y+12, end_x-10, end_y-10],
                  fill = "red", width=4)
        draw.line([init_x+10,end_y-10, end_x-11, init_y+11],
                  fill = "red", width=4)              

    shift = cat[0] % 2 * 25
    init_x = shift + cat[1]*50 + cat[1]*5
    end_x  = shift + (cat[1]+1)*50 + cat[1]*5
    init_y = cat[0]*49
    end_y  = (cat[0]+1)*49
    draw.ellipse([init_x, init_y, end_x, end_y],
                 fill = "orange")
    
    im.save("Gifs/ImagemTemp.png", 'PNG')
    im.save("Gifs/ImagemTemp2.png", 'PNG')
    
    del draw
    return im