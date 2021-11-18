my_sprite = sprites.create(assets.image("""myImage"""), SpriteKind.player)
jo=my_sprite
tiles.set_tilemap(tilemap("""level1 """))
controller.move_sprite(jo)
scene.camera_follow_sprite(jo)

my_sprite2 = sprites.create(assets.image("""pizza"""), SpriteKind.projectile)
pizza=my_sprite2

def on_a_pressed():
    pizza.follow(jo, 100)

        
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
