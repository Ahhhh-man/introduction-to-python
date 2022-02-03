from postcode.postcode_task import PostcodeApi

# postcode = PostcodeApi('se120nb')
postcode = PostcodeApi(''.join(input("What's your postcode? ").split()))
print(postcode.message())