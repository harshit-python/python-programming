"""
Python program to implement basic class
"""

class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie1 = Cookie("red")
cookie2 = Cookie("blue")
print("Cookie 1 is", cookie1.get_color())
print("Cookie 2 is", cookie2.get_color())

cookie1.set_color("green")
print("\nCookie 1 is now", cookie1.get_color())
print("Cookie 2 is still", cookie2.get_color())