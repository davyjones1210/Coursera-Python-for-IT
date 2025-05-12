def secure_website_domain(website):
 pattern = r"^https://www\.([a-zA-Z0-9_-]+)\.(com|co)$" # enter the regex pattern here
 result = re.search(pattern, website) # enter the re method here
 if result is None:
  return ""
 return result[1]# enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text



import re
def parse_city_country(text):
  pattern = r"^([\w\s]+)[,.]\s([\w\s]+)$" #enter the regex pattern here
  result = re.search(pattern, text) #enter the re method  here
  if result is None or len(result.groups()) != 2:
    return ""
  return result[1] #return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank


def find_productID(report):
  pattern = r"\b1\d{3}\-[A-Z]{2}\-\d{2}"#enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result
  
print(find_productID("Products 1234-AB-30 and 2234-AB-30, not items 12-AB-30 or 12345-AB-30")) # Should return ['1234-AB-30']
print(find_productID("Products of interest are 1234-AB-30, 1678-XZ-11, and 1561-CD-57. We're not interested in other products like 2345-AB-29.")) # Should return ['1234-AB-30', '1678-XZ-11', '1561-CD-57']