# minecraft-c2v
A Minecraft datapack namespace generator script

# What is c2v?
This namespace ("c2v", alias for Change to Variant) is used to replace a block (e.g. cobblestone_stair) with its variant (e.g. mossy_cobblestone_stair) whilst preserving blockstates.
Requires load function: NO
Requires tick function: NO

1. Run the execution function at the block
execute positioned ~ ~ ~ run function c2v:exe

2. The block is converted into one of its variants
