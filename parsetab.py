
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABS ADD AND BOOL BYTES CAR CDR COMPARE CONCAT CONS DROP DUP EDIV EMPTY_MAP EMPTY_SET EQ EXEC FAILWITH FALSE GE GET GT INT LAMBDA LBRACKET LE LEFT LPAIR LPARENS LSL LSR LT MEM MUL NAT NEG NEQ NIL NONE NOT NUMBER OR PAIR PAIR_CONSTRUCTOR PUSH RBRACKET RIGHT RPARENS SCOLON SIZE SLICE SOME STRING SUB SWAP TEXT TRUE UNIT UPDATE XORexecution : compound_statement\n            | compound_statement SCOLON\n            | bodycompound_statement : stmt\n            | compound_statement SCOLON stmt\n            | compound_statement SCOLON stmt SCOLONbody : LBRACKET compound_statement RBRACKET\n            | LBRACKET RBRACKETstmt : LAMBDA TYPE TYPE bodystmt : DROP stmt : DUP stmt : SWAP stmt : UNIT bool : TRUE\n        | FALSE value : NUMBER\n        | bool\n        | TEXT\n        | LPARENS PAIR_CONSTRUCTOR value value RPARENS stmt : EQ\n        | NEQ\n        | LT\n        | GT\n        | LE\n        | GE  stmt : OR\n        | AND\n        | XOR  stmt : COMPAREstmt : NEG\n         | ABS\n         | ADD\n         | SUB\n         | MUL\n         | EDIV\n         | LSL\n         | LSR  stmt : CONCAT\n            | SIZE\n            | SLICE stmt : PAIR\n            | CAR\n            | CDR  stmt : EMPTY_SET TYPE\n            | MEM\n            | UPDATE stmt : SOME\n            | NONE TYPE stmt : LEFT TYPE\n            | RIGHT TYPE stmt : CONS\n            | NIL TYPE stmt : NOTstmt : EXECTYPE : NAT\n        | STRING\n        | INT\n        | BOOL\n        | BYTES\n        | LPARENS LPAIR TYPE TYPE RPARENS stmt : PUSH TYPE valuestmt : FAILWITH '
    
