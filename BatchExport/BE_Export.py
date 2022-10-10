from ctypes import sizeof
import re
from this import d
import bpy
import bmesh
from . BE_Utils import *

class batch_export:

    def __init__(self, context):
        scene = context.scene
        self.__export_folder = scene.export_folder
        self.__clear_transform = scene.clear_transform
        self.__custom_prop = scene.custom_prop
        self.__forward_axis = scene.forward_axis
        self.__up_axis = scene.up_axis
        self.__use_space_transform = scene.use_space_transform
        self.__apply_transform = scene.apply_transform
        self.__export_subdivision_surface = scene.export_subdivision_surface
        self.__apply_modifiers = scene.apply_modifiers
        # self.__export_objects = context.selected_objects
        # self.__all_objects = bpy.data.objects

    def do_clear_transform(self, obj):
        if self.__clear_transform:
            old_transList = []
            loc = get_object_loc(obj)
            rot = get_object_rot(obj)
            scale = get_object_scale(obj)
            old_transList.append(loc)
            old_transList.append(rot)
            old_transList.append(scale)
            set_object_transformations(obj, (0,0,0), (0,0,0), (1,1,1))
            return old_transList

        return None

    def do_export(self):

        bpy.ops.object.mode_set(mode='OBJECT')
            
        ## EXPORT OBJECTS W/WO UCX ##

        for i in range(0, len(objWithUcx)):
            
            bpy.ops.object.select_all(action='DESELECT')
            for obj in objWithUcx[i]:
                obj.select_set(True)
                
                old_transList = self.do_clear_transform(obj)
                

            bpy.ops.export_scene.fbx    (
                                                filepath = self.__export_folder + "/" + objWithUcx[i][0].name + ".fbx",
                                                path_mode = 'ABSOLUTE',
                                                use_selection = True,
                                                use_custom_props = self.__custom_prop,
                                                axis_forward = self.__forward_axis,
                                                axis_up = self.__up_axis,
                                                use_space_transform = self.__use_space_transform,
                                                bake_space_transform = self.__apply_transform,
                                                use_subsurf = self.__export_subdivision_surface,
                                                use_mesh_modifiers = self.__apply_modifiers,
                                                bake_anim = False,
                                            )

            bpy.ops.object.select_all(action = 'DESELECT')
            for obj in objWithUcx[i]:
                obj.select_set(True)
                if old_transList is not None:
                    obj.location = old_transList[0]
                    obj.rotation_euler = old_transList[1]
                    obj.scale = old_transList[2]

