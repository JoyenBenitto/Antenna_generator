import template as temp
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

        # Creating the patch 
        ))