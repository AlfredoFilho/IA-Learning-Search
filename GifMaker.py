from PIL import Image, ImageDraw

def compute_image(cat, atual, listaExpansao, bloqueados, saida, images) :
    
    if len(images) == 0:
        im = Image.open("ImagemTabuleiro.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
    
    else:                
        im = Image.open("ImagemTemp.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
                
    for el in [atual] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "purple"
        )        
     
    for el in listaExpansao :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "gray"
        )  
    
    for el in [saida] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "blue"
        )
    for el in bloqueados :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.line([init_x+10, init_y+10, end_x-10, end_y-10],
                  fill = "red", width=6)
        draw.line([init_x+10,end_y-10, end_x-10, init_y+10],
                  fill = "red", width=6)

    for el in [cat] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "black"
        )

    im.save("ImagemTemp.png")
    
    del draw
    return im

def compute_image_rollback(voltar, images) :
    
    if len(images) == 0:
        im = Image.open("ImagemTabuleiro.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
    
    else:                
        im = Image.open("ImagemTemp.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
                
    for el in [voltar] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "orange"
        )        

    im.save("ImagemTemp.png")

    del draw
    return im

def compute_image_inicio(cat, bloqueados, saida, images) :
    
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
                     fill = "blue"
        )
        
    for el in bloqueados :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.line([init_x+10, init_y+10, end_x-10, end_y-10],
                  fill = "red", width=6)
        draw.line([init_x+10,end_y-10, end_x-10, init_y+10],
                  fill = "red", width=6)                

    for el in [cat] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "black"
        )
    
    im.save("ImagemTemp.png")
    
    del draw
    return im

def compute_image_walk(andar, images) :
    
    if len(images) == 0:
        im = Image.open("ImagemTabuleiro.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
    
    else:                
        im = Image.open("ImagemTemp.png").convert("RGBA")
        draw = ImageDraw.Draw(im)
                
    for el in [andar] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "black"
        )        
    
    im.save("ImagemTemp.png")
    
    del draw
    return im