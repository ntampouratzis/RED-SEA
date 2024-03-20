
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASTERISK BITFIELD CODELIT COLON COMMA CPPDIRECTIVE DBLCOLON DECODE DECODER DEF DEFAULT DOT EQUALS EXEC FORMAT GREATER HEADER ID INTLIT LBRACE LBRACKET LESS LET LPAREN NAMESPACE OPERANDS OPERAND_TYPES OUTPUT RBRACE RBRACKET RPAREN SEMI SIGNED SPLIT STRLIT TEMPLATEspecification : opt_defs_and_outputs top_level_decode_blockopt_defs_and_outputs : emptyopt_defs_and_outputs : defs_and_outputsdefs_and_outputs : def_or_outputdefs_and_outputs : defs_and_outputs def_or_outputdef_or_output : name_decl\n        | def_format\n        | def_bitfield\n        | def_bitfield_struct\n        | def_template\n        | def_operand_types\n        | def_operands\n        | output\n        | global_let\n        | splitsplit : SPLIT output_type SEMIoutput_type : DECODER\n        | HEADER\n        | EXECname_decl : NAMESPACE ID SEMIoutput : OUTPUT output_type CODELIT SEMIglobal_let : LET CODELIT SEMIdef_operand_types : DEF OPERAND_TYPES CODELIT SEMIdef_operands : DEF OPERANDS CODELIT SEMIdef_bitfield : DEF opt_signed BITFIELD ID LESS INTLIT COLON INTLIT GREATER SEMIdef_bitfield : DEF opt_signed BITFIELD ID LESS INTLIT GREATER SEMIdef_bitfield_struct : DEF opt_signed BITFIELD ID id_with_dot SEMIid_with_dot : IDid_with_dot : ID DOT id_with_dotopt_signed : SIGNEDopt_signed : emptydef_template : DEF TEMPLATE ID CODELIT SEMIdef_format : DEF FORMAT ID LPAREN param_list RPAREN CODELIT SEMIparam_list : positional_param_list COMMA nonpositional_param_listparam_list : positional_param_list\n        | nonpositional_param_listpositional_param_list : emptypositional_param_list : IDpositional_param_list : positional_param_list COMMA IDnonpositional_param_list : keyword_param_list COMMA excess_args_paramnonpositional_param_list : keyword_param_list\n        | excess_args_paramkeyword_param_list : keyword_paramkeyword_param_list : keyword_param_list COMMA keyword_paramkeyword_param : ID EQUALS exprexcess_args_param : ASTERISK IDtop_level_decode_block : decode_blockdecode_block : DECODE ID opt_default LBRACE decode_stmt_list RBRACEopt_default : emptyopt_default : DEFAULT instdecode_stmt_list : decode_stmtdecode_stmt_list : decode_stmt decode_stmt_listdecode_stmt : CPPDIRECTIVEdecode_stmt : FORMAT push_format_id LBRACE decode_stmt_list RBRACEpush_format_id : IDdecode_stmt : case_list COLON decode_blockdecode_stmt : case_list COLON inst SEMIcase_list : DEFAULTcase_list : INTLITcase_list : STRLITcase_list : case_list COMMA INTLITcase_list : case_list COMMA STRLITinst : ID LPAREN arg_list RPARENinst : ID DBLCOLON ID LPAREN arg_list RPARENarg_list : positional_arg_list COMMA keyword_arg_listarg_list : positional_arg_listarg_list : keyword_arg_listpositional_arg_list : emptypositional_arg_list : exprpositional_arg_list : positional_arg_list COMMA exprkeyword_arg_list : keyword_argkeyword_arg_list : keyword_arg_list COMMA keyword_argkeyword_arg : ID EQUALS exprexpr : ID\n        | INTLIT\n        | STRLIT\n        | CODELITexpr : LBRACKET list_expr RBRACKETlist_expr : exprlist_expr : list_expr COMMA exprlist_expr : emptyempty :'
    
