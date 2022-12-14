logregel = "85.12.51.25 Chrome homepage"
elementen = logregel.split(" ")

ip = elementen[0]
ua = elementen[1]
page = elementen[2]

print(f"ip: {ip}")
print(f"ua: {ua}")
print(f"page: {page}")

# Pro 1
ip_splitted = ip.split(".")
print(ip_splitted[0])
print(ip_splitted[1])
print(ip_splitted[2])
print(ip_splitted[3])

# Pro 2
for item in ip_splitted:
    print(item)

# Pro 3 'homepage'
for letter in page:
    print(letter)
