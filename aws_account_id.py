'''This program will display the account id from the arn. Example arn:
arn:aws:iam::123456789012:user/Development/product_123/*
Displays on the screen "The AWS account id is: account_id'''

arn = input ("Enter aws arn: ")
start_index=arn.find("iam::") #8
end_index=arn.find(":user")
account_id=arn[start_index+5:end_index]
print(f"The AWS account ID is: {account_id}")
# print(f"The AWS account ID is: {arn[13:25]}")