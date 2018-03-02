bl_info = {
"name": "FirstTry",
"author": "Janine Rickmeyer",
"version": (0, 0, 1),
"blender": (2, 78, 3),
"location": "View3D > Object > Move",
"description": "Moves an object",
"warning": "",
"wiki_url": "",
"tracker_url": "",
"category": "Object"}


import bpy

class MoveObject(bpy.types.Operator):
    """Moves an object"""
    bl_idname = "object.move_object"
    bl_label = "Move an object"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        context.active_object.location.x += 1
        return {'FINISHED'}
    
    
def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_func)
        
def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
        
def menu_func(self, context):
    self.layout.operator(MoveObject.bl_idname, 
    icon = 'MESH_CUBE')