_lr_action_items = {'DECODE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,24,40,47,48,55,56,57,73,91,96,134,136,151,],[-82,23,-2,-3,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-5,-20,-22,-16,-23,-24,-21,-32,-27,23,-33,-26,-25,]),'NAMESPACE':([0,4,5,6,7,8,9,10,11,12,13,14,15,24,40,47,48,55,56,57,73,91,134,136,151,],[16,16,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-5,-20,-22,-16,-23,-24,-21,-32,-27,-33,-26,-25,]),'DEF':([0,4,5,6,7,8,9,10,11,12,13,14,15,24,40,47,48,55,56,57,73,91,134,136,151,],[17,17,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-5,-20,-22,-16,-23,-24,-21,-32,-27,-33,-26,-25,]),'OUTPUT':([0,4,5,6,7,8,9,10,11,12,13,14,15,24,40,47,48,55,56,57,73,91,134,136,151,],[18,18,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-5,-20,-22,-16,-23,-24,-21,-32,-27,-33,-26,-25,]),'LET':([0,4,5,6,7,8,9,10,11,12,13,14,15,24,40,47,48,55,56,57,73,91,134,136,151,],[19,19,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-5,-20,-22,-16,-23,-24,-21,-32,-27,-33,-26,-25,]),'SPLIT':([0,4,5,6,7,8,9,10,11,12,13,14,15,24,40,47,48,55,56,57,73,91,134,136,151,],[20,20,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-5,-20,-22,-16,-23,-24,-21,-32,-27,-33,-26,-25,]),'$end':([1,21,22,92,],[0,-1,-47,-48,]),'ID':([16,23,26,28,42,51,52,53,69,77,82,83,84,86,87,89,96,108,126,128,129,133,145,],[25,39,41,43,53,60,61,70,88,95,98,109,110,114,117,70,60,110,110,98,143,98,110,]),'FORMAT':([17,58,75,76,92,121,122,138,148,],[26,77,77,-53,-48,77,-56,-57,-54,]),'TEMPLATE':([17,],[28,]),'OPERAND_TYPES':([17,],[29,]),'OPERANDS':([17,],[30,]),'SIGNED':([17,],[31,]),'BITFIELD':([17,27,31,32,],[-82,42,-30,-31,]),'DECODER':([18,20,],[34,34,]),'HEADER':([18,20,],[35,35,]),'EXEC':([18,20,],[36,36,]),'CODELIT':([19,29,30,33,34,35,36,43,82,84,85,108,126,128,133,145,],[37,44,45,46,-17,-18,-19,54,107,107,112,107,107,107,107,107,]),'SEMI':([25,34,35,36,37,38,44,45,46,54,70,72,112,118,120,123,127,147,150,],[40,-17,-18,-19,47,48,55,56,57,73,-28,91,134,-29,136,138,-63,151,-64,]),'DEFAULT':([39,58,75,76,92,121,122,138,148,],[51,79,79,-53,-48,79,-56,-57,-54,]),'LBRACE':([39,49,50,59,94,95,127,150,],[-82,58,-49,-50,121,-55,-63,-64,]),'LPAREN':([41,60,109,],[52,82,133,]),'COMMA':([52,61,63,65,66,68,78,79,80,81,82,98,100,101,102,103,104,105,106,107,108,110,111,114,116,124,125,130,131,132,133,139,140,141,142,144,149,],[-82,-38,86,-37,87,-43,97,-58,-59,-60,-82,-74,128,129,-68,-69,-71,-75,-76,-77,-82,-74,-45,-39,-44,-61,-62,145,-79,-81,-82,-73,129,-70,-72,-78,-80,]),'RPAREN':([52,61,62,63,64,65,66,67,68,82,88,98,99,100,101,102,103,104,105,106,107,110,111,113,114,115,116,133,139,140,141,142,144,146,],[-82,-38,85,-35,-36,-37,-41,-42,-43,-82,-46,-74,127,-66,-67,-68,-69,-71,-75,-76,-77,-74,-45,-34,-39,-40,-44,-82,-73,-65,-70,-72,-78,150,]),'ASTERISK':([52,86,87,],[69,69,69,]),'LESS':([53,],[71,]),'CPPDIRECTIVE':([58,75,76,92,121,122,138,148,],[76,76,-53,-48,76,-56,-57,-54,]),'INTLIT':([58,71,75,76,82,84,92,97,108,119,121,122,126,128,133,138,145,148,],[80,90,80,-53,105,105,-48,124,105,135,80,-56,105,105,105,-57,105,-54,]),'STRLIT':([58,75,76,82,84,92,97,108,121,122,126,128,133,138,145,148,],[81,81,-53,106,106,-48,125,106,81,-56,106,106,106,-57,106,-54,]),'DBLCOLON':([60,],[83,]),'EQUALS':([61,98,114,117,143,],[84,126,84,84,126,]),'DOT':([70,],[89,]),'RBRACE':([74,75,76,92,93,122,137,138,148,],[92,-51,-53,-48,-52,-56,148,-57,-54,]),'COLON':([78,79,80,81,90,124,125,],[96,-58,-59,-60,119,-61,-62,]),'LBRACKET':([82,84,108,126,128,133,145,],[108,108,108,108,108,108,108,]),'GREATER':([90,135,],[120,147,]),'RBRACKET':([105,106,107,108,110,130,131,132,144,149,],[-75,-76,-77,-82,-74,144,-79,-81,-78,-80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'specification':([0,],[1,]),'opt_defs_and_outputs':([0,],[2,]),'empty':([0,17,39,52,82,108,133,],[3,32,50,65,102,132,102,]),'defs_and_outputs':([0,],[4,]),'def_or_output':([0,4,],[5,24,]),'name_decl':([0,4,],[6,6,]),'def_format':([0,4,],[7,7,]),'def_bitfield':([0,4,],[8,8,]),'def_bitfield_struct':([0,4,],[9,9,]),'def_template':([0,4,],[10,10,]),'def_operand_types':([0,4,],[11,11,]),'def_operands':([0,4,],[12,12,]),'output':([0,4,],[13,13,]),'global_let':([0,4,],[14,14,]),'split':([0,4,],[15,15,]),'top_level_decode_block':([2,],[21,]),'decode_block':([2,96,],[22,122,]),'opt_signed':([17,],[27,]),'output_type':([18,20,],[33,38,]),'opt_default':([39,],[49,]),'inst':([51,96,],[59,123,]),'param_list':([52,],[62,]),'positional_param_list':([52,],[63,]),'nonpositional_param_list':([52,86,],[64,113,]),'keyword_param_list':([52,86,],[66,66,]),'excess_args_param':([52,86,87,],[67,67,115,]),'keyword_param':([52,86,87,],[68,68,116,]),'id_with_dot':([53,89,],[72,118,]),'decode_stmt_list':([58,75,121,],[74,93,137,]),'decode_stmt':([58,75,121,],[75,75,75,]),'case_list':([58,75,121,],[78,78,78,]),'push_format_id':([77,],[94,]),'arg_list':([82,133,],[99,146,]),'positional_arg_list':([82,133,],[100,100,]),'keyword_arg_list':([82,128,133,],[101,140,101,]),'expr':([82,84,108,126,128,133,145,],[103,111,131,139,141,103,149,]),'keyword_arg':([82,128,129,133,],[104,104,142,104,]),'list_expr':([108,],[130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> specification","S'",1,None,None,None),
  ('specification -> opt_defs_and_outputs top_level_decode_block','specification',2,'p_specification','isa_parser.py',929),
  ('opt_defs_and_outputs -> empty','opt_defs_and_outputs',1,'p_opt_defs_and_outputs_0','isa_parser.py',947),
  ('opt_defs_and_outputs -> defs_and_outputs','opt_defs_and_outputs',1,'p_opt_defs_and_outputs_1','isa_parser.py',950),
  ('defs_and_outputs -> def_or_output','defs_and_outputs',1,'p_defs_and_outputs_0','isa_parser.py',953),
  ('defs_and_outputs -> defs_and_outputs def_or_output','defs_and_outputs',2,'p_defs_and_outputs_1','isa_parser.py',956),
  ('def_or_output -> name_decl','def_or_output',1,'p_def_or_output','isa_parser.py',961),
  ('def_or_output -> def_format','def_or_output',1,'p_def_or_output','isa_parser.py',962),
  ('def_or_output -> def_bitfield','def_or_output',1,'p_def_or_output','isa_parser.py',963),
  ('def_or_output -> def_bitfield_struct','def_or_output',1,'p_def_or_output','isa_parser.py',964),
  ('def_or_output -> def_template','def_or_output',1,'p_def_or_output','isa_parser.py',965),
  ('def_or_output -> def_operand_types','def_or_output',1,'p_def_or_output','isa_parser.py',966),
  ('def_or_output -> def_operands','def_or_output',1,'p_def_or_output','isa_parser.py',967),
  ('def_or_output -> output','def_or_output',1,'p_def_or_output','isa_parser.py',968),
  ('def_or_output -> global_let','def_or_output',1,'p_def_or_output','isa_parser.py',969),
  ('def_or_output -> split','def_or_output',1,'p_def_or_output','isa_parser.py',970),
  ('split -> SPLIT output_type SEMI','split',3,'p_split','isa_parser.py',987),
  ('output_type -> DECODER','output_type',1,'p_output_type','isa_parser.py',993),
  ('output_type -> HEADER','output_type',1,'p_output_type','isa_parser.py',994),
  ('output_type -> EXEC','output_type',1,'p_output_type','isa_parser.py',995),
  ('name_decl -> NAMESPACE ID SEMI','name_decl',3,'p_name_decl','isa_parser.py',1000),
  ('output -> OUTPUT output_type CODELIT SEMI','output',4,'p_output','isa_parser.py',1017),
  ('global_let -> LET CODELIT SEMI','global_let',3,'p_global_let','isa_parser.py',1032),
  ('def_operand_types -> DEF OPERAND_TYPES CODELIT SEMI','def_operand_types',4,'p_def_operand_types','isa_parser.py',1072),
  ('def_operands -> DEF OPERANDS CODELIT SEMI','def_operands',4,'p_def_operands','isa_parser.py',1083),
  ('def_bitfield -> DEF opt_signed BITFIELD ID LESS INTLIT COLON INTLIT GREATER SEMI','def_bitfield',10,'p_def_bitfield_0','isa_parser.py',1101),
  ('def_bitfield -> DEF opt_signed BITFIELD ID LESS INTLIT GREATER SEMI','def_bitfield',8,'p_def_bitfield_1','isa_parser.py',1110),
  ('def_bitfield_struct -> DEF opt_signed BITFIELD ID id_with_dot SEMI','def_bitfield_struct',6,'p_def_bitfield_struct','isa_parser.py',1119),
  ('id_with_dot -> ID','id_with_dot',1,'p_id_with_dot_0','isa_parser.py',1129),
  ('id_with_dot -> ID DOT id_with_dot','id_with_dot',3,'p_id_with_dot_1','isa_parser.py',1133),
  ('opt_signed -> SIGNED','opt_signed',1,'p_opt_signed_0','isa_parser.py',1137),
  ('opt_signed -> empty','opt_signed',1,'p_opt_signed_1','isa_parser.py',1141),
  ('def_template -> DEF TEMPLATE ID CODELIT SEMI','def_template',5,'p_def_template','isa_parser.py',1145),
  ('def_format -> DEF FORMAT ID LPAREN param_list RPAREN CODELIT SEMI','def_format',8,'p_def_format','isa_parser.py',1153),
  ('param_list -> positional_param_list COMMA nonpositional_param_list','param_list',3,'p_param_list_0','isa_parser.py',1172),
  ('param_list -> positional_param_list','param_list',1,'p_param_list_1','isa_parser.py',1176),
  ('param_list -> nonpositional_param_list','param_list',1,'p_param_list_1','isa_parser.py',1177),
  ('positional_param_list -> empty','positional_param_list',1,'p_positional_param_list_0','isa_parser.py',1181),
  ('positional_param_list -> ID','positional_param_list',1,'p_positional_param_list_1','isa_parser.py',1185),
  ('positional_param_list -> positional_param_list COMMA ID','positional_param_list',3,'p_positional_param_list_2','isa_parser.py',1189),
  ('nonpositional_param_list -> keyword_param_list COMMA excess_args_param','nonpositional_param_list',3,'p_nonpositional_param_list_0','isa_parser.py',1193),
  ('nonpositional_param_list -> keyword_param_list','nonpositional_param_list',1,'p_nonpositional_param_list_1','isa_parser.py',1197),
  ('nonpositional_param_list -> excess_args_param','nonpositional_param_list',1,'p_nonpositional_param_list_1','isa_parser.py',1198),
  ('keyword_param_list -> keyword_param','keyword_param_list',1,'p_keyword_param_list_0','isa_parser.py',1202),
  ('keyword_param_list -> keyword_param_list COMMA keyword_param','keyword_param_list',3,'p_keyword_param_list_1','isa_parser.py',1206),
  ('keyword_param -> ID EQUALS expr','keyword_param',3,'p_keyword_param','isa_parser.py',1210),
  ('excess_args_param -> ASTERISK ID','excess_args_param',2,'p_excess_args_param','isa_parser.py',1214),
  ('top_level_decode_block -> decode_block','top_level_decode_block',1,'p_top_level_decode_block','isa_parser.py',1227),
  ('decode_block -> DECODE ID opt_default LBRACE decode_stmt_list RBRACE','decode_block',6,'p_decode_block','isa_parser.py',1244),
  ('opt_default -> empty','opt_default',1,'p_opt_default_0','isa_parser.py',1259),
  ('opt_default -> DEFAULT inst','opt_default',2,'p_opt_default_1','isa_parser.py',1267),
  ('decode_stmt_list -> decode_stmt','decode_stmt_list',1,'p_decode_stmt_list_0','isa_parser.py',1276),
  ('decode_stmt_list -> decode_stmt decode_stmt_list','decode_stmt_list',2,'p_decode_stmt_list_1','isa_parser.py',1280),
  ('decode_stmt -> CPPDIRECTIVE','decode_stmt',1,'p_decode_stmt_cpp','isa_parser.py',1302),
  ('decode_stmt -> FORMAT push_format_id LBRACE decode_stmt_list RBRACE','decode_stmt',5,'p_decode_stmt_format','isa_parser.py',1311),
  ('push_format_id -> ID','push_format_id',1,'p_push_format_id','isa_parser.py',1323),
  ('decode_stmt -> case_list COLON decode_block','decode_stmt',3,'p_decode_stmt_decode','isa_parser.py',1333),
  ('decode_stmt -> case_list COLON inst SEMI','decode_stmt',4,'p_decode_stmt_inst','isa_parser.py',1346),
  ('case_list -> DEFAULT','case_list',1,'p_case_list_0','isa_parser.py',1358),
  ('case_list -> INTLIT','case_list',1,'p_case_list_1','isa_parser.py',1371),
  ('case_list -> STRLIT','case_list',1,'p_case_list_2','isa_parser.py',1375),
  ('case_list -> case_list COMMA INTLIT','case_list',3,'p_case_list_3','isa_parser.py',1379),
  ('case_list -> case_list COMMA STRLIT','case_list',3,'p_case_list_4','isa_parser.py',1384),
  ('inst -> ID LPAREN arg_list RPAREN','inst',4,'p_inst_0','isa_parser.py',1392),
  ('inst -> ID DBLCOLON ID LPAREN arg_list RPAREN','inst',6,'p_inst_1','isa_parser.py',1406),
  ('arg_list -> positional_arg_list COMMA keyword_arg_list','arg_list',3,'p_arg_list_0','isa_parser.py',1421),
  ('arg_list -> positional_arg_list','arg_list',1,'p_arg_list_1','isa_parser.py',1425),
  ('arg_list -> keyword_arg_list','arg_list',1,'p_arg_list_2','isa_parser.py',1429),
  ('positional_arg_list -> empty','positional_arg_list',1,'p_positional_arg_list_0','isa_parser.py',1433),
  ('positional_arg_list -> expr','positional_arg_list',1,'p_positional_arg_list_1','isa_parser.py',1437),
  ('positional_arg_list -> positional_arg_list COMMA expr','positional_arg_list',3,'p_positional_arg_list_2','isa_parser.py',1441),
  ('keyword_arg_list -> keyword_arg','keyword_arg_list',1,'p_keyword_arg_list_0','isa_parser.py',1445),
  ('keyword_arg_list -> keyword_arg_list COMMA keyword_arg','keyword_arg_list',3,'p_keyword_arg_list_1','isa_parser.py',1449),
  ('keyword_arg -> ID EQUALS expr','keyword_arg',3,'p_keyword_arg','isa_parser.py',1454),
  ('expr -> ID','expr',1,'p_expr_0','isa_parser.py',1469),
  ('expr -> INTLIT','expr',1,'p_expr_0','isa_parser.py',1470),
  ('expr -> STRLIT','expr',1,'p_expr_0','isa_parser.py',1471),
  ('expr -> CODELIT','expr',1,'p_expr_0','isa_parser.py',1472),
  ('expr -> LBRACKET list_expr RBRACKET','expr',3,'p_expr_1','isa_parser.py',1476),
  ('list_expr -> expr','list_expr',1,'p_list_expr_0','isa_parser.py',1480),
  ('list_expr -> list_expr COMMA expr','list_expr',3,'p_list_expr_1','isa_parser.py',1484),
  ('list_expr -> empty','list_expr',1,'p_list_expr_2','isa_parser.py',1488),
  ('empty -> <empty>','empty',0,'p_empty','isa_parser.py',1495),
]