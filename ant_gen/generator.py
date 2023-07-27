import ant_gen.template as temp
import yaml 
from ant_gen.__init__ import __author__, __mail__
from tabulate import tabulate

def generator_msp(build_dir, src):
    '''
    Generates a microstrip patch fromt he given parameters in the yaml
    '''
    data = []
    optimization_flags = {}

    with open(f'{src}') as f:
        data = yaml.load(f, Loader= yaml.SafeLoader)
    for patch in data['ant']['Patch']:
        optimization_list = []
        for optim in data['ant']['Patch'][patch]['optimizations']:
            optimization_list.append(optim)
        optimization_flags[patch] = optimization_list

    project_name = data['project_name']
    unit = data['unit']
    ground_plane_X_size = data['ant']['substrate']['Dimensions'][0]
    ground_plane_Y_size = data['ant']['substrate']['Dimensions'][1]
    ground_plane_Z_size = data['ant']['substrate']['Dimensions'][2]
    ground_offset_x = data['ant']['substrate']['offset'][0]
    ground_offset_y = data['ant']['substrate']['offset'][1]
    ground_offset_z = data['ant']['substrate']['offset'][2]
    material_substrate =data['ant']['substrate']['Material']
    
    
    with open(f"{build_dir}/generated.py","w") as fp:
        # Creating the groud  plane and the substrate
        fp.write(temp.template_sub_and_gnd .format(
            project = project_name, 
        author = __author__,
            email = __mail__,
            unit = unit,
            ground_plane_X_pos = -ground_plane_X_size/2 + ground_offset_x,
            ground_plane_Y_pos = -ground_plane_Y_size/2 + ground_offset_y,
            ground_plane_Z_pos =  0,
            ground_plane_X_size = ground_plane_X_size,
            ground_plane_Y_size = ground_plane_Y_size,
            ground_plane_Z_size = ground_plane_Z_size,
            material = material_substrate
        ))
        # Creating the patch
        patches = data['ant']['Patch']
        for patch in patches:
            patch_X_size = data['ant']['Patch'][patch]['Dimensions'][0]
            patch_Y_size = data['ant']['Patch'][patch]['Dimensions'][1]
            fp.write(temp.template_patch.format(
                patch_plane_X_pos = - patch_X_size/2 + ground_offset_x,
                patch_plane_Y_pos = - patch_Y_size/2 + ground_offset_y,
                patch_plane_Z_pos =   ground_plane_Z_size,
                patch_plane_X_size = patch_X_size,
                patch_plane_Y_size = patch_Y_size,
                patch_name = patch,
                unit = unit
            ))
            
        # Creating a feed
        feed_width = data['ant']['Feed']['feed_width']
     
        fp.write(temp.template_feed.format(
            feed_X_pos = -feed_width/2,
            feed_Y_pos = -ground_plane_Y_size/2,
            feed_Z_pos =  ground_plane_Z_size,
            feed_size = patch_Y_size/2,
            feed_width = feed_width,
            feed_box_size = ground_plane_Z_size,
            feed_name = "feed",
            feed_box_X_pos = -feed_width/2,
            feed_box_Y_pos = -ground_plane_Y_size/2,
            feed_box_Z_pos = 0,
            feed_box_width = ground_plane_Z_size,
            feed_box_height = feed_width,
            unit = unit
            ))
        
        # Uniting the Feed to the patch
        feed_to_patch = data['ant']['Feed']['feed_to_patch']
        fp.write(temp.template_unite.format(
            unite1_name = feed_to_patch,
            unite2_name="feed"
        ))

        # Optimizations
        # check and make optimizations
        
        for patch in data['ant']['Patch']:
            for optimization in data['ant']['Patch'][patch]['optimizations']:
                # Adding cutout
                if optimization == 'cutout':
                    cutout_height = data['ant']['Patch'][patch]['optimizations']['cutout']['width']
                    cutout_width = data['ant']['Patch'][patch]['optimizations']['cutout']['height']
                    fp.write(temp.template_rectangle.format(
                        rect_X_pos = -feed_width/2,
                        rect_Y_pos = -patch_Y_size/2,
                        rect_Z_pos = ground_plane_Z_size,
                        rect_width = -cutout_width,
                        rect_size = cutout_height,
                        name = "cutout1",
                        unit = unit
                    ))
                    fp.write(temp.template_rectangle.format(
                        rect_X_pos = feed_width/2,
                        rect_Y_pos = -patch_Y_size/2,
                        rect_Z_pos = ground_plane_Z_size,
                        rect_width = cutout_width,
                        rect_size = cutout_height,
                        name = "cutout2",
                        unit = unit
                    ))

                    fp.write(temp.template_subtract.format(
                        to_be_subtracted = patch,
                        rect1= "cutout1",
                        rect2= "cutout2"
                    ))
                # Adding an slot 
                if optimization == 'slot':
                    slot_height = data['ant']['Patch'][patch]['optimizations']['slot']['width']
                    slot_width = data['ant']['Patch'][patch]['optimizations']['slot']['height']
                    offset_x = data['ant']['Patch'][patch]['optimizations']['slot']['offset'][0]
                    offset_y = data['ant']['Patch'][patch]['optimizations']['slot']['offset'][1]
                    fp.write(temp.template_rectangle.format(
                        rect_X_pos = -slot_height/2 + offset_x,
                        rect_Y_pos = -slot_width/2 -offset_y,
                        rect_Z_pos = ground_plane_Z_size,
                        rect_width = slot_width,
                        rect_size = slot_height,
                        name = "slot1",
                        unit = unit
                    ))
                    fp.write(temp.template_subtract_single_rect.format(
                        to_be_subtracted = patch,
                        rect1= "slot1"
                    ))
                # Adding the L slot    
                if optimization == 'L_slot':
                    base_width = 0.1
                    base_length = 0.5
                    head_width = 0.5
                    head_height = 0.2
                    offset_x = data['ant']['Patch'][patch]['optimizations']['L_slot']['offset'][0]
                    offset_y = data['ant']['Patch'][patch]['optimizations']['L_slot']['offset'][1]
                    fp.write(temp.template_rectangle.format(
                        rect_X_pos = -base_width/2 + offset_x,
                        rect_Y_pos = -base_length/2 -offset_y,
                        rect_Z_pos = ground_plane_Z_size,
                        rect_width = base_width,
                        rect_size = base_length,
                        name = "l1",
                        unit = unit
                    ))
                    fp.write(temp.template_rectangle.format(
                        rect_X_pos = -base_width/2 + offset_x,
                        rect_Y_pos =  base_width/2 +offset_y,
                        rect_Z_pos = ground_plane_Z_size,
                        rect_width = head_width,
                        rect_size = head_height,
                        name = "l2",
                        unit = unit
                    ))
                    fp.write(temp.template_subtract.format(
                        to_be_subtracted = patch,
                        rect1= "l1",
                        rect2= "l2"
                    ))

                    # Adding U slot to the MSP
                    if  optimization == 'U_slot':
                        pass
        # Adding port to the geometry
         
