#loadPlugin arnold for maya

import maya.cmds as mc

if not mc.pluginInfo('mtoa', q=1, loaded=1):
    mc.loadPlugin('mtoa')
mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
