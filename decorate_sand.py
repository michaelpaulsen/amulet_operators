# Fixed function example plugin
# The fixed function operation pipeline works in much the same way as MCEdit Unified filters with some modifications
# You define a function and it will appear in the UI for you to run


from amulet.api.selection import SelectionGroup
from amulet.api.level import BaseLevel
from amulet.api.data_types import Dimension
from amulet.api.block import Block

#the supported gameversion 
game_version = ("java", (1, 20, 2 ))
#the blocks needed
grass_block = Block("minecraft", "grass_block")
dirt = Block("minecraft", "dirt")
stone = Block("minecraft", "stone")
def get_block_and_block_above(level, dim, x,y,z):
    block, block_entity = level.get_version_block( x,y,z, dim, game_version)
    block1, block_entity1 = level.get_version_block( x,y+1,z,dim,game_version)
    return block, block1

def set_grass_piller(level,dim,x,y,z): 
        
        level.set_version_block( x,y,z,dim,game_version, grass_block)
        for yo in range(1,5):
            level.set_version_block( x,y-yo,z,dim,game_version, dirt)
            

def operator(
    world: BaseLevel, dimension: Dimension, selection: SelectionGroup, options: dict
):
    # world is the object that contains all the data related to the world
    # dimension in a string used to identify the currently loaded dimension. It can be used to access the right dimension from the world
    # selection is an object describing the selections made by the user. It is possible there may not be any boxes selected
    # options will be explored in further examples
    
    print("===-===")
    print("\nstarting operator\n\n\n\n\n")
    
    for x,y,z in selection.blocks: 
        block, block_above = get_block_and_block_above(world,dimension,x,y,z)
        if block!= None and block_above != None:
            ban = block_above.base_name
            bln = block.base_name
            if bln == "sand":
                if ban == "air": 
                   set_grass_piller(world, dimension,x,y,z) 
                else: 
                    level.set_version_block( x,y,z,dimension,game_version, grass_block)
            
    print("\n\n\n\nending operator")
    print("===-===")

export = {  
    "name": "test",  
    "operation": operation,
}
