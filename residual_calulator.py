#data points on graph (these where just the ones on my math homework
xs = [0.5, 2.5, 1, 2, 0.5, 1, 2, 1, 1.5, 2.5]
ys = [4.5, 1.6, 3, 1.8, 5, 4.2, 2.4, 3.6, 3.3, 1.4]

#equation of line of best fit
slope = -1.5
yint = 5.5

#for loop that loops through and prints residual and predicted values
i = 0
for nums in xs:
		nums = (nums * slope) + yint
		print("Predicted: ",nums)

		r = nums - ys[i]
		print("Residual :", r, "\n")

