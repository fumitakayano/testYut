#loadPlugin redshift for maya

import maya.cmds as mc

if not mc.pluginInfo('redshift4maya', q=1, loaded=1):
    mc.loadPlugin('redshift4maya')
mc.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')
