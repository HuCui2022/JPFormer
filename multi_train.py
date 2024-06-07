import os
pa_pe_cmds = [
    'python main.py --config config/nturgbd120-cross-set/joint.yaml',
    'python main.py --config config/nturgbd120-cross-set/bone.yaml',
    'python main.py --config config/nturgbd120-cross-set/vel.yaml',
    'python main.py --config config/nturgbd120-cross-set/bone_vel.yaml',
    'python main.py --config config/ucla/joint.yaml',
    'python main.py --config config/ucla/bone.yaml',
    'python main.py --config config/ucla/vel.yaml',
    'python main.py --config config/ucla/bone_vel.yaml',
    'python main.py --config config/shrec/joint14.yaml',
    'python main.py --config config/shrec/bone14.yaml',
    'python main.py --config config/shrec/motion14.yaml',
    'python main.py --config config/shrec/bmotion14.yaml',
    'python main.py --config config/shrec/joint28.yaml',
    'python main.py --config config/shrec/bone28.yaml',
    'python main.py --config config/shrec/motion28.yaml',
    'python main.py --config config/shrec/bmotion28.yaml'
]

for cmd in pa_pe_cmds:
    os.system(cmd)

