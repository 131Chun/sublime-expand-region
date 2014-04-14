try:
  import utils
except:
  from . import utils

def _expand_to_regex_rule(string, startIndex, endIndex, negativeRe, positiveRe, type):
  if(startIndex != endIndex):
    selection = string[startIndex:endIndex]
    if positiveRe.match(selection) is None:
      return None

  # look back
  searchIndex = startIndex - 1;
  while True:
    # begin of string is reached
    if searchIndex < 0:
      newStartIndex = searchIndex + 1
      break
    char = string[searchIndex:searchIndex+1]
    # character found, that does not fit into the search set 
    if negativeRe.match(char) is None:
      newStartIndex = searchIndex + 1
      break
    else:
      searchIndex -= 1

  # look forward
  searchIndex = endIndex;
  while True:
    # end of string reached
    if searchIndex > len(string) - 1:
      newEndIndex = searchIndex
      break
    char = string[searchIndex:searchIndex+1]
    # character found, that does not fit into the search set 
    if negativeRe.match(char) is None:
      newEndIndex = searchIndex
      break
    else:
      searchIndex += 1

  try:
    if startIndex == newStartIndex and endIndex == newEndIndex:
      return None
    else:
      return utils.create_return_obj(newStartIndex, newEndIndex, string, type)
  except NameError:
    # newStartIndex or newEndIndex might not have been defined above, because
    # the character was not found.
    return None