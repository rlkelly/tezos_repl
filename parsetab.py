
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABS ADD ADDRESS AND ASSERT ASSERT_EQ ASSERT_GT ASSERT_GTE ASSERT_LT ASSERT_LTE ASSERT_NEQ BLAKE2B BOOL BYTES CAR CDR CHECK_SIGNATURE CODE COMPARE CONCAT CONS CONTRACT DIP DROP DUP EDIV EMPTY_MAP EMPTY_SET EQ EXEC FAIL FAILWITH FALSE GE GET GT HASH_KEY IF_CONS IF_LEFT IF_RIGHT INT ITER LAMBDA LBRACKET LE LEFT LPAIR LPARENS LSL LSR LT MAP MEM MUL MUTEZ NAT NEG NEQ NIL NONE NOT NOW NUMBER OPERATION OR PAIR PAIR_CONSTRUCTOR PARAMETER PRINTER PUSH RBRACKET RIGHT RPARENS SCOLON SHA256 SHA512 SIZE SLICE SOME STEPS_TO_QUOTA STORAGE STRING SUB SWAP TEXT TIMESTAMP TRUE UNIT UPDATE XORcontract_run : contract_decl code_decl\n        |  executioncontract_decl : PARAMETER type SCOLON STORAGE type SCOLONcode_decl : CODE bodyexecution : compound_statement\n            | compound_statement SCOLON\n            | bodycompound_statement : stmt\n            | compound_statement SCOLON stmtbody : LBRACKET compound_statement SCOLON RBRACKET\n            | LBRACKET compound_statement RBRACKET\n            | LBRACKET RBRACKETstmt : LAMBDA type type bodystmt : DROPstmt : DUPstmt : SWAPstmt : UNITbool : TRUE\n        | FALSE value : NUMBER\n        | bool\n        | TEXT\n        | LPARENS PAIR_CONSTRUCTOR value value RPARENS stmt : EQ\n        | NEQ\n        | LT\n        | GT\n        | LE\n        | GE  stmt : OR\n        | AND\n        | XOR  stmt : COMPAREstmt : NEG\n         | ABS\n         | ADD\n         | SUB\n         | MUL\n         | EDIV\n         | LSL\n         | LSR stmt : SIZEstmt : CONCAT\n            | SLICEstmt : PAIR\n            | CAR\n            | CDR stmt : EMPTY_SET type\n            | MEM\n            | UPDATE stmt : EMPTY_MAP type type\n            | MAP body\n            | ITER body\n            | GETstmt : IF_LEFT body body\n        | IF_RIGHT body bodystmt : IF_CONS body bodystmt : SOME\n            | NONE type stmt : LEFT type\n            | RIGHT type stmt : CONS\n            | NIL type stmt : NOTstmt : EXECstmt : STEPS_TO_QUOTA\n            | NOW stmt : CONTRACT typestmt : HASH_KEY\n            | BLAKE2B\n            | SHA256\n            | SHA512\n            | CHECK_SIGNATUREtype : NAT\n        | STRING\n        | INT\n        | BOOL\n        | BYTES\n        | OPERATION\n        | ADDRESS\n        | TIMESTAMP\n        | LPARENS LPAIR type type RPARENS stmt : DIP bodystmt : PUSH type valuestmt : ASSERT\n        | ASSERT_EQ\n        | ASSERT_NEQ\n        | ASSERT_LT\n        | ASSERT_LTE\n        | ASSERT_GT\n        | ASSERT_GTEstmt : FAILWITH\n            | FAILstmt : PRINTER'
    