_lr_action_items = {'LBRACKET':([0,52,53,54,55,56,67,82,],[5,-55,-56,-57,-58,-59,5,-60,]),'LAMBDA':([0,5,48,66,],[6,6,6,6,]),'DROP':([0,5,48,66,],[7,7,7,7,]),'DUP':([0,5,48,66,],[8,8,8,8,]),'SWAP':([0,5,48,66,],[9,9,9,9,]),'UNIT':([0,5,48,66,],[10,10,10,10,]),'EQ':([0,5,48,66,],[11,11,11,11,]),'NEQ':([0,5,48,66,],[12,12,12,12,]),'LT':([0,5,48,66,],[13,13,13,13,]),'GT':([0,5,48,66,],[14,14,14,14,]),'LE':([0,5,48,66,],[15,15,15,15,]),'GE':([0,5,48,66,],[16,16,16,16,]),'OR':([0,5,48,66,],[17,17,17,17,]),'AND':([0,5,48,66,],[18,18,18,18,]),'XOR':([0,5,48,66,],[19,19,19,19,]),'COMPARE':([0,5,48,66,],[20,20,20,20,]),'NEG':([0,5,48,66,],[21,21,21,21,]),'ABS':([0,5,48,66,],[22,22,22,22,]),'ADD':([0,5,48,66,],[23,23,23,23,]),'SUB':([0,5,48,66,],[24,24,24,24,]),'MUL':([0,5,48,66,],[25,25,25,25,]),'EDIV':([0,5,48,66,],[26,26,26,26,]),'LSL':([0,5,48,66,],[27,27,27,27,]),'LSR':([0,5,48,66,],[28,28,28,28,]),'CONCAT':([0,5,48,66,],[29,29,29,29,]),'SIZE':([0,5,48,66,],[30,30,30,30,]),'SLICE':([0,5,48,66,],[31,31,31,31,]),'PAIR':([0,5,48,66,],[32,32,32,32,]),'CAR':([0,5,48,66,],[33,33,33,33,]),'CDR':([0,5,48,66,],[34,34,34,34,]),'EMPTY_SET':([0,5,48,66,],[35,35,35,35,]),'MEM':([0,5,48,66,],[36,36,36,36,]),'UPDATE':([0,5,48,66,],[37,37,37,37,]),'SOME':([0,5,48,66,],[38,38,38,38,]),'NONE':([0,5,48,66,],[39,39,39,39,]),'LEFT':([0,5,48,66,],[40,40,40,40,]),'RIGHT':([0,5,48,66,],[41,41,41,41,]),'CONS':([0,5,48,66,],[42,42,42,42,]),'NIL':([0,5,48,66,],[43,43,43,43,]),'NOT':([0,5,48,66,],[44,44,44,44,]),'EXEC':([0,5,48,66,],[45,45,45,45,]),'PUSH':([0,5,48,66,],[46,46,46,46,]),'FAILWITH':([0,5,48,66,],[47,47,47,47,]),'$end':([1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,42,44,45,47,48,50,52,53,54,55,56,58,59,60,61,62,64,65,69,70,71,72,74,75,76,77,82,84,],[0,-1,-3,-4,-10,-11,-12,-13,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,-46,-47,-51,-53,-54,-62,-2,-8,-55,-56,-57,-58,-59,-44,-48,-49,-50,-52,-5,-7,-61,-16,-17,-18,-14,-15,-6,-9,-60,-19,]),'SCOLON':([2,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,42,44,45,47,49,50,52,53,54,55,56,58,59,60,61,62,64,65,69,70,71,72,74,75,76,77,82,84,],[48,-4,-10,-11,-12,-13,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,-46,-47,-51,-53,-54,-62,66,-8,-55,-56,-57,-58,-59,-44,-48,-49,-50,-52,76,-7,-61,-16,-17,-18,-14,-15,-6,-9,-60,-19,]),'RBRACKET':([4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,42,44,45,47,49,50,52,53,54,55,56,58,59,60,61,62,64,65,69,70,71,72,74,75,76,77,82,84,],[-4,50,-10,-11,-12,-13,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,-46,-47,-51,-53,-54,-62,65,-8,-55,-56,-57,-58,-59,-44,-48,-49,-50,-52,-5,-7,-61,-16,-17,-18,-14,-15,-6,-9,-60,-19,]),'NAT':([6,35,39,40,41,43,46,51,52,53,54,55,56,68,78,82,],[52,52,52,52,52,52,52,52,-55,-56,-57,-58,-59,52,52,-60,]),'STRING':([6,35,39,40,41,43,46,51,52,53,54,55,56,68,78,82,],[53,53,53,53,53,53,53,53,-55,-56,-57,-58,-59,53,53,-60,]),'INT':([6,35,39,40,41,43,46,51,52,53,54,55,56,68,78,82,],[54,54,54,54,54,54,54,54,-55,-56,-57,-58,-59,54,54,-60,]),'BOOL':([6,35,39,40,41,43,46,51,52,53,54,55,56,68,78,82,],[55,55,55,55,55,55,55,55,-55,-56,-57,-58,-59,55,55,-60,]),'BYTES':([6,35,39,40,41,43,46,51,52,53,54,55,56,68,78,82,],[56,56,56,56,56,56,56,56,-55,-56,-57,-58,-59,56,56,-60,]),'LPARENS':([6,35,39,40,41,43,46,51,52,53,54,55,56,63,68,70,71,72,74,75,78,79,81,82,84,],[57,57,57,57,57,57,57,57,-55,-56,-57,-58,-59,73,57,-16,-17,-18,-14,-15,57,73,73,-60,-19,]),'NUMBER':([52,53,54,55,56,63,70,71,72,74,75,79,81,82,84,],[-55,-56,-57,-58,-59,70,-16,-17,-18,-14,-15,70,70,-60,-19,]),'TEXT':([52,53,54,55,56,63,70,71,72,74,75,79,81,82,84,],[-55,-56,-57,-58,-59,72,-16,-17,-18,-14,-15,72,72,-60,-19,]),'TRUE':([52,53,54,55,56,63,70,71,72,74,75,79,81,82,84,],[-55,-56,-57,-58,-59,74,-16,-17,-18,-14,-15,74,74,-60,-19,]),'FALSE':([52,53,54,55,56,63,70,71,72,74,75,79,81,82,84,],[-55,-56,-57,-58,-59,75,-16,-17,-18,-14,-15,75,75,-60,-19,]),'RPARENS':([52,53,54,55,56,70,71,72,74,75,80,82,83,84,],[-55,-56,-57,-58,-59,-16,-17,-18,-14,-15,82,-60,84,-19,]),'LPAIR':([57,],[68,]),'PAIR_CONSTRUCTOR':([73,],[79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'execution':([0,],[1,]),'compound_statement':([0,5,],[2,49,]),'body':([0,67,],[3,77,]),'stmt':([0,5,48,66,],[4,4,64,64,]),'TYPE':([6,35,39,40,41,43,46,51,68,78,],[51,58,59,60,61,62,63,67,78,80,]),'value':([63,79,81,],[69,81,83,]),'bool':([63,79,81,],[71,71,71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> execution","S'",1,None,None,None),
  ('execution -> compound_statement','execution',1,'p_execution','main.py',233),
  ('execution -> compound_statement SCOLON','execution',2,'p_execution','main.py',234),
  ('execution -> body','execution',1,'p_execution','main.py',235),
  ('compound_statement -> stmt','compound_statement',1,'p_compound_statement','main.py',246),
  ('compound_statement -> compound_statement SCOLON stmt','compound_statement',3,'p_compound_statement','main.py',247),
  ('compound_statement -> compound_statement SCOLON stmt SCOLON','compound_statement',4,'p_compound_statement','main.py',248),
  ('body -> LBRACKET compound_statement RBRACKET','body',3,'p_body','main.py',255),
  ('body -> LBRACKET RBRACKET','body',2,'p_body','main.py',256),
  ('stmt -> LAMBDA TYPE TYPE body','stmt',4,'p_lambda_statement','main.py',263),
  ('stmt -> DROP','stmt',1,'p_statement_drop','main.py',268),
  ('stmt -> DUP','stmt',1,'p_statement_dup','main.py',272),
  ('stmt -> SWAP','stmt',1,'p_statement_swap','main.py',276),
  ('stmt -> UNIT','stmt',1,'p_statement_unit','main.py',280),
  ('bool -> TRUE','bool',1,'p_bool','main.py',284),
  ('bool -> FALSE','bool',1,'p_bool','main.py',285),
  ('value -> NUMBER','value',1,'p_statement_value','main.py',289),
  ('value -> bool','value',1,'p_statement_value','main.py',290),
  ('value -> TEXT','value',1,'p_statement_value','main.py',291),
  ('value -> LPARENS PAIR_CONSTRUCTOR value value RPARENS','value',5,'p_statement_value','main.py',292),
  ('stmt -> EQ','stmt',1,'p_statement_generic_comparison','main.py',299),
  ('stmt -> NEQ','stmt',1,'p_statement_generic_comparison','main.py',300),
  ('stmt -> LT','stmt',1,'p_statement_generic_comparison','main.py',301),
  ('stmt -> GT','stmt',1,'p_statement_generic_comparison','main.py',302),
  ('stmt -> LE','stmt',1,'p_statement_generic_comparison','main.py',303),
  ('stmt -> GE','stmt',1,'p_statement_generic_comparison','main.py',304),
  ('stmt -> OR','stmt',1,'p_boolean_comparison','main.py',321),
  ('stmt -> AND','stmt',1,'p_boolean_comparison','main.py',322),
  ('stmt -> XOR','stmt',1,'p_boolean_comparison','main.py',323),
  ('stmt -> COMPARE','stmt',1,'p_compare_operation','main.py',348),
  ('stmt -> NEG','stmt',1,'p_integer_operations','main.py',360),
  ('stmt -> ABS','stmt',1,'p_integer_operations','main.py',361),
  ('stmt -> ADD','stmt',1,'p_integer_operations','main.py',362),
  ('stmt -> SUB','stmt',1,'p_integer_operations','main.py',363),
  ('stmt -> MUL','stmt',1,'p_integer_operations','main.py',364),
  ('stmt -> EDIV','stmt',1,'p_integer_operations','main.py',365),
  ('stmt -> LSL','stmt',1,'p_integer_operations','main.py',366),
  ('stmt -> LSR','stmt',1,'p_integer_operations','main.py',367),
  ('stmt -> CONCAT','stmt',1,'p_string_operations','main.py',400),
  ('stmt -> SIZE','stmt',1,'p_string_operations','main.py',401),
  ('stmt -> SLICE','stmt',1,'p_string_operations','main.py',402),
  ('stmt -> PAIR','stmt',1,'p_pair_operations','main.py',420),
  ('stmt -> CAR','stmt',1,'p_pair_operations','main.py',421),
  ('stmt -> CDR','stmt',1,'p_pair_operations','main.py',422),
  ('stmt -> EMPTY_SET TYPE','stmt',2,'p_set_operations','main.py',439),
  ('stmt -> MEM','stmt',1,'p_set_operations','main.py',440),
  ('stmt -> UPDATE','stmt',1,'p_set_operations','main.py',441),
  ('stmt -> SOME','stmt',1,'p_option_operations','main.py',457),
  ('stmt -> NONE TYPE','stmt',2,'p_option_operations','main.py',458),
  ('stmt -> LEFT TYPE','stmt',2,'p_union_operations','main.py',466),
  ('stmt -> RIGHT TYPE','stmt',2,'p_union_operations','main.py',467),
  ('stmt -> CONS','stmt',1,'p_list_operations','main.py',474),
  ('stmt -> NIL TYPE','stmt',2,'p_list_operations','main.py',475),
  ('stmt -> NOT','stmt',1,'p_boolean_not','main.py',485),
  ('stmt -> EXEC','stmt',1,'p_exec','main.py',496),
  ('TYPE -> NAT','TYPE',1,'p_statement_type','main.py',505),
  ('TYPE -> STRING','TYPE',1,'p_statement_type','main.py',506),
  ('TYPE -> INT','TYPE',1,'p_statement_type','main.py',507),
  ('TYPE -> BOOL','TYPE',1,'p_statement_type','main.py',508),
  ('TYPE -> BYTES','TYPE',1,'p_statement_type','main.py',509),
  ('TYPE -> LPARENS LPAIR TYPE TYPE RPARENS','TYPE',5,'p_statement_type','main.py',510),
  ('stmt -> PUSH TYPE value','stmt',3,'p_statement_push','main.py',525),
  ('stmt -> FAILWITH','stmt',1,'p_statement_failwith','main.py',544),
]
