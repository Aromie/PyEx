projects = {}
flag=True
while (flag):
    temp=input("What's the Project Name? (Type 'exit' to quit) ")
    if temp=="exit":
        flag=False
        break
    else:        
        try:
            num= int(input("How many lines did you code? "))
            if temp in projects:
                projects[temp]=projects[temp]+num
            else:
                projects[temp]=num    
                        
        except ValueError:
            print("You typed wrong! Enter a number.")
            
for key, value in projects.items():
    print(f"Project: {key}: {value} lines")
print(f"Grand Total: {sum(projects.values())} lines")
