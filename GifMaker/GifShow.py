import pyglet

class Gif():
    def __init__(self, path, title):
        self.path = path
        self.title = title
    
    def run(self):
        animation = pyglet.image.load_animation(self.path)
        animSprite = pyglet.sprite.Sprite(animation)
         
        w = animSprite.width
        h = animSprite.height
         
        window = pyglet.window.Window(width=w, height=h)
        window.set_caption(self.title)
         
        r,g,b,alpha = 0.5,0.5,0.8,0.5
         
        pyglet.gl.glClearColor(r,g,b,alpha)
         
        @window.event
        def on_draw():
            window.clear()
            animSprite.draw()
     
        pyglet.app.run()