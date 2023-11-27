from kanren import facts,Relation

connectsTo = Relation()
facts(connectsTo,
       ('Pune',('Mumbai',10)),
       ('Mumbai',('Pune',10)),
       ('Pune',('Pimpri',510)),
       ('Pimpri',('Nashik',60)),
       ('Mumbai',('Nashik',30)),
       ('Nashik',('Delhi',30)),
      ('Nashik',('Delhi',30)),
      ('Nashik',('Pune',30))
   ('Aurangabad',('Kashmir',30)),
       )

def go(x,y):
    pass

def distance(x,y):
    pass

def road(x,y):
    pass



go('Pune','Nashik')
# Output: ["Pune -> Mumbai -> Nashik","Pune -> Pimpri -> Nashik"] 

distance('Pune','Delhi')
# Output: [70,10] 

road('Pune','Kashmir')
# False 