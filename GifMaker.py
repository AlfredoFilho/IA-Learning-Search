from PIL import Image, ImageDraw

def fill_dot(a_list, color, images):
    a_list = [a_list]
    if len(images) == 0:
        im = Image.open("ImagemTabuleiro.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
    
    else:                
        im = Image.open("ImagemTemp.png").convert("RGBA")
        draw = ImageDraw.Draw(im)

    for el in a_list:
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = color
        )      
            
    im.save("ImagemTemp.png")
    
    del draw
    return im


def compute_initial_image(cat, bloqueados, saida, images) :
    
    if len(images) == 0:
        im = Image.open("ImagemTabuleiro.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
    
    else:                
        im = Image.open("ImagemTemp.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
    
    for el in [saida] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "#61b76b"
        )
        
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

    for el in [cat] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "#61b76b"
        )
    
    im.save("ImagemTemp.png")
    
    del draw
    return im