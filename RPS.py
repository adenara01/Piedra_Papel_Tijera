# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    
    # Si es el primer juego, elige un movimiento aleatorio
    if len(opponent_history) == 1:
        return random.choice(["R", "P", "S"])
    
    # Trata de predecir la siguiente jugada del oponente basado en su jugada anterior
    last_play = opponent_history[-1]
    if last_play == "R":
        return "P"  # Papel vence a Piedra
    elif last_play == "P":
        return "S"  # Tijera vence a Papel
    else:
        return "R"  # Piedra vence a Tijera