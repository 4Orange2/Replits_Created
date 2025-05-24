color = str(input("What color is the traffic light? "))

if color == "green":
  print("go")
elif color == "yellow":
  distance = int(input("What is your distance from the light? "))
  if distance < 20:
    print("go")
  else:
    print("Stop. Wait for a green, then go.")
elif color == "red":
  print("Stop. Wait for a green, then go.")
else:
  print("pull over, make an appointment with an optometrist and get your vision checked.")