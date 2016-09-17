# Mari2MayaEx


from pymel.core import *
import maya.cmds as cmds

def Mari2MayaEx():

    a = ls( selected() )

    for i in a:
        print i

    c = PyNode.connections(a[0], connections = True)

    e = '1'

    f = 5

    for i in range(f):
        d = c[5][1][-f]
        if d.isdigit():
            e = c[5][1][-f:]
            break
        f = f - 1

    x = int(e)

    b = []

    for i in range( len(a) ):
        b.append( 'place2dTexture%d'%x )
        x = x + 1

    for i in b:
        print i

    # Setting Wrap U and Wrap V to Off

    for i in b:
        setAttr( str( i + '.wrapU' ), 0 )
        setAttr( str( i + '.wrapV' ), 0 )

    # Setting Translate Values for Texture Patches

    for i in range( len(a) ):
        if float(a[i][-3]) == 0:
            setAttr( str( b[i] + '.translateFrame' ), 9 , float(a[i][-4]) - 1 )
        else:
            setAttr( str( b[i] + '.translateFrame' ), float(a[i][-3]) - 1 , float(a[i][-4]) )

    # Setting the Default Color to Black

    cmds.selectPref(tso=0) if cmds.selectPref(q=1,tso=1) else cmds.selectPref(tso=1)

    print cmds.ls(os=1,fl=1)

    texcol = cmds.ls(os=1,fl=1)

    for i in range( len(texcol) ):
        try:
            connectAttr( str( texcol[i] + '.outColor' ), str( texcol[i+1] + '.defaultColor' ) )
        except IndexError:
            mel.hyperShadePanelGraphCommand("hyperShadePanel1", "showUpAndDownstream");
        else:
            mel.hyperShadePanelGraphCommand("hyperShadePanel1", "showUpAndDownstream");
