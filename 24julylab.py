# Hi! I am new to Python numpy. Can you generate some real world situations where 
# i can use a numpy array with some source code.

# Daily stock prices
prices = np.array([100, 101, 102, 105, 107])

# Calculate daily returns
returns = (prices[1:] - prices[:-1]) / prices[:-1]
print("Daily returns:", returns)


from scipy.ndimage import gaussian_filter

# Example grayscale image as a 2D NumPy array
image = np.array([[0, 50, 100],
                  [150, 200, 250],
                  [50, 100, 150]])

# Apply Gaussian filter
filtered_image = gaussian_filter(image, sigma=1)
print("Filtered image:\n", filtered_image)