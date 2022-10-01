import bpy

def stripSuffix(obj):
    return obj.name.rstrip(".0123456789")