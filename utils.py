## safe input func
def safe_input(prompt: str = "") str -> :
  try :
    usr_input = input(prompt + "\n>>>")
  except Exception as e:
    print("Error :", e)
    return none
  return usr_input
  
