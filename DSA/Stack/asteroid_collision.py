'''735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row. The indices of the 
asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 4:

Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. 
On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
'''
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        ''' $NOTE$ for - else & while - else
        here the else part will execute only when for / while is not break'ed
        '''

        '''
        Asteroid can meet only when stack top has +ve and array item is -ve

        reverse wont work, why
        
        stack = [-5] and a = 10, -5 is going left and 10 is going right

        when a is smaller than stack top, a is gone
        when both are same, both are gone

        recursive logic is only when a > stack[top] and it will keep on popping stack top
        with same three logics. And finally if it survives then we need to add it to the stack
        
        '''
        stack = []

        for a in asteroids:

            while stack and stack[-1] > 0 and a < 0:

                # when both are same, both gets destroyed. exit
                if stack[-1] == -a:
                    stack.pop()
                    break # no need to add anything

                # when a is smaller than top
                elif stack[-1] > -a: # or abs(a)
                    break

                # when a is bigger than top
                elif stack[-1] < -a:
                    stack.pop()

            else:
                ''' As mentioned all those a's which broke while, will not appended
                if you want a simpler approach see below
                '''
                stack.append(a)

        return stack
    
    def asteroidCollisionSimpler(self, asteroids: list[int]) -> list[int]:

        stack = []

        for a in asteroids:
            
            alive = True
            while stack and stack[-1] > 0 and a < 0:
                
                # when both are same, both gets destroyed. exit
                if stack[-1] == -a:
                    stack.pop()
                    alive = False
                    break # no need to add anything

                # when a is smaller than top
                elif stack[-1] > -a: # or abs(a)
                    alive = False
                    break

                # when a is bigger than top
                elif stack[-1] < -a:
                    stack.pop()

            if alive: 
                stack.append(a)

        return stack