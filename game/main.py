# imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# import the textures
dirt = load_texture('textures/dirt.jpg')
cobblestone = load_texture('textures/cobblestone.png')
oak_wood = load_texture('textures/oak_wood.jpg')
brick = load_texture('textures/brick.png')
chosen_block = 1


# a function that always called
def update():
    global chosen_block
    if held_keys['1']:
        chosen_block = 1
    elif held_keys['2']:
        chosen_block = 2
    elif held_keys['3']:
        chosen_block = 3
    elif held_keys['4']:
        chosen_block = 4


# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=dirt):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.10,

            texture=texture,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
            scale=1
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if chosen_block == 1:
                    voxel = Voxel(position=self.position + mouse.normal, texture=dirt)
                if chosen_block == 2:
                    voxel = Voxel(position=self.position + mouse.normal, texture=cobblestone)
                if chosen_block == 3:
                    voxel = Voxel(position=self.position + mouse.normal, texture=oak_wood)
                if chosen_block == 4:
                    voxel = Voxel(position=self.position + mouse.normal, texture=brick)

            if key == 'left mouse down':
                destroy(self)


for z in range(16):
    for x in range(16):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
app.run()
