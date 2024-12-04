class_members = {"Alice", "Bob", "Charlie", "David", "Eve"}
singers = {member for member in class_members if member in {"Alice", "Bob", "David"}}
dancers = {member for member in class_members if member in {"Bob", "Charlie", "Eve"}}
print(f"Singers: {singers}")
print(f"Dancers: {dancers}")
all_artists = singers.union(dancers)
print(f"All artists: {all_artists}")
allrounders = singers.intersection(dancers)
print(f"All-rounders: {allrounders}")
dancers_but_not_singers = dancers.difference(singers)
print(f"Dancers but not singers: {dancers_but_not_singers}")
singers_but_not_dancers = singers.difference(dancers)
print(f"Singers but not dancers: {singers_but_not_dancers}")
dancers_or_singers_only = dancers.symmetric_difference(singers)
print(f"Dancers but not singers cum Singers but not dancers: {dancers_or_singers_only}")