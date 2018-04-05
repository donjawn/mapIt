import webbrowser

print
print("This script will Google Maps the address you enter below.")
print("---------------------------------")
print("created by github user @donjawn")
print("---------------------------------")
print("""Instructions:
1. On the first command, enter the first address line ONLY, unless there \nis an APT/SUITE (ie. 123 Wall Street)
2. On the second command, enter the zip code (ie. 90210)""")
print("---------------------------------")
print

      
address1 = input("Enter the address you want to Google Maps: ")
address2 = input("Enter the zip code: ")
fullAddress = address1 + " " + address2


# https://www.google.com/maps/place/<ADDRESS>    
webbrowser.open("https://www.google.com/maps/dir//" + fullAddress)
