has_horn = int(input("Enter has_horn (1 or 0): "))
can_fly = int(input("Enter can_fly (1 or 0): "))

if has_horn == 1 and can_fly == 0:
    print("unicorn")
elif has_horn == 0 and can_fly == 1:
    print("pegasus")
elif has_horn == 1 and can_fly == 1:
    print("alicorn")
else:
    print("horse")