_lr_action_items = {'PARAMETER':([0,],[4,]),'LBRACKET':([0,42,43,45,46,47,64,77,79,80,81,82,83,84,85,86,90,96,97,98,111,112,126,133,],[8,8,8,8,8,8,8,8,-74,-75,-76,-77,-78,-79,-80,-81,-12,8,8,8,-11,8,-10,-82,]),'LAMBDA':([0,8,88,110,],[9,9,9,9,]),'DROP':([0,8,88,110,],[10,10,10,10,]),'DUP':([0,8,88,110,],[11,11,11,11,]),'SWAP':([0,8,88,110,],[12,12,12,12,]),'UNIT':([0,8,88,110,],[13,13,13,13,]),'EQ':([0,8,88,110,],[14,14,14,14,]),'NEQ':([0,8,88,110,],[15,15,15,15,]),'LT':([0,8,88,110,],[16,16,16,16,]),'GT':([0,8,88,110,],[17,17,17,17,]),'LE':([0,8,88,110,],[18,18,18,18,]),'GE':([0,8,88,110,],[19,19,19,19,]),'OR':([0,8,88,110,],[20,20,20,20,]),'AND':([0,8,88,110,],[21,21,21,21,]),'XOR':([0,8,88,110,],[22,22,22,22,]),'COMPARE':([0,8,88,110,],[23,23,23,23,]),'NEG':([0,8,88,110,],[24,24,24,24,]),'ABS':([0,8,88,110,],[25,25,25,25,]),'ADD':([0,8,88,110,],[26,26,26,26,]),'SUB':([0,8,88,110,],[27,27,27,27,]),'MUL':([0,8,88,110,],[28,28,28,28,]),'EDIV':([0,8,88,110,],[29,29,29,29,]),'LSL':([0,8,88,110,],[30,30,30,30,]),'LSR':([0,8,88,110,],[31,31,31,31,]),'SIZE':([0,8,88,110,],[32,32,32,32,]),'CONCAT':([0,8,88,110,],[33,33,33,33,]),'SLICE':([0,8,88,110,],[34,34,34,34,]),'PAIR':([0,8,88,110,],[35,35,35,35,]),'CAR':([0,8,88,110,],[36,36,36,36,]),'CDR':([0,8,88,110,],[37,37,37,37,]),'EMPTY_SET':([0,8,88,110,],[38,38,38,38,]),'MEM':([0,8,88,110,],[39,39,39,39,]),'UPDATE':([0,8,88,110,],[40,40,40,40,]),'EMPTY_MAP':([0,8,88,110,],[41,41,41,41,]),'MAP':([0,8,88,110,],[42,42,42,42,]),'ITER':([0,8,88,110,],[43,43,43,43,]),'GET':([0,8,88,110,],[44,44,44,44,]),'IF_LEFT':([0,8,88,110,],[45,45,45,45,]),'IF_RIGHT':([0,8,88,110,],[46,46,46,46,]),'IF_CONS':([0,8,88,110,],[47,47,47,47,]),'SOME':([0,8,88,110,],[48,48,48,48,]),'NONE':([0,8,88,110,],[49,49,49,49,]),'LEFT':([0,8,88,110,],[50,50,50,50,]),'RIGHT':([0,8,88,110,],[51,51,51,51,]),'CONS':([0,8,88,110,],[52,52,52,52,]),'NIL':([0,8,88,110,],[53,53,53,53,]),'NOT':([0,8,88,110,],[54,54,54,54,]),'EXEC':([0,8,88,110,],[55,55,55,55,]),'STEPS_TO_QUOTA':([0,8,88,110,],[56,56,56,56,]),'NOW':([0,8,88,110,],[57,57,57,57,]),'CONTRACT':([0,8,88,110,],[58,58,58,58,]),'HASH_KEY':([0,8,88,110,],[59,59,59,59,]),'BLAKE2B':([0,8,88,110,],[60,60,60,60,]),'SHA256':([0,8,88,110,],[61,61,61,61,]),'SHA512':([0,8,88,110,],[62,62,62,62,]),'CHECK_SIGNATURE':([0,8,88,110,],[63,63,63,63,]),'DIP':([0,8,88,110,],[64,64,64,64,]),'PUSH':([0,8,88,110,],[65,65,65,65,]),'ASSERT':([0,8,88,110,],[66,66,66,66,]),'ASSERT_EQ':([0,8,88,110,],[67,67,67,67,]),'ASSERT_NEQ':([0,8,88,110,],[68,68,68,68,]),'ASSERT_LT':([0,8,88,110,],[69,69,69,69,]),'ASSERT_LTE':([0,8,88,110,],[70,70,70,70,]),'ASSERT_GT':([0,8,88,110,],[71,71,71,71,]),'ASSERT_GTE':([0,8,88,110,],[72,72,72,72,]),'FAILWITH':([0,8,88,110,],[73,73,73,73,]),'FAIL':([0,8,88,110,],[74,74,74,74,]),'PRINTER':([0,8,88,110,],[75,75,75,75,]),'$end':([1,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,44,48,52,54,55,56,57,59,60,61,62,63,66,67,68,69,70,71,72,73,74,75,76,79,80,81,82,83,84,85,86,88,90,92,94,95,99,100,101,102,103,104,106,109,111,113,114,115,116,117,118,119,120,122,123,126,127,133,135,],[0,-2,-5,-7,-8,-14,-15,-16,-17,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-49,-50,-54,-58,-62,-64,-65,-66,-67,-69,-70,-71,-72,-73,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-1,-74,-75,-76,-77,-78,-79,-80,-81,-6,-12,-48,-52,-53,-59,-60,-61,-63,-68,-83,-4,-9,-11,-51,-55,-56,-57,-84,-20,-21,-22,-18,-19,-10,-13,-82,-23,]),'CODE':([2,132,],[77,-3,]),'NAT':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[79,79,79,79,79,79,79,79,79,79,-74,-75,-76,-77,-78,-79,-80,-81,79,79,79,79,79,-82,]),'STRING':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[80,80,80,80,80,80,80,80,80,80,-74,-75,-76,-77,-78,-79,-80,-81,80,80,80,80,80,-82,]),'INT':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[81,81,81,81,81,81,81,81,81,81,-74,-75,-76,-77,-78,-79,-80,-81,81,81,81,81,81,-82,]),'BOOL':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[82,82,82,82,82,82,82,82,82,82,-74,-75,-76,-77,-78,-79,-80,-81,82,82,82,82,82,-82,]),'BYTES':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[83,83,83,83,83,83,83,83,83,83,-74,-75,-76,-77,-78,-79,-80,-81,83,83,83,83,83,-82,]),'OPERATION':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[84,84,84,84,84,84,84,84,84,84,-74,-75,-76,-77,-78,-79,-80,-81,84,84,84,84,84,-82,]),'ADDRESS':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[85,85,85,85,85,85,85,85,85,85,-74,-75,-76,-77,-78,-79,-80,-81,85,85,85,85,85,-82,]),'TIMESTAMP':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,108,124,125,133,],[86,86,86,86,86,86,86,86,86,86,-74,-75,-76,-77,-78,-79,-80,-81,86,86,86,86,86,-82,]),'LPARENS':([4,9,38,41,49,50,51,53,58,65,79,80,81,82,83,84,85,86,91,93,105,108,118,119,120,122,123,124,125,128,131,133,135,],[87,87,87,87,87,87,87,87,87,87,-74,-75,-76,-77,-78,-79,-80,-81,87,87,121,87,-20,-21,-22,-18,-19,87,87,121,121,-82,-23,]),'SCOLON':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,44,48,52,54,55,56,57,59,60,61,62,63,66,67,68,69,70,71,72,73,74,75,78,79,80,81,82,83,84,85,86,89,90,92,94,95,99,100,101,102,103,104,109,111,113,114,115,116,117,118,119,120,122,123,126,127,129,133,135,],[88,-8,-14,-15,-16,-17,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-49,-50,-54,-58,-62,-64,-65,-66,-67,-69,-70,-71,-72,-73,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,107,-74,-75,-76,-77,-78,-79,-80,-81,110,-12,-48,-52,-53,-59,-60,-61,-63,-68,-83,-9,-11,-51,-55,-56,-57,-84,-20,-21,-22,-18,-19,-10,-13,132,-82,-23,]),'RBRACKET':([7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,44,48,52,54,55,56,57,59,60,61,62,63,66,67,68,69,70,71,72,73,74,75,79,80,81,82,83,84,85,86,89,90,92,94,95,99,100,101,102,103,104,109,110,111,113,114,115,116,117,118,119,120,122,123,126,127,133,135,],[-8,90,-14,-15,-16,-17,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-49,-50,-54,-58,-62,-64,-65,-66,-67,-69,-70,-71,-72,-73,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-74,-75,-76,-77,-78,-79,-80,-81,111,-12,-48,-52,-53,-59,-60,-61,-63,-68,-83,-9,126,-11,-51,-55,-56,-57,-84,-20,-21,-22,-18,-19,-10,-13,-82,-23,]),'NUMBER':([79,80,81,82,83,84,85,86,105,118,119,120,122,123,128,131,133,135,],[-74,-75,-76,-77,-78,-79,-80,-81,118,-20,-21,-22,-18,-19,118,118,-82,-23,]),'TEXT':([79,80,81,82,83,84,85,86,105,118,119,120,122,123,128,131,133,135,],[-74,-75,-76,-77,-78,-79,-80,-81,120,-20,-21,-22,-18,-19,120,120,-82,-23,]),'TRUE':([79,80,81,82,83,84,85,86,105,118,119,120,122,123,128,131,133,135,],[-74,-75,-76,-77,-78,-79,-80,-81,122,-20,-21,-22,-18,-19,122,122,-82,-23,]),'FALSE':([79,80,81,82,83,84,85,86,105,118,119,120,122,123,128,131,133,135,],[-74,-75,-76,-77,-78,-79,-80,-81,123,-20,-21,-22,-18,-19,123,123,-82,-23,]),'RPARENS':([79,80,81,82,83,84,85,86,118,119,120,122,123,130,133,134,135,],[-74,-75,-76,-77,-78,-79,-80,-81,-20,-21,-22,-18,-19,133,-82,135,-23,]),'LPAIR':([87,],[108,]),'STORAGE':([107,],[124,]),'PAIR_CONSTRUCTOR':([121,],[128,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'contract_run':([0,],[1,]),'contract_decl':([0,],[2,]),'execution':([0,],[3,]),'compound_statement':([0,8,],[5,89,]),'body':([0,42,43,45,46,47,64,77,96,97,98,112,],[6,94,95,96,97,98,104,106,114,115,116,127,]),'stmt':([0,8,88,110,],[7,7,109,109,]),'code_decl':([2,],[76,]),'type':([4,9,38,41,49,50,51,53,58,65,91,93,108,124,125,],[78,91,92,93,99,100,101,102,103,105,112,113,125,129,130,]),'value':([105,128,131,],[117,131,134,]),'bool':([105,128,131,],[119,119,119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> contract_run","S'",1,None,None,None),
  ('contract_run -> contract_decl code_decl','contract_run',2,'p_contract','main.py',310),
  ('contract_run -> execution','contract_run',1,'p_contract','main.py',311),
  ('contract_decl -> PARAMETER type SCOLON STORAGE type SCOLON','contract_decl',6,'p_contract_constructor','main.py',315),
  ('code_decl -> CODE body','code_decl',2,'p_contract_code','main.py',320),
  ('execution -> compound_statement','execution',1,'p_execution','main.py',332),
  ('execution -> compound_statement SCOLON','execution',2,'p_execution','main.py',333),
  ('execution -> body','execution',1,'p_execution','main.py',334),
  ('compound_statement -> stmt','compound_statement',1,'p_compound_statement','main.py',343),
  ('compound_statement -> compound_statement SCOLON stmt','compound_statement',3,'p_compound_statement','main.py',344),
  ('body -> LBRACKET compound_statement SCOLON RBRACKET','body',4,'p_body','main.py',353),
  ('body -> LBRACKET compound_statement RBRACKET','body',3,'p_body','main.py',354),
  ('body -> LBRACKET RBRACKET','body',2,'p_body','main.py',355),
  ('stmt -> LAMBDA type type body','stmt',4,'p_lambda_statement','main.py',362),
  ('stmt -> DROP','stmt',1,'p_statement_drop','main.py',369),
  ('stmt -> DUP','stmt',1,'p_statement_dup','main.py',376),
  ('stmt -> SWAP','stmt',1,'p_statement_swap','main.py',383),
  ('stmt -> UNIT','stmt',1,'p_statement_unit','main.py',390),
  ('bool -> TRUE','bool',1,'p_bool','main.py',397),
  ('bool -> FALSE','bool',1,'p_bool','main.py',398),
  ('value -> NUMBER','value',1,'p_statement_value','main.py',402),
  ('value -> bool','value',1,'p_statement_value','main.py',403),
  ('value -> TEXT','value',1,'p_statement_value','main.py',404),
  ('value -> LPARENS PAIR_CONSTRUCTOR value value RPARENS','value',5,'p_statement_value','main.py',405),
  ('stmt -> EQ','stmt',1,'p_statement_generic_comparison','main.py',412),
  ('stmt -> NEQ','stmt',1,'p_statement_generic_comparison','main.py',413),
  ('stmt -> LT','stmt',1,'p_statement_generic_comparison','main.py',414),
  ('stmt -> GT','stmt',1,'p_statement_generic_comparison','main.py',415),
  ('stmt -> LE','stmt',1,'p_statement_generic_comparison','main.py',416),
  ('stmt -> GE','stmt',1,'p_statement_generic_comparison','main.py',417),
  ('stmt -> OR','stmt',1,'p_boolean_comparison','main.py',438),
  ('stmt -> AND','stmt',1,'p_boolean_comparison','main.py',439),
  ('stmt -> XOR','stmt',1,'p_boolean_comparison','main.py',440),
  ('stmt -> COMPARE','stmt',1,'p_compare_operation','main.py',468),
  ('stmt -> NEG','stmt',1,'p_integer_operations','main.py',483),
  ('stmt -> ABS','stmt',1,'p_integer_operations','main.py',484),
  ('stmt -> ADD','stmt',1,'p_integer_operations','main.py',485),
  ('stmt -> SUB','stmt',1,'p_integer_operations','main.py',486),
  ('stmt -> MUL','stmt',1,'p_integer_operations','main.py',487),
  ('stmt -> EDIV','stmt',1,'p_integer_operations','main.py',488),
  ('stmt -> LSL','stmt',1,'p_integer_operations','main.py',489),
  ('stmt -> LSR','stmt',1,'p_integer_operations','main.py',490),
  ('stmt -> SIZE','stmt',1,'p_size_operation','main.py',526),
  ('stmt -> CONCAT','stmt',1,'p_string_operations','main.py',535),
  ('stmt -> SLICE','stmt',1,'p_string_operations','main.py',536),
  ('stmt -> PAIR','stmt',1,'p_pair_operations','main.py',553),
  ('stmt -> CAR','stmt',1,'p_pair_operations','main.py',554),
  ('stmt -> CDR','stmt',1,'p_pair_operations','main.py',555),
  ('stmt -> EMPTY_SET type','stmt',2,'p_set_operations','main.py',576),
  ('stmt -> MEM','stmt',1,'p_set_operations','main.py',577),
  ('stmt -> UPDATE','stmt',1,'p_set_operations','main.py',578),
  ('stmt -> EMPTY_MAP type type','stmt',3,'p_map_operations','main.py',602),
  ('stmt -> MAP body','stmt',2,'p_map_operations','main.py',603),
  ('stmt -> ITER body','stmt',2,'p_map_operations','main.py',604),
  ('stmt -> GET','stmt',1,'p_map_operations','main.py',605),
  ('stmt -> IF_LEFT body body','stmt',3,'p_if_left_right','main.py',648),
  ('stmt -> IF_RIGHT body body','stmt',3,'p_if_left_right','main.py',649),
  ('stmt -> IF_CONS body body','stmt',3,'p_if_cons','main.py',669),
  ('stmt -> SOME','stmt',1,'p_option_operations','main.py',687),
  ('stmt -> NONE type','stmt',2,'p_option_operations','main.py',688),
  ('stmt -> LEFT type','stmt',2,'p_union_operations','main.py',700),
  ('stmt -> RIGHT type','stmt',2,'p_union_operations','main.py',701),
  ('stmt -> CONS','stmt',1,'p_list_operations','main.py',713),
  ('stmt -> NIL type','stmt',2,'p_list_operations','main.py',714),
  ('stmt -> NOT','stmt',1,'p_boolean_not','main.py',732),
  ('stmt -> EXEC','stmt',1,'p_exec','main.py',744),
  ('stmt -> STEPS_TO_QUOTA','stmt',1,'p_special_operations','main.py',760),
  ('stmt -> NOW','stmt',1,'p_special_operations','main.py',761),
  ('stmt -> CONTRACT type','stmt',2,'p_contract_push','main.py',773),
  ('stmt -> HASH_KEY','stmt',1,'p_cryptographic_primitives','main.py',787),
  ('stmt -> BLAKE2B','stmt',1,'p_cryptographic_primitives','main.py',788),
  ('stmt -> SHA256','stmt',1,'p_cryptographic_primitives','main.py',789),
  ('stmt -> SHA512','stmt',1,'p_cryptographic_primitives','main.py',790),
  ('stmt -> CHECK_SIGNATURE','stmt',1,'p_cryptographic_primitives','main.py',791),
  ('type -> NAT','type',1,'p_statement_type','main.py',816),
  ('type -> STRING','type',1,'p_statement_type','main.py',817),
  ('type -> INT','type',1,'p_statement_type','main.py',818),
  ('type -> BOOL','type',1,'p_statement_type','main.py',819),
  ('type -> BYTES','type',1,'p_statement_type','main.py',820),
  ('type -> OPERATION','type',1,'p_statement_type','main.py',821),
  ('type -> ADDRESS','type',1,'p_statement_type','main.py',822),
  ('type -> TIMESTAMP','type',1,'p_statement_type','main.py',823),
  ('type -> LPARENS LPAIR type type RPARENS','type',5,'p_statement_type','main.py',824),
  ('stmt -> DIP body','stmt',2,'p_dip','main.py',847),
  ('stmt -> PUSH type value','stmt',3,'p_statement_push','main.py',861),
  ('stmt -> ASSERT','stmt',1,'p_assertion_macros','main.py',885),
  ('stmt -> ASSERT_EQ','stmt',1,'p_assertion_macros','main.py',886),
  ('stmt -> ASSERT_NEQ','stmt',1,'p_assertion_macros','main.py',887),
  ('stmt -> ASSERT_LT','stmt',1,'p_assertion_macros','main.py',888),
  ('stmt -> ASSERT_LTE','stmt',1,'p_assertion_macros','main.py',889),
  ('stmt -> ASSERT_GT','stmt',1,'p_assertion_macros','main.py',890),
  ('stmt -> ASSERT_GTE','stmt',1,'p_assertion_macros','main.py',891),
  ('stmt -> FAILWITH','stmt',1,'p_statement_failwith','main.py',934),
  ('stmt -> FAIL','stmt',1,'p_statement_failwith','main.py',935),
  ('stmt -> PRINTER','stmt',1,'p_printer','main.py',950),
]