def tabulator(build_dir, src):
    '''Returns a summary of the synthesised antenna
    '''
    data = []
    optimization_flags = {}
    table = []
    with open(f'{src}') as f:
        data = yaml.load(f, Loader= yaml.SafeLoader)
    for patch in data['ant']['Patch']:
        optimization_list = []
        table = []
       
        for optim in data['ant']['Patch'][patch]['optimizations']:
            optimization_list.append(optim)
            if optim == 'cutout':
                pass
            # Adding an slot 
            if optim == 'slot':
                pass
            # Adding the L slot    
            if optim == 'L_slot':
                pass
            # Adding U slot to the MSP
            if  optim == 'U_slot':
                pass
        table.append(["optimizations",optimization_list])
        optimization_flags[patch] = optimization_list
        print(tabulate(table, headers=[patch,"Desc"],tablefmt="outline"))
        print("\n ________________________________________________\n")


    print("Below is your tabulation history")



def generator(build_dir, src):
    '''
    Generates the appropriate antenna according to the input yaml
    '''
    with open(f'{src}') as f:
        data = yaml.load(f, Loader= yaml.SafeLoader)
    if data['antenna_type'] == "MSP":
        generator_msp(build_dir, src)
        tabulator(build_dir, src)
    else:
        print("Enter a valid antenna type !")