def autocomplete(input_, dictionary):
  matches = []
  lenm = len(input_)
  for i in dictionary:
    if i[0:lenm] == input_:
      matches.append(i)
  if len(matches)>5:
    return matches[0:5]
  else:
    return matches

