import numpy as np 



class MagicSquare:
	"""
		takes n as length of square
		returns magic square of size n
	"""

	def __init__(self,n):
		self.n = n
		self.square = np.zeros((n,n))
		self.middel = n//2
		self.fill_down()
		self.fill_up()

	def fill_down(self):
		"""fills lower half below antidiagonal"""
		self.fill_center_5(self.middel)
		self.fill_adparallel_up(self.middel, self.middel)
		self.fill_adparallel_down(self.middel, self.middel)
		self.fill_adparallel_down(self.middel+1, self.middel)
		self.fill_adparallel_up(self.middel, self.middel+1)

	def fill_up(self):
		"""Fills upper half above antidiagonal"""
		self.fill_dparallel_up(self.middel, self.middel)
		self.fill_dparallel_up(self.middel, self.middel-1, p_up=False)
		self.fill_dperpendicualr_down(self.middel, self.middel-1)
		self.fill_dparallel_up(self.middel-1, self.middel, p_down=False)
		self.fill_dperpendicular_up(self.middel-1, self.middel)

	def fill_center_5(self,middel):
		"""
		Fills the middel 5 squares
				|
			  -	- -
				|
		"""
		#fills middel 5 squares
		self.square[self.middel][self.middel] = (self.n**2 + 1) // 2
		self.square[self.middel][self.middel+1] = (self.n**2+1-self.n)
		self.square[self.middel][self.middel-1] = self.n 
		self.square[self.middel-1][self.middel] = self.n**2
		self.square[self.middel+1][self.middel] = 1

	def fill_adparallel_down(self, x, y):
		"""
			fills the squares parallel to anti-diagonal in downward
			direction
		"""
		if max(x+1, y+1) > self.n-1:
			return

		self.square[x+1][y-1] = (self.square[x][y] + self.n) % (self.n**2)
		self.fill_adparallel_down(x+1,y-1)
		self.fill_dparallel_down(x, y)

	def fill_adparallel_up(self,x,y):
		"""
			fills the squares parallel to anti-diagonal in upward
			direction
		"""
		if max(x+1, y+1) > self.n-1:
			return

		self.square[x-1][y+1] = (self.square[x][y] -self.n) % (self.n**2)
		self.fill_adparallel_up(x-1, y+1)
		self.fill_dparallel_down(x, y)


	def fill_dparallel_down(self, x, y):
		"""
			fills parallel to main diagonal in downward direction
		"""
		if max(x+1, y+1) > self.n-1:
			return

		self.square[x+1][y+1] = (self.square[x][y] + 1) % (self.n**2)
		self.fill_dparallel_down(x+1, y+1)

	def fill_dparallel_up(self, x, y, p_down=True, p_up=True):
		"""
			fills mail diagonal parallel squares
		"""
		if min(x-1, y-1) <= -1:
			return

		self.square[x-1][y-1] = (self.square[x][y] - 1) % (self.n**2)
		self.fill_dparallel_up(x-1, y-1)
		if p_down:
			self.fill_dperpendicualr_down(x-1,y-1)
		if p_up:
			self.fill_dperpendicular_up(x-1, y-1)

	def fill_dperpendicualr_down(self, x, y, down_up=True):
		"""
			fills the below squares perpendicular to the main diagonal
		"""
		if min(x-1, y-1) <= -1:
			return

		self.square[x+1][y-1] = (self.square[x][y]+self.n) % (self.n**2)

		self.fill_dperpendicualr_down(x+1, y-1)

	def fill_dperpendicular_up(self, x, y):
		"""
			fills the upper squares perpendicular to the main diagonal
		"""
		if min(x-1, y-1) <= -1:
			return

		self.square[x-1][y+1] = (self.square[x][y]-self.n) % (self.n**2)

		self.fill_dperpendicular_up(x-1, y+1)

	def __repr__(self):
		return str(self.square)


square = MagicSquare(int(input()))
print(square)