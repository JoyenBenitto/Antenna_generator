import template as temp

def generator(build_dir):
    with open(f"{build_dir}/generated.py","w") as fp:
        fp.write(temp.template_msp)