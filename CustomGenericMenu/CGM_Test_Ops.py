import bpy

class Test_01(bpy.types.Operator):
    bl_label = "CGM Test_01"
    bl_idname = "test.01"

    def execute(self, context):
        self.dict = {}
        
        for i in range(6):
            key = str("x" + str(i))
            self.dict[key] = i

        print(self.dict)

        for key, value in self.dict.items():
            exec(f'self.{key}={value}')

        print(self.x1)



        return{'FINISHED'}

########################################################################################
########################################################################################

