# minecraft-c2v
minecraft-c2v is a Minecraft datapack namespace generator script, written in Python. It utilizes a recursive function to automatically create a directory tree, containing 270+ files and 90+ folders.

# What is c2v?
This namespace ("c2v", alias for Change to Variant) is used to replace a block (e.g. cobblestone_stair) with its variant (e.g. mossy_cobblestone_stair) whilst preserving blockstates. Since c2v is a namespace, it is easily integrated into datapacks.

Requires load function: NO

Requires tick function: NO

1. Run the execution function at the block
execute positioned ~ ~ ~ run function c2v:exe

2. The block is converted into one of its variants



# Why a generator script?
To change a block into its variant with a minimal amount of commands, a directory tree structure must be created to minimize the amount of block state checks.

In combination with c2v_blocks.json, changes are easy to make.
