#---------------------------------------------------------------------------
# Name:        etg/ribbon_buttonbar.py
# Author:      Robin Dunn
#
# Created:     20-Jun-2016
# Copyright:   (c) 2016 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"   
MODULE    = "_ribbon"
NAME      = "ribbon_buttonbar"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ 'wxRibbonButtonBar',
           'wxRibbonButtonBarEvent',
           ]    
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.

    module.addHeaderCode('#include <wx/ribbon/buttonbar.h>')
    module.insertItem(0, etgtools.WigCode("""\
        // forward declarations
        class wxRibbonButtonBarButtonBase;
        """))

    c = module.find('wxRibbonButtonBar')
    assert isinstance(c, etgtools.ClassDef)
    tools.fixWindowClass(c)


    c = module.find('wxRibbonButtonBarEvent')
    tools.fixEventClass(c)

    c.addPyCode("""\
        EVT_RIBBONBUTTONBAR_CLICKED = PyEventBinder( wxEVT_RIBBONBUTTONBAR_CLICKED, 1 )
        EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED = PyEventBinder( wxEVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED, 1 )
        """)
    
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()

