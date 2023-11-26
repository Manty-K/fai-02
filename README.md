# FAI Assignment 2

https://github.com/logpy/logpy

**Note: This is group assignment. Create the groups among all you. Group must contain
maximum 2 students in it.**

Develop a system for reasoning for the following problem:
Consider a window-based computer interface. your representation should be able to
describe:

- The state of a window: minimized, displayed, or non-existent.
- Which window (if any) is the active window.
- The position of every window at a given time.
- The order (front to back) of overlapping windows.
- The actions of creating, destroying, resizing, and moving windows and
  changing the state of a window and bringing a window to the front.

Treat these actions as atomic; that is, do not deal with the issue of relating them to mouse actions. Give axioms describing the effects of actions on fluent. You may use event.

Assume the x and y coordinates of the windows.

Define a language over a list of constants, function symbols, and predicates with an English description of each. If you need to add more categories (e.g., pixels). Implement all the reason and facts in python.

---

Planning a route for a robot to take from one city to another. The basic action taken by
the robot is Go(x,y), which takes it from city x to city y if there is a route between those
cities. Road(x,y) is true if and only if there is a road connecting cities x and y; if there
is, then Distance(x,y) gives the length of the road. The robot begins in Pune and must
reach to Pimpri.
• Write a suitable logical description of the initial situation of the robot.
• Write a suitable logical query whose solutions provide possible paths to the
goal.
• Write a sentence describing the Go action.

---

Implement the above in python.

1. Provide knowledge representation for tic-tac-toe game. Define all necessary conditions
   you need while representing the knowledge.
