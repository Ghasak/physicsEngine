
def vector_projection_fn(pygame,screen,COLOR_PALETTE,CVector2d, show_position_vector ):
    # This will get us at each frame the position vector of a mouse
    mouse_position = pygame.Vector2(pygame.mouse.get_pos())
    #pygame.draw.line(screen, 'blue', (0,0), (vec3), 3)
    path= pygame.Vector2(200, 60)
    pos= pygame.Vector2(100,200)


    head = pygame.Vector2(path + pos)
    # pygame.draw.line(screen, 'black', pos, head, 3)

    a = mouse_position - pos
    pygame.draw.line(screen, COLOR_PALETTE['red'], pos, a + pos, 3)
    pygame.draw.line(screen, COLOR_PALETTE['red'], pos,head, 3)

    #v =pygame.math.Vector2.project(a,path)
    a_dash =  CVector2d.converate_pygame_vector_to_cvector2d(a)
    path_dash =  CVector2d.converate_pygame_vector_to_cvector2d(path)
    #v = CVector2d.project(a,path)
    v1 = CVector2d.project(a_dash,path_dash)
    # You can also use

    #v2 = a_dash.vectorProjection(path_dash)
    # v2 =CVector2d.vectorProjection( a_dash,path_dash)
    # v3 =CVector2d.vectorProjection2( a_dash,path_dash)
    #console.log(f"v2 is -> {v2} while v3 is -> {v3}")

    #v = CVector2d.converate_cvector2d_to_pygame_vector(v2)
    # pygame.draw.line(screen, 'deepskyblue4', v + pos, mouse_position, 5)
    # pygame.draw.line(screen, 'deepskyblue4', pos,v + pos, 5)
    #
    # show_position_vector(screen = screen ,vec = mouse_position, text ="Vector M ->")
    # show_position_vector(screen = screen ,vec = pos, text ="Vector pos ->")
    # show_position_vector(screen = screen ,vec = pos + path, text ="Vector path ->")

    # To find the opposite projection (projection the path on a)
    # vx = (path).project(a)
    # pygame.draw.line(screen, 'deepskyblue4', pos, vx + pos, 5)
    # pygame.draw.line(screen, 'deepskyblue4',vx + pos, pos + path, 5)

    # Find the box that start from position and end at the mouse position

    a = mouse_position - pos
    projx_a_on_b = a.project(path)
    projy_a_on_b = a - projx_a_on_b
    pygame.draw.line(screen, COLOR_PALETTE['blue'],pos ,  pos + projx_a_on_b , 5)
    pygame.draw.line(screen, COLOR_PALETTE['blue'],pos ,  pos + projy_a_on_b , 5)
    pygame.draw.line(screen, COLOR_PALETTE['gray'],  pos + projx_a_on_b, mouse_position , 3)
    pygame.draw.line(screen, COLOR_PALETTE['gray'],  pos + projy_a_on_b, mouse_position , 3)
    pygame.draw.line(screen, COLOR_PALETTE['gray'],  path, pos + path, 1)


    # show the vectors
    show_position_vector(screen = screen ,vec = path, text ="path ->")
    show_position_vector(screen = screen ,vec = mouse_position, text ="Vector M ->")
    show_position_vector(screen = screen ,vec = pos, text ="Vector pos ->")
    show_position_vector(screen = screen ,vec = pos + path, text ="Vector path ->")

