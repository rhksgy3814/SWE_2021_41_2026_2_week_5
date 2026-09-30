def isHappy(n):
  total = 0
  while n > 0:
    tmp = n % 10
    total += tmp * tmp
    n = n // 10

  if total == 1:
    return True
  elif total == 4:
    return False
  else:
    return isHappy(total)

if __name__ == "__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)

  with open("/app/bind_mount/output.txt", "w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")
    
  print("Results saved to /app/bind_mount/output.txt")