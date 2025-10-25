print(" --ANIME TITLES COLLECTOR!-- ")
print("Type 'done' to finish collecting. \n")
r = []

uling = ""
while uling != "done":
    
    uling = input("Enter an anime name: ")
    
    if uling != "done":
        r.append(uling)
        print(f"'{uling}' has been added to your anime list.")

print("\n--- DONE COLLECTING ---")

print("Your Favorite Anime List:")
for title in r:
    print(f"- {title}")