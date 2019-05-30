import mtoa.aovs as aovs

# Create AOV
def addAOV(aovName):
    aov = aovs.AOVInterface().addAOV('beauty:aovName')
    return aov
