import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
WINDOW_SIZE = (600, 600)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode(WINDOW_SIZE)

# Titre de la fenêtre
pygame.display.set_caption("Tic Tac Toe")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Création d'une grille pour le Tic Tac Toe
board = [[None, None, None], [None, None, None], [None, None, None]]

# Fonction pour dessiner la grille de Tic Tac Toe
def draw_board():
    # Dessiner les lignes de la grille
    pygame.draw.line(screen, GRAY, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, GRAY, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, GRAY, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, GRAY, (0, 400), (600, 400), 5)

    # Dessiner les jetons
    for row in range(3):
        for column in range(3):
            if board[row][column] == "X":
                pygame.draw.line(screen, WHITE, (column * 200 + 55, row * 200 + 55), (column * 200 + 145, row * 200 + 145), 5)
                pygame.draw.line(screen, WHITE, (column * 200 + 145, row * 200 + 55), (column * 200 + 55, row * 200 + 145), 5)
            elif board[row][column] == "O":
                pygame.draw.circle(screen, WHITE, (column * 200 + 100, row * 200 + 100), 70, 5)

# Fonction pour vérifier si le jeu est terminé
def check_win():
    # Vérifier les lignes
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != None:
            return board[row][0]

    # Vérifier les colonnes
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != None:
            return board[0][column]

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]

    # Vérifier s'il y a une égalité
    if all([all(row) for row in board]):
        return "Tie"

    # Le jeu n'est pas terminé
    return None

# Tour du joueur
player = "X"

while True:
    # Vérifier les événements
    for event in pygame.event.get():
        # Fermer la fenêtre
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Cliquer sur une case
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenir la position de la souris
            x, y = pygame.mouse.get_pos()

            # Obtenir la ligne et la colonne de la case cliquée
            row = y // 200
            column = x // 200

            # Vérifier si la case est vide
            if board[row][column] == None:
                # Ajouter le jeton du joueur actuel
                board[row][column] = player

                # Changer de joueur
                if player == "X":
                    player = "O"
                else:
                    player = "X"

    # Dessiner la grille et les jetons
    draw_board()

    # Vérifier si le jeu est terminé
    winner = check_win()
    if winner != None:
        # Afficher le gagnant ou l'égalité
        font = pygame.font.Font(None, 100)
        if winner == "Tie":
            text = font.render("Tie", True, WHITE)
        else:
            text = font.render("{} wins!".format(winner), True, WHITE)
        screen.blit(text, (150, 250))
        pygame.display.update()

        # Attendre 3 secondes
        pygame.time.wait(3000)

        # Réinitialiser la grille
        board = [[None, None, None], [None, None, None], [None, None, None]]
        player = "X"

    # Mettre à jour l'affichage
    pygame.display.update()