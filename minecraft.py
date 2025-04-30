import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Eşya Toplama ve Envanter")
player_img = pygame.image.load("stever.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))
pickaxe_img = pygame.image.load("pickaxe.png").convert_alpha()
pickaxe_img = pygame.transform.scale(pickaxe_img, (30, 30))
wood_img = pygame.image.load("wood.png").convert_alpha()
wood_img = pygame.transform.scale(wood_img, (30, 30))
chest_img = pygame.image.load("chest.png").convert_alpha()
chest_img = pygame.transform.scale(chest_img, (50, 50))

player = pygame.Rect(100, 100, 50, 50)
chest = pygame.Rect(400, 300, 50, 50)
pickaxe = pygame.Rect(200, 150, 30, 30)
woods = [pygame.Rect(300, 400, 30, 30), pygame.Rect(500, 200, 30, 30)]
inventory = {"Pickaxe": 0, "Wood": 0}

chest_opened = False
has_pickaxe = False
items_collected = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    if pickaxe and player.colliderect(pickaxe):
        if keys[pygame.K_e]:
            has_pickaxe = True
            inventory["Pickaxe"] = 1
            pickaxe = None

    if has_pickaxe:
        for wood in woods[:]:
            if player.colliderect(wood):
                if keys[pygame.K_SPACE]:
                    inventory["Wood"] += 1

    if inventory["Wood"] >= 20 and player.colliderect(chest):
        print("You Win!")
        running = False

    screen.fill((255, 255, 255))

    if chest_opened:
        screen.blit(chest_img, (chest.x, chest.y))
    else:
        screen.blit(chest_img, (chest.x, chest.y))

    if pickaxe:
        screen.blit(pickaxe_img, (pickaxe.x, pickaxe.y))

    for wood in woods:
        screen.blit(wood_img, (wood.x, wood.y))

    screen.blit(player_img, (player.x, player.y))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Wood: {inventory['Wood']}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    if has_pickaxe:
        pickaxe_text = font.render("Pickaxe: Yes", True, (0, 0, 0))
    else:
        pickaxe_text = font.render("Pickaxe: No", True, (0, 0, 0))
    screen.blit(pickaxe_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
