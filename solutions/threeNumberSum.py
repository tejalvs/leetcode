def threeNumberSum(array, targetSum):
	final_list=[]
	print("hi")
    for i in range(0,len(array)):
		rem=targetSum-array[i]
		print(rem)
		for j in range (i+1,len(array)-1):
			rem=rem-array[i]
			print(rem)
			if rem in array:
				result=[]
				result.append(rem)
				result.append(array[i])
				result.append(array[j])
				final_list.append(result)

			
    return final_list



threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],12)