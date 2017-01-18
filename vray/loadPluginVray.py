#loadPlugin vrayformaya and xgenVRay

import maya.cmds as mc

if not mc.pluginInfo('vrayformaya', q=1, loaded=1):
    mc.loadPlugin('vrayformaya')
    mc.loadPlugin('xgenVRay')
mc.setAttr('defaultRenderGlobals.currentRenderer', 'vray', type='string')
