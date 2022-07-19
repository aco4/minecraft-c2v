# This script generates a Minecraft "Change to Variant" ("c2v") datapack namespace
#
# Define blocks, their relevant blockstates and their variants in c2v_blocks.json

import os, json, copy





def branch(block_name, list_of_blockstates, list_of_block_variants, script_dir, previous_parent_dir, parent_dir, previous_node, final_state_string):

    # c2v/functions/exe.mcfunction
    #
    # execute if block ~ ~ ~ cobblestone_stairs run function c2v:cobblestone_stairs
    # execute if block ~ ~ ~ cobblestone_slab run function c2v:cobblestone_slab
    #
    # Folders/files created:
    #
    # c2v/functions/cobblestone_stairs
    # c2v/functions/cobblestone_slab
    #
    # c2v/functions/cobblestone_stairs.mcfunction
    # c2v/functions/cobblestone_slab.mcfunction
    #

    # c2v/functions/cobblestone_stairs.mcfunction
    #
    # execute if block ~ ~ ~ cobblestone_stairs[facing=north] run function c2v:cobblestone_stairs/facing_north
    # execute if block ~ ~ ~ cobblestone_stairs[facing=south] run function c2v:cobblestone_stairs/facing_south
    #
    # Folders/files created:
    #
    # c2v/functions/cobblestone_stairs/facing_north
    # c2v/functions/cobblestone_slab/facing_south
    #
    # c2v/functions/cobblestone_stairs/facing_north.mcfunction
    # c2v/functions/cobblestone_slab/facing_south.mcfunction
    #

    # c2v/functions/cobblestone_stairs/facing_north.mcfunction
    #
    # execute if block ~ ~ ~ cobblestone_stairs[half=bottom] run function c2v:cobblestone_stairs/facing_north/half_bottom
    # execute if block ~ ~ ~ cobblestone_stairs[half=top] run function c2v:cobblestone_stairs/facing_north/half_top
    #
    # Folders/files created:
    #
    # c2v/functions/cobblestone_stairs/facing_north/half_bottom
    # c2v/functions/cobblestone_slab/facing_north/half_top
    #
    # c2v/functions/cobblestone_stairs/facing_north/half_bottom.mcfunction
    # c2v/functions/cobblestone_slab/facing_north/half_top.mcfunction
    #

    # c2v/functions/cobblestone_stairs/facing_north/half_bottom.mcfunction
    #
    # execute if block ~ ~ ~ cobblestone_stairs[shape=inner_left] run function c2v:cobblestone_stairs/facing_north/half_bottom/shape_inner_left
    # execute if block ~ ~ ~ cobblestone_stairs[shape=inner_right] run function c2v:cobblestone_stairs/facing_north/half_bottom/shape_inner_right
    #
    # Folders/files created:
    #
    # c2v/functions/cobblestone_stairs/facing_north/half_bottom/shape_inner_left
    # c2v/functions/cobblestone_slab/facing_north/half_bottom/shape_inner_right
    #
    # c2v/functions/cobblestone_stairs/facing_north/half_bottom/shape_inner_left.mcfunction
    # c2v/functions/cobblestone_slab/facing_north/half_bottom/shape_inner_right.mcfunction
    #

    # c2v/functions/cobblestone_stairs/facing_north/half_bottom/shape_inner_left.mcfunction
    #
    # setblock ~ ~ ~ mossy_cobblestone_stairs[facing=north,half=bottom,shape=inner_left]
    # execute if predicate c2v:rand_50 run setblock ~ ~ ~ mossy_cobblestone_stairs[facing=north,half=bottom,shape=inner_left]
    #



    # General Format
    #
    # {script_dir}/c2v/functions/{previous_parent_dir}/{previous_node}.mcfunction
    #
    # execute if block ~ ~ ~ {block_name}[{this_node_blockstate}={this_node_state}] run function c2v:{parent_dir}/{this_node_blockstate}_{this_node_state}
    # execute if block ~ ~ ~ {block_name}[{this_node_blockstate}={this_node_state}] run function c2v:{parent_dir}/{this_node_blockstate}_{this_node_state}
    #
    # Folders/files created:
    #
    # {script_dir}/c2v/functions/{parent_dir}/{this_node_blockstate}_{this_node_state}
    # {script_dir}/c2v/functions/{parent_dir}/{this_node_blockstate}_{this_node_state}.mcfunction
    #
    #
    # branch(block_name, list_of_blockstates, list_of_block_variants, script_dir, previous_parent_dir, parent_dir, previous_node, final_state_string)
    #

    print()
    print('New branch!')
    print('Inital parameters:')
    print(f'block_name = {block_name}')
    print(f'list_of_blockstates = {list_of_blockstates}')
    print(f'list_of_block_variants = {list_of_block_variants}')
    print(f'script_dir = {script_dir}')
    print(f'previous_parent_dir = {previous_parent_dir}')
    print(f'parent_dir = {parent_dir}')
    print(f'previous_node = {previous_node}')
    print(f'final_state_string = {final_state_string}')
    print()

    list_of_blockstates_copy = copy.deepcopy(list_of_blockstates)
    blockstate = list_of_blockstates_copy[0]
    list_of_blockstates_copy.pop(0)
    print(f'blockstate = {blockstate}')
    print(f'list_of_blockstates_copy.pop(0) = {list_of_blockstates_copy}')
    print()

    print(f'opening {os.path.join(script_dir, "c2v/functions", previous_parent_dir, f"{previous_node}.mcfunction")}')
    f_previous_node = open(os.path.join(script_dir, 'c2v/functions', previous_parent_dir, f'{previous_node}.mcfunction'), 'a')

    if len(list_of_blockstates_copy):
        for this_node_state in blockstate[1]:
            #this_node_blockstate = blockstate[0]

            print()
            print(f'this_node_state = {this_node_state}')
            print(f'this_node_blockstate = {blockstate[0]}')
            print()

            f_previous_node.write(f'execute if block ~ ~ ~ {block_name}[{blockstate[0]}={this_node_state}] run function c2v:{parent_dir}/{blockstate[0]}_{this_node_state}\n')
            print(f'execute if block ~ ~ ~ {block_name}[{blockstate[0]}={this_node_state}] run function c2v:{parent_dir}/{blockstate[0]}_{this_node_state}\n')

            if len(list_of_blockstates_copy) > 1:
                global folder_count
                folder_count += 1
                print(f'Created new folder, {os.path.join(script_dir, "c2v/functions", parent_dir, f"{blockstate[0]}_{this_node_state}")}')
                os.mkdir(os.path.join(script_dir, 'c2v/functions', parent_dir, f'{blockstate[0]}_{this_node_state}'))

            global file_count
            file_count += 1
            print(f'Created new .mcfunction file, {os.path.join(script_dir, "c2v/functions", parent_dir, f"{blockstate[0]}_{this_node_state}.mcfunction")}')
            new_file = open(os.path.join(script_dir, 'c2v/functions', parent_dir, f'{blockstate[0]}_{this_node_state}.mcfunction'), 'x')
            new_file.close()

            print('Outgoing branch!')
            branch(block_name, list_of_blockstates_copy, list_of_block_variants, script_dir, parent_dir, f'{parent_dir}/{blockstate[0]}_{this_node_state}', f'{blockstate[0]}_{this_node_state}', final_state_string + f'{blockstate[0]}={this_node_state},')

        f_previous_node.close()

    else:
        for this_node_state in blockstate[1]:
            print()
            print(f'this_node_state = {this_node_state}')
            print(f'this_node_blockstate = {blockstate[0]}')
            print()

            # ISSUE: This assumes there are no more than 2 variants
            f_previous_node.write(f'execute if block ~ ~ ~ {block_name}[{blockstate[0]}={this_node_state}] run setblock ~ ~ ~ {list_of_block_variants[0]}[{final_state_string}{blockstate[0]}={this_node_state}]\n')
            print(f'execute if block ~ ~ ~ {block_name}[{blockstate[0]}={this_node_state}] run setblock ~ ~ ~ {list_of_block_variants[0]}[{final_state_string}{blockstate[0]}={this_node_state}]')
            if len(list_of_block_variants) > 2:
                f_previous_node.write(f'execute if predicate c2v:rand_50 if block ~ ~ ~ {block_name}[{blockstate[0]}={this_node_state}] run setblock ~ ~ ~ {list_of_block_variants[1]}[{final_state_string}{blockstate[0]}={this_node_state}]')
                print(f'execute if predicate c2v:rand_50 if block ~ ~ ~ {block_name}[{blockstate[0]}={this_node_state}] run setblock ~ ~ ~ {list_of_block_variants[1]}[{final_state_string}{blockstate[0]}={this_node_state}]')

        f_previous_node.close()





