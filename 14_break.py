
count = 1

while True:
  
  count += 1
  if count == 20:
    print("좀 쉬어야겠다")
    continue
  
  print(f"{count}바퀴째")
  if count > 20:
    break

print("달리기를 마쳤습니다.")