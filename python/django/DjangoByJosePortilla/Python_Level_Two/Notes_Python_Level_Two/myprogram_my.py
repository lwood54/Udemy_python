#### BASIC IMPORT ####
# import mymodule_my
#
# mymodule_my.func_in_module()

#### ALTERNATE IMPORT ####
# import mymodule_my as mm
#
# mm.func_in_module()

## ALTERNATE that only imports a few functions isntead of the whole module. ##
# from mymodule_my import func_in_module
# #then you don't have to put anything prefacing the function:
# func_in_module()

## ALTERNATE that is highly frowned on for wasting cpu memory, but is still optional ##
from mymodule_my import*
func_in_module()
## I guess the small gain is that you don't have to preface the function with anything, but at the cost of performance problems.
