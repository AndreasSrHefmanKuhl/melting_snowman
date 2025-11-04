

# ascii_art.py

# Stages of the Snowman Meltdown (6 stages total: 0 to 5)
STAGES = [
     # Stage 0 (0 mistakes): Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1 (1 mistake): Loss of a button
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     (   ) 
     """,
     # Stage 2 (2 mistakes): Loss of another button
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 3 (3 mistakes): Bottom part starts melting
     """
      ___  
     /___\\ 
     (o .) 
     ( : ) 
     """,
     # Stage 4 (4 mistakes): Only the head remains and is melting
     """
      ___  
     /___\\ 
     ( . ) 
     """,
     # Stage 5 (5 mistakes): Snowman completely melted (Loss condition)
     """
      ___  
     /___\\ 
     """
 ]