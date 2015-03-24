"""
=========================================================
                       SimplifyUML.py
 Generate a USE OCL specification from a UML package
=========================================================

FILL THIS SECTION AS SHOWN BELOW AND LINES STARTING WITH ###
@author Joris ROSIER <rosier.joris@hotmail.fr>
@author Gael PICOT <gael.picot@free.fr>
@group  G236

Current state of the generator
----------------------------------
FILL THIS SECTION 
Explain which UML constructs are supported, which ones are not.
What is good in your generator?
What are the current limitations?

Current state of the tests
--------------------------
FILL THIS SECTION 
Explain how did you test this generator.
Which test are working? 
Which are not?

Observations
------------
Additional observations could go there
"""
import copy


def CopyPackage(package):
    if isinstance(package, Package):
        s = IModuleSession.getSession()
        new_package = 0
        return new_package
    else:
        raise TypeError('package is not a Package')
    

pack = CopyPackage(selectedElements[0])
pack.setName(pack.getName() + '_simplified')
