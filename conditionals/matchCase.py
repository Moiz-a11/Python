
color =input("enter color :")

match color:
    case"red":
         print("stop")
    case"green":
         print("go")
    case "yellow":
        print("look")
    case _: # default case
          print("wrong color ")