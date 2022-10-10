import bpy
import re
from bpy.types import Panel

class BATCH_EXPORT_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label =  "Batch Export Selected"
    bl_category = "Batch Export"
    
    def draw(self, context):

        ##
        self.__selected_objects = context.selected_objects
        self.__all_objects = bpy.data.objects

        layout = self.layout
        scene = context.scene

        scene.objWithUcx.clear()

        scene.ucxObjects.clear()


        n=0

        for obj in self.__all_objects:
            
            objName = obj.name

            if objName[0:4] == "UCX_":
                scene.ucxObjects.append(obj)

        for obj in self.__selected_objects:

            objName = obj.name

            if objName[0:4] != "UCX_" :
                scene.objWithUcx[n] = []
                scene.objWithUcx[n].append(obj)
                objName = obj.name

                for ucxObj in scene.ucxObjects:
                    ucxObjName = ucxObj.name
                    checkName = re.search(objName, ucxObjName)

                    if checkName:
                        scene.objWithUcx[n].append(ucxObj)
                
                n += 1
        ##
        
        
        row = layout.row()
        row.label(text = "Export Folder:")
        
        row = layout.row()
        row.prop(scene, "export_folder", text = "")

        row = layout.row()
        row = layout.row()

        row = layout.row()
        row.label(text = "Include:")

        row = layout.row()
        row.prop(scene, "custom_prop", text = "Custom Properties")

        row = layout.row()
        row = layout.row()

        row = layout.row()
        row.label(text = "Transform:")

        row = layout.row()
        row.prop(scene, "clear_transform", text = "Clear Transformations")
        
        row = layout.row()
        row.prop(scene, "forward_axis", text = "Forward")

        row = layout.row()
        row.prop(scene, "up_axis", text = "Up")

        row = layout.row()
        row.prop(scene, "use_space_transform", text = "Use Space Transform")

        row = layout.row()
        row.prop(scene, "apply_transform", text = "Apply Transform")

        row = layout.row()
        row = layout.row()

        row = layout.row()
        row.label(text = "Geometry:")

        row = layout.row()
        row.prop(scene, "export_subdivision_surface", text = "Export Subdivision Surface")

        row = layout.row()
        row.prop(scene, "apply_modifiers", text = "Apply Modifiers")

        row = layout.row()
        row.operator('object.be_ot_operator', text = "Export")

        for i in range(0, len(scene.objWithUcx)) :
            if len(scene.objWithUcx[i]) == 1 :
                row = layout.row()
                row.label(text = f'{scene.objWithUcx[i][0].name}')
            else :
                for ii in range(0, len(scene.objWithUcx[i])) :
                    row = layout.row()
                    if ii == 0 :
                        row.label(text = f'{scene.objWithUcx[i][ii].name}')
                    else :
                        row.label(text = f'    {scene.objWithUcx[i][ii].name}')