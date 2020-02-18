#Copyright (c) 2020 HenryFleming
#see LICENSE for more

def parse_line(cmds,line):
  parts = []
  last_part = ""
  skiping = False
  for char in line:
    if char==" "and not skiping:
      parts.append(last_part)
      last_part=""
    if not char==" " or skiping:
      if not char=='"':
        last_part+=char
    if char=='"':
      skiping=not skiping
  parts.append(last_part)
  last_part=""
  try:
    cmd = parts[0]
    args = parts[1:len(parts)]
    argsStr = ""
    for e in args:
      argsStr+='"'+e+'",'
    exec('cmds.'+cmd+'(['+argsStr[0:len(argsStr)-1]+'])')
  except:
    pass
