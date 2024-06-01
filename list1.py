# ask user to guess a number,
a=[1,2,3]
b=[4,5,6]
c=a+b
#c(2) would give you item 3 bc
print(c)
print(a)
# slicing lists: t=[9,12,14,15] t[1:3] outputs 12 and 14
nums=[3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

nums.append('book')
nums.append(12)
print(nums)
print(nums[6])
print(nums[-1])
#last number in a list is -1 using neg. indexing

print(41 in nums)
print(72 in nums)
x= 12 in nums
print(x)
y= 5 in nums
print(y)
#gives true or false in this case true
#ask user to guess a number and ask user to guess a word
ans1=int(input('Please guess a whole number'))
ans2=str(input('Please guess a word'))



"""would also work w just x=ans1 in nums and y=ans2 in nums. would print true or false"""
if ans1 and ans2 in nums:
    print('correct')
else:
    print('incorrect')


x=list()
for i in range(0,11):
    x.append(i)
    print(x)

#x.reverse()
#for i in range (0,len(x)):
#print(x[i])
# this code will reverse the iteration going from end of list to front this format helps bc
# don't need to know number of items in list
