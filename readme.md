# [Minim TestKit](https://bitbucket.org/danedens/minimtestkit)  


# Project Description
        
Parent command and control hub for Test automation Kits for the DVT Lab.  

### Problems ->> (
        Current Layout is overwhelming.  
            Will Update python scripts into modules for reusablity and readablity  
        Not fully Automated
        Breaks on job failure  
        Reports manually handled post job  
        
###     )
    
### Proposed Solutions ->> (  
        There will be this parent repo, which will be capable of importing sub-repo testkits depending on usecase per machine.
        Create single entry point with validatin tests, Streamlined Arguments, and 
        Add MQTT pubs to various stages of build for Debug mode and monitoring        
        
###     )  

### Upstream Brainstorm "would be cool if" ->> (  
        All - Pipelines intergrate directly to Jira Issues for triggering and reports  
        All- Complete configuration from Webportal  
        SoakTest - Local Webserver - GUI for scheduling commands and device statuses interface.  
        All - Status screen in DVT lab, LEDs or Dashboard Indicators for Device status and recent Test pass/fail  
        
###     ) 


# Documentation Tree  

### /root/Readme.md  
        Project Overview  
        Sub-Repos  
        Tools proposed:  
            1. host BitBucket => Jira Issue Intergration  
            2. Sphinx using RST => Confluence(Automation board)  
### /root/docs/  
        \--build  
        \--source  
            conf.py  
                Upload settings and styling variables
            index.rst  
                Page Layout
            arguments.rst  
                Docs for runtime arguments
            readme.rst
                Usage and Installation
            docstringtest.rst  
                Import all function docstring in single location for devolpment
                Not visable from index
            SoakTestKit.md (sys link to /root/SoakTestKit/readme.md)
            CDRouterTest.md (sys link to /root/CDRouterTestKit/readme.md
        make.bat
        Makefile  
        publishToConfluence.bat  
        
### /root/data
        runlogs
        artifacts (reports)
        Tempfiles

### /root/venv
    Python Env

### /root/.bin
    Non-python Scripts and binarys

### /root/.run
    Pycharm build scripts
    
### /root/TestKit
    |--tests
        pytest files (non-DVT tests)
    __init__.py
        Imports and Argument parsing
    config.py
        Configuration methods
    devices.py
        Device specific methods
    TestKit.py
        Thread manager Entry point
    utlis.py
        Utility methods
    
# Sub-Repositories  


    1. CDRouterTestKit (currently being built from DVT repo)  
        Furthur Information - [CDRouterTestKit Readme](brokenlink)  
        ToDo:  
            1. Roadmap project.   
            1. Break CDRouter into standalone repo. To Be renamed CDRouterTestKit once isolated   
    
    1. SoakTestKit   
        Furthur Information - [SoakTestKit Brainstorm](brokenlink)  
        ToDO:  
            1. Roadmap project  
            1. Document current functions   
            1. Data brainstorm  
            1. Version control and remote maintenance brainstorm  
