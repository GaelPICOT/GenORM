"""
=========================================================
                       GenOCL.py
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


#---------------------------------------------------------
#   Helpers on the source metamodel (UML metamodel)
#---------------------------------------------------------
# The functions below can be seen as extensions of the
# modelio metamodel. They define useful elements that 
# are missing in the current metamodel but that allow to
# explorer the UML metamodel with ease.
# These functions are independent from the particular 
# problem at hand and could be reused in other 
# transformations taken UML models as input.
#---------------------------------------------------------

# example
def isAssociationClass(element):
    """ 
    Return True if and only if the element is an association 
    that have an associated class, or if this is a class that
    has a associated association. (see the Modelio metamodel
    for details)
    """
    if isinstance(element, Class):
        return element.getLinkToAssociation() is not None
    else:
        return False
    
 
#---------------------------------------------------------
#   Application dependent helpers on the source metamodel
#---------------------------------------------------------
# The functions below are defined on the UML metamodel
# but they are defined in the context of the transformation
# from UML Class diagramm to USE OCL. There are not
# intended to be reusable. 
#--------------------------------------------------------- 

# example
def associationsInPackage(package):
    """
    Return the list of all associations that start or
    arrive to a class which is recursively contained in
    a package.
    """
    list_association = []
    for element in package.getOwnedElement():
        if isinstance(element, Class):
            list_association.extend(element.getOwnedEnd())
        elif isinstance(element, Package):
            list_association.extend(associationsInPackage(element))
    return list_association

    
#---------------------------------------------------------
#   Helpers for the target representation (text)
#---------------------------------------------------------
# The functions below aims to simplify the production of
# textual languages. They are independent from the 
# problem at hand and could be reused in other 
# transformation generating text as output.
#---------------------------------------------------------


# for instance a function to indent a multi line string if
# needed, or to wrap long lines after 80 characters, etc.

#---------------------------------------------------------
#           Transformation functions: UML2OCL
#---------------------------------------------------------
# The functions below transform each element of the
# UML metamodel into relevant elements in the OCL language.
# This is the core of the transformation. These functions
# are based on the helpers defined before. They can use
# print statement to produce the output sequentially.
# Another alternative is to produce the output in a
# string and output the result at the end.
#---------------------------------------------------------



# examples

def umlEnumeration2OCL(enumeration):
    """
    Generate USE OCL code for the enumeration
    """
    result = "enum " + enumeration.getName() + " "
    values = [value.getName() for value in enumeration.getValue()]
    result += ', '.join(values) + "\n\n"
    return result

def umlClass2OCL(class_):
    return "class_" + "\n\n"

def umlBasicType2OCL(basicType):
    """
    Generate USE OCL basic type. Note that
    type conversions are required.
    """
    return "basicType" + "\n\n"

def umlAssociation2OCL(asociation):
    return "asociation" + "\n\n"

def umlInvariant2OCL(invatriant):
    return "invatriant" + "\n\n"

def umlAssociationClass2OCL(asociationClass):
    return "asociationClass" + "\n\n"
    
# etc.

def package2OCL(package):
    """
    Generate a complete OCL specification for a given package.
    The inner package structure is ignored. That is, all
    elements useful for USE OCL (enumerations, classes, 
    associationClasses, associations and invariants) are looked
    recursively in the given package and output in the OCL
    specification. The possibly nested package structure that
    might exist is not reflected in the USE OCL specification
    as USE is not supporting the concept of package.
    """
    result = ""
    for element in package.getOwnedElement():
        if isinstance(element, Class):
            if isAssociationClass(element):
                result += umlAssociationClass2OCL(element)
            else:
                result += umlClass2OCL(element)
        elif isinstance(element, Package):
            result += package2OCL(element)
        elif isinstance(element, Enumeration):
            result += umlEnumeration2OCL(element)
    for association in associationsInPackage(package):
        result += umlAssociation2OCL(association)
    # TODO : invariant
    return result



#---------------------------------------------------------
#           User interface for the Transformation 
#---------------------------------------------------------
# The code below makes the link between the parameter(s)
# provided by the user or the environment and the 
# transformation functions above.
# It also produces the end result of the transformation.
# For instance the output can be written in a file or
# printed on the console.
#---------------------------------------------------------

# (1) computation of the 'package' parameter
# (2) call of package2OCL(package)
# (3) do something with the result