file_count = 0
folder_count = 0

# The parent directory of the script
# This is where the namespace shall be generated
print(f'Getting parent directory')
script_directory = os.path.dirname(__file__)

print(f'Parsing JSON from c2v_blocks.json')
with open(os.path.join(script_directory, 'c2v_blocks.json'), 'r') as c2v_file:
    block_list = json.load(c2v_file)
    print(block_list)


if os.path.exists(os.path.join(script_directory, 'c2v')):
    print('FAILED: namespace exists. Delete current namespace first before generating.')
else:
    folder_count += 1
    print(f'Making c2v')
    os.mkdir(os.path.join(script_directory, 'c2v'))

    file_count += 1
    print(f'Making c2v/README.txt')
    with open(os.path.join(script_directory, 'c2v/README.txt'), 'w') as f:
        print(f'Writing c2v/README.txt')
        f.write('''# This namespace ("c2v", alias for Change to Variant) is used to replace a block (e.g. cobblestone_stair) with its variant (e.g. mossy_cobblestone_stair) whilst preserving blockstates.
# Requires load function: NO
# Requires tick function: NO

# 1. Run the execution function at the block
execute positioned ~ ~ ~ run function c2v:exe

# 2. The block is converted into one of its variants''')

    folder_count += 1
    print(f'Making c2v/predicates')
    os.mkdir(os.path.join(script_directory, 'c2v/predicates'))

    file_count += 1
    print(f'Making c2v/predicates/rand_50.json')
    with open(os.path.join(script_directory, 'c2v/predicates/rand_50.json'), 'w') as f:
        print(f'Writing c2v/predicates/rand_50.json')
        f.write('''{
  "condition": "minecraft:random_chance",
  "chance": 0.5
}''')

    folder_count += 1
    print(f'Making c2v/functions')
    os.mkdir(os.path.join(script_directory, 'c2v/functions'))

    file_count += 1
    print(f'Making c2v/functions/exe.mcfunction')
    #with open(os.path.join(script_directory, 'c2v/functions/exe.mcfunction'), 'a') as f_exe:


    for block_dict in block_list:
        if 'blockstates' in block_dict:
            print(f'block_dict["blockstates"] = {block_dict["blockstates"]}')
            print(f'block_dict["blockstates"].items() = {block_dict["blockstates"].items()}')
            print(f'list(block_dict["blockstates"].items()) = {list(block_dict["blockstates"].items())}')

            f_exe = open(os.path.join(script_directory, 'c2v/functions/exe.mcfunction'), 'a')
            f_exe.write(f'execute if block ~ ~ ~ {block_dict["name"]} run function c2v:{block_dict["name"]}\n')
            f_exe.close()

            if len(block_dict['blockstates'].items()) > 1:

                folder_count += 1
                print(f'Created new folder, {os.path.join(script_directory, "c2v/functions", block_dict["name"])}')
                os.mkdir(os.path.join(script_directory, 'c2v/functions', block_dict['name']))

                file_count += 1
                tmp = block_dict['name']
                print(f'Created new .mcfunction file, {os.path.join(script_directory, "c2v/functions", f"{tmp}.mcfunction")}')
                del tmp
                new_file = open(os.path.join(script_directory, 'c2v/functions', f'{block_dict["name"]}.mcfunction'), 'x')
                new_file.close()

                branch(block_dict['name'], list(block_dict["blockstates"].items()), block_dict['variants'], script_directory, '', block_dict['name'], block_dict['name'], '')
            else:
                # branch(block_name, list_of_blockstates, list_of_block_variants, script_dir, previous_parent_dir, parent_dir, previous_node, final_state_string)
                branch(block_dict['name'], list(block_dict["blockstates"].items()), block_dict['variants'], script_directory, '', '', block_dict['name'], '')
        else:

            # ISSUE: This assumes there are no more than 2 variants
            f_exe = open(os.path.join(script_directory, 'c2v/functions/exe.mcfunction'), 'a')
            f_exe.write(f'execute if block ~ ~ ~ {block_dict["name"]} run setblock ~ ~ ~ {block_dict["variants"][0]}\n')

            if len(block_dict["variants"]) > 1:
                f_exe.write(f'execute if block ~ ~ ~ {block_dict["variants"][0]} if predicate c2v:rand_50 run setblock ~ ~ ~ {block_dict["variants"][1]}\n')

            f_exe.close()


    print()
    print('Successfully generated c2v namespace!')
    print()
    print(f'File count: {file_count}')
    print(f'Folder count: {folder_count}')











