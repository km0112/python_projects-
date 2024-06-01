#You are to do 6 programs with the following guidelines:
#* At least one from the first two tiers.
#* If you do one from the third tier it is worth 2 programs.

blocks=[3,0,0,2,0,4]

if(blocks[0])>(blocks[len(blocks)-1]):
    height=(blocks[len(blocks)-1])

elif(blocks[len(blocks)-1])>(blocks[0]):
    height=(blocks[0])

#this gives the max height of the water that can be trapped
for block in blocks:
    answer=(height-block)
    """blocks2=[]
    blocks2.append(answer)"""
    if answer<0:
        break
    print(answer)
