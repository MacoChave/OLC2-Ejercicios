
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALNOIGUALMENORMAYORMENORIGUALMAYORIGUALleftORleftANDrightNOTAND DIV ID IGUAL MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS NOIGUAL NOT NUM OR PARD PARI PORstart : logic_ologic_o : logic_o OR logic_alogic_o : logic_alogic_a : logic_a AND logic_nlogic_a : logic_nlogic_n : NOT logic_ologic_n : exp_rexp_r    : exp_e MENOR exp_e\n                | exp_e MENORIGUAL exp_e\n                | exp_e MAYOR exp_e\n                | exp_e MAYORIGUAL exp_e\n                | exp_e IGUAL exp_e\n                | exp_e NOIGUAL exp_eexp_e    : exp_e MAS exp_t\n                | exp_e MENOS exp_texp_e : exp_texp_t    : exp_t POR exp_f\n                | exp_t DIV exp_fexp_t : exp_fexp_f : PARI exp_e PARDexp_f : IDexp_f : NUM'
    
_lr_action_items = {'NOT':([0,5,13,14,],[5,5,5,5,]),'PARI':([0,5,10,13,14,16,17,18,19,20,21,22,23,24,25,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ID':([0,5,10,13,14,16,17,18,19,20,21,22,23,24,25,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'NUM':([0,5,10,13,14,16,17,18,19,20,21,22,23,24,25,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'$end':([1,2,3,4,6,8,9,11,12,15,27,28,29,30,31,32,33,34,35,36,37,38,39,],[0,-1,-3,-5,-7,-16,-19,-21,-22,-6,-2,-4,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-20,]),'OR':([2,3,4,6,8,9,11,12,15,27,28,29,30,31,32,33,34,35,36,37,38,39,],[13,-3,-5,-7,-16,-19,-21,-22,-6,-2,-4,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-20,]),'AND':([3,4,6,8,9,11,12,15,27,28,29,30,31,32,33,34,35,36,37,38,39,],[14,-5,-7,-16,-19,-21,-22,-6,14,-4,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-20,]),'MENOR':([7,8,9,11,12,35,36,37,38,39,],[16,-16,-19,-21,-22,-14,-15,-17,-18,-20,]),'MENORIGUAL':([7,8,9,11,12,35,36,37,38,39,],[17,-16,-19,-21,-22,-14,-15,-17,-18,-20,]),'MAYOR':([7,8,9,11,12,35,36,37,38,39,],[18,-16,-19,-21,-22,-14,-15,-17,-18,-20,]),'MAYORIGUAL':([7,8,9,11,12,35,36,37,38,39,],[19,-16,-19,-21,-22,-14,-15,-17,-18,-20,]),'IGUAL':([7,8,9,11,12,35,36,37,38,39,],[20,-16,-19,-21,-22,-14,-15,-17,-18,-20,]),'NOIGUAL':([7,8,9,11,12,35,36,37,38,39,],[21,-16,-19,-21,-22,-14,-15,-17,-18,-20,]),'MAS':([7,8,9,11,12,26,29,30,31,32,33,34,35,36,37,38,39,],[22,-16,-19,-21,-22,22,22,22,22,22,22,22,-14,-15,-17,-18,-20,]),'MENOS':([7,8,9,11,12,26,29,30,31,32,33,34,35,36,37,38,39,],[23,-16,-19,-21,-22,23,23,23,23,23,23,23,-14,-15,-17,-18,-20,]),'PARD':([8,9,11,12,26,35,36,37,38,39,],[-16,-19,-21,-22,39,-14,-15,-17,-18,-20,]),'POR':([8,9,11,12,35,36,37,38,39,],[24,-19,-21,-22,24,24,-17,-18,-20,]),'DIV':([8,9,11,12,35,36,37,38,39,],[25,-19,-21,-22,25,25,-17,-18,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'logic_o':([0,5,],[2,15,]),'logic_a':([0,5,13,],[3,3,27,]),'logic_n':([0,5,13,14,],[4,4,4,28,]),'exp_r':([0,5,13,14,],[6,6,6,6,]),'exp_e':([0,5,10,13,14,16,17,18,19,20,21,],[7,7,26,7,7,29,30,31,32,33,34,]),'exp_t':([0,5,10,13,14,16,17,18,19,20,21,22,23,],[8,8,8,8,8,8,8,8,8,8,8,35,36,]),'exp_f':([0,5,10,13,14,16,17,18,19,20,21,22,23,24,25,],[9,9,9,9,9,9,9,9,9,9,9,9,9,37,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> logic_o','start',1,'p_start','gramatica.py',85),
  ('logic_o -> logic_o OR logic_a','logic_o',3,'p_logic_o','gramatica.py',89),
  ('logic_o -> logic_a','logic_o',1,'p_to_logic_a','gramatica.py',94),
  ('logic_a -> logic_a AND logic_n','logic_a',3,'p_logic_a','gramatica.py',98),
  ('logic_a -> logic_n','logic_a',1,'p_to_logic_not','gramatica.py',103),
  ('logic_n -> NOT logic_o','logic_n',2,'p_logic_not','gramatica.py',107),
  ('logic_n -> exp_r','logic_n',1,'p_logic_rel','gramatica.py',111),
  ('exp_r -> exp_e MENOR exp_e','exp_r',3,'p_rel','gramatica.py',115),
  ('exp_r -> exp_e MENORIGUAL exp_e','exp_r',3,'p_rel','gramatica.py',116),
  ('exp_r -> exp_e MAYOR exp_e','exp_r',3,'p_rel','gramatica.py',117),
  ('exp_r -> exp_e MAYORIGUAL exp_e','exp_r',3,'p_rel','gramatica.py',118),
  ('exp_r -> exp_e IGUAL exp_e','exp_r',3,'p_rel','gramatica.py',119),
  ('exp_r -> exp_e NOIGUAL exp_e','exp_r',3,'p_rel','gramatica.py',120),
  ('exp_e -> exp_e MAS exp_t','exp_e',3,'p_adicion','gramatica.py',163),
  ('exp_e -> exp_e MENOS exp_t','exp_e',3,'p_adicion','gramatica.py',164),
  ('exp_e -> exp_t','exp_e',1,'p_to_multiplo','gramatica.py',175),
  ('exp_t -> exp_t POR exp_f','exp_t',3,'p_multiplicacion','gramatica.py',179),
  ('exp_t -> exp_t DIV exp_f','exp_t',3,'p_multiplicacion','gramatica.py',180),
  ('exp_t -> exp_f','exp_t',1,'p_to_f','gramatica.py',191),
  ('exp_f -> PARI exp_e PARD','exp_f',3,'p_parentesis','gramatica.py',195),
  ('exp_f -> ID','exp_f',1,'p_soloid','gramatica.py',199),
  ('exp_f -> NUM','exp_f',1,'p_num','gramatica.py',203),
]
