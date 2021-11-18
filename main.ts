let my_sprite = sprites.create(assets.image`myImage`, SpriteKind.Player)
let jo = my_sprite
tiles.setTilemap(tilemap`level1 `)
controller.moveSprite(jo)
scene.cameraFollowSprite(jo)
let my_sprite2 = sprites.create(assets.image`pizza`, SpriteKind.Projectile)
let pizza = my_sprite2
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    pizza.follow(jo, 100)
})
