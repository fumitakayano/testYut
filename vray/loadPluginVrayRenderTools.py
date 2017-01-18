#loadPlugin renderTools

import maya.cmds as cmds

def vrayLoad(*args):
    if not cmds.pluginInfo('vrayformaya', q=1, loaded=1):
        cmds.loadPlugin('vrayformaya')
        cmds.loadPlugin('xgenVRay')
    cmds.setAttr('defaultRenderGlobals.currentRenderer', 'vray', type='string')

def UI():

	cmds.window('RenderTools!', mxb=False, sizeable=False)
	cmds.frameLayout('Controls', borderStyle = 'in', w=150)
	cmds.columnLayout(w=150)
	cmds.button("VrayForMaya", w=150, h=35, align='center',backgroundColor=[0.447,0.588,0.356],c=vrayLoad)
	cmds.setParent('..')
	cmds.showWindow()

UI()
