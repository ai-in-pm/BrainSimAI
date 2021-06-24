#
# Copyright (c) Andre Slabber. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
#  

import os
import time
import shutil
import pyautogui
from pyscreeze import ImageNotFoundException

import testtoolkit as tk     # the very basic routines we use from PyAutoGUI again and again.

def harmless_click_to_focus():
    return tk.click(145, 1028)

def clear_appdata():
    futureai_localappdata = os.path.join(os.getenv('LOCALAPPDATA'), 'FutureAI')
    shutil.rmtree(futureai_localappdata)
    return True

def select_no_on_save_prompt():
    time.sleep(0.2)
    if tk.wait_and_hover('save_question'):
        time.sleep(0.2)
        tk.click(975, 600)
    return True

def do_menu_choice(menu, item):
    if not harmless_click_to_focus():
        return False
    if not tk.wait_and_click(menu):
        return False
    if not tk.wait_and_click(item):
        return False
    
def do_icon_choice(icon_choice):
    if not harmless_click_to_focus():
        return False
    if not tk.wait_and_click(icon_choice):
        return False
    return True

def check_new_network_complete():
    if not tk.wait_for_center('new_network_dialog_title'):
        return False 
    if not tk.wait_for_center('new_network_dialog_textblock'):
        return False 
    if not tk.wait_for_center('new_network_dialog_width'):
        return False 
    if not tk.wait_for_center('new_network_dialog_height'):
        return False 
    if not tk.wait_for_center('new_network_dialog_refractory_cycles'):
        return False 
    if not tk.wait_for_center('new_network_dialog_use_servers_unchecked'):
        return False 
    if not tk.wait_for_center('new_network_dialog_ok_default'):
        return False 
    if not tk.wait_for_center('new_network_dialog_title'):
        return False 
    if not tk.wait_and_click('new_network_dialog_cancel_enabled'):
        return False 
    return True
    
def check_file_new_shows_new_network_dialog():
    do_menu_choice('bs2_file_menu', 'bs2_file_new_item')
    return check_new_network_complete()

def check_icon_new_shows_new_network_dialog():
    do_icon_choice('bs2_icon_new_enabled')
    return check_new_network_complete()
 
def check_open_network_dialog_complete():
    if not tk.wait_for_center('file_open_dialog_title'):
        return False 
    if not tk.wait_for_center('file_open_dialog_filename'):
        return False 
    if not tk.wait_for_center('file_open_dialog_filetype'):
        return False 
    if not tk.wait_for_center('file_open_dialog_open_default'):
        return False 
    if not tk.wait_and_click('file_open_dialog_cancel_enabled'):
        return False 
    return True
    
def check_file_open_shows_network_load_dialog():
    do_menu_choice('bs2_file_menu', 'bs2_file_open_item')
    return check_open_network_dialog_complete()

def check_icon_open_shows_network_load_dialog():
    do_icon_choice('bs2_icon_open_enabled')
    return check_open_network_dialog_complete()

def check_save_as_dialog_complete():
    if not tk.wait_for_center('save_as_dialog_title'):
        return False 
    if not tk.wait_for_center('save_as_dialog_filename'):
        return False 
    if not tk.wait_for_center('save_as_dialog_filetype'):
        return False 
    if not tk.wait_for_center('save_as_dialog_save_default'):
        return False 
    if not tk.wait_and_click('save_as_dialog_cancel_enabled'):
        return False 
    return True
    
def check_file_save_as_shows_network_save_as_dialog():
    do_menu_choice('bs2_file_menu', 'bs2_file_save_as_item')
    return check_save_as_dialog_complete()

def check_icon_save_as_shows_network_save_as_dialog():
    do_icon_choice('bs2_icon_save_as_enabled')
    return check_save_as_dialog_complete()
    
def check_network_library_entry(menu_item, relevant_part):
    harmless_click_to_focus()
    if not tk.wait_and_click('bs2_file_menu'):
        return False
    if not tk.wait_and_click('bs2_file_library_item'):
        return False
    if not tk.wait_and_click(menu_item):
        return False
    if not tk.wait_and_click('notes_ok_button_enabled'):
        return False
    if not tk.wait_for_center(relevant_part):
        return False
    return True

def check_recent_network_entry(menu_item, tool_tip, relevant_part):
    harmless_click_to_focus()
    if not tk.wait_and_click('bs2_file_menu'):
        return False
    if not tk.wait_and_click('bs2_file_recent_item'):
        return False
    if not tk.wait_and_hover(menu_item):
        return False
    if not tk.wait_for_center(tool_tip):
        return False
    if not tk.wait_and_click(menu_item):
        return False
    if not tk.wait_and_click('notes_ok_button_enabled'):
        return False
    if not tk.wait_for_center(relevant_part):
        return False
    return True

def check_synapse_is_drawn_correctly(weight, model, drawn_synapse):
    select_weight_combobox(int(weight))
    select_model_combobox(int(model))
    tk.drag_from_to(30, 115, 95, 115, 0.2)
    harmless_click_to_focus()
    if not tk.wait_and_hover(drawn_synapse):
        return False  
    pyautogui.hotkey('control', 'Z')
    return True

def select_module_combobox(page, option):
    ys = [92, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290,
          310, 330, 350, 370, 390, 410]
    tk.click(1411, 67)
    time.sleep(0.5)
    # go to first page
    for i in range(2):
        tk.click(1460, 103)
    # go to correct page
    for i in range(page):
        tk.click(1460, 420)
    tk.click(1411, ys[option])
    
def select_weight_combobox(option):
    ys = [92, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290]
    tk.click(1630, 67)
    time.sleep(0.1)
    tk.click(1630, ys[option])
    
def select_model_combobox(option):
    ys = [92, 110, 130, 150]
    tk.click(1756, 67)
    time.sleep(0.1)
    tk.click(1756, ys[option])

def insert_module(page, index):
    select_module_combobox(int(page), int(index))
    pyautogui.moveTo([95, 185])
    pyautogui.click([95, 185])
    harmless_click_to_focus()

def select_module(page, screenshot):
    # go to first page
    for i in range(2):
        tk.click(365, 350)
    # go to correct page
    for i in range(page):
        tk.click(365, 670)
    if not tk.wait_and_click(screenshot):
        result = False  

def remove_module():
    pyautogui.rightClick([70, 150])
    return tk.wait_and_click('delete_module_item')
    
def check_module_is_inserted_correctly_with_warning(page, index, drawn_module, warning):
    result = check_module_is_inserted_correctly(page, index, drawn_module)
    if not tk.wait_and_click(warning):
        result = False  
    pyautogui.press('escape')
    pyautogui.press('escape')
    remove_module()
    return result
