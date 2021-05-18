#
# Copyright (c) Andre Slabber. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
#  

*** Settings ***
Documentation		This testset runs with no setup or teardown whatsoever, 
...					basic tests for starting and stopping programs.

Library   			testtoolkit.py
Library   			teststeps.py

*** Test Cases ***

Are Prerequisites Taken Care Of?
	[Tags]              Complete
	${Result}    		Check Test Requirements
	Should Be True		${Result}
	
Can We Clear Appdata?
	[Tags]              Complete
	${Result}    		Clear Appdata
	Should Be True		${Result}

# This immediately follows the above test so we can reset the checkmark.
Can We Start Brain Simulator II with Getting Started?
	[Tags]              Complete
	${Result}    		Start Brain Simulator with Getting Started
	Should Be True		${Result}

Can We Stop Brain Simulator II?
	[Tags]              Complete
	${Result}    		Stop Brain Simulator
	Should Be True		${Result}

Can We Start Neuron Server?
	[Tags]                                                     Complete
	${Result}    		Start Neuron Server
	Should Be True		${Result}

Can We Stop Neuron Server?
	[Tags]                                                     Complete
	${Result}    		Stop Neuron Server
	Should Be True		${Result}


	