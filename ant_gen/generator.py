import ant_gen.template as temp
import yaml
import time


def generator(build_dir):
    ti = time.ctime()
    data = []
    with open('test/pass/pass1.yaml') as f:
        data = yaml.load(f, Loader= yaml.SafeLoader)

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
            time = ti,
            month = "Jul",
            day = 12,
            year = 2023,
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
        feed_width = 0.1
        feed_h = 0.5
        fp.write(temp.template_feed.format(
            feed_X_pos = -feed_width/2,
            feed_Y_pos = -ground_plane_Y_size/2,
            feed_Z_pos =  ground_plane_Z_size,
            feed_size = feed_h,
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
        # CUTOUT
        
        
        cutout_width = 0.1
        cutout_height = 0.3
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
            to_be_subtracted = "patch1",
            rect1= "cutout1",
            rect2= "cutout2"
        ))