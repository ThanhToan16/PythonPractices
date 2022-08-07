import bpy
from bpy.types import Operator

from . BE_Export import batch_export


class BATCH_EXPORT_OT_Operator(Operator):
    bl_idname = "object.be_ot_operator"
    bl_label = "Batch Export"
    bl_description = "Export Selected Objects as FBX"
    bl_options = {'REGISTER'}

    def execute(self, context):

        bat_exp = batch_export(context)
        bat_exp.do_export()
        # bat_exp.do_test()

        self.report({'INFO'}, "Done Test!!!")
        return {'FINISHED'}