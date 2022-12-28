content=True
i=1

with open('log.txt') as f:
    while content:
     content = f.readline()
     if 'python' in content.lower():
        # print(content)
        print(f"available in line number {i}")
    #  else:
    #     print("Not Available")
     i+=1
        