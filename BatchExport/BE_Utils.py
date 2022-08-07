import bpy

def get_object_loc(obj):
    return obj.location.copy()

def get_object_rot(obj):
    return obj.rotation_euler.copy()

def get_object_scale(obj):
    return obj.scale.copy()

def set_object_transformations(obj, loc, rot, scale):
    obj.location = loc
    obj.rotation_euler = rot
    obj.scale = scale